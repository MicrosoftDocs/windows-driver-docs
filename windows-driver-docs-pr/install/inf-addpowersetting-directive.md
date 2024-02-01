---
title: INF AddPowerSetting Directive
description: An AddPowerSetting directive references one or more sections that are used to modify or create power setting information.
keywords:
- INF AddPowerSetting Directive Device and Driver Installation
topic_type:
- apiref
ms.topic: reference
api_name:
- INF AddPowerSetting Directive
api_type:
- NA
ms.date: 06/14/2022
---

# INF AddPowerSetting directive

An **AddPowerSetting** directive references one or more sections that are used to modify or create power setting information. Each _add-power-setting-section_ defines a power setting, the allowed values for the power setting, the friendly name of the power setting, and the description of the power setting. An _add-power-setting-section_ also specifies the default value for each power scheme personality. For more information about power settings and power scheme personalities, see [Managing Device Performance States](../kernel/managing-device-performance-states.md).

```inf
[DDInstall] | 
[DDInstall.HW] | 
[DDInstall.CoInstallers] | 
[ClassInstall32] | 
[ClassInstall32.ntx86] | 
[ClassInstall32.ntia64] |  (Windows Vista)
[ClassInstall32.ntamd64] | (Windows Vista)
[ClassInstall32.ntarm] | (Windows 8 and later versions of Windows)
[ClassInstall32.ntarm64] (Windows 10 version 1709 and later versions of Windows)

AddPowerSetting=add-power-setting-section[,add-power-setting-section]
```

In general, an _add-power-setting-section_ includes the following directives:

- A **SubGroup** directive.

- A **Setting** directive

- A list of two or more **Value** directives or one **ValueRange** directive.

- A set of six **Default** directives.

An _add-power-setting-section_ takes one of the following two possible forms:

- If the allowed power settings values can best be defined as a set of two or more discrete values, use a list of **Value** directives to specify the allowed values, as follows:

    ```inf
    [add-power-setting-section]

    [SubGroup = {subgroup-guid}] | SubGroup = {subgroup-guid}, subgroup-name, subgroup-description, subgroup-icon
    Setting = {setting-guid}, [setting-name],[setting-description],[setting-icon]
    Value = value-index, value-name,[value-description], value-flags, value-data 
    Value = value-index, value-name,[value-description], value-flags, value-data
    [Value = value-index, value-name,[value-description], value-flags, value-data
    ...
    Value = value-index, value-name,[value-description], value-flags, value-data]

    (Six required Default directives, each one of which has the following form)
    Default = power-scheme-personality-GUID, AC/DC-index, default-setting-index | default-setting-value 
    ...
    ```

- If the allowed power settings values can best be defined as an incremented sequence of nonnegative integer values within a specified range, use one **ValueRange** directive to specify allowed values, as follows:

    ```inf
    [add-power-setting-section]

    [SubGroup = {subgroup-guid}] | 
    SubGroup = {subgroup-guid}, subgroup-name, subgroup-description, subgroup-icon
    Setting = {setting-guid}, [setting-name],[setting-description],[setting-icon]
    ValueRange = range-minimum-value, range-maximum-value, range-increment, [range-unit-label] 

    (Six required Default directives, each one of which has the following form)
    Default = power-scheme-personality-GUID, AC/DC-index, default-setting-index | default-setting-value 
    ...
    ```

## Entries

