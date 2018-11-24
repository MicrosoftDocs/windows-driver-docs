---
title: INF DelReg Directive
description: A DelReg directive references one or more INF-writer-defined sections describing keys and/or value entries to be removed from the registry.
ms.assetid: a456327f-9b2c-42e6-a575-47ad788aa8b1
keywords:
- INF DelReg Directive Device and Driver Installation
topic_type:
- apiref
api_name:
- INF DelReg Directive
api_type:
- NA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# INF DelReg Directive


**Note**  If you are building a universal or mobile driver package, this directive is not valid. See [Using a Universal INF File](using-a-universal-inf-file.md).

 

A **DelReg** directive references one or more INF-writer-defined sections describing keys and/or value entries to be removed from the registry.

```cpp
[DDInstall] | 
[DDInstall.CoInstallers] | 
[ClassInstall32] | 
[ClassInstall32.ntx86] | 
[ClassInstall32.ntia64] |  (Windows XP and later versions of Windows)
[ClassInstall32.ntamd64]  (Windows XP and later versions of Windows)
 
DelReg=del-registry-section[,del-registry-section]...
```

Each *del-registry-section* referenced by a **DelReg** directive has the following form:

```cpp
[del-registry-section]
reg-root-string,subkey[,value-entry-name][,flags][,value]
reg-root-string,subkey[,value-entry-name][,flags][,value]
...
```

A *del-registry-section* can have any number of entries, each on a separate line.

## Entries


<a href="" id="reg-root-string"></a>*reg-root-string*  
Identifies the root of the registry tree for other values supplied in this entry. The value can be one of the following:

<a href="" id="hkcr"></a>**HKCR**  
Abbreviation for **HKEY_CLASSES_ROOT**.

<a href="" id="hkcu"></a>**HKCU**  
Abbreviation for **HKEY_CURRENT_USER**.

<a href="" id="hklm"></a>**HKLM**  
Abbreviation for **HKEY_LOCAL_MACHINE**.

<a href="" id="hku"></a>**HKU**  
Abbreviation for **HKEY_USERS**.

<a href="" id="hkr"></a>**HKR**  
Relative root, in which keys that are specified by using this abbreviation are relative to the registry key associated with the INF section in which this **DelReg** directive appears, as indicated in the following table.

| NF Section Containing AddReg Directive                                     | Registry Key Referenced by HKR                                                        |
|----------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| INF [***DDInstall***](inf-ddinstall-section.md) section                   | The device's [*software key*](https://msdn.microsoft.com/library/windows/hardware/ff556336#wdkgloss-software-key) |
| INF [***DDInstall*.HW**](inf-ddinstall-hw-section.md) section             | The device's [*hardware key*](https://msdn.microsoft.com/library/windows/hardware/ff556288#wdkgloss-hardware-key) |
| INF [***DDInstall*.Services**](inf-ddinstall-services-section.md) section | The **Services** key                                                                  |

 

**Note**  **HKR** cannot be used in an *del-registry-section* referenced from an [**INF DefaultInstall section**](inf-defaultinstall-section.md).

 

For more information about driver information that is stored under the **HKEY_LOCAL_MACHINE** root, see [Registry Trees and Keys for Devices and Drivers](registry-trees-and-keys.md).

<a href="" id="subkey"></a>*subkey*  
This optional value, formed either as a %*strkey*% token defined in a [**Strings**](inf-strings-section.md) section of the INF or as a registry path under the given *reg-root* (<em>key1</em>**\\**<em>key2</em>**\\**<em>key3</em>...), specifies one of the following:

-   A subkey to be deleted from the registry at the end of the given registry path
-   An existing subkey from which the given value-entry-name is to be deleted

<a href="" id="value-entry-name"></a>*value-entry-name*  
This value identifies a named value entry to be removed from the given subkey. This value and its preceding comma should be omitted if the subkey itself is being removed from the registry.

