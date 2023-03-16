---
title: INF AddReg directive
description: An AddReg directive references one or more INF-writer-defined add-registry-sections that are used to modify or create registry information.
keywords:
- INF AddReg Directive Device and Driver Installation
topic_type:
- apiref
ms.topic: reference
api_name:
- INF AddReg Directive
api_type:
- NA
ms.date: 06/14/2022
---

# INF AddReg directive

An **AddReg** directive references one or more INF-writer-defined _add-registry-sections* that are used to modify or create registry information.

```inf
[DDInstall] | 
[DDInstall.HW] | 
[DDInstall.CoInstallers] | 
[ClassInstall32] | 
[ClassInstall32.ntx86] | 
[ClassInstall32.ntia64] | (Windows XP and later versions of Windows)
[ClassInstall32.ntamd64] | (Windows XP and later versions of Windows) 
[ClassInstall32.ntarm] | (Windows 8 and later versions of Windows) 
[ClassInstall32.ntarm64] | (Windows 10 version 1709 and later versions of Windows) 
[install-interface-section] | 
[service-install-section] | 
[event-log-install] | 
[add-interface-section]

AddReg=add-registry-section[,add-registry-section] ...
```

Each _add-registry-section_ can have entries to do the following:

- Add new keys, possibly with initial value entries, to the registry.

- Add new value entries to existing registry keys.

- Modify existing value entries of particular keys in the registry.

Each named _add-registry-section_ referenced by an **AddReg** directive has the following format:

```inf
[add-registry-section]
reg-root,[subkey],[value-entry-name],[flags],[value][,[value]]
reg-root,[subkey],[value-entry-name],[flags],[value][,[value]]
 ...

[[add-registry-section.security]
"security-descriptor-string"]
```

An _add-registry-section_ can have any number of entries, each on a separate line. An INF can also contain one or more optional _add-registry-section_**.security** sections, each specifying a security descriptor that is applied to all registry values described within a named _add-registry-section_.

## Entries

_reg-root_  
Identifies the root of the registry tree for other values supplied in this entry. The value can be one of the following:

**HKCR**  
Abbreviation for **HKEY_CLASSES_ROOT**

**HKCU**  
Abbreviation for **HKEY_CURRENT_USER**

**HKLM**  
Abbreviation for **HKEY_LOCAL_MACHINE**

**HKU**  
Abbreviation for **HKEY_USERS**

**HKR**  
Relative root, in which keys that are specified by using this abbreviation are relative to the registry key associated with the INF section in which this **AddReg** directive appears, as indicated in the following table.

| INF Section Containing AddReg Directive | Registry Key Referenced by HKR |
|--|--|
| INF [**_DDInstall_**](inf-ddinstall-section.md) section | The device's _software key_ |
| INF [**_DDInstall_.HW**](inf-ddinstall-hw-section.md) section | The device's _hardware key_ |
| INF _[service-install-section\]_ section | The **Services** key |
| INF _[event-log-install\]_ section | The **EventLog** key |
| INF _[add-interface-section\]_ section | The device interface's registry key |

> [!NOTE]
> **HKR** cannot be used in an _add-registry-section_ referenced from an [**INF DefaultInstall section**](inf-defaultinstall-section.md).

For more information about driver information that is stored under the **HKEY_LOCAL_MACHINE** root, see [Registry Trees and Keys for Devices and Drivers](registry-trees-and-keys.md).

_subkey_  
This optional value, formed either as a %_strkey_% token defined in a [**Strings**](inf-strings-section.md) section of the INF or as a registry path under the given _reg-root_ (_key1_**\\**_key2_**\\**_key3_...), specifies one of the following:

- A new subkey to be added to the registry at the end of the given registry path.
- An existing subkey in which the additional values specified in this entry is written (possibly replacing the value of an existing named value entry of the given subkey).
- Both a new subkey to be added to the registry together with its initial value entry.

_value-entry-name_  
This optional value either names an existing value entry in the given (existing) _subkey_ or creates the name of a new value entry to be added in the specified _subkey_, whether it already exists or is a new key to be added to the registry. This value can be expressed either as **"**_quoted string_**"** or as a %_strkey_% token that is defined in the INF's [**Strings**](inf-strings-section.md) section. (If this is omitted for a string-type value, the _value-entry-name_ is the default "unnamed" value entry for this key.)

The operating system supports some system-defined special _value-entry-name_ keywords. See the end of this **Remarks** section for more information.

_flags_  
This optional hexadecimal value, expressed as an ORed bitmask of system-defined low word and high word flag values, defines the data type for a value entry and/or controls the add-registry operation.

