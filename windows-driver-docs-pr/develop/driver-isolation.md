---
title: Driver Package Isolation
description: This page describes driver isolation, a requirement for a Windows Driver.
ms.date: 11/03/2021
ms.localizationpriority: medium
---

# Driver Package Isolation

Driver package isolation is a requirement for [Windows Drivers](./getting-started-with-windows-drivers.md) that makes driver packages more resilient to external changes, easier to update, and more straightforward to install.

> [!NOTE]
> While Driver Package Isolation is required for Windows Drivers, Windows Desktop Drivers still benefit from it through improved resiliency and serviceability.

The following table shows some example legacy driver practices that are no longer allowed for Windows Drivers in the left column along with the required behavior for Windows Drivers in the right column.

|Non-isolated Driver|Isolated Driver|
|-|-|
|INF copies files to %windir%\System32 or %windir%\System32\drivers|Driver files are run from the driver store|
|Interacts with device stacks/drivers using hardcoded paths|Interacts with device stacks/drivers using system-supplied functions or device interfaces|
|Hardcodes path to global registry locations|Uses HKR and system-supplied functions for relative location of registry and file state|
|Runtime file writes to any location|Files are written relative to locations supplied by the operating system|


## Run From Driver Store

All isolated driver packages leave their driver package files in the driver store. This means that they specify [**DIRID 13**](../install/using-dirids.md) in their INF to specify the location for driver package files on install.

A WDM or KMDF driver that is running from the DriverStore on Windows 10 version 1803 and later which needs to access other files from its driver package should call [**IoGetDriverDirectory**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetdriverdirectory) with *DriverDirectoryImage* as the directory type to get the directory path that the driver was loaded from.

Alternatively for drivers that need to support OS versions before Windows 10 version 1803, use [**IoQueryFullDriverPath**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-ioqueryfulldriverpath) to find the driver's path, get the directory path it was loaded from, and look for configuration files relative to that path.  If the kernel mode driver is a KMDF driver, it can use [**WdfDriverWdmGetDriverObject**](/windows-hardware/drivers/ddi/wdfdriver/nf-wdfdriver-wdfdriverwdmgetdriverobject) to retrieve the WDM driver object to pass to IoQueryFullDriverPath. UMDF drivers can use [**GetModuleHandleExW**](/windows/win32/api/libloaderapi/nf-libloaderapi-getmodulehandleexw) and [**GetModuleFileNameW**](/windows/win32/api/libloaderapi/nf-libloaderapi-getmodulefilenamew) to determine where the driver was loaded from.  For example:

```cpp
bRet = GetModuleHandleExW(GET_MODULE_HANDLE_EX_FLAG_FROM_ADDRESS,
                         (PCWSTR)&DriverEntry,
                         &handleModule);
if (bRet) {
    charsWritten = GetModuleFileNameW(handleModule,
                                      path,
                                      pathLength);
    …
```

For a file payloaded by an INF, the *subdir* listed in the [**SourceDisksFiles**](../install/inf-sourcedisksfiles-section.md) entry for the file in the INF must match the subdir listed in the [**DestinationDirs**](../install/inf-destinationdirs-section.md) entry for the file in the INF.

Additionally, a [**CopyFiles**](../install/inf-copyfiles-directive.md) directive cannot be used to rename a file. These restrictions are required so that the installation of an INF on a device does not result in the creation of new files in the DriverStore directory.

Since [**SourceDisksFiles**](../install/inf-sourcedisksfiles-section.md) entries cannot have multiple entries with the same filename and CopyFiles cannot be used to rename a file, every file that an INF references must have a unique file name.

### Dynamically finding and loading files from the Driver Store

In some scenarios, a driver package may contain a file that is intended to be loaded by a binary in another driver package or by a user mode component.

Here are a couple of examples:

* A user mode DLL provides an interface for communicating with a driver in the driver package.
* An extension driver package contains a configuration file that is loaded by the driver in the base driver package.

In these situations, the driver package should set some state indicating the path of the file or a device interface exposed by the device.

For example, the driver package could use an HKR [**AddReg**](../install/inf-addreg-directive.md) to set this state. For this example, it should be assumed that for `ExampleFile.dll`, the driver package has a [**SourceDisksFiles**](../install/inf-sourcedisksfiles-section.md) entry with no *subdir*.  This results in the file being at the root of the driver package directory, and the [**DestinationDirs**](../install/inf-destinationdirs-section.md) for a [**CopyFiles**](../install/inf-copyfiles-directive.md) directive specifies **dirid** 13.

Here is an INF example for setting this as device state:

