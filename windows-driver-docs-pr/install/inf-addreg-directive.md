---
title: INF AddReg Directive
description: An AddReg directive references one or more INF-writer-defined add-registry-sections that are used to modify or create registry information.
ms.assetid: e8162e20-0d8c-4400-9f4d-5f4abe81305b
keywords:
- INF AddReg Directive Device and Driver Installation
topic_type:
- apiref
api_name:
- INF AddReg Directive
api_type:
- NA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# INF AddReg Directive


An **AddReg** directive references one or more INF-writer-defined *add-registry-sections* that are used to modify or create registry information.

```cpp
[DDInstall] | 
[DDInstall.HW] | 
[DDInstall.CoInstallers] | 
[ClassInstall32] | 
[ClassInstall32.ntx86] | 
[ClassInstall32.ntia64] |  (Windows XP and later versions of Windows)
[ClassInstall32.ntamd64]  (Windows XP and later versions of Windows) 
[install-interface-section] | 
[service-install-section] | 
[event-log-install] | 
[add-interface-section]
AddReg=add-registry-section[,add-registry-section] ...
```

Each *add-registry section* can have entries to do the following:

-   Add new keys, possibly with initial value entries, to the registry.
-   Add new value entries to existing registry keys.
-   Modify existing value entries of particular keys in the registry.

Each named *add-registry section* referenced by an **AddReg** directive has the following format:

```cpp
[add-registry-section]
reg-root, [subkey],[value-entry-name],[flags],[value][,[value]]
reg-root, [subkey],[value-entry-name],[flags],[value][,[value]]
 ...
[[add-registry-section.security]
"security-descriptor-string"]
```

An *add-registry-section* can have any number of entries, each on a separate line. An INF can also contain one or more optional <em>add-registry-section</em>**.security** sections, each specifying a security descriptor that is applied to all registry values described within a named *add-registry-section*.

## Entries


<a href="" id="reg-root"></a>*reg-root*  
Identifies the root of the registry tree for other values supplied in this entry. The value can be one of the following:

<a href="" id="hkcr"></a>**HKCR**  
Abbreviation for **HKEY_CLASSES_ROOT**

<a href="" id="hkcu"></a>**HKCU**  
Abbreviation for **HKEY_CURRENT_USER**

<a href="" id="hklm"></a>**HKLM**  
Abbreviation for **HKEY_LOCAL_MACHINE**

<a href="" id="hku"></a>**HKU**  
Abbreviation for **HKEY_USERS**

<a href="" id="hkr"></a>**HKR**  
Relative root, in which keys that are specified by using this abbreviation are relative to the registry key associated with the INF section in which this **AddReg** directive appears, as indicated in the following table.

| INF Section Containing AddReg Directive                        | Registry Key Referenced by HKR                                                        |
|----------------------------------------------------------------|---------------------------------------------------------------------------------------|
| INF [***DDInstall***](inf-ddinstall-section.md) section       | The device's [*software key*](https://msdn.microsoft.com/library/windows/hardware/ff556336#wdkgloss-software-key) |
| INF [***DDInstall*.HW**](inf-ddinstall-hw-section.md) section | The device's [*hardware key*](https://msdn.microsoft.com/library/windows/hardware/ff556288#wdkgloss-hardware-key) |
| INF *\[service-install-section\]* section                      | The **Services** key                                                                  |
| INF *\[event-log-install\]* section                            | The **EventLog** key                                                                  |
| INF *\[add-interface-section\]* section                        | The device interface's registry key                                                    |


**Note**  **HKR** cannot be used in an *add-registry-section* referenced from an [**INF DefaultInstall section**](inf-defaultinstall-section.md).

 

For more information about driver information that is stored under the **HKEY_LOCAL_MACHINE** root, see [Registry Trees and Keys for Devices and Drivers](registry-trees-and-keys.md).

<a href="" id="subkey"></a>*subkey*  
This optional value, formed either as a %*strkey*% token defined in a [**Strings**](inf-strings-section.md) section of the INF or as a registry path under the given *reg-root* (<em>key1</em>**\\**<em>key2</em>**\\**<em>key3</em>...), specifies one of the following:

-   A new subkey to be added to the registry at the end of the given registry path.
-   An existing subkey in which the additional values specified in this entry is written (possibly replacing the value of an existing named value entry of the given subkey).
-   Both a new subkey to be added to the registry together with its initial value entry.