Bitmask values for each of these flags are as follows:

**0x00000001** (FLG_ADDREG_BINVALUETYPE)  
The given value is "raw" data. (This value is identical to the FLG_ADDREG_TYPE_BINARY.)

**0x00000002** (FLG_ADDREG_NOCLOBBER)  
Prevent a given value from replacing the value of an existing value entry.

**0x00000004** (FLG_ADDREG_DELVAL)  
Delete the given _subkey_ from the registry, or delete the specified _value-entry-name_ from the specified registry _subkey_.

**0x00000008** (FLG_ADDREG_APPEND)  
Append a given _value_ to that of an existing named value entry. This flag is valid only if FLG_ADDREG_TYPE_MULTI_SZ is also set. The specified string value is not appended if it already exists.

**0x00000010** (FLG_ADDREG_KEYONLY)  
Create the given _subkey_, but ignore any supplied value-entry-name and/or value.

**0x00000020** (FLG_ADDREG_OVERWRITEONLY)  
Reset to the supplied _value_ only if the specified _value-entry-name_ already exists in the given _subkey_.

**0x00001000** (FLG_ADDREG_64BITKEY)  
(Windows XP and later versions of Windows.) Make the specified change in the 64-bit registry. If not specified, the change is made to the native registry.

**0x00002000** (FLG_ADDREG_KEYONLY_COMMON)  
(Windows XP and later versions of Windows.) This is the same as FLG_ADDREG_KEYONLY but also works in a _del-registry-section_ of an [**INF DelReg directive**](inf-delreg-directive.md).

**0x00004000** (FLG_ADDREG_32BITKEY)  
(Windows XP and later versions of Windows.) Make the specified change in the 32-bit registry. If not specified, the change is made to the native registry.

**0x00000000** (FLG_ADDREG_TYPE_SZ)  
The given value entry and/or value is of type [REG_SZ](/windows/desktop/SysInfo/registry-value-types).

> [!NOTE]
> This value is the default type for a specified value entry, so the flags value can be omitted from any _reg-root=_ line in an _add-registry-section_ that operates on a value entry of this type.

**0x00010000** (FLG_ADDREG_TYPE_MULTI_SZ)  
The given value entry and/or value is of the registry type [REG_MULTI_SZ](/windows/desktop/SysInfo/registry-value-types). The value field that follows can be a list of strings separated by commas. This specification does not require any NULL terminator for a given string value.

**0x00020000** (FLG_ADDREG_TYPE_EXPAND_SZ)  
The given _value-entry-name_ and/or _value_ is of the registry type [REG_EXPAND_SZ](/windows/desktop/SysInfo/registry-value-types).

**0x00010001** (FLG_ADDREG_TYPE_DWORD)  
The given _value-entry-name_ and/or _value_ is of the registry type [REG_DWORD](/windows/desktop/SysInfo/registry-value-types).

**0x00020001** (FLG_ADDREG_TYPE_NONE)  
The given _value-entry-name_ and/or _value_ is of the registry type [REG_NONE](/windows/desktop/SysInfo/registry-value-types).

_value_  
This optionally specifies a new value for the specified _value-entry-name_ to be added to the given registry key. Such a _value_ can be a "replacement" value for an existing named value entry in an existing key, a value to be appended (_flag_ value **0x00010008**) to an existing named [REG_MULTI_SZ](/windows/desktop/SysInfo/registry-value-types)-type value entry in an existing key, a new value entry to be written into an existing key, or the initial value entry for a new _subkey_ to be added to the registry.

The expression of such a _value_ depends on the registry type specified for the _flag_, as follows:

- A registry string-type value can be expressed either as a "_quoted string_" or as a %_strkey_% token defined in a [**Strings**](inf-strings-section.md) section of the INF file. Such an INF-specified value does not have to include a NULL terminator at the end of each string.

- A registry numerical-type value can be expressed as a hexadecimal (by using 0x notation) or decimal number.

_security-descriptor-string_  
Specifies a security descriptor, to be applied to all registry entries created by the named _add-registry-section_. The _security-descriptor-string_ is a string with tokens to indicate the DACL (**D:**) security component.

If an _add-registry-section_**.security** section is not specified, registry entries inherit the security settings of the parent key.

If an _add-registry-section_**.security** section is specified, the following ACE's must be included so that installations and upgrades of devices and system service packs can occur:

- (A;;GA;;;SY) − Grants all access to the local system.
- (A;;GA;;;BA) − Grants all access to built-in administrators.