> [!NOTE]
> Except for a _value-data_ entry, all the following entries that supply a string value can specify the string in one of the ways that are described in [Specifying an AddPowerSetting String Entry Value](#specifying-an-addpowersetting-string-entry-value).

**SubGroup**  
A subgroup groups power settings that are logically related.

To specify a system-defined subgroup, include a **SubGroup** directive and supply only the _subgroup-guid_ entry. The system-defined subgroups are represented by the constants GUID_*Xxx*_SUBGROUP and NO_SUBGROUP_GUID, which are defined in _Wdm.h_.

For example, GUID_VIDEO_SUBGROUP represents the subgroup that contains the video power settings for a power scheme personality. The NO_SUBGROUP_GUID constant represents a collection of settings that do not logically belong to any subgroup. If a **SubGroup** directive is not included, the setting is added by default to the collection of settings that do not logically belong to any subgroup.

To define a new subgroup, include the **SubGroup** directive and supply the following required entries: _subgroup-guid_, _subgroup-name_, _subgroup-description_, and _subgroup-icon._ The GUID of the new subgroup must be unique and the other entries should be as descriptive as possible.

_subgroup-guid_  
The required entry supplies the GUID that identifies the subgroup. The format of this entry is **{**_XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX_**}**, where "X" is a hexadecimal digit.

For example, the value of the system-defined constant GUID_VIDEO_SUBGROUP is {7516B95F-F776-4464-8C53-06167F40CC99}. This GUID represents the subgroup that contains the video power settings for a power scheme personality.

_subgroup-name_  
A string that specifies the subgroup name of the power setting. If the subgroup is a system-defined subgroup, this entry should not be supplied. If the subgroup is new, this entry is required.

_subgroup-description_  
A string that describes to the user the power subgroup. If the subgroup is a system-defined subgroup, this entry should not be supplied. If the subgroup is new, this entry is required.

_subgroup-icon_  
A reference to an icon resource. If the subgroup is a system-defined subgroup, this entry should not be supplied. If the subgroup is new, this entry is required.

An icon resource must be specified as a language-neutral registry value. For information about how to specify a language-neutral registry value, see [Specifying an AddPowerSetting String Entry Value](#specifying-an-addpowersetting-string-entry-value).

**Setting**  
The **Setting** directive identifies the setting to which all the other entries in the section apply. One **Setting** directive is required in an add-power-setting section and there can only be one **Setting** directive in an add-power-setting section. If an INF file defines more than one setting, each setting must be defined in its own add-power-setting section.

The following are the entries that are associated with a **Setting** directive.

_setting-guid_  
A required entry that specifies the GUID that represents the power setting. The format of this entry is **{**_XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX_**}**, where each "X" is a hexadecimal digit.

For example, the following is a custom GUID value: {BFC0D9E9-549C-483D-AD2A-3D90C98A8B03}.

_setting-name_  
An optional entry that specifies a string that contains the friendly name of the power setting. **Power Options** in Control Panel displays this friendly name to a user.

_setting-description_  
An optional entry that specifies a string that describes to the user the power setting and the effect that the setting has on system power and performance.

_setting-icon_  
An optional entry that is a reference to an icon resource. An icon resource must be specified by a language-neutral registry value.

For information about how to specify a language-neutral-registry value, see [Specifying an AddPowerSetting String Entry Value](#specifying-an-addpowersetting-string-entry-value).

**Value**  
A **Value** directive defines an allowed value for a power setting. The **Value** directive should be used if the values can best be defined as a set of two or more values, where each value can have a value-specific custom data type. In this situation, an add-power-setting-section should include two or more **Value** directives. A user can select one of these values in **Power Options** in Control Panel to configure a power scheme.

If the allowed power setting values can best be described as incremented set of non-negative integers within a range, use the **ValueRange** directive instead of the **Value** directive to specify the allowed power setting values.

_value-index_  
A required entry that specifies a unique index value, which is greater than or equal to zero, and that is used to reference the corresponding setting value. **Power Options** in Control Panel displays power setting values to a user in order of their corresponding index values, from lowest to highest.

_value-name_  
A required entry that supplies a string that provides the friendly name for the corresponding setting value. **Power Options** in Control Panel displays the friendly names of the power setting values to a user.

_value-description_  
An optional entry that supplies a string that describes to the user the power setting value and the effect that the setting value has on system power and performance.

_value-flags_  
A required entry that specifies the data type of the corresponding value-data entry, as indicated in the following table.

| Flag value | Data type |
|--|--|
| 0x00000001 | [REG_BINARY](/windows/desktop/SysInfo/registry-value-types) |
| 0x00010001 | [REG_DWORD](/windows/desktop/SysInfo/registry-value-types) |
| 0x00000000 | [REG_SZ](/windows/desktop/SysInfo/registry-value-types) |

_value-data_  
A required entry that supplies the data for the corresponding setting value, the format of which depends on the data type that is specified by corresponding _value-flags_ entry, as follows:

- A [REG_BINARY](/windows/desktop/SysInfo/registry-value-types) value can be specified in hexadecimal format by using 0x notation, or as a comma-separated list of paired hexadecimal numbers without the 0x notation.

    For example, the following entries are equivalent: 0xFEDCBA9876543210 and the following comma-separated list of paired hexadecimal digits: FE, DC, BA, 98, 76, 54, 32, 10.

- A [REG_DWORD](/windows/desktop/SysInfo/registry-value-types) value can be specified either in hexadecimal format (by using 0x notation) or in decimal format.

- A [REG_SZ](/windows/desktop/SysInfo/registry-value-types) value can only be expressed as a string enclosed in double quotation marks ("_quoted-string_") or as a %_strkey_% token that is defined in the INF [**Strings**](inf-strings-section.md) section of an INF file.

> [!NOTE]
> You should not use string values because they cannot be localized. Instead, use values of type [REG_BINARY](/windows/desktop/SysInfo/registry-value-types) or [REG_DWORD](/windows/desktop/SysInfo/registry-value-types).

**ValueRange**  
Use the **ValueRange** directive if the allowed power settings values can best be defined as an incremented sequence of non-negative integer values within a specified range. The power manager validates that a setting that a user selects in **Power Options** in Control Panel is one of these allowed values. The set of allowed values is determined by a minimum allowed value, a maximum allowed value, and an increment between the allowed values within the range. A value is allowed if it satisfies the following:

```inf
range-minimum-value + k*range-increment
```

where _range-minimum-value_ is greater than or equal to zero, _k_ and _range-increment_ are greater than or equal to one, and the value is less than or equal to _range-maximum-value_. In addition, _range-maximum-value_ should be equal to _range-minimum-value_ + _k_\*_range-increment_ for some k.

For example, for a _range-minimum-value_ equal to 0, a _range-maximum-value_ equal to 10, and a _range-increment_ equal to 2, the allowed values are as follows: 0, 2, 4, 6, 8, and 10.

If the allowed power setting values can best be described as a list of values, where each value can have a value-specific custom data type, use the **Value** directive instead of the **ValueRange** directive.

_range-minimum-value_  
A value of type [REG_DWORD](/windows/desktop/SysInfo/registry-value-types) that specifies the minimum allowed power setting.

_range-maximum-value_  
A value of type [REG_DWORD](/windows/desktop/SysInfo/registry-value-types) that specifies the maximum allowed power setting value. The maximum value must be greater than or equal to minimum-value and should be equal to range-minimum-value + _k\*range-increment_, for some integer _k_ that is greater than zero.

_range-increment_  
A value of type [REG_DWORD](/windows/desktop/SysInfo/registry-value-types) that is greater than zero. This value specifies the difference between consecutive values within the inclusive range that is specified by _range-minimum-value_ and _range-maximum-value_.

_range-unit-label_  
An optional string that describes the power setting value. The string, together with _setting-name_, informs the user of what type of data to enter.

For example, the string can be used to specify the value units, such as "minutes" or "%" (representing percent).

**Default**  
There are six **Default** directives that must be included in an **AddPowerSetting** section. A **Default** directive specifies the default value for one of the three system-defined power scheme personalities that apply to an AC power state and the three system-defined power scheme personalities that apply to a DC power state.

It is extremely important that the defaults be valid and accurate. If the user does not manually set a power setting, the power manager uses the default value that is specified by the **Default** directive.

_power-scheme-personality-GUID_  
One of the following GUIDs, which identifies the power scheme that the default value applies to.

| Personality | GUID |
|--|--|
| Power saver | {A1841308-3541-4FAB-BC81-F71556F20B4A} |
| High performance | {8C5E7FDA-E8BF-4A96-9A85-A6E23A8C635C} |
| Balanced | {381B4222-F694-41F0-9685-FF5BB260DF2E} |

These GUIDs are defined in _Wdm.h_.

_AC/DC-index_  
If _AC/DC-index_ is 0, the setting applies to an AC power state and if _AC/DC-index_ is 1, the setting applies to a DC power state. A value other than 0 or 1 is not valid.

_default-setting-index_  
If the **Value** directive is used to specify allowed values, _default-setting-index_ is the value of the _value-index entry_ of the **Value** directive. If the **ValueRange** directive is used to specify allowed values, this entry does not apply.

_default-setting-value_  
If the **ValueRange** directive is used to specify allowed values, _default-setting-value_ is one of the allowed values that are specified by the **ValueRange** directive. If the **Value** directive is used to specify allowed values, this entry does not apply.

## Remarks

An _add-power-setting-section_ name must be unique in an INF file, but it can be referenced by more than one **AddPowerSetting** directive in the same INF file. Each section name must follow the general rules that are described in [General Syntax Rules for INF Files](general-syntax-rules-for-inf-files.md).

The power manager does not automatically remove device power policies after a device is uninstalled. Installation or removal of power settings, values, and defaults can be performed by a co-installer through the system-supplied power setting routines that are defined in _Powrprof.h_. For more information about these power management routines, see the power management reference that is provided with the Microsoft Windows SDK documentation.

In addition, the _Powercfg.exe_ command-line tool can be used to change power settings. For information about _Powercfg.exe_, see the Microsoft Help and Support Center.

For more information about how to use the system-defined **.nt**, **.ntx86**, **.ntia64**, **.ntamd64**, **.ntarm**, and **.ntarm64** extensions, see [Creating INF Files for Multiple Platforms and Operating Systems](creating-inf-files-for-multiple-platforms-and-operating-systems.md).

### Specifying an AddPowerSetting string entry value

Except for _value-data_ entries of type [REG_SZ](/windows/desktop/SysInfo/registry-value-types), all the other string entry values that are supplied with an **AddPowerSetting** directive can be expressed as a string enclosed in double quotation marks ("_quoted-string_"), as a %_strkey_% token that is defined in the INF string section of an INF file, or as language-neutral registry value.

Language-neutral registry values are used to support Windows Multilingual User Interface (MUI) and are specified as follows:

```inf
"@file-path,-resourceID[;comment]"
```

The entries that specify a language-neutral registry value are as follows:

_file-path_  
The fully qualified path of the file that contains the resource.

_resourceID_  
The resource ID of the corresponding resource. In the case of a string, the _resourceID_ references a string. In the case of an icon, the _resourceID_ references an icon.

_Comment_  
An optional value that can be used to aid debugging or to provide an additional comment about the setting. In the case of a string resource, the power manager does not combine or display the comment string with specified resource string.

For more information about how to specify language-neutral registry values, see [Rendering Shell and Registry Strings](/previous-versions//ms776232(v=vs.85)).

## Examples

The following two examples define power settings that control the brightness of an LCD. The first example shows how to use the **Value** directive to define a minimum, a medium, and a maximum LCD brightness value.

```inf
// Within a DDinstall or ClassInstall23 section
AddPowerSetting=LCDDim
...

[LCDDim]
SubGroup = {7516B95F-F776-4464-8C53-06167F40CC99}
Setting = {381B4222-F694-41F0-9685-FF5BB260DF2E}, "LCD Brightness", "Controls the brightness of the LCD display"

Value = 0, "Low", "Minimum Brightness", %FLG_ADDREG_TYPE_DWORD%, 0x50
Value = 1, "Medium", "Medium Brightness", %FLG_ADDREG_TYPE_DWORD%, 0x75
Value = 2, "High", "Maximum Brightness", %FLG_ADDREG_TYPE_DWORD%, 0x100

Default = %GUID_MAX_POWER_SAVINGS%, %AC%, 0
Default = %GUID_MAX_POWER_SAVINGS%, %DC%, 0
Default = %GUID_TYPICAL_POWER_SAVINGS%, %AC%, 2
Default = %GUID_TYPICAL_POWER_SAVINGS%, %DC%, 1
Default = %GUID_MIN_POWER_SAVINGS%, %AC%, 2
Default = %GUID_MIN_POWER_SAVINGS%, %DC%, 2
...

[Strings]
GUID_MAX_POWER_SAVINGS = {a1841308-3541-4fab-bc81-f71556f20b4a}
GUID_TYPICAL_POWER_SAVINGS = {381b4222-f694-41f0-9685-ff5bb260df2e}
GUID_MIN_POWER_SAVINGS = {8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c}
AC = 0
DC = 1
FLG_ADDREG_TYPE_DWORD = 0x00010001
```

The second example shows how to use the **ValueRange** directive to define a range of allowed LCD brightness values that varies from 0% through 100%, with an increment of 1% between allowed values.

```inf
// Within a DDinstall or a ClassInstall23 section
AddPowerSetting=LCDDimRange
...

[LCDDimRange]
SubGroup = {7516B95F-F776-4464-8C53-06167F40CC99}
Setting = {381B4222-F694-41F0-9685-FF5BB260DF2E}, "LCD Brightness", "Controls the brightness of the LCD display"
ValueRange = 0, 100, 1, "%"
Default = %GUID_MAX_POWER_SAVINGS%, %AC%, 50
Default = %GUID_MAX_POWER_SAVINGS%, %DC%, 50
Default = %GUID_TYPICAL_POWER_SAVINGS%, %AC%, 95
Default = %GUID_TYPICAL_POWER_SAVINGS%, %DC%, 50
Default = %GUID_MIN_POWER_SAVINGS%, %AC%, 100
Default = %GUID_MIN_POWER_SAVINGS%, %DC%, 100

[Strings]
GUID_MAX_POWER_SAVINGS = {a1841308-3541-4fab-bc81-f71556f20b4a}
GUID_TYPICAL_POWER_SAVINGS = {381b4222-f694-41f0-9685-ff5bb260df2e}
GUID_MIN_POWER_SAVINGS = {8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c}
AC = 0
DC = 1
```

## See also

[**ClassInstall32**](inf-classinstall32-section.md)

[**_DDInstall_**](inf-ddinstall-section.md)

[**_DDInstall_.CoInstallers**](inf-ddinstall-coinstallers-section.md)

[**_DDInstall_.HW**](inf-ddinstall-hw-section.md)

[**_DDInstall_.Interfaces**](inf-ddinstall-interfaces-section.md)

[**_DDInstall_.Services**](inf-ddinstall-services-section.md)
