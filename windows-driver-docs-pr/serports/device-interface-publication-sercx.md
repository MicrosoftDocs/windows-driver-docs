---
title: Device Interface publication for a SerCx or SerCx2 managed Serial Port
description: Learn how to publish a device interface for a SerCx or SerCx2 managed serial port.
ms.date: 01/20/2023
---

# Device Interface publication for a SerCx or SerCx2 managed Serial Port

Starting with Windows 10 version 1903 and later, SerCx and SerCx2 include support for publishing a `GUID_DEVINTERFACE_COMPORT` *device interface*. Applications and services on a system are able to use this device interface to interact with the serial port.

This feature can be enabled on SoC-based platforms which feature an integrated UART with a SerCx/SerCx2 client driver, if the UART is exposed as a physical port, or if regular applications (UWP or Win32) need to communicate directly with a device attached to the UART. This is as opposed to [accessing the SerCx/SerCx2 controller via a connection ID](opening-a-sercx2-managed-serial-port.md) - which exclusively enables access to the UART from a dedicated peripheral driver.

When using this feature for SerCx/SerCx2 managed serial ports, a COM port number is not assigned for these devices, and no symbolic link is created - meaning that applications must use the approach described in this document to open the serial port as a device interface.

Using the device interface (`GUID_DEVINTERFACE_COMPORT`) is the recommended way to discover and access a COM port. Using legacy COM port names is prone to name collisions and doesn't provide state change notifications to a client. Using the legacy COM port names is not recommended and not supported with SerCx2 and SerCx.


## Enabling device interface creation

Below are the instructions to enable device interface creation. Note that serial ports are **exclusive**, meaning if the serial port is accessible as a device interface, a connection resource in ACPI should **not** be provided to any other devices - e.g. no `UARTSerialBusV2` resource should be provided to any other devices on the system; the port should be made **exclusively** accessible via the device interface.

### ACPI Configuration
A system manufacturer or integrator may enable this behavior by modifying the ACPI (ASL) definition of the **existing** SerCx/SerCx2 device to add a `_DSD` definition for key-value device properties with UUID `daffd814-6eba-4d8c-8a91-bc9bbf4aa301`. Inside this definition, the property `SerCx-FriendlyName` is defined with a system specific description of the serial port, for example, `UART0`, `UART1`, etc.

Example device definition (excluding vendor specific information necessary to define the device):
```
    Device(URT0) {
        Name(_HID, ...)
        Name(_CID, ...)

        Name(_DSD, Package() {
            ToUUID("daffd814-6eba-4d8c-8a91-bc9bbf4aa301"),
            Package() {
                Package(2) {"SerCx-FriendlyName", "UART0"}
            }
        })
    }
```

The specified UUID (`daffd814-6eba-4d8c-8a91-bc9bbf4aa301`) **must** be used, and the entry `SerCx-FriendlyName` must be defined for SerCx/SerCx2 to create the device interface.

