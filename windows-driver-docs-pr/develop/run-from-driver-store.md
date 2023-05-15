---
title: Run From Driver Store
description: This page describes how to make use of 'run from Driver Store' concepts in a driver package.
ms.date: 05/10/2023
---

# Run From Driver Store

An INF that is using 'run from [Driver Store](../install/driver-store.md)' means that the INF uses [**DIRID 13**](../install/using-dirids.md) to specify the location for [driver package](../install/driver-packages.md) files on install.

For a 'run from Driver Store' file payloaded by an INF, the *subdir* listed in the [**SourceDisksFiles**](../install/inf-sourcedisksfiles-section.md) entry for the file in the INF **must** match the subdir listed in the [**DestinationDirs**](../install/inf-destinationdirs-section.md) entry for the file in the INF.

Additionally, a [**CopyFiles**](../install/inf-copyfiles-directive.md) directive can't be used to rename a file that is run from Driver Store. These restrictions are required so that the installation of an INF on a device doesn't result in the creation of new files in the Driver Store directory.

Since [**SourceDisksFiles**](../install/inf-sourcedisksfiles-section.md) entries can't have multiple entries with the same filename and CopyFiles can't be used to rename a file, every 'run from Driver Store' file that an INF references must have a unique file name.

Driver packages have general support for 'run from Driver Store' starting with Windows 10 1709. However, certain device stacks may place extra restrictions on files you need to provide that plug into that stack. Some examples are these device stacks that didn't support 'run from Driver Store' until Windows 10 1803:

- UMDF driver binaries: See [Restricting the Loading Location of UMDF Drivers](../wdf/restricting-the-loading-location-of-umdf-drivers.md) for more information

- UEFI firmware update: See [Authoring an update driver package](../bringup/authoring-an-update-driver-package.md) for more information

If providing a binary that plugs into a particular device stack, please consult the documentation for the specific device stack you're plugging into to check if it supports providing a full file path to the binary and if there are any restrictions on that full file path. If it supports providing a full file path to the binary with no restrictions on that path, then it should support the file being 'run from Driver Store'.

## Dynamically finding and loading files from the Driver Store

Sometimes there's a need for a component to load a file that is part of a driver package that uses 'run from Driver Store'.  Paths to these driver package files shouldn't be hardcoded as they can be different between different versions of the driver package, different OS versions, different OS editions, etc.  When such a need to load driver package files arises, these driver package files should be discovered and loaded dynamically using some of the paradigms described below.

### Find and load files in the same driver package

When a file in a driver package needs to load another file from the same driver package, one potential option for dynamically discovering that file is to determine the directory that this file is running from and to load the other file relative to that directory.

A WDM or KMDF driver that is running from the Driver Store on Windows 10 version 1803 and later that needs to access other files from its driver package should call [**IoGetDriverDirectory**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetdriverdirectory) with *DriverDirectoryImage* as the directory type to get the directory path that the driver was loaded from. Alternatively for drivers that need to support OS versions before Windows 10 version 1803, use [**IoQueryFullDriverPath**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-ioqueryfulldriverpath) to find the driver's path, get the directory path it was loaded from, and look for files relative to that path.  If the kernel mode driver is a KMDF driver, it can use [**WdfDriverWdmGetDriverObject**](/windows-hardware/drivers/ddi/wdfdriver/nf-wdfdriver-wdfdriverwdmgetdriverobject) to retrieve the WDM driver object to pass to IoQueryFullDriverPath.

User mode binaries can use [**GetModuleHandleExW**](/windows/win32/api/libloaderapi/nf-libloaderapi-getmodulehandleexw) and [**GetModuleFileNameW**](/windows/win32/api/libloaderapi/nf-libloaderapi-getmodulefilenamew) to determine where the driver was loaded from.  For example, a UMDF driver binary may do something like the following:

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

### Find and load files in any driver package

In some scenarios, a driver package may contain a file that is intended to be loaded by a binary in another driver package or by a user mode component.  This method can also be used for files from the same driver package if this is preferred over the method described above for loading files from the same driver package.

Here are a couple of examples of scenarios that may involve loading files from a driver package:

