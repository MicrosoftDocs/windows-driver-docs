---
title: INF UpdateInis Directive
description: An UpdateInis directive specifies an INI file from which to read a section to be applied to an existing INI file of the same name on a target computer.
keywords:
- INF UpdateInis Directive Device and Driver Installation
topic_type:
- apiref
ms.topic: reference
api_name:
- INF UpdateInis Directive
api_type:
- NA
ms.date: 07/17/2023
---

# INF UpdateInis directive

[!INCLUDE [Caution invalid INF directive](../includes/inf-directive-invalid-22h2.md)]

An **UpdateInis** directive references one or more named sections, specifying an INI file from which a particular section or line is to be read and applied to an existing INI file of the same name on the target computer. Optionally, line-by-line modifications from and to such INI files can be specified in the *update-ini-section*.

```inf
[DDInstall] | 
[DDInstall.CoInstallers] | 
[ClassInstall32] | 
[ClassInstall32.ntx86] | 
[ClassInstall32.ntia64] | (Windows XP and later versions of Windows)
[ClassInstall32.ntamd64] | (Windows XP and later versions of Windows)
[ClassInstall32.ntarm] | (Windows 8 and later versions of Windows)
[ClassInstall32.ntarm64] (Windows 10 version 1709 and later versions of Windows)

UpdateInis=update-ini-section[,update-ini-section]...
```

This directive is almost never specified in INF files for installation on Windows, due to the lack of necessity for INI files. However, the **UpdateInis** directive is valid in any of the sections shown in the formal syntax statement, as well as in INF-writer-defined sections referenced by an **AddInterface** directive or referenced in an **InterfaceInstall32** section.

Each named section referenced by an **UpdateInis** directive has the following form:

```inf
[update-ini-section]
 
ini-file,ini-section[,old-ini-entry][,new-ini-entry][,flags]
...
```

An *update-ini-section* can have any INF-writer-determined number of entries, each on a separate line.

## Entries

*ini-file*  
Specifies the name of an INI file supplied on the source media and, implicitly, that of the INI file to be updated on the target computer. This value can be expressed as a *filename* or as a %*strkey*% token that is defined in a [**Strings**](inf-strings-section.md) section of the INF file.

*ini-section*  
Specifies the name of the section within the given INI file. If the next two values are specified, this section contains an entry to be changed. If an *old-ini-entry* is omitted but a *new-ini-entry* is provided, the new entry is to be added as this section is read.

*old-ini-entry*  
This optional value specifies the name of an entry in the given *ini-section*, usually expressed in the following form:

```inf
"key=value"
```

Either or both of *key* and *value* can be expressed as %*strkey*% tokens defined in a **Strings** section of the INF file. The asterisk (\*) can be specified as a wild-card for either the *key* or the *value*.

*new-ini-entry*  
This optional value specifies either a change to a given *old-ini-entry* or the addition of a new entry. This value can be expressed in the same manner as *old-ini-entry*.

*flags*  
This optional value controls the interpretation of the given *old-ini-entry* and/or *new-ini-entry*. The *flags* entry can be one of the following numeric values:

| Value | Meaning |
|--|--|
| **0** | This is the default value for the *flags* entry if it is omitted.<br><br>If the given *old-ini-entry* key is present in the INI files, replace that *key=value* with the given *new-ini-entry*. Only the keys in the INI files must match. The corresponding value of each such key is ignored.<br><br>To add a *new-ini-entry* to the destination INI file unconditionally, omit the *old-ini-entry* value from the entry in the *update-ini* section of the INF.<br><br>To delete an *old-ini-entry* from the destination INI file unconditionally, omit the *new-ini-entry* value. |
| **1** | If the given *old-ini-entry* (*key=value*) exists in the INI files, replace it in the destination INI file that has the given *new-ini-entry*. Both the *key* and *value* of the specified *old-ini-entry* must match those in the INI files for such a replacement to be made, not just their keys as for the preceding *flags* value. |
| **2** | If the *key* that is specified for *old-ini-entry* cannot be found in the destination INI file, do nothing. Otherwise, the changes made depend on matches found in the INI files for the given keys of *old-ini-entry* and *new-ini-entry*, as follows:<br><br>(1) If the *key* of the *old-ini-entry* exists in the INI files but so does the *key* of the *new-ini-entry*, replace the *old-ini-entry* with the *new-ini-entry* in the destination INI file and, then, remove the superfluous *new-ini-entry* from that INI file.<br><br>(2) If the *key* of the *old-ini-entry* exists in the INI files but the key of the *new-ini-entry* does not, replace the *old-ini-entry* *key* with that of the *new-ini-entry* in the destination INI file but leave the value of the *old-ini-entry* unchanged. |
| **3** | If the *key* and *value* specified for *old-ini-entry* cannot be found in the INI files, do nothing. Otherwise, the changes made depend on matches found in the INI files for the given keys and values of *old-ini-entry* and *new-ini-entry*, as follows:<br><br>(1) If the *key=value* of the *old-ini-entry* exists in the INI files but so does the *key=value* of the *new-ini-entry*, replace the *old-ini-entry* with the *new-ini-entry* in the destination INI file and, then, remove the superfluous *new-ini-entry* from that INI file.<br><br>(2) If the *key=value* of the *old-ini-entry* exists in the INI files but the *new-ini-entry* does not, replace the *old-ini-entry* with the *new-ini-entry* in the destination INI file but leave the value of the *old-ini-entry* unchanged. |

## Remarks

A given *update-ini-section* name must be unique within the INF file and must follow the general rules for defining section names. For more information about these rules, see [General Syntax Rules for INF Files](general-syntax-rules-for-inf-files.md).

The INF provides the full path of the given *ini-file* on the distribution media in one of the following ways:

- In IHV/OEM-supplied INF files, by using the [**SourceDisksNames**](inf-sourcedisksnames-section.md) and [**SourceDisksFiles**](inf-sourcedisksfiles-section.md) sections of this INF to explicitly specify the full path of each named source file that is not in the root directory (or directories) on the distribution media.

- In system-supplied INF files, by supplying one or more additional INF files, identified in the **LayoutFile** entry in the [**Version**](inf-version-section.md) section of the INF file.

Any *filename* specified within an *old-ini-entry* or *new-ini-entry* should designate the destination directory that contains that file. Such a destination directory path of a *filename* in an *update-ini-section* entry must be specified as a *dirid*. For lists of possible *dirid* values, see [Using Dirids](using-dirids.md).

## See also

[**AddInterface**](inf-addinterface-directive.md)

[**ClassInstall32**](inf-classinstall32-section.md)

[***DDInstall***](inf-ddinstall-section.md)

[**DestinationDirs**](inf-destinationdirs-section.md)

[**Ini2Reg**](inf-ini2reg-directive.md)

[**InterfaceInstall32**](inf-interfaceinstall32-section.md)

[**ProfileItems**](inf-profileitems-directive.md)

[**SourceDisksFiles**](inf-sourcedisksfiles-section.md)

[**SourceDisksNames**](inf-sourcedisksnames-section.md)

[**Strings**](inf-strings-section.md)

[**UpdateIniFields**](inf-updateinifields-directive.md)

[**Version**](inf-version-section.md)