<a href="" id="value-entry-name"></a>*value-entry-name*  
This optional value either names an existing value entry in the given (existing) *subkey* or creates the name of a new value entry to be added in the specified *subkey*, whether it already exists or is a new key to be added to the registry. This value can be expressed either as **"**<em>quoted string</em>**"** or as a %*strkey*% token that is defined in the INF's [**Strings**](inf-strings-section.md) section. (If this is omitted for a string-type value, the *value-entry-name* is the default "unnamed" value entry for this key.)

The operating system supports some system-defined special *value-entry-name* keywords. See the end of this **Remarks** section for more information.

<a href="" id="flags"></a>*flags*  
This optional hexadecimal value, expressed as an ORed bitmask of system-defined low word and high word flag values, defines the data type for a value entry and/or controls the add-registry operation.

Bitmask values for each of these flags are as follows:

<a href="" id="0x00000001--flg-addreg-binvaluetype---"></a>**0x00000001** (FLG_ADDREG_BINVALUETYPE)   
The given value is "raw" data. (This value is identical to the FLG_ADDREG_TYPE_BINARY.)

<a href="" id="0x00000002--flg-addreg-noclobber---"></a>**0x00000002** (FLG_ADDREG_NOCLOBBER)   
Prevent a given value from replacing the value of an existing value entry.

<a href="" id="0x00000004--flg-addreg-delval-"></a>**0x00000004** (FLG_ADDREG_DELVAL)  
Delete the given *subkey* from the registry, or delete the specified *value-entry-name* from the specified registry *subkey*.

<a href="" id="0x00000008--flg-addreg-append--"></a>**0x00000008** (FLG_ADDREG_APPEND)   
Append a given *value* to that of an existing named value entry. This flag is valid only if FLG_ADDREG_TYPE_MULTI_SZ is also set. The specified string value is not appended if it already exists.

<a href="" id="0x00000010--flg-addreg-keyonly-"></a>**0x00000010** (FLG_ADDREG_KEYONLY)  
Create the given *subkey*, but ignore any supplied value-entry-name and/or value.

<a href="" id="0x00000020--flg-addreg-overwriteonly--"></a>**0x00000020** (FLG_ADDREG_OVERWRITEONLY)   
Reset to the supplied *value* only if the specified *value-entry-name* already exists in the given *subkey*.

<a href="" id="0x00001000--flg-addreg-64bitkey--"></a>**0x00001000** (FLG_ADDREG_64BITKEY)   
(Windows XP and later versions of Windows.) Make the specified change in the 64-bit registry. If not specified, the change is made to the native registry.

<a href="" id="0x00002000--flg-addreg-keyonly-common-"></a>**0x00002000** (FLG_ADDREG_KEYONLY_COMMON)  
(Windows XP and later versions of Windows.) This is the same as FLG_ADDREG_KEYONLY but also works in a *del-registry-section* of an [**INF DelReg directive**](inf-delreg-directive.md).

<a href="" id="0x00004000--flg-addreg-32bitkey-"></a>**0x00004000** (FLG_ADDREG_32BITKEY)  
(Windows XP and later versions of Windows.) Make the specified change in the 32-bit registry. If not specified, the change is made to the native registry.

