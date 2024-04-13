---
title: INF UpdateIniFields Directive
description: An UpdateIniFields directive references one or more named sections in which fine-grained modifications within the lines of an INI file can be specified.
keywords:
- INF UpdateIniFields Directive Device and Driver Installation
topic_type:
- apiref
ms.topic: reference
api_name:
- INF UpdateIniFields Directive
api_type:
- NA
ms.date: 07/17/2023
---

# INF UpdateIniFields directive

[!INCLUDE [Caution invalid INF directive](../includes/inf-directive-invalid-22h2.md)]

An **UpdateIniFields** directive references one or more named sections in which fine-grained modifications within the lines of an INI file can be specified.

```inf
[DDInstall] | 
[DDInstall.CoInstallers] | 
[ClassInstall32] | 
[ClassInstall32.ntx86] | 
[ClassInstall32.ntia64] | (Windows XP and later versions of Windows)
[ClassInstall32.ntamd64] | (Windows XP and later versions of Windows)
[ClassInstall32.ntarm] | (Windows 8 and later versions of Windows)
[ClassInstall32.ntarm64] (Windows 10 version 1709 and later versions of Windows)

UpdateIniFields=update-inifields-section[,update-inifields-section]...
```

Each named section referenced by an **UpdateIniFields** directive has the following form:

```inf
[update-inifields-section]
 
ini-file,ini-section,profile-name[,old-field][,new-field][,flags]
...
```

An *update-inifields-section* can have any INF-writer-determined number of entries, each on a separate line.

## Entries

*ini-file*  
Specifies the name of an INI file supplied on the source media and, implicitly, that of a to-be-updated INI file on the target computer. This value can be expressed as a *filename* or as a %*strkey*% token that is defined in a [**Strings**](inf-strings-section.md) section of the INF file.

*ini-section*  
Specifies the name of the section within the given INI files that contains the line to be modified.

*profile-name*  
Specifies the name of the line to be modified within the given INI section. At least one of the *old-field* and/or *new-field* entries must be specified to effect a modification of this line.

*old-field*  
Specifies an existing field within the given line. If *new-field* is omitted from this section entry, this field is deleted from the given line. Otherwise, the given *new-field* value should replace this field.

*new-field*  
Specifies a replacement for a given *old-field* or, if *old-field* is omitted, an addition to the given line.

*flags*  
Specifies (in bit 0) how to interpret given *old*-*field* and/or *new*-*field* if either or both contain an asterisk (\*), and/or (in bit 1) which separator character to use when appending a given *new-field* to the given line, as follows:

Bit zero = **0**  
Interpret any asterisk (\*) in the specified *old-field* and/or *new-field* entries literally, not as a wild-card character, when searching for a match in the given line of the INI file. This is the default value.

Bit zero = **1**  
Interpret any asterisk (\*) in the specified *old-field* and/or *new-field* entries as a wild-card character when searching for a match in the given line of the INI file.

Bit one = **0**  
Use a space character as a separator when adding the specified *new-field* entry to the given line of the INI file. This is the default value.

Bit one = **1**  
Use a comma (,) as a separator when adding the specified *new-field* entry to the given line of the INI file.

## Remarks

The **UpdateIniFields** directive is almost never specified in INF files for installations on Windows because it is not necessary to have INI files on their distribution media. However, the **UpdateIniFields** directive is valid in any of the sections shown in the formal syntax statement, as well as in INF-writer-defined sections referenced by an [**AddInterface**](inf-addinterface-directive.md) directive or referenced in an [**InterfaceInstall32**](inf-interfaceinstall32-section.md) section.

Each *update-inifields-section* name must be unique to the INF file. Each INF-writer-created section name must be unique within the INF file and must follow the general rules for defining section names. For more information about these rules, see [General Syntax Rules for INF Files](general-syntax-rules-for-inf-files.md).

Unlike a section referenced by the [**UpdateInis**](inf-updateinis-directive.md) directive, a section referenced by **UpdateIniFields** replaces, adds, or deletes parts of a line in an existing INI file line instead of affecting the whole value of a particular line. At least one of the *old-field* and/or *new-field* values must be specified in each section entry.

Any comments in a to-be-modified INI file line are removed because they might not be applicable after changes made according to this section. When looking for fields in the line in the INI files, spaces, tabs, and commas are interpreted as field delimiters. However, a space character is used as the default separator when a new field is appended to a line.

The INF provides the full path of the given *ini-file* on the distribution media in one of the following ways:

- In IHV/OEM-supplied INF files, by using the [**SourceDisksNames**](inf-sourcedisksnames-section.md) and [**SourceDisksFiles**](inf-sourcedisksfiles-section.md) sections of this INF to explicitly specify the full path of each named source file that is not in the root directory (or directories) on the distribution media.

- In system-supplied INF files, by supplying one or more additional INF files, identified in the **LayoutFile** entry in the [**Version**](inf-version-section.md) section of the INF file.

## See also

[**AddInterface**](inf-addinterface-directive.md)

[**ClassInstall32**](inf-classinstall32-section.md)

[***DDInstall***](inf-ddinstall-section.md)

[**Ini2Reg**](inf-ini2reg-directive.md)

[**InterfaceInstall32**](inf-interfaceinstall32-section.md)

[**SourceDisksFiles**](inf-sourcedisksfiles-section.md)

[**SourceDisksNames**](inf-sourcedisksnames-section.md)

[**Strings**](inf-strings-section.md)

[**UpdateInis**](inf-updateinis-directive.md)

[**Version**](inf-version-section.md)