Do _not_ specify ACE strings that grant write access to nonprivileged users.

For information about security descriptor strings, see [Security Descriptor Definition Language (Windows)](/windows/desktop/SecAuthZ/security-descriptor-definition-language). For information about the format of security descriptor strings, see Security Descriptor Definition Language (Windows).

For more information about how to specify security descriptors, see [Creating Secure Device Installations](creating-secure-device-installations.md).

## Remarks

An **AddReg** directive can be specified under any of the sections shown in the formal syntax statement above. This directive can also be specified under any of the following INF-writer-defined sections:

- A _service-install-section_ or _event-log-install_ section referenced by the [**AddService**](inf-addservice-directive.md) directive in an [**INF _DDInstall_.Services section**](inf-ddinstall-services-section.md).

- An _add-interface-section_ referenced by the [**AddInterface**](inf-addinterface-directive.md) directive in an [**INF _DDInstall_.Interfaces section**](inf-ddinstall-interfaces-section.md).

- An _install-interface-section_ referenced in an [**INF InterfaceInstall32 section**](inf-interfaceinstall32-section.md).

Each _add-registry-section_ name must be unique to the INF file, but it can be referenced by **AddReg** directives in other sections of the same INF. Each section name must follow the general rules for defining section names described in [General Syntax Rules for INF Files](general-syntax-rules-for-inf-files.md).

> [!NOTE]
> The lower-order bit of the low word in a flag value distinguishes between character and binary data.

To represent a number of a registry type other than one of the predefined REG_*XXX* types, specify a new type number in the high word of the _flag_ ORed with FLG_ADDREG_BINVALUETYPE in its low word.

The data for such a _value_ must be specified in binary format as a sequence of bytes separated by commas. For example, to store 16 bytes of data of a new registry data type, such as 0x38, as a value entry, the add-registry section entry would be something like the following:

```inf
HKR,,MYValue,0x00380001,1,0,2,3,4,5,6,7,8,9,A,B,C,D,E,F
```

This technique can be used to define new registry types for numeric values, but not for values of type [REG_EXPAND_SZ](/windows/desktop/SysInfo/registry-value-types), [REG_MULTI_SZ](/windows/desktop/SysInfo/registry-value-types), [REG_NONE](/windows/desktop/SysInfo/registry-value-types), or [REG_SZ](/windows/desktop/SysInfo/registry-value-types). For more info about these types, see [Registry value types](/windows/desktop/SysInfo/registry-value-types).

### Special _value-entry-name_ keywords

Special keywords are defined for use in the HKR **AddReg** entries. The format for the entries that use these keywords is as follows:

