---
title: INF DDInstall.Components Section
description: The DDInstall.Components section contains one or more INF AddComponent directives that reference additional INF-writer-defined sections in a driver package INF file.
ms.date: 10/17/2018
---

# INF DDInstall.Components Section

This optional section contains one or more [**INF AddComponent directives**](inf-addcomponent-directive.md) that reference additional INF-writer-defined sections in a driver package INF file.  This section is supported for Windows 10 Version 1703 and later.

```inf
[install-section-name.Components] |
[install-section-name.nt.Components] |
[install-section-name.ntx86.Components] |
[install-section-name.ntia64.Components] |
[install-section-name.ntamd64.Components] |
[install-section-name.ntarm.Components] |
[install-section-name.ntarm64.Components] |
 
AddComponent=ComponentName,[flags],component-install-section
```

You can provide a *DDInstall*.**Components** section with one or more **AddComponent** directives to create a symbolic relationship between a driver package and any number of software components.

## Entries

**AddComponent**=*ComponentName,[flags],component-install-section*

This directive references an INF-writer-defined component-install-section elsewhere in the INF file for the drivers of the devices covered by this *DDInstall* section.  For more information, see [**INF AddComponent Directive**](inf-addcomponent-directive.md).

## Remarks

*DDInstall*.**Components** sections should have the same platform and operating system decorations as their related *DDInstall* sections.  For example, an *install-section-name*.**ntx86** section would have a corresponding *install-section-name*.**ntx86.Components** section.

The specified *DDInstall* section must be referenced in a device/models-specific entry under the per-manufacturer *Models* section of the INF file.  The case-insensitive extensions to the *install-section-name* shown in the formal syntax statement can be inserted into such a *DDInstall*.**Components** section name in cross-platform INF files.

For more information about how to use the system-defined **.nt**, **.ntx86**, **.ntia64**, **.ntamd64**, **.ntarm**, and **.ntarm64** extensions, see [Creating INF Files for Multiple Platforms and Operating Systems](creating-inf-files-for-multiple-platforms-and-operating-systems.md).

## Examples

```inf
[ContosoGrfx.NT.Components]
AddComponent = ContosoControlPanel,,Component_Inst

[Component_Inst]
ComponentIDs = VID0001&PID0001&SID0001
DisplayName = %ContosoControlPanelDisplayName%
```

## See also

[Using a Component INF File](using-a-component-inf-file.md)

[INF AddComponent Directive](inf-addcomponent-directive.md)
