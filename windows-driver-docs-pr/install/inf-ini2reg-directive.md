---
title: INF Ini2Reg Directive
description: An Ini2Reg directive references one or more named sections in which lines or sections from a supplied INI file are moved into the registry. This creates or replaces one or more value entries under a specified key.
keywords:
- INF Ini2Reg Directive Device and Driver Installation
topic_type:
- apiref
ms.topic: reference
api_name:
- INF Ini2Reg Directive
api_type:
- NA
ms.date: 07/17/2023
---

# INF Ini2Reg directive

[!INCLUDE [Caution invalid INF directive](../includes/inf-directive-invalid-22h2.md)]

An **Ini2Reg** directive references one or more named sections in which lines or sections from a supplied INI file are moved into the registry. This creates or replaces one or more value entries under a specified key.

```inf
[DDInstall] | 
[DDInstall.CoInstallers] | 
[ClassInstall32] | 
[ClassInstall32.ntx86] | 
[ClassInstall32.ntia64] | (Windows XP and later versions of Windows)
[ClassInstall32.ntamd64] | (Windows XP and later versions of Windows)
[ClassInstall32.ntarm] | (Windows 8 and later versions of Windows)
[ClassInstall32.ntarm64] (Windows 10 version 1709 and later versions of Windows)
  
Ini2Reg=ini-to-registry-section[,ini-to-registry-section]...
```

Each named section referenced by an **Ini2Reg** directive has the following form:

```inf
[ini-to-registry-section]
 
ini-file,ini-section,[ini-key],reg-root,subkey[,flags]
...
```

An *ini-to-registry-section* can have any INF-writer-determined number of entries, each on a separate line.

## Entries

*ini-file*  
Specifies the name of an INI file supplied on the source media. This value can be expressed as a *filename* or as a %*strkey*% token that is defined in a [**Strings**](inf-strings-section.md) section of the INF file.

*ini-section*  
Specifies the name of the section within the given INI file that contains the registry information to be copied.

*ini-key*  
Specifies the name of the key in the INI file to copy to the registry. If this value is omitted, the whole *ini-section* is to be transferred to the specified registry *subkey*.

*reg-root*  
Identifies the root of the registry tree for other values supplied in this entry. For specifics, see the reference for the [**AddReg directive**](inf-addreg-directive.md).

*subkey*  
Identifies the subkey to receive the value, expressed either as a %*strkey*% token defined in a [**Strings**](inf-strings-section.md) section of the INF or as an explicit registry path (_key1_**\\**_key2_**\\**_key3_...) from the given *reg-root*.

*flags*  
Specifies (in bit 0) how to handle the INI file after transferring the given information to the registry and/or (in bit 1) whether to overwrite existing registry information, as follows:

Bit zero = **0**  
Do not remove the given information from the INI file after copying it into the registry. This is the default.

Bit zero = **1**  
Delete the given information from the INI file after moving it into the registry.

Bit one = **0**  
If the specified subkey already exists in the registry, do not transfer the INI-supplied information into this *subkey*. Otherwise, create the specified *subkey* in the registry with this INI-supplied information as its value entry. This is the default.

Bit one = **1**  
If the specified subkey already exists in the registry, replace its value entry with the INI-supplied information.

## Remarks

The **Ini2Reg** directive is valid in any of the sections shown in the formal syntax statement. This directive is also valid in INF-writer-defined sections referenced by an [**AddInterface**](inf-addinterface-directive.md) directive or referenced in an [**InterfaceInstall32**](inf-interfaceinstall32-section.md) section.

If an INF file is used to install devices on Windows XP and later versions of Windows, the INF file should not contain **Ini2Reg** directives. INF files that contain **Ini2Reg** directives will not pass ["Designed For Windows" logo testing](/windows-hardware/drivers), will not receive a digital signature, and therefore will be untrusted by Windows (see [How Windows Selects Drivers](./how-windows-selects-a-driver-for-a-device.md)).

Each *ini-to-registry-section* name must be unique to the INF file. Each INF-writer-created section name must be unique within the INF file and must follow the general rules for defining section names. For more information about these rules, see [General Syntax Rules for INF Files](general-syntax-rules-for-inf-files.md).

The INF provides the full path of the given *ini-file* on the distribution media in one of the following ways:

- In IHV/OEM-supplied INF files, by using the [**SourceDisksNames**](inf-sourcedisksnames-section.md) and, possibly, [**SourceDisksFiles**](inf-sourcedisksfiles-section.md) sections of this INF to explicitly specify the full path of each named source file that is not in the root directory (or directories) on the distribution media.

- In system-supplied INF files, by supplying one or more additional INF files, identified in the **LayoutFile** entry in the [**Version**](inf-version-section.md) section of the INF file.

## See also

[**AddInterface**](inf-addinterface-directive.md)

[**AddReg**](inf-addreg-directive.md)

[**ClassInstall32**](inf-classinstall32-section.md)

[***DDInstall***](inf-ddinstall-section.md)

[**InterfaceInstall32**](inf-interfaceinstall32-section.md)

[**SourceDisksFiles**](inf-sourcedisksfiles-section.md)

[**SourceDisksNames**](inf-sourcedisksnames-section.md)

[**Strings**](inf-strings-section.md)

[**UpdateIniFields**](inf-updateinifields-directive.md)

[**UpdateInis**](inf-updateinis-directive.md)

[**Version**](inf-version-section.md)