```inf
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

**DeviceCharacteristics**  
A **DeviceCharacteristics** HKR **AddReg** entry specifies characteristics for the device. The _characteristics_ value is a numeric value that is the result of using OR on one or more FILE_\* file characteristics values, which are defined in _Wdm.h_ and _Ntddk.h_.

Only the following values can be specified in an INF:

```cpp
#define FILE_REMOVABLE_MEDIA            0x00000001
#define FILE_READ_ONLY_DEVICE           0x00000002
#define FILE_FLOPPY_DISKETTE            0x00000004
#define FILE_WRITE_ONCE_MEDIA           0x00000008
#define FILE_DEVICE_SECURE_OPEN         0x00000100
```

For a description of these values, see [**IoCreateDevice**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocreatedevice).

The characteristics values, which are specified by using a **DeviceCharacteristics** entry, are ORed with those specified in each call to **IoCreateDevice** that creates a device object on the device stack. The OR operation occurs after all device objects are added, but before the device is started.

The _characteristics_ value (including a value of zero) overrides any class-wide device characteristics that were specified in the associated class installer INF.

For more information about device characteristics, see [Specifying Device Characteristics](../kernel/specifying-device-characteristics.md).

**DeviceType**  
A **DeviceType** HKR **AddReg** entry specifies a device type for the device. The device-type is the numeric value of a FILE_DEVICE_*XXX* constant defined in _Wdm.h_ or _Ntddk.h_. The flag value of 0x10001 specifies that the device-type value is a [REG_DWORD](/windows/desktop/SysInfo/registry-value-types). For more information, see [Specifying Device Types](../kernel/specifying-device-types.md).

A class-installer INF should specify the device type that applies to all, or almost all, of the devices in the class. For example, if the devices in the class are of type FILE_DEVICE_CD_ROM, specify a _device-type_ of 0x02. If a device INF specifies a value for **DeviceType**, it overrides the value set by the class installer, if any. If the class or device INF specifies a **DeviceType** value, the PnP manager applies that type to the _physical device object (PDO)_ created by the device's bus driver.

**Security**  
A **Security** HKR **AddReg** entry specifies a security descriptor for the device. The _security-descriptor-string_ is a string with tokens to indicate the DACL (**D:**) security component.

A class-installer INF can specify a security descriptor for a device class. A device INF can specify a security descriptor for an individual device, overriding the security for the class. If the class and/or device INF specifies a _security-descriptor-string_, the PnP manager propagates the descriptor to all the device objects ( _DOs_) for a device. This includes the function device object (_FDO_), optional _filter DOs_, and the PDO.

For information about the format of security descriptor strings, see the Microsoft Windows SDK documentation.

For more information about how to specify security descriptors, see [Creating Secure Device Installations](creating-secure-device-installations.md).

**UpperFilters**  
An **UpperFilters** HKR **AddReg** entry specifies a PnP upper-filter driver. This entry in a [**_DDInstall_.HW**](inf-ddinstall-hw-section.md) section defines one or more device-specific upper-filter drivers. In a [**ClassInstall32**](inf-classinstall32-section.md) section, this entry defines one or more class-wide upper-filter drivers.

**LowerFilters**  
A **LowerFilters** HKR **AddReg** entry specifies a PnP lower-filter driver. This entry in a _DDInstall_**.HW section** defines one or more device-specific lower-filter drivers. In a **ClassInstall32** section, this entry defines one or more class-wide lower-filter drivers.

**Exclusive**  
An **Exclusive** HKR **AddReg** entry, if it exists and is set to "1", specifies that the device is an _exclusive device_. Otherwise the device is not treated as exclusive. For more information, see [Specifying Exclusive Access to Device Objects](../kernel/specifying-exclusive-access-to-device-objects.md).

**EnumPropPages32**  
An **EnumPropPages32** HKR **AddReg** entry specifies the name of a dynamic-link library (_DLL_) file that is a device-specific property page provider. It also specifies the name of the **ExtensionPropSheetPageProc** callback function as implemented by the DLL. For more information about property pages and functions, see the Microsoft Windows Software Development Kit (SDK) for Windows 7 and .NET Framework 4.0.

> [!IMPORTANT]
> Both the name of the DLL and **ExtensionPropSheetPageProc** callback function must be enclosed together within quotation marks (" ").

**LocationInformationOverride**  
(Windows XP and later versions of Windows) A **LocationInformationOverride** HKR **AddReg** entry can be used to specify a text string that describes a device's physical location. It overrides the **LocationInformation** string that the device's bus driver supplies in response to an [**IRP_MN_QUERY_DEVICE_TEXT**](../kernel/irp-mn-query-device-text.md) request.

**ResourcePickerTags**  
A **ResourcePickerTags** HKR **AddReg** entry specifies resource picker tags for a device.

**ResourcePickerExceptions**  
A **ResourcePickerExceptions** HKR **AddReg** entry specifies the resource conflicts that are allowed for a device.

## Examples

An **AddReg** directive referenced the (SCSI) Miniport_EventLog_AddReg section in this example, under an INF-writer-defined section referenced by the **AddService** directive in a _DDInstall_**.Services** section of this INF.

```inf
[Miniport_EventLog_AddReg]
HKR,,EventMessageFile,0x00020000,"%%SystemRoot%%\System32\IoLogMsg.dll" 
; double quotation marks delimiters in preceding entry prevent truncation 
; if line wraps
 
HKR,,TypesSupported,0x00010001,7 
```

Note that you can either specify flag values in hexadecimal format, as shown in the example, or you can define string placeholders such as `%FLG_ADDREG_TYPE_DWORD%` in the [Strings] section of each INF file.

## See also

[**AddInterface**](inf-addinterface-directive.md)

[**AddService**](inf-addservice-directive.md)

[**BitReg**](inf-bitreg-directive.md)

[**ClassInstall32**](inf-classinstall32-section.md)

[**_DDInstall_**](inf-ddinstall-section.md)

[**_DDInstall_.CoInstallers**](inf-ddinstall-coinstallers-section.md)

[**_DDInstall_.HW**](inf-ddinstall-hw-section.md)

[**_DDInstall_.Interfaces**](inf-ddinstall-interfaces-section.md)

[**_DDInstall_.Services**](inf-ddinstall-services-section.md)

[**DelReg**](inf-delreg-directive.md)

[**InterfaceInstall32**](inf-interfaceinstall32-section.md)

[**Strings**](inf-strings-section.md)