- A user mode DLL in a driver package provides an interface for communicating with a driver in the driver package.

- An [extension driver package](../install/using-an-extension-inf-file.md) contains a configuration file that is loaded by the driver in the base driver package.

In these situations, the driver package should set some state on a device or device interface that indicates the path of the file that is expected to be loaded.

A driver package would typically use an HKR [**AddReg**](../install/inf-addreg-directive.md) to set this state. For this example, it should be assumed that for `ExampleFile.dll`, the driver package has a [**SourceDisksFiles**](../install/inf-sourcedisksfiles-section.md) entry with no *subdir*.  This results in the file being at the root of the driver package directory. It should also be assumed that the [**DestinationDirs**](../install/inf-destinationdirs-section.md) for a [**CopyFiles**](../install/inf-copyfiles-directive.md) directive specifies **dirid** 13.

Here's an INF example for setting this as device state:

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

The previous examples use an empty flags value, which results in a REG_SZ registry value. This results in the **%13%** being turned into a fully qualified user mode file path. In many cases, it's preferable to have the path be relative to an environment variable. If a flags value of **0x20000** is used, the registry value is of type REG_EXPAND_SZ and the **%13%** converts to a path with appropriate environment variables to abstract the location of the path. When retrieving this registry value, call [**ExpandEnvironmentStrings**](/windows/win32/api/rrascfg/nn-rrascfg-ieapproviderconfig) to resolve the environment variables in the path.

