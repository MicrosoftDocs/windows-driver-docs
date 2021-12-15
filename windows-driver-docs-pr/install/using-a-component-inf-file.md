---
title: Using a Component INF File
description: Describes how to use software components to include user-mode software that is specific to a device.
ms.date: 10/17/2018
---

# Using a Component INF File

If you want to include user-mode software for use with a device on Windows 10, you have the following options to create a [DCH-compliant driver](../develop/getting-started-with-windows-drivers.md):
    
|Method|Scenario|
|---|---|
|[Hardware support apps (HSA)](../devapps/hardware-support-app--hsa--steps-for-driver-developers.md) | Device add-on software packaged as a UWP app that is delivered and serviced from the Microsoft Store.  Recommended approach. |
|Software components|Device add-on software is an MSI or EXE binary, a Win32 service, or software installed using AddReg and CopyFiles.  Referenced binary only runs on desktop editions (Home, Pro, and Enterprise).  The referenced binary will not run on Windows 10S.|

A software component is a separate, standalone driver package that can install one or more software modules.  The installed software enhances the value of the device, but is not necessary for basic device functionality and does not require an associated function driver service.  

This page provides guidelines for the use of software components.

## Getting started

To create components, an [extension INF file](using-an-extension-inf-file.md) specifies the [INF AddComponent directive](inf-addcomponent-directive.md) one or more times in the [INF DDInstall.Components](inf-ddinstall-components-section.md) section.  For each software component referenced in an extension INF file, the system creates a virtual software-enumerated child device.  More than one driver package can reference the same software component. 

Virtual device children can be updated independently just like any other device, as long as the parent device is started.  We recommend separating functionality into as many different groupings as makes sense from a servicing perspective, and then creating one software component for each grouping.

You'll provide an INF file for each software component.

If your software component INF specifies the [**AddSoftware** directive](inf-addsoftware-directive.md), the component INF:

* Must be a [universal INF file](../install/using-a-universal-inf-file.md).
* Must specify the **SoftwareComponent** setup class.

You can specify the [**AddSoftware** directive](inf-addsoftware-directive.md) one or more times.

>[!NOTE]
>When using Type 2 of the AddSoftware directive, it is not required to utilize a Component INF.  The directive can be used in any INF successfully.  An AddSoftware directive of Type 1, however, must be used from a Component INF.

Additionally, any INF (component or not) matching on a software component device:

* Can specify Win32 user services using the [AddService directive](inf-addservice-directive.md).
* Can install software using the [INF AddReg directive](inf-addreg-directive.md) and the [INF CopyFiles directive](inf-copyfiles-directive.md).
* Does not require a function driver service.
* Can be uninstalled by the user independently from the parent device.

