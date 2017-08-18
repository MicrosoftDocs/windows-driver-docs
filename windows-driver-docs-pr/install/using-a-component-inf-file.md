---
title: Adding Software Components with an INF file
description: Describes how to use software components to include user-mode software that is specific to a device.
ms.author: windowsdriverdev
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Using a Component INF File

If you want to include user-mode software for use with a device on Windows 10, you have the following options to create a [DCHU-compliant universal driver](../develop/getting-started-with-universal-drivers.md):
    
|Method|Scenario|
|---|---|
|[Hardware support apps (HSA)](../devapps/creating-a-custom-capability-to-pair-driver-with-hsa.md) | Device add-on software packaged as a UWP app that is delivered and serviced from the Windows Store.  Recommended approach. |
|Software components|Device add-on software is an MSI or EXE binary, a Win32 service, or software installed using AddReg and CopyFiles.  Referenced binary only runs on desktop editions (Home, Pro, and Enterprise).  The referenced binary will not run on Windows 10S.|

A software component is a separate, standalone driver package that can install one or more software modules.  The installed software enhances the value of the device, but is not necessary for basic device functionality and has no associated function driver service.  

This page provides guidelines for the use of software components.

## Getting started

To create components, an [extension INF file](using-an-extension-inf-file.md) specifies the [INF AddComponent Directive](inf-addcomponent-directive.md) one or more times in the [INF DDInstall.Components](inf-ddinstall-components-section.md) section.  For each software component referenced in an extension INF file, the system creates a virtual software-enumerated child device.  More than one driver package can reference the same software component. 


Virtual device children can be updated independently just like any other device, as long as the parent device is started.  We recommend separating functionality into as many different groupings as makes sense from a servicing perspective, and then creating one software component for each grouping.

You'll provide an INF file for each software component.  A component INF:

* Must be a [universal INF file](../install/using-a-universal-inf-file.md).
* Can specify Win32 user services using the [AddService directive](inf-addservice-directive.md).
* Can install software modules by specifying the the [**AddSoftware** directive](inf-addsoftware-directive.md) one or more times.
* Can install software using the [INF AddReg directive](inf-addreg-directive.md) and the [INF CopyFiles directive](inf-copyfiles-directive.md).
* Cannot specify a function driver service.
* Can be uninstalled by the user independently from the parent device.

You can find an [example of an component INF](https://github.com/Microsoft/Windows-driver-samples/blob/master/general/DCHU/osrfx2_DCHU_component/osrfx2_DCHU_component/osrfx2_DCHU_component.inx) in the [Driver package installation toolkit for universal drivers](https://github.com/Microsoft/Windows-driver-samples/tree/master/general/DCHU).

## Accessing a device from a software component

To retrieve the device instance ID of a device that is associated with a software component, use the **SoftwareArguments** value in the [INF AddSoftware directive](inf-addsoftware-directive.md) section with the `<<DeviceInstanceID>>` runtime context variable.

The executable can then retrieve the device instance ID of the software component from its incoming argument list.  

Next, if the software component is targeting the Universal [target platform](../develop/windows-10-editions-for-universal-drivers.md), use the following procedure:

1. Call [**CM_Locate_DevNode**](https://msdn.microsoft.com/library/windows/hardware/ff538742) with the device instance ID of the software component to retrieve a device handle.
2. Call [**CM_Get_Parent**](https://msdn.microsoft.com/library/windows/hardware/ff538610) to retrieve a handle to that device’s parent.  This parent is the device that added the software component using the [INF AddComponent Directive](inf-addcomponent-directive.md).
3. Then, to retrieve the device instance ID of the parent, call [**CM_Get_Device_ID**](https://msdn.microsoft.com/library/windows/hardware/ff538405) on the handle from [**CM_Get_Parent**](https://msdn.microsoft.com/library/windows/hardware/ff538610).

If the software component is targeting the Desktop [target platform](../develop/windows-10-editions-for-universal-drivers.md) only, use the following procedure:

1. Call [**SetupDiCreateDeviceInfoList**](https://msdn.microsoft.com/library/windows/hardware/ff550956) to create an empty device information set.
2. Call [**SetupDiOpenDeviceInfo**](https://msdn.microsoft.com/library/windows/hardware/ff552071) with the software component device's device instance ID.
3. Call [**SetupDiGetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551963) with `DEVPKEY_Device_Parent` to retrieve the device instance ID of the parent.

## Example

The following example shows how you might use a software component to install a control panel using an executable for a graphics card.

### Driver package INF file

```
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

```
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

The driver validation and submission process is the same for component INFs as for regular INFs. For more info, see [Windows HLK Getting Started](https://msdn.microsoft.com/library/windows/hardware/dn915002).

For more info on setup classes, see [System-Defined Device Setup Classes Available to Vendors](https://msdn.microsoft.com/library/windows/hardware/ff553426).

## See Also

[INF AddComponent Directive](inf-addcomponent-directive.md)

[INF AddSoftware directive](inf-addsoftware-directive.md)

[INF DDInstall.Components Section](inf-ddinstall-components-section.md)

[INF DDInstall.Software Section](inf-ddinstall-software-section.md)