If the value needs to be read by a kernel mode component, the value should be a REG_SZ value. When the kernel mode component reads that value, it should prepend `\??\` before passing it to APIs such as [**ZwOpenFile**](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwopenfile).

To access this setting when it's part of the device's state, first the application must find the identity of the device.  User mode code can use [**CM_Get_Device_ID_List_Size**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_device_id_list_sizea) and [**CM_Get_Device_ID_List**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_device_id_lista) to get a list of devices, filtered as necessary. That list of devices might contain multiple devices, so search for the appropriate device before reading state from the device. For example, call [**CM_Get_DevNode_Property**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_devnode_propertyw) to retrieve properties on the device when looking for a device matching specific criteria.

Once the correct device is found, call [**CM_Open_DevNode_Key**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_open_devnode_key) to get a handle to the registry location where the device state was stored.

Kernel mode code should retrieve a PDO (physical device object) to the device with the state and call [**IoOpenDeviceRegistryKey**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioopendeviceregistrykey).  One possible way for the kernel mode code to retrieve the PDO of the device would be to discover an enabled interface exposed by the device and use [**IoGetDeviceObjectPointer**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetdeviceobjectpointer) to retrieve the device object.

To access this setting when it's device interface state, User mode code can call [**CM_Get_Device_Interface_List_Size**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_device_interface_list_sizea) and [**CM_Get_Device_Interface_List**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_device_interface_lista).

Additionally [**CM_Register_Notification**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_register_notification) can be used to be notified of arrivals and removals of device interfaces so the code gets notified when the interface is enabled and then can retrieve the state. There may be multiple device interfaces in the device interface class used in the above APIs.  Examine those interfaces to determine which is the correct interface for the setting to read.

Once the correct device interface is found, call [**CM_Open_Device_Interface_Key**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_open_device_interface_keyw).

Kernel mode code can retrieve a symbolic link name for the device interface from which to get state. To do so, call [**IoRegisterPlugPlayNotification**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioregisterplugplaynotification) to register for device interface notifications on the appropriate device interface class.  Alternatively, call [**IoGetDeviceInterfaces**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetdeviceinterfaces) to get a list of current device interfaces on the system.  There may be multiple device interfaces in the device interface class used in the above APIs.  Examine those interfaces to determine which is the correct interface that should have the setting to be read.

Once the appropriate symbolic link name is found, call [**IoOpenDeviceInterfaceRegistryKey**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioopendeviceinterfaceregistrykey) to retrieve a handle to the registry location where the device interface state was stored.

> [!NOTE]
> Use the **CM_GETIDLIST_FILTER_PRESENT** flag with [CM_Get_Device_ID_List_Size](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_device_id_list_sizea) and [**CM_Get_Device_ID_List**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_device_id_lista) or the **CM_GET_DEVICE_INTERFACE_LIST_PRESENT** flag with [**CM_Get_Device_Interface_List_Size**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_device_interface_list_sizew) and [**CM_Get_Device_Interface_List**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_device_interface_lista). This ensures that the hardware related to the state that contains the file path is present and ready for communication.

## Removing driver package

By default, a driver package can't be removed from the system if it's still installed on any devices.  However, some options for removing a driver package from the system allow for it to be attempted to be 'force' removed.  This attempts to remove the driver package even if that driver package is still installed on some devices on the system.  Force removals aren't allowed for driver packages that have any files that are 'run from Driver Store'.  When a driver package is removed from the system, its Driver Store contents are removed.  If there are any devices that are still installed with that driver package, any 'run from Driver Store' files in that driver package will now be gone and those missing files may cause that device to malfunction.  To prevent putting the device into a bad state like that, driver packages that contain any 'run from Driver Store' files can't be force removed.  They can only be removed once they're no longer installed on any devices.  To aid in removals of such driver packages, [**DiUninstallDriver**](/windows/win32/api/newdev/nf-newdev-diuninstalldriverw) or [pnputil /delete-driver <oem#.inf> /uninstall](../devtest/pnputil-command-syntax.md) can be used.  These methods of removal will first update any devices using the driver package being removed to no longer be installed with that driver package before attempting to remove the driver package.

## Driver package development

### Testing private binaries

When developing a driver package, if there's a need to replace a particular executable file from the driver package with a private version instead of fully rebuilding and replacing the driver package on the system, then it's recommended that a kernel debugger is used along with the [**.kdfiles**](../debugger/-kdfiles--set-driver-replacement-map-.md) command.  Since the full path to the file in the Driver Store shouldn't be hardcoded, it's recommended that in the .kdfiles mapping, the *OldDriver* file name is just the direct name of the file with no preceding path information.  To facilitate this (and other scenarios), names of files in driver packages should be as unique as possible so it doesn't match the name of a file from an unrelated driver package on the system.

## Porting an INF to use run from Driver Store

If you have an existing driver package with an INF that doesn't use run from Driver Store and are porting it to use run from Driver Store, the following examples show some common file usage in INFs and patterns on updating those files to be run from DriverStore.

### Quick reference for destination directory updates

The following table provides a quick reference for finding the appropriate guidance based on the current destination directory [**DIRID**](../install/using-dirids.md) that a driver package INF specifies for a file.

| DIRID | Subdirectory | Details |
| -- | -- | -- |
| 13 | | The file is already using 'run from Driver Store'. No further work is needed. |
|  1 | | DIRID 1 shouldn't be used. There's no guarantee that the source directory will be available when a reference to the file needs to be resolved. Instead, if components in the driver package depend on specific files, include those files in the driver package and run them from the Driver Store. |
| 10 | Firmware | For info on how to use DIRID 13 with a firmware update driver package to make it use 'run from Driver Store', see [Authoring an update driver package](../bringup/authoring-an-update-driver-package.md) for.|
| 10 | | See [Other files](#other-files). |
| 11 | | See [Other files](#other-files). |
| 12 | UMDF | See [UMDF driver binary](#umdf-driver-binary).|
| 12 | | Most files with a destination of DIRID 12 represent driver service binaries. See [Service binary](#service-binary). |
| 16422, 16426, 16427, 16428 | | Most files with a destination of these DIRIDs represent installing an application. Instead, provide a Universal Windows Platform (UWP) application and install it using an [AddSoftware directive](../install/inf-addsoftware-directive.md) from a [DDInstall.Software section](../install/inf-ddinstall-software-section.md) of the driver package INF. For details, see [Pairing a driver with a Universal Windows Platform (UWP) app](../install/pairing-app-and-driver-versions.md). |


### Service binary

If your INF adds a service and the binary isn't run from Driver Store, then your INF may look like:

```inf
[DestinationDirs]
 ; Copy the file to %windir%\system32\drivers
 Example_CopyFiles = 12

[ExampleDDInstall]
CopyFiles = Example_CopyFiles

