---
title: INF DDInstall.Filters Section
description: The DDInstall.Filters section contains one or more INF AddFilter directives that reference additional INF-writer-defined sections in a device driver INF file.
ms.date: 05/11/2022
---

# INF DDInstall.Filters Section

Each per-Models *DDInstall*.**Filters** section contains one or more [**INF AddFilter directives**](inf-addfilter-directive.md) that reference additional INF-writer-defined sections in a device driver INF file.  This section is supported in Windows 10 Version 1903 and later.

```inf
[install-section-name.Filters] |
[install-section-name.nt.Filters] |
[install-section-name.ntx86.Filters] |
[install-section-name.ntia64.Filters] |
[install-section-name.ntamd64.Filters] |
[install-section-name.ntarm.Filters] |
[install-section-name.ntarm64.Filters]
 
AddFilters=FilterName,[flags],filter-install-section
```

You can provide a *DDInstall*.**Filters** section with at least one [AddFilter directive](inf-addfilter-directive.md) to add a filter to a device stack.

## Entries

**AddFilter**=*FilterName,[flags],filter-install-section*

The specified *FilterName* must be the name of a driver service. This service will be added to the device stack using the [declarative filter model](../develop/device-filter-driver-ordering.md), which does not rely on the UpperFilters or LowerFilters registry values.

This directive references an INF-writer-defined *filter-install-section* elsewhere in the device driver INF file.  For more information, see [**INF AddFilter directive**](inf-addfilter-directive.md).

## Remarks

*DDInstall*.**Filter** sections should have the same platform and operating system decorations as their related *DDInstall* sections.  For example, an *install-section-name*.**ntx86** section would have a corresponding *install-section-name*.**ntx86.Filters** section.

The specified *DDInstall* section must be referenced in a device/models-specific entry under the per-manufacturer *Models* section of the INF file. The case-insensitive extensions to the *install-section-name* shown in the formal syntax statement can be inserted into such a <em>DDInstall</em>**.Filters** section name in cross-platform INF files.

For more information about how to use the system-defined **.nt**, **.ntx86**, **.ntia64**, **.ntamd64**, **.ntarm**, and **.ntarm64** extensions, see [Creating INF Files for Multiple Platforms and Operating Systems](creating-inf-files-for-multiple-platforms-and-operating-systems.md).

## Example

```inf
[Contoso.NT.Filters]
AddFilter = MyUpperFilter,, UpperFilter_Inst

[UpperFilter_Inst]
FilterPosition = Upper

[Contoso.NT.Services]
AddService = MyUpperFilter,, MyUpperFilter_Inst

[MyUpperFilter_Inst]
...
```

## See also

[Device filter driver ordering](../develop/device-filter-driver-ordering.md)