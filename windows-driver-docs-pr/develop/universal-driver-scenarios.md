---
title: Universal Driver Scenarios
description: Describes how the DCHU universal driver sample applies the DCHU design principles (Declarative, Componentized, Hardware Support Apps [HSA], and Universal API compliance).
ms.date: 04/04/2018
ms.localizationpriority: medium
---

# Universal Driver Scenarios

This topic describes how the [DCHU universal driver sample](https://github.com/Microsoft/Windows-driver-samples/tree/master/general/DCHU) applies the DCHU [design principles](getting-started-with-universal-drivers.md) (Declarative, Componentized, Hardware Support Apps [HSA], and Universal API compliance).  You can use it as a model for your own universal driver package.

If you would like a local copy of the sample repo, clone from [Windows-driver-samples](https://github.com/Microsoft/Windows-driver-samples).

This sample is intended to be used with Windows 10 Version 1703 and later.

## Prerequisites

Before you read this section, check out the requirements and best practices for universal driver packages described in [Getting Started with Universal Windows drivers](getting-started-with-universal-drivers.md).

## Overview

The DCHU sample provides example scenarios where two hardware partners, Contoso (a system builder, or OEM) and Fabrikam (a device manufacturer, or IHV) are working together to create a Universal Windows Driver for a device in Contoso's upcoming system.  The device in question is an [OSR USB FX2 learning kit](https://go.microsoft.com/fwlink/p/?linkid=2113717).  In the past, Fabrikam would write a non-universal driver package that was customized to a specific Contoso product line, and then hand it to the OEM to handle servicing.  This resulted in significant maintenance overhead, so Fabrikam decides to refactor the code and create a universal driver package instead.

## Use only declarative sections and directives

First, Fabrikam reviews the [list of INF sections and directives](../install/using-a-universal-inf-file.md#which-inf-sections-are-invalid-in-a-universal-inf-file) that are invalid in universal driver packages.  During this exercise, Fabrikam notices that they're using many of these sections and directives in their driver package.  

Their non-universal driver INF registers a co-installer that applies platform-dependent settings and files.  This means that the driver package is larger than it should be, and it is harder to service the driver when a bug affects only a subset of the OEM systems that ship the driver.  Also, most of the OEM-specific modifications are related to branding, so Fabrikam needs to update the driver package every time an OEM is added or when a minor issue affects a subset of OEM systems.

Fabrikam removes the non-universal sections and directives and uses the [InfVerif](../devtest/infverif.md) tool to verify that the new driver package's INF file is universal.

## Use extension INFs to componentize a driver package

Next, Fabrikam separates customizations that are specific to OEM partners (such as Contoso) from the base driver package into an [extension INF](../install/using-an-extension-inf-file.md).

The following snippet, updated from [`osrfx2_DCHU_extension.inx`], specifies the `Extension` class and identifies Contoso as the provider since they will own the extension driver package:

```cpp
[Version]
Class       = Extension
ClassGuid   = {e2f84ce7-8efa-411c-aa69-97454ca4cb57}
Provider    = Contoso
ExtensionId = {zzzzzzzz-zzzz-zzzz-zzzz-zzzzzzzzzzzz} ; replace with your own GUID
```

In [`osrfx2_DCHU_base.inx`], Fabrikam specifies the following entries:

```cpp
[OsrUsbFx2_AddReg]
HKR, OSR, "OperatingMode",, "Default" ; FLG_ADDREG_TYPE_SZ
HKR, OSR, "OperatingParams",, "None" ; FLG_ADDREG_TYPE_SZ
```

In [`osrfx2_DCHU_extension.inx`], Contoso overrides the **OperatingParams** registry value set by the base and adds **OperatingExceptions**:

```cpp
[OsrUsbFx2Extension_AddReg]
HKR, OSR, "OperatingParams",, "-Extended"
HKR, OSR, "OperatingExceptions",, "x86"
```

Note that extensions are always processed after the base INF in no definite order. If a base INF is updated to a newer version, then the extensions will still be re-applied after the new base INF is installed.

## Install a service from an INF file

Fabrikam uses a Win32 service to control the LEDs on the OSR board. They view this component as part of the core functionality of the device, so they include it as part of their base INF ([`osrfx2_DCHU_base.inx`]).  This user-mode service (usersvc) can be added and started declaratively by specifying the [**AddService**](../install/inf-addservice-directive.md) directive in the INF file:

```cpp
[OsrFx2_Install.NT]
CopyFiles = OsrFx2_UserSvcCopyFiles

[OsrFx2_Install.NT.Services]
AddService = osrfx2_DCHU_usersvc, 0x00000800, UserSvc_ServiceInstall

[UserSvc_ServiceInstall]
DisplayName = %UserSvcDisplayName%
ServiceType = 0x00000010
StartType = 3
ErrorControl = 1
ServiceBinary = %13%\osrfx2_DCHU_usersvc.exe

[OsrFx2_UserSvcCopyFiles]
osrfx2_DCHU_usersvc.exe
```

Note that such a service could also be installed in a component or extension INF, depending on the scenario.

## Use a component to install legacy software from a driver package

Fabrikam has an executable file `osrfx2_DCHU_componentsoftware.exe` that they previously installed using a co-installer.  This legacy software displays the registry keys set by the board and is required by the OEM.  This is a GUI-based executable that only runs on Windows for desktop editions.  To install it, Fabrikam creates a separate component driver package and adds it in their extension INF.

The following snippet from [`osrfx2_DCHU_extension.inx`] uses the [**AddComponent**](../install/inf-addcomponent-directive.md) directive to create a virtual child device:

```cpp
[OsrFx2Extension_Install.NT.Components]
AddComponent = osrfx2_DCHU_component,,OsrFx2Extension_ComponentInstall


[OsrFx2Extension_ComponentInstall]
ComponentIds=VID_045e&PID_94ab
```

Then, in the component INF [`osrfx2_DCHU_component.inx`], Fabrikam specifies the [**AddSoftware**](../install/inf-addsoftware-directive.md) directive to install the optional executable:

```cpp
[OsrFx2Component_Install.NT.Software]
AddSoftware = osrfx2_DCHU_componentsoftware,, OsrFx2Component_SoftwareInstall

[OsrFx2Component_SoftwareInstall]
SoftwareType = 1
SoftwareBinary = osrfx2_DCHU_componentsoftware.exe
SoftwareArguments = <<DeviceInstanceId>>
SoftwareVersion = 1.0.0.0

[OsrFx2Component_CopyFiles]
osrfx2_DCHU_componentsoftware.exe
```

The [source code for the Win32 app](https://github.com/Microsoft/Windows-driver-samples/tree/master/general/DCHU/osrfx2_DCHU_extension_loose/osrfx2_DCHU_componentsoftware) is included in the DCHU sample.

Note that the component driver package is only distributed on Desktop SKUs due to targeting set in the [Windows Hardware Dev Center dashboard](https://partner.microsoft.com/dashboard/Registration/Hardware).  For more info, see [Publish a driver to Windows Update](https://docs.microsoft.com/windows-hardware/drivers/dashboard/publish-a-driver-to-windows-update).

## Allow communication with a hardware support app

Fabrikam would like to provide a GUI-based companion app as part of the universal driver package.  Because Win32-based companion applications cannot be part of a universal driver package, they port their Win32 app to the Universal Windows Platform (UWP) and [pair the app with the device](https://docs.microsoft.com/windows-hardware/drivers/devapps/hardware-access-for-universal-windows-platform-apps).

The following snippet from [`osrfx2_DCHU_base/device.c`](https://github.com/Microsoft/Windows-driver-samples/blob/master/general/DCHU/osrfx2_DCHU_base/osrfx2_DCHU_base/device.c) shows how the base driver package adds a custom capability to the device interface instance:

```cpp
    WDF_DEVICE_INTERFACE_PROPERTY_DATA PropertyData = { 0 };
    static const wchar_t customCapabilities[] = L"CompanyName.yourCustomCapabilityNameTBD_YourStorePubId\0";

    WDF_DEVICE_INTERFACE_PROPERTY_DATA_INIT(&PropertyData,
                                            &GUID_DEVINTERFACE_OSRUSBFX2,
                                            &DEVPKEY_DeviceInterface_UnrestrictedAppCapabilities);

    Status = WdfDeviceAssignInterfaceProperty(Device,
                                              &PropertyData,
                                              DEVPROP_TYPE_STRING_LIST,
                                              sizeof(customCapabilities),
                                              (PVOID)customCapabilities);
```

The new app (not included in the DCHU sample) is secure and can be updated easily in the Microsoft Store.   With the UWP application ready, Contoso uses [DISM - Deployment Image Servicing and Management](https://docs.microsoft.com/windows-hardware/manufacture/desktop/dism---deployment-image-servicing-and-management-technical-reference-for-windows) to pre-load the application on Windows desktop edition images.

## Registering a COM component in an INF file

Fabrikam needs to register a COM component without using a co-installer.  In order to accomplish this in a universal INF file, they use the [Reg2inf tool](https://docs.microsoft.com/windows-hardware/drivers/devtest/reg2inf) distributed in the WDK.  After building their COM server project (taken from the [In-process ATL COM server sample](https://go.microsoft.com/fwlink/p/?linkid=2112596), they provide the COM .dll as an input to the Reg2inf tool.  The tool then generates the following INF directives that Fabrikam includes in their base INF ([`osrfx2_DCHU_base.inx`]):

```cpp
; Add all registry keys to successfully register the
; In-Process ATL COM Server MSFT Sample.
[OsrFx2_AddReg_COM]
HKCR,AppID\ATLDllCOMServer.DLL,AppID,,"{9DD18FED-55F6-4741-AF25-798B90C4AED5}"
HKCR,AppID\{9DD18FED-55F6-4741-AF25-798B90C4AED5},,,"ATLDllCOMServer"
HKCR,ATLDllCOMServer.SimpleObject,,,"SimpleObject Class"
HKCR,ATLDllCOMServer.SimpleObject\CLSID,,,"{92FCF37F-F6C7-4F8A-AA09-1A14BA118084}"
HKCR,ATLDllCOMServer.SimpleObject\CurVer,,,"ATLDllCOMServer.SimpleObject.1"
HKCR,ATLDllCOMServer.SimpleObject.1,,,"SimpleObject Class"
HKCR,ATLDllCOMServer.SimpleObject.1\CLSID,,,"{92FCF37F-F6C7-4F8A-AA09-1A14BA118084}"
HKCR,CLSID\{92FCF37F-F6C7-4F8A-AA09-1A14BA118084},,,"SimpleObject Class"
HKCR,CLSID\{92FCF37F-F6C7-4F8A-AA09-1A14BA118084}\InprocServer32,,%REG_EXPAND_SZ%,"%%SystemRoot%%\System32\ATLDllCOMServer.dll"
HKCR,CLSID\{92FCF37F-F6C7-4F8A-AA09-1A14BA118084}\InprocServer32,ThreadingModel,,"Apartment"
HKCR,CLSID\{92FCF37F-F6C7-4F8A-AA09-1A14BA118084}\ProgID,,,"ATLDllCOMServer.SimpleObject.1"
HKCR,CLSID\{92FCF37F-F6C7-4F8A-AA09-1A14BA118084}\Programmable,,%FLG_ADDREG_KEYONLY%
HKCR,CLSID\{92FCF37F-F6C7-4F8A-AA09-1A14BA118084}\TypeLib,,,"{9B23EFED-A0C1-46B6-A903-218206447F3E}"
HKCR,CLSID\{92FCF37F-F6C7-4F8A-AA09-1A14BA118084}\VersionIndependentProgID,,,"ATLDllCOMServer.SimpleObject"
```

## Tightly coupling multiple INF files

Ideally, there should be strong versioning contracts between base, extensions and components.  There are servicing advantages in having these three packages serviced independently (the "loosely coupled" scenario), but there are scenarios where they need to be bundled in a single driver package ("tightly coupled") due to poor versioning contracts.  The sample includes examples of both scenarios:

* [DCHU_Sample\osrfx2_DCHU_extension_loose](https://github.com/Microsoft/Windows-driver-samples/tree/master/general/DCHU/osrfx2_DCHU_extension_loose)
* [DCHU_Sample\osrfx2_DCHU_extension_tight](https://github.com/Microsoft/Windows-driver-samples/tree/master/general/DCHU/osrfx2_DCHU_extension_tight)

  When the extension and component are in the same driver package ("tightly coupled"), the extension INF specifies the [CopyINF directive](../install/inf-copyinf-directive.md) to cause the component INF to be copied to the target system.  This is demonstrated in [DCHU_Sample\osrfx2_DCHU_extension_tight\osrfx2_DCHU_extension\osrfx2_DCHU_extension.inx](https://github.com/Microsoft/Windows-driver-samples/blob/master/general/DCHU/osrfx2_DCHU_extension_tight/osrfx2_DCHU_extension/osrfx2_DCHU_extension.inx):

```cpp
[OsrFx2Extension_Install.NT]
CopyInf=osrfx2_DCHU_component.inf
```

This directive can also be used to coordinate installation of INF files in multifunction devices.  For more details, see [Copying INF files](https://docs.microsoft.com/windows-hardware/drivers/install/copying-inf-files).

> [!NOTE]
> While a base driver can payload an extension (and target the base driver in the shipping label), an extension bundled with another driver cannot be published to the extension hardware ID.

## Run from the driver store

To make it easier to update the driver, Fabrikam specifies the [Driver Store](../install/driver-store.md) as the destination to copy the driver files by using [**dirid** 13](../install/using-dirids.md) where possible.  Using a destination directory value of 13 can result in improved stability during the driver update process.  Here is an example from [`osrfx2_DCHU_base.inx`]:

```cpp
[DestinationDirs]
OsrFx2_UserSvcCopyFiles = 13 ; copy to Driver Store
```

A kernel mode driver that is running from the Driver Store can call [**IoQueryFullDriverPath**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ntddk/nf-ntddk-ioqueryfulldriverpath) and use that path to find configuration files relative to it.  If the kernel mode driver is a KMDF driver, it can use [**WdfDriverWdmGetDriverObject**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdfdriver/nf-wdfdriver-wdfdriverwdmgetdriverobject) to retrieve the WDM driver object to pass to IoQueryFullDriverPath. UMDF drivers can use [**GetModuleHandleExW**](https://docs.microsoft.com/windows/desktop/api/libloaderapi/nf-libloaderapi-getmodulehandleexw) and [**GetModuleFileNameW**](https://docs.microsoft.com/windows/desktop/api/libloaderapi/nf-libloaderapi-getmodulefilenamew) to determine where the driver was loaded from.  For example:

```cpp
bRet = GetModuleHandleExW(GET_MODULE_HANDLE_EX_FLAG_FROM_ADDRESS,
                         (PCWSTR)&DriverEntry,
                         &handleModule);
if (bRet) {
   winErr = GetModuleFileNameW(handleModule,
                               path,
                               pathLength);
     …
```

### Dynamically finding and loading files from the Driver Store

In some scenarios, a driver package may contain a file that is intended to be loaded by a binary in another driver package or by a user mode component.

Here are a couple examples:

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

The above examples use an empty flags value, which results in a REG_SZ registry value. This results in the **%13%** being turned into a fully qualified user mode file path. In many cases, it is preferable to have the path be relative to an environment variable. If a flags value of **0x20000** is used, the registry value is of type REG_EXPAND_SZ and the **%13%** converts to a path with appropriate environment variables to abstract the location of the path. When retrieving this registry value, call [**ExpandEnvironmentStrings**](https://docs.microsoft.com/windows/win32/api/processenv/nf-processenv-expandenvironmentstringsw) to resolve the environment variables in the path.

If the value needs to be read by a kernel mode component, the value should be a REG_SZ value. When the kernel mode component reads that value, it should prepend `\??\` before passing it to APIs such as [**ZwOpenFile**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nf-wdm-zwopenfile).

To access this setting when it is part of the device's state, first the application must find the identity of the device.  User mode code can use [**CM_Get_Device_ID_List_Size**](https://docs.microsoft.com/windows/desktop/api/cfgmgr32/nf-cfgmgr32-cm_get_device_id_list_sizew) and [**CM_Get_Device_ID_List**](https://docs.microsoft.com/windows/desktop/api/cfgmgr32/nf-cfgmgr32-cm_get_device_id_listw) to get a list of devices, filtered as necessary. That list of devices might contain multiple devices, so search for the appropriate device before reading state from the device. For example, call [**CM_Get_DevNode_Property**](https://docs.microsoft.com/windows/desktop/api/cfgmgr32/nf-cfgmgr32-cm_get_devnode_propertyw) to retrieve properties on the device when looking for a device matching specific criteria.

Once the correct device is found, call [**CM_Open_DevNode_Key**](https://docs.microsoft.com/windows/desktop/api/cfgmgr32/nf-cfgmgr32-cm_open_devnode_key) to get a handle to the registry location where the device state was stored.

Kernel mode code should retrieve a PDO (physical device object) and call [**IoOpenDeviceRegistryKey**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nf-wdm-ioopendeviceregistrykey).

To access this setting when it is device interface state, User mode code can call [**CM_Get_Device_Interface_List_Size**](https://docs.microsoft.com/windows/desktop/api/cfgmgr32/nf-cfgmgr32-cm_get_device_interface_list_sizew) and [**CM_Get_Device_Interface_List**](https://docs.microsoft.com/windows/desktop/api/cfgmgr32/nf-cfgmgr32-cm_get_device_interface_listw).

Additionally [**CM_Register_Notification**](https://docs.microsoft.com/windows/desktop/api/cfgmgr32/nf-cfgmgr32-cm_register_notification) can be used to be notified of arrivals and removals of device interfaces so the code gets notified when the interface is enabled and then can retrieve the state. There may be multiple device interfaces in the device interface class used in the above APIs.  Examine those interfaces to determine which is the correct interface for the setting to read.

Once the correct device interface is found, call [**CM_Open_Device_Interface_Key**](https://docs.microsoft.com/windows/desktop/api/cfgmgr32/nf-cfgmgr32-cm_open_device_interface_keyw).

Kernel mode code can retrieve a symbolic link name for the device interface from which to get state. To do so, call [**IoRegisterPlugPlayNotification**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nf-wdm-ioregisterplugplaynotification) to register for device interface notifications on the appropriate device interface class.  Alternatively, call [**IoGetDeviceInterfaces**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetdeviceinterfaces) to get a list of current device interfaces on the system.  There may be multiple device interfaces in the device interface class used in the above APIs.  Examine those interfaces to determine which is the correct interface that should have the setting to be read.

Once the appropriate symbolic link name is found, call [**IoOpenDeviceInterfaceRegistryKey**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nf-wdm-ioopendeviceinterfaceregistrykey) to retrieve a handle to the registry location where the device interface state was stored.

> [!NOTE]
> Use the **CM_GETIDLIST_FILTER_PRESENT** flag with [CM_Get_Device_ID_List_Size](https://docs.microsoft.com/windows/desktop/api/cfgmgr32/nf-cfgmgr32-cm_get_device_id_list_sizew) and [**CM_Get_Device_ID_List**](https://docs.microsoft.com/windows/desktop/api/cfgmgr32/nf-cfgmgr32-cm_get_device_id_listw) or the **CM_GET_DEVICE_INTERFACE_LIST_PRESENT** flag with [**CM_Get_Device_Interface_List_Size**](https://docs.microsoft.com/windows/desktop/api/cfgmgr32/nf-cfgmgr32-cm_get_device_interface_list_sizew) and [**CM_Get_Device_Interface_List**](https://docs.microsoft.com/windows/desktop/api/cfgmgr32/nf-cfgmgr32-cm_get_device_interface_listw). This ensures that hardware is present and ready for communication.

## Summary

The following diagram shows the driver packages that Fabrikam and Contoso created for their Universal Windows Driver.  In the loosely coupled example, they will make three separate submissions on the [Windows Hardware Dev Center dashboard](https://partner.microsoft.com/dashboard/Registration/Hardware): one for the base, one for the extension, and one for the component.  In the tightly coupled example, they will make two submissions: base and extension/component.

![Extension, base, and component driver packages](images/universal-scenarios.png)

Note that the component INF will match on the component hardware ID, whereas the base and extensions will match on the board's hardware ID.

## See also

[Getting Started with Universal Windows drivers](getting-started-with-universal-drivers.md)

[Using an Extension INF File](../install/using-an-extension-inf-file.md)

[`osrfx2_DCHU_base.inx`]: https://github.com/Microsoft/Windows-driver-samples/blob/master/general/DCHU/osrfx2_DCHU_base/osrfx2_DCHU_base/osrfx2_DCHU_base.inx
[`osrfx2_DCHU_usersvc.inx`]: https://github.com/Microsoft/Windows-driver-samples/blob/master/general/DCHU/osrfx2_DCHU_base/osrfx2_DCHU_usersvc/osrfx2_DCHU_usersvc.inx
[`osrfx2_DCHU_component.inx`]: https://github.com/Microsoft/Windows-driver-samples/blob/master/general/DCHU/osrfx2_DCHU_extension_loose/osrfx2_DCHU_component/osrfx2_DCHU_component.inx
[`osrfx2_DCHU_extension.inx`]: https://github.com/Microsoft/Windows-driver-samples/blob/master/general/DCHU/osrfx2_DCHU_extension_loose/osrfx2_DCHU_extension/osrfx2_DCHU_extension.inx
