---
title: Run From Driver Store
description: This page describes how to make use of 'run from driver store' concepts in a driver package.
ms.date: 11/05/2021
ms.localizationpriority: medium
---

# Run From Driver Store

An INF that is using 'run from [Driver Store](/windows-hardware/drivers/install/driver-store)' means that the INF uses [**DIRID 13**](../install/using-dirids.md) to specify the location for driver package files on install.

A WDM or KMDF driver that is running from the Driver Store on Windows 10 version 1803 and later which needs to access other files from its driver package should call [**IoGetDriverDirectory**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetdriverdirectory) with *DriverDirectoryImage* as the directory type to get the directory path that the driver was loaded from.

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

Additionally, a [**CopyFiles**](../install/inf-copyfiles-directive.md) directive cannot be used to rename a file. These restrictions are required so that the installation of an INF on a device does not result in the creation of new files in the Driver Store directory.

Since [**SourceDisksFiles**](../install/inf-sourcedisksfiles-section.md) entries cannot have multiple entries with the same filename and CopyFiles cannot be used to rename a file, every file that an INF references must have a unique file name.

## Dynamically finding and loading files from the Driver Store

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
