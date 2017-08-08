---
title: Adding Software Components with an INF file
description: Describes how to use software components to include user-mode software that is specific to a device.
ms.author: windowsdriverdev
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Adding Software Components with an INF file

If you want to include user-mode software for use with a device on Windows 10, you have the following options:
    
|Method|Scenario|
|---|---|
|[Hardware support apps](../devapps/hardware-access-for-universal-windows-platform-apps.md)| Device add-on software packaged as a UWP app.  Recommended approach. |
|Software components|Device add-on software is an MSI or EXE binary.  Allowed in [Universal Windows drivers](../develop/windows-10-editions-for-universal-drivers.md) but referenced binary only runs on desktop editions (Home, Pro, and Enterprise).  The referenced binary will not run on Windows 10S.|
|Co-installers| Device add-on software is an MSI or EXE binary. Available on Desktop only for legacy support. Not recommended for new development. |

This page provides guidelines for the use of software components.

## Getting started

A software component is a separate, standalone driver package that can install one or more software modules.  The installed software enhances the value of the device, but is not necessary for basic device functionality and has no associated function driver service.  

An [extension INF file](using-an-extension-inf-file.md) references one or more software components by specifying the [INF AddComponent Directive](inf-addcomponent-directive.md) one or more times in the [INF DDInstall.Components](inf-ddinstall-components-section.md) section.

**Note**: You should only specify the [INF AddComponent Directive](inf-addcomponent-directive.md) in an extension INF file.

More than one driver package can reference the same software component. 

For each software component referenced in an extension INF file, the system creates a virtual child device.

Virtual device children can be updated independently just like any other device, as long as the parent device is started.  We recommend separating functionality into as many different groupings as makes sense from a servicing perspective, and then creating one software component for each grouping.

You'll provide an INF file for each software component.  A component INF can perform all INF operations except specifying a function driver service.  A component INF can specify Win32 user services.

To install software, each component INF in turn specifies the [**AddSoftware** directive](inf-addsoftware-directive.md) one or more times in its [*DDInstall*.**Software**](inf-ddinstall-software-section.md) section.

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

## See Also

[INF AddComponent Directive](inf-addcomponent-directive.md)

[INF AddSoftware directive](inf-addsoftware-directive.md)

[INF DDInstall.Components Section](inf-ddinstall-components-section.md)

[INF DDInstall.Software Section](inf-ddinstall-software-section.md)