[Example_CopyFiles]
ExampleBinary.sys

[ExampleDDInstall.Services]
AddService = ExampleService,0x2,Example_Service_Inst

[Example_Service_Inst]
DisplayName   = %SvcDesc%
ServiceType   = %SERVICE_KERNEL_DRIVER%
StartType     = %SERVICE_DEMAND_START%
ErrorControl  = %SERVICE_ERROR_NORMAL%
; Point at the file in %windir%\system32\drivers
ServiceBinary = %12%\ExampleBinary.sys
```

To move this file to be run from the Driver Store, you would need to update the DestinationDirs entry for where the file will be copied to and update the ServiceBinary directive referencing the location of this file.

```inf
[DestinationDirs]
; Update the destination to DIRID 13
Example_CopyFiles = 13

[ExampleDDInstall]
CopyFiles = Example_CopyFiles

[Example_CopyFiles]
ExampleBinary.sys

[ExampleDDInstall.Services]
AddService = ExampleService,0x2,Example_Service_Inst

[Example_Service_Inst]
DisplayName   = %SvcDesc%
ServiceType   = %SERVICE_KERNEL_DRIVER%
StartType     = %SERVICE_DEMAND_START%
ErrorControl  = %SERVICE_ERROR_NORMAL%
; Point at the run from Driver Store file using DIRID 13
ServiceBinary = %13%\ExampleBinary.sys
```

### UMDF driver binary

If your INF adds a UMDF driver and the binary isn't run from Driver Store, then your INF may look like:

```inf
[DestinationDirs]
; Copy the file to %windir%\system32\drivers\UMDF
Example_CopyFiles = 12, UMDF

[ExampleDDInstall]
CopyFiles = Example_CopyFiles

[Example_CopyFiles]
ExampleUmdfDriver.dll

[ExampleDDInstall.Wdf]
UmdfService = ExampleUmdfDriver,Example_UMDF_Inst
...

[Example_UMDF_Inst]
; Point at the file in %windir%\system32\drivers\UMDF
ServiceBinary = %12%\UMDF\ExampleUmdfDriver.dll
...
```

To move this file to be run from the Driver Store, you would need to update the DestinationDirs entry for where the file will be copied to and update the ServiceBinary directive referencing the location of this file.

```inf
[DestinationDirs]
; Update the destination to DIRID 13
Example_CopyFiles = 13

[ExampleDDInstall]
CopyFiles = Example_CopyFiles

[Example_CopyFiles]
ExampleUmdfDriver.dll

[ExampleDDInstall.Wdf]
UmdfService = ExampleUmdfDriver,Example_UMDF_Inst
...

[Example_UMDF_Inst]
; Point at the run from Driver Store file using DIRID 13
ServiceBinary = %13%\ExampleUmdfDriver.dll
...
```

### Other files

If your INF adds a file that may be loaded by other components and isn't run from Driver Store, then your INF may look like the following. In this example, only the name of the file is written to the device's registry state. Components that read this registry value to determine what file to load would be depending on the file being in `%windir%\system32` or be depending on [LoadLibrary](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibraryw)'s search order being able to find the file.

```inf
[DestinationDirs]
; Copy the file to %windir%\system32
Example_CopyFiles = 11

[ExampleDDInstall]
CopyFiles=Example_CopyFiles
AddReg=Example_AddReg

[Example_CopyFiles]
ExampleFile.dll

[Example_AddReg]
HKR,,FileLocation,,"ExampleFile.dll"
```

To move this file to be run from the Driver Store, you would need to update the DestinationDirs entry for where the file will be copied to and update the location saved in the device's state. This requires components that read that registry value to be able to handle that registry value being the full path to a file instead of a file relative to `%windir%\system32`.

```inf
[DestinationDirs]
Example_CopyFiles = 13 ; update the destination to DIRID 13

[ExampleDDInstall]
CopyFiles=Example_CopyFiles
AddReg=Example_AddReg

[Example_CopyFiles]
ExampleFile.dll

[Example_AddReg]
; Point at the run from Driver Store file using DIRID 13
HKR,,FileLocation,,"%13%\ExampleFile.dll"
```