### Registry Key
For development purposes, the `SerCxFriendlyName` may also be configured as a property in the device's hardware key in the registry. The `CM_Open_DevNode_Key` method may be used to access the device's [hardware key](https://learn.microsoft.com/en-us/windows-hardware/drivers/install/opening-a-device-s-hardware-key) and add the property `SerCxFriendlyName` to the device, which is used by SerCx/SerCx2 to retrieve the friendly name for the device interface.

It is not recommended to set this key via an extension INF - it is provided primarily for testing and development purposes. The recommended approach is to enable the feature via ACPI as documented above.

## Device Interface
If a `FriendlyName` is defined using the methods above, SerCx/SerCx2 will publish a `GUID_DEVINTERFACE_COMPORT` *device interface* for the controller. This device interface will have the `DEVPKEY_DeviceInterface_Serial_PortName` property set to the specified friendly name, which may be used by applications to locate a specific controller/port.

### Enabling unprivileged access
By default, the controller/port will be accessible only to privileged users and applications. If access from unprivileged applications is required, the SerCx/SerCx2 client must override the default security descriptor after calling `SerCx2InitializeDeviceInit()` or `SerCxDeviceInitConfig()`, but before calling `SerCx2InitializeDevice()` or `SerCxInitialize()`, at which time the applied security descriptor is propogated to the controller PDO.

An example of how to enable unprivileged access on SerCx2 from within the SerCx2 client controller driver's `EvtDeviceAdd` is below.

```cpp
SampleControllerEvtDeviceAdd(
    WDFDRIVER WdfDriver,
    WDFDEVICE_INIT WdfDeviceInit
)
{
    ...

    NTSTATUS status = SerCx2InitializeDeviceInit(WdfDeviceInit);
    if (!NT_SUCCESS(status)) {
        ...
    }

    // Declare a security descriptor allowing access to all
    DECLARE_CONST_UNICODE_STRING(
        SDDL_DEVOBJ_SERCX_SYS_ALL_ADM_ALL_UMDF_ALL_USERS_RDWR,
        L"D:P(A;;GA;;;SY)(A;;GA;;;BA)(A;;GA;;;UD)(A;;GRGW;;;BU)");

    // Assign it to the device, overwriting the default SerCx2 security descriptor
    status = WdfDeviceInitAssignSDDLString(
                WdfDeviceInit,
                &SDDL_DEVOBJ_SERCX_SYS_ALL_ADM_ALL_UMDF_ALL_USERS_RDWR);

    if (!NT_SUCCESS(status)) {
        ...
    }

    ...
}
```

### Behavior changes when using a Device Interface
Opting in to this feature results in the following behavioral changes in SerCx/SerCx2 (as opposed to [accessing the SerCx/SerCx2 controller via a connection ID](opening-a-sercx2-managed-serial-port.md)):

- No default configuration is applied to the port (speed, parity, etc). As there is no connection resource in ACPI to describe this, the port begins in an uninitialized state. Software that interacts with the device interface is required to configure the port using the defined [serial IOCTL interface](/windows-hardware/drivers/ddi/ntddser/).

- Calls from the SerCx/SerCx2 client driver to query or apply the default configuration will return a failure status. Additionally, `IOCTL_SERIAL_APPLY_DEFAULT_CONFIGURATION` requests to the device interface will be failed as there is no default configuration specified to apply.


## Accessing the Serial Port Device Interface
For UWP applications, the published interface may be accessed using the `Windows.Devices.SerialCommunication` namespace APIs like any other compliant serial port.

For Win32 applications, the device interface is located and accessed using the following process:
1. Application calls `CM_Get_Device_Interface_ListW` to get a list of all `GUID_DEVINTERFACE_COMPORT` class device interfaces on the system
2. Application calls `CM_Get_Device_Interface_PropertyW` for each returned interface to query the `DEVPKEY_DeviceInterface_Serial_PortName` for each interface discovered
3. When the desired port is found by name, application uses the symbolic link string returned in (1) to open a handle to the port via `CreateFile()`

Sample code for this flow:
```cpp
#include <windows.h>
#include <cfgmgr32.h>
#include <initguid.h>
#include <devpropdef.h>
#include <devpkey.h>
#include <ntddser.h>

...

DWORD ret;
ULONG deviceInterfaceListBufferLength;

//
// Determine the size (in characters) of buffer required for to fetch a list of
// all GUID_DEVINTERFACE_COMPORT device interfaces present on the system.
//
ret = CM_Get_Device_Interface_List_SizeW(
        &deviceInterfaceListBufferLength,
        (LPGUID) &GUID_DEVINTERFACE_COMPORT,
        NULL,
        CM_GET_DEVICE_INTERFACE_LIST_PRESENT);
if (ret != CR_SUCCESS) {
    // Handle error
    ...
}

//
// Allocate buffer of the determined size.
//
PWCHAR deviceInterfaceListBuffer = (PWCHAR) malloc(deviceInterfaceListBufferLength * sizeof(WCHAR));
if (deviceInterfaceListBuffer == NULL) {
    // Handle error
    ...
}

//
// Fetch the list of all GUID_DEVINTERFACE_COMPORT device interfaces present
// on the system.
//
ret = CM_Get_Device_Interface_ListW(
        (LPGUID) &GUID_DEVINTERFACE_COMPORT,
        NULL,
        deviceInterfaceListBuffer,
        deviceInterfaceListBufferLength,
        CM_GET_DEVICE_INTERFACE_LIST_PRESENT);
if (ret != CR_SUCCESS) {
    // Handle error
    ...
}

//
// Iterate through the list, examining one interface at a time
//
PWCHAR currentInterface = deviceInterfaceListBuffer;
while (*currentInterface) {
    //
    // Fetch the DEVPKEY_DeviceInterface_Serial_PortName for this interface
    //
    CONFIGRET configRet;
    DEVPROPTYPE devPropType;
    PWCHAR devPropBuffer;
    ULONG devPropSize = 0;

    // First, get the size of buffer required
    configRet = CM_Get_Device_Interface_PropertyW(
        currentInterface,
        &DEVPKEY_DeviceInterface_Serial_PortName,
        &devPropType,
        NULL,
        &devPropSize,
        0);
    if (configRet != CR_BUFFER_SMALL) {
        // Handle error
        ...
    }

    // Allocate the buffer
    devPropBuffer = malloc(devPropSize);
    if (devPropBuffer == NULL) {
        // Handle error
        free(devPropBuffer);
        ...
    }

    configRet = CM_Get_Device_Interface_PropertyW(
        currentInterface,
        &DEVPKEY_DeviceInterface_Serial_PortName,
        &devPropType,
        (PBYTE) devPropBuffer,
        &devPropSize,
        0);
    if (configRet != CR_SUCCESS) {
        // Handle error
        free(devPropBuffer);
        ...
    }

    // Verify the value is the correct type and size
    if ((devPropType != DEVPROP_TYPE_STRING) ||
        (devPropSize < sizeof(WCHAR))) {
        // Handle error
        free(devPropBuffer);
        ...
    }

    // Now, check if the interface is the one we are interested in
    if (wcscmp(devPropBuffer, L"UART0") == 0) {
        free(devPropBuffer);
        break;
    }

    // Advance to the next string (past the terminating NULL)
    currentInterface += wcslen(currentInterface) + 1;
    free(devPropBuffer);
}

//
// currentInterface now either points to NULL (there was no match and we iterated
// over all interfaces without a match) - or, it points to the interface with
// the friendly name UART0, in which case we can open it.
//
if (*currentInterface == L'\0') {
    // Handle interface not found error
    ...
}

//
// Now open the device interface as we would a COMx style serial port.
//
HANDLE portHandle = CreateFileW(
                        currentInterface,
                        GENERIC_READ | GENERIC_WRITE,
                        0,
                        NULL,
                        OPEN_EXISTING,
                        0,
                        NULL);
if (portHandle == INVALID_HANDLE_VALUE) {
    // Handle error
    ...
}

free(deviceInterfaceListBuffer);
deviceInterfaceListBuffer = NULL;
currentInterface = NULL;

//
// We are now able to send IO requests to the device.
//
... = ReadFile(portHandle, ..., ..., ..., NULL);
```

Note that an application may also [subscribe for notifications of device interface arrival and device removal](../install/registering-for-notification-of-device-interface-arrival-and-device-removal.md) in order to open or close a handle to the controller/port when the device becomes available or unavailable.