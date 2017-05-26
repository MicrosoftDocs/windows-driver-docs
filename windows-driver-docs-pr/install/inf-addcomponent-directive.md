---
title: INF AddComponent Directive
description: An AddComponent directive creates a software component device underneath the current device.
ms.author: windowsdriverdev
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# INF AddComponent Directive

An **AddComponent** directive is used within an INF *DDInstall*.**Components** section.  It creates a virtual child device for the software component under the current device.  This directive is supported for Windows 10 Version 1703 and later.

```
[DDInstall.Components]

**AddComponent**=ComponentName,[flags],component-install-section
```

## Entries

**ComponentName**

Specifies the name of the software component to create.  Each **AddComponent** directive in an INF file must have a unique value.

*flags*

Specifies one or more (ORed) flags, currently undefined but reserved for future use.

*component-install-section*

References an INF-writer-defined section that contains information for creating the named software component for this device.  

## Remarks

Each INF-writer-created section name must be unique within the INF file and must follow the general rules for defining section names.  For more information about these rules, see [General Syntax Rules for INF Files](general-syntax-rules-for-inf-files.md).

An **AddComponent** directive must reference a named *component-install-section* elsewhere in the INF file.  Each such section has the following form:

```
[component-install-section]

ComponentIDs=component-id[,component-id] …
[DisplayName=name]
[Description=description]
```

Each *component-install-section* must have at least the **ComponentIDs** entry as shown here. However, the remaining entries are optional.

## Component-Install Section Entries and Values
	
**ComponentIDs**=*id1[, id2] … [, idN]*

Specifies the component identifiers for a software component.  Component IDs work the same way that Hardware IDs do, and should follow [similar formatting](hardware-ids.md). For a software component, the system prepends the INF-supplied values with `SWC\` to create the Hardware IDs.  For example, a **ComponentIDs** value of `VID0001&PID0001` results in a hardware ID of `SWC\VID0001&PID0001`.

**DisplayName**=*name*

Optionally specifies a friendly name for the software component, typically for localization, expressed as a %strkey% token defined in an [INF Strings section](inf-strings-section.md).  Use this if you want to give the software component device a different display name before the software component device has its own driver installed.

**Description**=*description*

Optionally specifies a string that describes the software component, typically for localization, expressed as a %strkey% token defined in an [INF Strings section](inf-strings-section.md).

This string gives the user more information about the software component than the **DisplayName**. For example, the **DisplayName** might be something like *DHCP Control Panel* and the Description might be something like *Manages device settings and capabilities*.
	
If a description string contains any %strkey% tokens, each token can represent a maximum of 511 characters. The total string, after any string token substitutions, should not exceed 1024 characters.

## See Also

[Adding Software Components with an INF file](adding-software-components-with-an-inf-file.md).

[*DDInstall*.**Components**](inf-ddinstall-components-section.md)

[INF AddSoftware Directive](inf-addsoftware-directive.md)