```cpp
[ExampleDDInstall.HW]
AddReg = Example_DDInstall.AddReg

[Example_DDInstall.AddReg]
HKR,,ExampleValue,,%13%\ExampleFile.dll
```

An INF example for setting this as device interface state would be:

```cpp
[ExampleDDInstall.Interfaces]
AddInterface = {<fill in an interface class GUID for an interface exposed by the device>},,Example_Add_Interface_Section

[Example_Add_Interface_Section]
AddReg = Example_Add_Interface_Section.AddReg

[Example_Add_Interface_Section.AddReg]
HKR,,ExampleValue,,%13%\ExampleFile.dll
```

The previous examples use an empty flags value, which results in a REG_SZ registry value. This results in the **%13%** being turned into a fully qualified user mode file path. In many cases, it is preferable to have the path be relative to an environment variable. If a flags value of **0x20000** is used, the registry value is of type REG_EXPAND_SZ and the **%13%** converts to a path with appropriate environment variables to abstract the location of the path. When retrieving this registry value, call [**ExpandEnvironmentStrings**](/windows/win32/api/rrascfg/nn-rrascfg-ieapproviderconfig) to resolve the environment variables in the path.

If the value needs to be read by a kernel mode component, the value should be a REG_SZ value. When the kernel mode component reads that value, it should prepend `\??\` before passing it to APIs such as [**ZwOpenFile**](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwopenfile).

To access this setting when it is part of the device's state, first the application must find the identity of the device.  User mode code can use [**CM_Get_Device_ID_List_Size**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_device_id_list_sizea) and [**CM_Get_Device_ID_List**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_device_id_lista) to get a list of devices, filtered as necessary. That list of devices might contain multiple devices, so search for the appropriate device before reading state from the device. For example, call [**CM_Get_DevNode_Property**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_devnode_propertyw) to retrieve properties on the device when looking for a device matching specific criteria.

Once the correct device is found, call [**CM_Open_DevNode_Key**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_open_devnode_key) to get a handle to the registry location where the device state was stored.

Kernel mode code should retrieve a PDO (physical device object) and call [**IoOpenDeviceRegistryKey**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioopendeviceregistrykey).

To access this setting when it is device interface state, User mode code can call [**CM_Get_Device_Interface_List_Size**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_device_interface_list_sizea) and [**CM_Get_Device_Interface_List**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_device_interface_lista).

Additionally [**CM_Register_Notification**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_register_notification) can be used to be notified of arrivals and removals of device interfaces so the code gets notified when the interface is enabled and then can retrieve the state. There may be multiple device interfaces in the device interface class used in the above APIs.  Examine those interfaces to determine which is the correct interface for the setting to read.

Once the correct device interface is found, call [**CM_Open_Device_Interface_Key**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_open_device_interface_keyw).

Kernel mode code can retrieve a symbolic link name for the device interface from which to get state. To do so, call [**IoRegisterPlugPlayNotification**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioregisterplugplaynotification) to register for device interface notifications on the appropriate device interface class.  Alternatively, call [**IoGetDeviceInterfaces**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetdeviceinterfaces) to get a list of current device interfaces on the system.  There may be multiple device interfaces in the device interface class used in the above APIs.  Examine those interfaces to determine which is the correct interface that should have the setting to be read.

Once the appropriate symbolic link name is found, call [**IoOpenDeviceInterfaceRegistryKey**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioopendeviceinterfaceregistrykey) to retrieve a handle to the registry location where the device interface state was stored.

> [!NOTE]
> Use the **CM_GETIDLIST_FILTER_PRESENT** flag with [CM_Get_Device_ID_List_Size](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_device_id_list_sizea) and [**CM_Get_Device_ID_List**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_device_id_lista) or the **CM_GET_DEVICE_INTERFACE_LIST_PRESENT** flag with [**CM_Get_Device_Interface_List_Size**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_device_interface_list_sizew) and [**CM_Get_Device_Interface_List**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_device_interface_lista). This ensures that hardware is present and ready for communication.


## Using Device Interfaces

When state needs to be shared between drivers, there should be a single driver that owns the shared state, and it should expose a way for other drivers to *read* and *modify* that state.

Typically, the driver that owns the state exposes a device interface in a custom device interface class. When the driver is ready for other drivers to have access to the state, it enables the interface. Other drivers can register for [device interface arrival notifications](../install/registering-for-notification-of-device-interface-arrival-and-device-removal.md). To access the state, the custom device interface class can define one of two contracts:

* An *I/O contract* can be associated with that device interface class that provides a mechanism for accessing the state. Other drivers use the enabled device interface to send I/O requests that conform to the contract.
* A *direct-call interface* that gets returned via a query interface. Other drivers could send [IRP_MN_QUERY_INTERFACE](../kernel/irp-mn-query-interface.md) to retrieve function pointers from the driver to call.

Alternatively, if the driver that owns the state allows direct access to the state, other drivers could access state by using system-supplied functions for programmatic access to device interface state.

These interfaces or state (depending on sharing method used) need to be properly versioned so the driver owning the state can be serviced independently of other drivers that access that state. Driver vendors cannot rely on both drivers being serviced at the same time and staying at the same version.  

Because devices and drivers controlling interfaces come and go, drivers and applications should avoid calling [**IoGetDeviceInterfaces**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetdeviceinterfaces) at component start-up to get a list of enabled interfaces.

Instead, the best practice is to register for notifications of device interface arrival or removal and then call the appropriate function to get the list of existing enabled interfaces on the machine.

For more information about device interfaces, see:

* [Using Device Interfaces](../wdf/using-device-interfaces.md)
* [Registering for Notification of Device Interface Arrival and Device Removal](../install/registering-for-notification-of-device-interface-arrival-and-device-removal.md)
* [Registering for Device Interface Change Notification](../kernel/registering-for-device-interface-change-notification.md)

## Reading and Writing State

> [!NOTE]
> If your component is using device or device interface *properties* to store state, continue to use that method and the appropriate OS API's to store and access state. The following guidance is for *other* state that needs to be stored by a component.

Access to various state should be done by calling functions that provide a caller with the location of the state and then the state is read/written relative to that location. Do not use hardcoded absolute registry paths and file paths.

This section contains the following subsections:

* [PnP Device Registry State](#pnp-device-registry-state)
* [Device Interface Registry State](#device-interface-registry-state)
* [Service Registry State](#service-registry-state)
* [Device File State](#device-file-state)
* [Service File State](#service-file-state)

### PnP Device Registry State

Isolated driver packages and user-mode components typically use two locations to store device state in the registry. These are the *hardware key* (device key) for the device and the *software key* (driver key) for the device. To retrieve a handle to these registry locations, use one of the following options, based on the platform you are using:


* [**IoOpenDeviceRegistryKey**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioopendeviceregistrykey) (WDM)
* [**WdfDeviceOpenRegistryKey**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceopenregistrykey), [**WdfFdoInitOpenRegistryKey**](/windows-hardware/drivers/ddi/wdffdo/nf-wdffdo-wdffdoinitopenregistrykey) (WDF)
* [**CM_Open_DevNode_Key**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_open_devnode_key) (user-mode code)
* [**INF AddReg**](../install/inf-addreg-directive.md) directive using HKR *reg-root* entries in an *add-registry-section* referenced from an [INF DDInstall](../install/inf-ddinstall-section.md) section or [DDInstall.HW](../install/inf-ddinstall-hw-section.md) section, as shown below:

```
[ExampleDDInstall.HW]
AddReg = Example_DDInstall.AddReg

