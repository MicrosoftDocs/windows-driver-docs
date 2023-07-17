---
title: INF BitReg directive
description: A BitReg directive references one or more INF-writer-defined sections used to set or clear bits within an existing REG_BINARY-type value entry in the registry (this directive is rarely used in device/driver INF files).
keywords:
- INF BitReg Directive Device and Driver Installation
topic_type:
- apiref
ms.topic: reference
api_name:
- INF BitReg Directive
api_type:
- NA
ms.date: 07/08/2022
---

# INF BitReg directive

> [!CAUTION]
> Starting with Windows 11 version 22H2, a driver package using this directive will no longer be able to receive a signature from Hardware Developer Center.
  
> [!CAUTION]
> If you are building a universal or Windows Driver package, this directive is not valid. See [Using a Universal INF File](using-a-universal-inf-file.md) and [Getting Started with Windows Drivers](../develop/getting-started-with-windows-drivers.md).

A **BitReg** directive references one or more INF-writer-defined sections used to set or clear bits within an existing [REG_BINARY](/windows/desktop/SysInfo/registry-value-types)-type value entry in the registry. However, this directive is rarely used in device/driver INF files.

```inf
[DDInstall] | 
[DDInstall.HW] | 
[DDInstall.CoInstallers] | 
[ClassInstall32] | 
[ClassInstall32.ntx86] | 
[ClassInstall32.ntia64] | (Windows XP and later versions of Windows)
[ClassInstall32.ntamd64] | (Windows XP and later versions of Windows)
[ClassInstall32.ntarm] | (Windows 8 and later versions of Windows)
[ClassInstall32.ntarm64] (Windows 10 version 1709 and later versions of Windows)
 
BitReg=bit-registry-section[,bit-registry-section]...
```

A **BitReg** directive can be specified under any of the sections shown in the formal syntax statement above. This directive can also be specified under any of the following INF-writer-defined sections:

- A *service-install-section* or *event-log-install* section referenced by the [**AddService**](inf-addservice-directive.md) directive in a DDInstall.Services section.
- An *add-interface-section* referenced by the [**AddInterface**](inf-addinterface-directive.md) directive in a [***DDInstall*.Interfaces**](inf-ddinstall-interfaces-section.md) section.
- An *install-interface-section* referenced in an [**InterfaceInstall32**](inf-interfaceinstall32-section.md) section

Each named section referenced by a **BitReg** directive has the following form:

```inf
[bit-registry-section]
reg-root, [subkey], value-entry-name, [flags], byte-mask, byte-to-modify
reg-root, [subkey], value-entry-name, [flags], byte-mask, byte-to-modify
...
```

A *bit-registry-section* can have any number of entries, each on a separate line.

## Entries

*reg-root*  
Identifies the root of the registry tree for other values supplied in this entry. The value can be one of the following:

**HKCR**  
Abbreviation for **HKEY_CLASSES_ROOT**.

**HKCU**  
Abbreviation for **HKEY_CURRENT_USER**.

**HKLM**  
Abbreviation for **HKEY_LOCAL_MACHINE**.

**HKU**  
Abbreviation for **HKEY_USERS**.

**HKR**  
Relative root − that is, keys that are specified by using this abbreviation are relative to the registry key associated with the INF section in which this **BitReg** directive appears, as indicated in the following table.

| INF Section Containing BitReg Directive | Registry Key Referenced by HKR |
|--|--|
| INF [***DDInstall***](inf-ddinstall-section.md) section | The device's *software key* |
| INF [***DDInstall*.HW**](inf-ddinstall-hw-section.md) section | The device's *hardware key* |
| INF [***DDInstall*.Services**](inf-ddinstall-services-section.md) section | The **Services** key |

> [!NOTE]
> **HKR** cannot be used in a bit-registry-section referenced from an INF [***DefaultInstall***](inf-defaultinstall-section.md) section.

For more information about driver information that is stored under the **HKEY_LOCAL_MACHINE** root, see [Registry Trees and Keys for Devices and Drivers](registry-trees-and-keys.md).

*subkey*  
This optional value, expressed either as a %*strkey*% token defined in a [**Strings**](inf-strings-section.md) section of the INF or as a registry path under the given *reg-root* (*key1\\key2\\key3*...), specifies the key that contains the value entry to be modified.

*value-entry-name*  
Specifies the name of an existing [REG_BINARY](/windows/desktop/SysInfo/registry-value-types)-type value entry in the (existing) subkey to be modified. It can be expressed either as "*quoted string*" or as a %*strkey*% token that is defined in the INF's [**Strings**](inf-strings-section.md) section.

*flags*  
This optional hexadecimal value, expressed as an ORed bitmask of system-defined low word and high word flag values, specifies whether to clear or set the bits specified in the given byte-mask. Its default value is zero, which clears the bits in the 64-bit section of the registry.

Bitmask values for each of these flags are as follows:

**0x00000000** (FLG_BITREG_CLEARBITS)  
Clear the bits specified by *byte-mask*.

**0x00000001** (FLG_BITREG_SETBITS)  
Set the bits specified by *byte-mask*.

**0x00004000** (FLG_BITREG_32BITKEY) (Windows XP and later versions of Windows.)  
 Make the specified change in the 32-bit registry. If not specified, the change is made to the native registry.

*byte-mask*  
This byte-sized mask, expressed in hexadecimal notation, specifies which bits to clear or set in the current value of the given *value-entry-name*.

*byte-to-modify*  
This byte-sized value, expressed in decimal, specifies the zero-based index of the byte within the [REG_BINARY](/windows/desktop/SysInfo/registry-value-types)-type value to be modified.

## Remarks

Each *bit-registry-section* name must be unique to the INF file, but it can be referenced by **BitReg** directives in other sections of the same INF. Each INF-writer-created section name must be unique within the INF file and must follow the general rules for defining section names. For more information about these rules, see [General Syntax Rules for INF Files](general-syntax-rules-for-inf-files.md).

The value of an existing [REG_BINARY](/windows/desktop/SysInfo/registry-value-types)-type value entry can also be modified by overwriting its current value within an add-registry section elsewhere in the INF file. For more information about add-registry sections, see the reference for the [**AddReg**](inf-addreg-directive.md) directive.

Using a **BitReg** directive requires the definition of another INF file section. However, the value of an existing [REG_BINARY](/windows/desktop/SysInfo/registry-value-types)-type value entry can be modified bit-by-bit in such a section, thereby preserving the values of all remaining bits.

## Examples

The following example shows a bit-registry section for a fictional application.

```inf
[AppX_BitReg]
; set first bit of byte 0 in ProgramData value entry
HKLM,Software\AppX,ProgramData,1,0x01,0 
; preceding would change value 30,00,10 to 31,00,10

; clear high bit of byte 2 in ProgramData value entry
HKLM,Software\AppX,ProgramData,,0x80,2
; preceding would change value 30,00,f0 to 30,00,70

; set second and third bits of byte 1 in ProgramData value entry
HKLM,Software\AppX,ProgramData,1,0x06,1
; preceding would change value 30,00,f0 to 30,06,f0
```

## See also

[**AddInterface**](inf-addinterface-directive.md)

[**AddReg**](inf-addreg-directive.md)

[**AddService**](inf-addservice-directive.md)

[**ClassInstall32**](inf-classinstall32-section.md)

[***DDInstall***](inf-ddinstall-section.md)

[***DDInstall*.CoInstallers**](inf-ddinstall-coinstallers-section.md)

[***DDInstall*.HW**](inf-ddinstall-hw-section.md)

[**InterfaceInstall32**](inf-interfaceinstall32-section.md)
