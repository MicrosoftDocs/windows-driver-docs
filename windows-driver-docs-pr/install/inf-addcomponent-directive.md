---
title: INF AddComponent Directive
description: An AddComponent directive creates a software component device underneath the current device.
ms.author: windowsdriverdev
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# INF AddComponent Directive

An **AddComponent** directive is used within an [**INF *DDInstall*.Components**](inf-ddinstall-components-section.md) section of an [extension INF file](using-an-extension-inf-file.md).  It creates a virtual child device for the software component under the current device. This directive is supported for Windows 10 version 1703 and later. 

```
[DDInstall.Components]

AddComponent=ComponentName,[flags],component-install-section
```

## Entries

*ComponentName*

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
[Description=description]
```

Each *component-install-section* must have at least the **ComponentIDs** entry as shown here. However, the remaining entries are optional.

Note that **ComponentIDs** are [HardwareIDs](hardware-ids.md), which means they are strings defined by the hardware developer.  To ensure uniqueness of these IDs, in most cases, we recommend following the identifier schema used for [PCI devices](identifiers-for-pci-devices.md).  It is possible that a vendor might want to use a different schema, but that depends on the scenario.

For example, a vendor with multiple components hanging off of a device may want a relationship between the HardwareIDs of the component and the parent. In this case, they would create their **ComponentID** by appending a four-character vendor-defined component identifier to the parents' HardwareID.

## Component-Install Section Entries and Values
	
**ComponentIDs**=*id1[, id2] … [, idN]*

Specifies the component identifiers for a software component.  Component IDs work the same way that Hardware IDs do, and should follow [similar formatting](hardware-ids.md). For a software component, the system prepends the INF-supplied values with `SWC\` to create the Hardware IDs.  For example, a **ComponentIDs** value of `VID0001&PID0001` results in a hardware ID of `SWC\VID0001&PID0001`.

**Description**=*description*

Optionally specifies a string that describes the software component, typically for localization, expressed as a %strkey% token defined in an [INF Strings section](inf-strings-section.md).
	
If a description string contains any %strkey% tokens, each token can represent a maximum of 511 characters. The total string, after any string token substitutions, should not exceed 1024 characters.

## See Also

[Using a Component INF File](using-a-component-inf-file.md).

[*DDInstall*.**Components**](inf-ddinstall-components-section.md)

[INF AddSoftware Directive](inf-addsoftware-directive.md)