[Example_DDInstall.AddReg] 
HKR,,ExampleValue,,%13%\ExampleFile.dll
```
### Device Interface Registry State

Use device interfaces to share state with other drivers and components. Do not hardcode paths to global registry locations.

To read and write device interface registry state, use one of the following options, based on the platform you are using:

* [**IoOpenDeviceInterfaceRegistryKey**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioopendeviceinterfaceregistrykey) (WDM) 
* [**CM_Open_Device_Interface_Key**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_open_device_interface_keyw) (user-mode code)
* [INF AddReg](../install/inf-addreg-directive.md) directive using HKR *reg-root* entries in an *add-registry-section* referenced from an [add-interface-section](../install/inf-addinterface-directive.md) section

### Service Registry State

Registry values that are set by the INF for driver and Win32 services should be stored under the "Parameters" subkey of the service by providing an HKR line in an [AddReg](../install/inf-addreg-directive.md) section, and then referencing that section in the service install section in the INF.  For example:

```
[ExampleDDInstall.Services]
Addservice = ExampleService, 0x2, Example_Service_Inst

[Example_Service_Inst]
DisplayName    = %ExampleService.SvcDesc%
ServiceType    = 1
StartType      = 3
ErrorControl   = 1
ServiceBinary  = %13%\ExampleService.sys
AddReg=Example_Service_Inst.AddReg