You can find an example of a component INF in the [Driver package installation toolkit for universal drivers](https://github.com/Microsoft/Windows-driver-samples/tree/master/general/DCHU).

**Note**: In order for a software-enumerated component device to function, its parent must be started. If there is no driver available for the parent device, driver developers can create their own and optionally leverage the pass-through driver "umpass.sys". This driver is included in Windows and, effectively, does nothing other than start the device. In order to use umpass.sys, developers should use the Include/Needs INF directives in the [DDInstall section](inf-ddinstall-section.md) for each possible [DDInstall.\*] section to the corresponding [UmPass.\*] sections as shown below, regardless of whether the INF specifies any directives for that section or not:

```cpp
[DDInstall]
Include=umpass.inf
Needs=UmPass
; also include any existing DDInstall directives

[DDInstall.HW]
Include=umpass.inf
Needs=UmPass.HW
; also include any existing DDInstall.HW directives

[DDInstall.Interfaces]
Include=umpass.inf
Needs=UmPass.Interfaces
; also include any existing DDInstall.Interfaces directives

[DDInstall.Services]
Include=umpass.inf
Needs=UmPass.Services
; also include any existing any DDInstall.Services directives
```

## Accessing a device from a software component

To retrieve the device instance ID of a device that is associated with a software component, use the **SoftwareArguments** value in the [INF AddSoftware directive](inf-addsoftware-directive.md) section with the `<<DeviceInstanceID>>` runtime context variable.

The executable can then retrieve the device instance ID of the software component from its incoming argument list.  

Next, if the software component is targeting the Universal [target platform](../develop/target-platforms.md), use the following procedure:

1. Call [**CM_Locate_DevNode**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_locate_devnodea) with the device instance ID of the software component to retrieve a device handle.
2. Call [**CM_Get_Parent**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_parent) to retrieve a handle to that device’s parent.  This parent is the device that added the software component using the [INF AddComponent Directive](inf-addcomponent-directive.md).
3. Then, to retrieve the device instance ID of the parent, call [**CM_Get_Device_ID**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_device_idw) on the handle from [**CM_Get_Parent**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_parent).

If the software component is targeting the Desktop [target platform](../develop/target-platforms.md) only, use the following procedure:

1. Call [**SetupDiCreateDeviceInfoList**](/windows/win32/api/setupapi/nf-setupapi-setupdicreatedeviceinfolist) to create an empty device information set.
2. Call [**SetupDiOpenDeviceInfo**](/windows/win32/api/setupapi/nf-setupapi-setupdiopendeviceinfoa) with the software component device's device instance ID.
3. Call [**SetupDiGetDeviceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdevicepropertyw) with `DEVPKEY_Device_Parent` to retrieve the device instance ID of the parent.

## Example

The following example shows how you might use a software component to install a control panel using an executable for a graphics card.

### Driver package INF file

```cpp
[Version]
Signature   = "$WINDOWS NT$"
Class       = Extension
ClassGuid   = {e2f84ce7-8efa-411c-aa69-97454ca4cb57}
ExtensionId = {zzzzzzzz-zzzz-zzzz-zzzz-zzzzzzzzzzzz} ; replace with your own GUID
Provider    = %CONTOSO%
DriverVer   = 06/21/2006,1.0.0.0
CatalogFile = ContosoGrfx.cat

[Manufacturer]
%CONTOSO%=Contoso,NTx86

[Contoso.NTx86]
%ContosoGrfx.DeviceDesc%=ContosoGrfx, PCI\VEN0001&DEV0001

[ContosoGrfx.NT]
;empty

[ContosoGrfx.NT.Components]
AddComponent = ContosoControlPanel,, Component_Inst

[Component_Inst]
ComponentIDs = VID0001&PID0001&SID0001

[Strings]
CONTOSO = "Contoso Inc."
ContosoGrfx.DeviceDesc = "Contoso Graphics Card Extension"
```

### Software component INF file

```cpp
[Version]
Signature   = "$WINDOWS NT$"
Class       = SoftwareComponent
ClassGuid   = {5c4c3332-344d-483c-8739-259e934c9cc8}
Provider    = %CONTOSO%
DriverVer   = 06/21/2006,1.0.0.0
CatalogFile = ContosoCtrlPnl.cat

[SourceDisksNames]
1 = %Disk%,,,""

[SourceDisksFiles]
ContosoCtrlPnl.exe = 1

[DestinationDirs]
DefaultDestDir = 13

[Manufacturer]
%CONTOSO%=Contoso,NTx86

[Contoso.NTx86]
%ContosoCtrlPnl.DeviceDesc%=ContosoCtrlPnl, SWC\VID0001&PID0001&SID0001

[ContosoCtrlPnl.NT]
CopyFiles=ContosoCtrlPnl.NT.Copy

[ContosoCtrlPnl.NT.Copy]
ContosoCtrlPnl.exe

[ContosoCtrlPNl.NT.Services]
AddService = , %SPSVCINST_ASSOCSERVICE%

[ContosoCtrlPnl.NT.Software]
AddSoftware = ContosoGrfx1CtrlPnl,, Software_Inst

[Software_Inst]
SoftwareType = 1
SoftwareBinary = %13%\ContosoCtrlPnl.exe
SoftwareArguments = <<DeviceInstanceID>>
SoftwareVersion = 1.0.0.0

[Strings]
SPSVCINST_ASSOCSERVICE = 0x00000002
CONTOSO = "Contoso"
ContosoCtrlPnl.DeviceDesc = "Contoso Control Panel" 
```

The driver validation and submission process is the same for component INFs as for regular INFs. For more info, see [Windows HLK Getting Started](/windows-hardware/test/hlk/getstarted/windows-hlk-getting-started).

For more info on setup classes, see [System-Defined Device Setup Classes Available to Vendors](./system-defined-device-setup-classes-available-to-vendors.md).

## See Also

[INF AddComponent Directive](inf-addcomponent-directive.md)

[INF AddSoftware directive](inf-addsoftware-directive.md)

[INF DDInstall.Components Section](inf-ddinstall-components-section.md)

[INF DDInstall.Software Section](inf-ddinstall-software-section.md)