<a href="" id="flags"></a>*flags*  
(Windows XP and later versions of Windows.) This optional hexadecimal value, expressed as an ORed bitmask of system-defined low word and high word flag values, defines the data type for a value entry, or controls the delete-registry operation. If *flags* is not specified, the *value-entry-name* (if specified) or *subkey* will be deleted.

Bitmask values for each of these flags are as follows:

<a href="" id="0x00002000--flg-delreg-keyonly-common---"></a>**0x00002000** (FLG_DELREG_KEYONLY_COMMON)   
Delete the entire subkey.

<a href="" id="0x00004000---flg-delreg-32bitkey-"></a>**0x00004000** (FLG_DELREG_32BITKEY)  
Make the specified change in the 32-bit registry. If not specified, the change is made to the native registry.

<a href="" id="0x00018002--flg-delreg-multi-sz-delstring-"></a>**0x00018002** (FLG_DELREG_MULTI_SZ_DELSTRING)  
Within a multistring registry entry, delete all strings matching a string value specified by value. Case is ignored.

<a href="" id="value"></a>*value*  
(Windows XP and later versions of Windows.) Specifies a registry value, if *flags* indicates that a registry value is required.

Remarks
-------

A **DelReg** directive can be specified under any of the sections shown in the formal syntax statement above. This directive can also be specified under any of the following INF-writer-defined sections:

-   A *service-install-section* or *event-log-install* section referenced by the [**AddService**](inf-addservice-directive.md) directive in an [**INF *DDInstall*.Services section**](inf-ddinstall-services-section.md).
-   An *add-interface-section* referenced by the [**AddInterface**](inf-addinterface-directive.md) directive in an [**INF *DDInstall*.Interfaces section**](inf-ddinstall-interfaces-section.md).
-   An *install-interface-section* referenced in an [**INF InterfaceInstall32 section**](inf-interfaceinstall32-section.md).

In general, an INF should never attempt to delete subkeys or value entries within existing subkeys that were set up by system components or by the INF files for other devices. The purpose of a *delete-registry section* is to clean stale registry information from a previous installation by using a new INF file supplied by the same provider.

Each *del-registry-section* name must be unique to the INF file, but it can be referenced by **DelReg** directives in other sections of the same INF. Each section name must follow the general rules for defining section names. For more information about these rules, see [General Syntax Rules for INF Files](general-syntax-rules-for-inf-files.md).

With operating system versions prior to Windows XP, the only way to delete a key is by specifying the following:

```cpp
reg-root-string, subkey
```

For Windows XP and later versions of Windows, the following is also permitted (to specify the 32-bit registry):

```cpp
reg-root-string, subkey,,0x4000
```

Examples
--------

This example shows how the system-supplied COM/LPT ports class installer's INF removes stale NT-specific registry information about COM ports from the registry.

```cpp
[ComPort.NT]
CopyFiles=ComPort.NT.Copy
AddReg=ComPort.AddReg, ComPort.NT.AddReg
 ... ; more directives omitted here

[ComPort.NT.HW]
DelReg=ComPort.NT.HW.DelReg

[ComPort.NT.Copy]
serial.sys
serenum.sys

[Comport.NT.AddReg]
HKR,,EnumPropPages32,,"MSPorts.dll,SerialPortPropPageProvider"

[ComPort.NT.HW.DelReg]
HKR,,UpperFilters
```

## See also


[**AddReg**](inf-addreg-directive.md)

[**AddInterface**](inf-addinterface-directive.md)

[**AddService**](inf-addservice-directive.md)

[**BitReg**](inf-bitreg-directive.md)

[**ClassInstall32**](inf-classinstall32-section.md)

[***DDInstall***](inf-ddinstall-section.md)

[***DDInstall*.CoInstallers**](inf-ddinstall-coinstallers-section.md)

[***DDInstall*.HW**](inf-ddinstall-hw-section.md)

[***DDInstall*.Services**](inf-ddinstall-services-section.md)

[**InterfaceInstall32**](inf-interfaceinstall32-section.md)

[**Strings**](inf-strings-section.md)

 

 