[Example_Service_Inst.AddReg]
HKR, Parameters, ExampleValue, 0x00010001, 1
```

To access the location of this state, use one of these functions, based on your platform:

* [**IoOpenDriverRegistryKey**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioopendriverregistrykey) (WDM) with a DRIVER_REGKEY_TYPE of **DriverRegKeyParameters**
* [**WdfDriverOpenParametersRegistryKey**](/windows-hardware/drivers/ddi/wdfdriver/nf-wdfdriver-wdfdriveropenparametersregistrykey) (WDF)
* [**GetServiceRegistryStateKey**](/windows/win32/api/winsvc/nf-winsvc-getserviceregistrystatekey) (Win32 Services) with a SERVICE_REGISTRY_STATE_TYPE of **ServiceRegistryStateParameters**

These registry values supplied by the INF in the “Parameters” subkey for the service should not be modified at runtime and should be treated as read only.  Registry values that are written at runtime should be written under a different location.  To access the location for state to be written at runtime, use one of these functions:

* [**IoOpenDriverRegistryKey**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioopendriverregistrykey) (WDM) with a DRIVER_REGKEY_TYPE of **DriverRegKeyPersistentState** or **DriverRegKeySharedPersistentState**
* [**WdfDriverOpenPersistentStateRegistryKey**](/windows-hardware/drivers/ddi/wdfdriver/nf-wdfdriver-wdfdriveropenpersistentstateregistrykey) (WDF)
* [**GetServiceRegistryStateKey**](/windows/win32/api/winsvc/nf-winsvc-getserviceregistrystatekey) (Win32 Services) with a SERVICE_REGISTRY_STATE_TYPE of **ServiceRegistryStatePersistent**
* [**GetSharedServiceRegistryStateKey**](/windows/win32/api/winsvc/nf-winsvc-getsharedserviceregistrystatekey) (Win32 Services) with a SERVICE_SHARED_REGISTRY_STATE_TYPE of **ServiceSharedRegistryPersistentState**

### Device File State

If files related to a device need to be written, those files should be stored relative to a handle or file path provided via OS API’s. Configuration files specific to that device is one example of what types of files to be stored here.

* [**IoGetDeviceDirectory**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetdevicedirectory) (WDM) with the **DirectoryType** parameter set to **DeviceDirectoryData**
* [**WdfDeviceRetrieveDeviceDirectoryString**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceretrievedevicedirectorystring) (WDF)

### Service File State

Both Win32 and driver services read and write state about themselves.

To access its own internal state values, a service uses one of the following options: 

* [**IoGetDriverDirectory**](/windows-hardware/drivers/ddi/content/wdm/nf-wdm-iogetdriverdirectory) (WDM) with the **DirectoryType** parameter set to **DriverDirectoryData** or **DriverDirectorySharedData**
* [**IoGetDriverDirectory**](/windows-hardware/drivers/ddi/content/wdm/nf-wdm-iogetdriverdirectory) (KMDF) with the **DirectoryType** parameter set to **DriverDirectoryData** or **DriverDirectorySharedData**
* [**WdfDriverRetrieveDriverDataDirectoryString**](/windows-hardware/drivers/ddi/content/wdfdriver/nf-wdfdriver-wdfdriverretrievedriverdatadirectorystring) (UMDF)
* [**GetServiceDirectory**](/windows/win32/api/winsvc/nf-winsvc-getservicedirectory) (Win32 Services) with the **eDirectoryType** parameter set to **ServiceDirectoryPersistentState**
* [**GetSharedServiceDirectory**](/windows/win32/api/winsvc/nf-winsvc-getsharedservicedirectory) (Win32 Services) with the **DirectoryType** parameter set to **ServiceSharedDirectoryPersistentState**

To share internal state of the service with other components, use a controlled, versioned interface instead of direct registry or file reads.

## DriverData and ProgramData

Files that are to be used as part of intermediate operations that can be shared with other components should be written to either *DriverData* or *ProgramData* locations.

These locations offer components a location to write temporary state or state that is meant to be consumed by other components and potentially collected and copied from a system to be processed by another system.  For example, custom log files or crash dumps fit this description.

Avoid writing files in the root of the `DriverData` or `ProgramData` directories. Instead, create a subdirectory with your company name and then write files and further subdirectories within that directory.

For example, for a company name of Contoso, a kernel-mode driver could write a custom log to `\DriverData\Contoso\Logs` and a user-mode application could collect or analyze the log files from `%DriverData%\Contoso\Logs`.

### DriverData

The `DriverData` directory is available in Windows 10, version 1803 and later, and is accessible to administrators and UMDF drivers.

Kernel-mode drivers access the `DriverData` directory by using a system-supplied symbolic link called `\DriverData`.
User-mode programs access the `DriverData` directory by using the environment variable `%DriverData%`.

### ProgramData

The `%ProgramData%` user-mode environment variable is available for user-mode components to use when storing data. 

