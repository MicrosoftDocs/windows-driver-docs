---
title: INF DDInstall.Software Section
description: The DDInstall.Software section contains one or more INF AddSoftware directives that reference additional INF-writer-defined sections in a software component INF file.
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# INF DDInstall.Software Section

Each per-Models *DDInstall*.**Software** section contains one or more [**INF AddSoftware directives**](inf-addsoftware-directive.md) that reference additional INF-writer-defined sections in a software component INF file.  This section is supported for Windows 10 Version 1703 and later.

```cpp
[install-section-name.Software] |
[install-section-name.nt.Software] |
[install-section-name.ntx86.Software] |
[install-section-name.ntia64.Software] |
[install-section-name.ntamd64.Software] |
[install-section-name.ntarm.Software] |
[install-section-name.ntarm64.Software]
 
AddSoftware=SoftwareName,[flags],software-install-section
```

You can provide a *DDInstall*.**Software** section with at least one [AddSoftware directive](inf-addsoftware-directive.md) to install software from a software component.

The software installation must be non-interactive.

## Entries

**AddSoftware**=*SoftwareName,[flags],software-install-section*

This directive references an INF-writer-defined *software-install-section* elsewhere in the software component INF file.  For more information, see [**INF AddSoftware directive**](inf-addsoftware-directive.md).

## Remarks

*DDInstall*.**Software** sections should have the same platform and operating system decorations as their related *DDInstall* sections.  For example, an *install-section-name*.**ntx86** section would have a corresponding *install-section-name*.**ntx86.Software** section.
	
The specified *DDInstall* section must be referenced in a device/models-specific entry under the per-manufacturer *Models* section of the INF file. The case-insensitive extensions to the *install-section-name* shown in the formal syntax statement can be inserted into such a <em>DDInstall</em>**.Software** section name in cross-platform INF files.

For more information about how to use the system-defined **.nt**, **.ntx86**, **.ntia64**, and **.ntamd64** extensions, see [Creating INF Files for Multiple Platforms and Operating Systems](creating-inf-files-for-multiple-platforms-and-operating-systems.md).

## Examples

```cpp
[ContosoCtrlPnl.NT.Software]
AddSoftware = ContosoGrfx1CtrlPnl,, Software_Inst

[Software_Inst]
SoftwareType = 1
SoftwareBinary =  %13%\ContosoCtrlPnl.exe
SoftwareArguments = <<DeviceInstanceID>>
SoftwareVersion = 1.0.0.0
```

## See also

[Using a Component INF File](using-a-component-inf-file.md).

[INF AddSoftware Directive](inf-addsoftware-directive.md)