<a href="" id="0x00000000--flg-addreg-type-sz-"></a>**0x00000000** (FLG_ADDREG_TYPE_SZ)  
The given value entry and/or value is of type [REG_SZ](https://docs.microsoft.com/windows/desktop/SysInfo/registry-value-types).

**Note**  This value is the default type for a specified value entry, so the flags value can be omitted from any r*eg-root=* line in an *add-registry-section* that operates on a value entry of this type.

 

<a href="" id="0x00010000--flg-addreg-type-multi-sz-"></a>**0x00010000** (FLG_ADDREG_TYPE_MULTI_SZ)  
The given value entry and/or value is of the registry type [REG_MULTI_SZ](https://docs.microsoft.com/windows/desktop/SysInfo/registry-value-types). The value field that follows can be a list of strings separated by commas. This specification does not require any NULL terminator for a given string value.

<a href="" id="0x00020000--flg-addreg-type-expand-sz--"></a>**0x00020000** (FLG_ADDREG_TYPE_EXPAND_SZ)   
The given *value-entry-name* and/or *value* is of the registry type [REG_EXPAND_SZ](https://docs.microsoft.com/windows/desktop/SysInfo/registry-value-types).

<a href="" id="0x00010001--flg-addreg-type-dword---flg-addreg-type-dword-"></a>**0x00010001** (FLG_ADDREG_TYPE_DWORD) (FLG_ADDREG_TYPE_DWORD)  
The given *value-entry-name* and/or *value* is of the registry type [REG_DWORD](https://docs.microsoft.com/windows/desktop/SysInfo/registry-value-types).

<a href="" id="0x00020001--flg-addreg-type-none-"></a>**0x00020001** (FLG_ADDREG_TYPE_NONE)  
The given *value-entry-name* and/or *value* is of the registry type [REG_NONE](https://docs.microsoft.com/windows/desktop/SysInfo/registry-value-types).

<a href="" id="value"></a>*value*  
This optionally specifies a new value for the specified *value-entry-name* to be added to the given registry key. Such a *value* can be a "replacement" value for an existing named value entry in an existing key, a value to be appended (*flag* value **0x00010008**) to an existing named [REG_MULTI_SZ](https://docs.microsoft.com/windows/desktop/SysInfo/registry-value-types)-type value entry in an existing key, a new value entry to be written into an existing key, or the initial value entry for a new *subkey* to be added to the registry.

The expression of such a *value* depends on the registry type specified for the *flag*, as follows:

-   A registry string-type value can be expressed either as a "*quoted string*" or as a %*strkey*% token defined in a [**Strings**](inf-strings-section.md) section of the INF file. Such an INF-specified value does not have to include a NULL terminator at the end of each string.
-   A registry numerical-type value can be expressed as a hexadecimal (by using 0x notation) or decimal number.

<a href="" id="security-descriptor-string"></a>*security-descriptor-string*  
Specifies a security descriptor, to be applied to all registry entries created by the named *add-registry-section*. The *security-descriptor-string* is a string with tokens to indicate the DACL (**D:**) security component.

If an <em>add-registry-section</em>**.security** section is not specified, registry entries inherit the security settings of the parent key.

If an <em>add-registry-section</em>**.security** section is specified, the following ACE's must be included so that installations and upgrades of devices and system service packs can occur:

-   (A;;GA;;;SY) − Grants all access to the local system.
-   (A;;GA;;;BA) − Grants all access to built-in administrators.

Do *not* specify ACE strings that grant write access to nonprivileged users.

For information about security descriptor strings, see [Security Descriptor Definition Language (Windows)](https://msdn.microsoft.com/library/windows/desktop/aa379567). For information about the format of security descriptor strings, see Security Descriptor Definition Language (Windows).

For more information about how to specify security descriptors, see [Creating Secure Device Installations](creating-secure-device-installations.md).

Remarks
-------

An **AddReg** directive can be specified under any of the sections shown in the formal syntax statement above. This directive can also be specified under any of the following INF-writer-defined sections:

-   A *service-install-section* or *event-log-install* section referenced by the [**AddService**](inf-addservice-directive.md) directive in an [**INF *DDInstall*.Services section**](inf-ddinstall-services-section.md).
-   An *add-interface-section* referenced by the [**AddInterface**](inf-addinterface-directive.md) directive in an [**INF *DDInstall*.Interfaces section**](inf-ddinstall-interfaces-section.md).
-   An *install-interface-section* referenced in an [**INF InterfaceInstall32 section**](inf-interfaceinstall32-section.md).

Each *add-registry-section* name must be unique to the INF file, but it can be referenced by **AddReg** directives in other sections of the same INF. Each section name must follow the general rules for defining section names described in [General Syntax Rules for INF Files](general-syntax-rules-for-inf-files.md).

**Note**  The lower-order bit of the low word in a flag value distinguishes between character and binary data.

 

To represent a number of a registry type other than one of the predefined REG_*XXX* types, specify a new type number in the high word of the *flag* ORed with FLG_ADDREG_BINVALUETYPE in its low word. The data for such a *value* must be specified in binary format as a sequence of bytes separated by commas. For example, to store 16 bytes of data of a new registry data type, such as 0x38, as a value entry, the add-registry section entry would be something like the following:

```cpp
HKR,,MYValue,0x00380001,1,0,2,3,4,5,6,7,8,9,A,B,C,D,E,F
```

This technique can be used to define new registry types for numeric values, but not for values of type [REG_EXPAND_SZ](https://docs.microsoft.com/windows/desktop/SysInfo/registry-value-types), [REG_MULTI_SZ](https://docs.microsoft.com/windows/desktop/SysInfo/registry-value-types), [REG_NONE](https://docs.microsoft.com/windows/desktop/SysInfo/registry-value-types), or [REG_SZ](https://docs.microsoft.com/windows/desktop/SysInfo/registry-value-types). For more info about these types, see [Registry value types](https://docs.microsoft.com/windows/desktop/SysInfo/registry-value-types).

### Special *value-entry-name* Keywords

Special keywords are defined for use in the HKR **AddReg** entries. The format for the entries that use these keywords is as follows:

```cpp
[HKR,,DeviceCharacteristics,0x10001,characteristics] 
[HKR,,DeviceType,0x10001,device-type] 
[HKR,,Security,,security-descriptor-string] 
[HKR,,UpperFilters,0x10000,service-name] 
[HKR,,LowerFilters,0x10000,service-name] 
[HKR,,Exclusive,0x10001,exclusive-device] 
[HKR,,EnumPropPages32,,"prop-provider.dll,provider-entry-point"]
[HKR,,LocationInformationOverride,,"text-string"] 
[HKR,,ResourcePickerTags,,"text-string"] 
[HKR,,ResourcePickerExceptions,,"text-string"] ,
```

The following describes the HKR **AddReg** entries that use these special keywords:

<a href="" id="devicecharacteristics"></a>**DeviceCharacteristics**  
A **DeviceCharacteristics** HKR **AddReg** entry specifies characteristics for the device. The *characteristics* value is a numeric value that is the result of using OR on one or more FILE_\* file characteristics values, which are defined in *Wdm.h* and *Ntddk.h*.

Only the following values can be specified in an INF:

```cpp
#define FILE_REMOVABLE_MEDIA            0x00000001
#define FILE_READ_ONLY_DEVICE           0x00000002
#define FILE_FLOPPY_DISKETTE            0x00000004
#define FILE_WRITE_ONCE_MEDIA           0x00000008
#define FILE_DEVICE_SECURE_OPEN         0x00000100
```

For a description of these values, see [**IoCreateDevice**](https://msdn.microsoft.com/library/windows/hardware/ff548397).

The characteristics values, which are specified by using a **DeviceCharacteristics** entry, are ORed with those specified in each call to **IoCreateDevice** that creates a device object on the device stack. The OR operation occurs after all device objects are added, but before the device is started.

The *characteristics* value (including a value of zero) overrides any class-wide device characteristics that were specified in the associated class installer INF.

For more information about device characteristics, see [Specifying Device Characteristics](https://msdn.microsoft.com/library/windows/hardware/ff563818).

<a href="" id="devicetype"></a>**DeviceType**  
A **DeviceType** HKR **AddReg** entry specifies a device type for the device. The device-type is the numeric value of a FILE_DEVICE_*XXX* constant defined in *Wdm.h* or *Ntddk.h*. The flag value of 0x10001 specifies that the device-type value is a [REG_DWORD](https://docs.microsoft.com/windows/desktop/SysInfo/registry-value-types). For more information, see [Specifying Device Types](https://msdn.microsoft.com/library/windows/hardware/ff563821).

A class-installer INF should specify the device type that applies to all, or almost all, of the devices in the class. For example, if the devices in the class are of type FILE_DEVICE_CD_ROM, specify a *device-type* of 0x02. If a device INF specifies a value for **DeviceType**, it overrides the value set by the class installer, if any. If the class or device INF specifies a **DeviceType** value, the PnP manager applies that type to the [*physical device object (PDO)*](https://msdn.microsoft.com/library/windows/hardware/ff556325#wdkgloss-physical-device-object--pdo-) created by the device's bus driver.

<a href="" id="security"></a>**Security**  
A **Security** HKR **AddReg** entry specifies a security descriptor for the device. The *security-descriptor-string* is a string with tokens to indicate the DACL (**D:**) security component.

A class-installer INF can specify a security descriptor for a device class. A device INF can specify a security descriptor for an individual device, overriding the security for the class. If the class and/or device INF specifies a *security-descriptor-string*, the PnP manager propagates the descriptor to all the device objects ( [*DOs*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-object)) for a device. This includes the function device object ([*FDO*](https://msdn.microsoft.com/library/windows/hardware/ff556280#wdkgloss-fdo)), optional [*filter DOs*](https://msdn.microsoft.com/library/windows/hardware/ff556280#wdkgloss-filter-device-object), and the PDO.

For information about the format of security descriptor strings, see the Microsoft Windows SDK documentation.

For more information about how to specify security descriptors, see [Creating Secure Device Installations](creating-secure-device-installations.md).

<a href="" id="upperfilters"></a>**UpperFilters**  
An **UpperFilters** HKR **AddReg** entry specifies a PnP upper-filter driver. This entry in a [***DDInstall*.HW**](inf-ddinstall-hw-section.md) section defines one or more device-specific upper-filter drivers. In a [**ClassInstall32**](inf-classinstall32-section.md) section, this entry defines one or more class-wide upper-filter drivers.

<a href="" id="lowerfilters"></a>**LowerFilters**  
A **LowerFilters** HKR **AddReg** entry specifies a PnP lower-filter driver. This entry in a <em>DDInstall</em>**.HW section** defines one or more device-specific lower-filter drivers. In a **ClassInstall32** section, this entry defines one or more class-wide lower-filter drivers.

<a href="" id="exclusive"></a>**Exclusive**  
An **Exclusive** HKR **AddReg** entry, if it exists and is set to "1", specifies that the device is an [*exclusive device*](https://msdn.microsoft.com/library/windows/hardware/ff556279#wdkgloss-exclusive-device). Otherwise the device is not treated as exclusive. For more information, see [Specifying Exclusive Access to Device Objects](https://msdn.microsoft.com/library/windows/hardware/ff563827).

<a href="" id="enumproppages32"></a>**EnumPropPages32**  
An **EnumPropPages32** HKR **AddReg** entry specifies the name of a dynamic-link library (*DLL*) file that is a device-specific property page provider. It also specifies the name of the **ExtensionPropSheetPageProc** callback function as implemented by the DLL. For more information about property pages and functions, see the Microsoft Windows Software Development Kit (SDK) for Windows 7 and .NET Framework 4.0.

**Important**  Both the name of the DLL and **ExtensionPropSheetPageProc** callback function must be enclosed together within quotation marks (" ").

 

<a href="" id="locationinformationoverride"></a>**LocationInformationOverride**  
(Windows XP and later versions of Windows) A **LocationInformationOverride** HKR **AddReg** entry can be used to specify a text string that describes a device's physical location. It overrides the **LocationInformation** string that the device's bus driver supplies in response to an [**IRP_MN_QUERY_DEVICE_TEXT**](https://msdn.microsoft.com/library/windows/hardware/ff551674) request.

<a href="" id="resourcepickertags"></a>**ResourcePickerTags**  
A **ResourcePickerTags** HKR **AddReg** entry specifies resource picker tags for a device.

<a href="" id="resourcepickerexceptions"></a>**ResourcePickerExceptions**  
A **ResourcePickerExceptions** HKR **AddReg** entry specifies the resource conflicts that are allowed for a device.

Examples
--------

An **AddReg** directive referenced the (SCSI) Miniport_EventLog_AddReg section in this example, under an INF-writer-defined section referenced by the **AddService** directive in a <em>DDInstall</em>**.Services** section of this INF.

```cpp
[Miniport_EventLog_AddReg]
HKR,,EventMessageFile,0x00020000,"%%SystemRoot%%\System32\IoLogMsg.dll" 
; double quotation marks delimiters in preceding entry prevent truncation 
; if line wraps
 
HKR,,TypesSupported,0x00010001,7 
```

## See also


[**AddInterface**](inf-addinterface-directive.md)

[**AddService**](inf-addservice-directive.md)

[**BitReg**](inf-bitreg-directive.md)

[**ClassInstall32**](inf-classinstall32-section.md)

[***DDInstall***](inf-ddinstall-section.md)

[***DDInstall*.CoInstallers**](inf-ddinstall-coinstallers-section.md)

[***DDInstall*.HW**](inf-ddinstall-hw-section.md)

[***DDInstall*.Interfaces**](inf-ddinstall-interfaces-section.md)

[***DDInstall*.Services**](inf-ddinstall-services-section.md)

[**DelReg**](inf-delreg-directive.md)

[**InterfaceInstall32**](inf-interfaceinstall32-section.md)

[**Strings**](inf-strings-section.md)

 

 






