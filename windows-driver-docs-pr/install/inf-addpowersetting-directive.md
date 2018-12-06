---
title: INF AddPowerSetting Directive
description: An AddPowerSetting directive references one or more sections that are used to modify or create power setting information.
ms.assetid: 0231ba90-5de4-4f5a-83bb-0f73be4b23ae
keywords:
- INF AddPowerSetting Directive Device and Driver Installation
topic_type:
- apiref
api_name:
- INF AddPowerSetting Directive
api_type:
- NA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# INF AddPowerSetting Directive


An **AddPowerSetting** directive references one or more sections that are used to modify or create power setting information. Each *add-power-setting-section* defines a power setting, the allowed values for the power setting, the friendly name of the power setting, and the description of the power setting. An *add-power-setting-section* also specifies the default value for each power scheme personality. For more information about power settings and power scheme personalities, see [Managing Device Performance States](https://msdn.microsoft.com/library/windows/hardware/ff554353).

```cpp
[DDInstall] | 
[DDInstall.HW] | 
[DDInstall.CoInstallers] | 
[ClassInstall32] | 
[ClassInstall32.ntx86] | 
[ClassInstall32.ntia64] |  (Windows Vista)
[ClassInstall32.ntamd64]  (Windows Vista)

AddPowerSetting=add-power-setting-section[,add-power-setting-section]
```

In general, an *add-power-setting-section* includes the following directives:

-   A **SubGroup** directive.
-   A **Setting** directive
-   A list of two or more **Value** directives or one **ValueRange** directive.
-   A set of six **Default** directives.

An *add-power-setting-section* takes one of the following two possible forms:

-   If the allowed power settings values can best be defined as a set of two or more discrete values, use a list of **Value** directives to specify the allowed values, as follows:

    ```cpp
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

-   If the allowed power settings values can best be defined as an incremented sequence of nonnegative integer values within a specified range, use one **ValueRange** directive to specify allowed values, as follows:

    ```cpp
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


**Note**  Except for a *value-data* entry, all the following entries that supply a string value can specify the string in one of the ways that are described in [Specifying an AddPowerSetting String Entry Value](#specifying-an-addpowersetting-string-entry-value).

 

<a href="" id="subgroup"></a>**SubGroup**  
A subgroup groups power settings that are logically related.

To specify a system-defined subgroup, include a **SubGroup** directive and supply only the *subgroup-guid* entry. The system-defined subgroups are represented by the constants GUID_*Xxx*_SUBGROUP and NO_SUBGROUP_GUID, which are defined in *Wdm.h*.

For example, GUID_VIDEO_SUBGROUP represents the subgroup that contains the video power settings for a power scheme personality. The NO_SUBGROUP_GUID constant represents a collection of settings that do not logically belong to any subgroup. If a **SubGroup** directive is not included, the setting is added by default to the collection of settings that do not logically belong to any subgroup.

To define a new subgroup, include the **SubGroup** directive and supply the following required entries: *subgroup-guid*, *subgroup-name*, *subgroup-description*, and *subgroup-icon.* The GUID of the new subgroup must be unique and the other entries should be as descriptive as possible.

<a href="" id="subgroup-guid"></a>*subgroup-guid*  
The required entry supplies the GUID that identifies the subgroup. The format of this entry is **{**<em>XXXXXXXX-XXXX-XXXX-XXXXXXXXXXXX</em>**}**, where "X" is a hexadecimal digit.

For example, the value of the system-defined constant GUID_VIDEO_SUBGROUP is {7516B95F-F776-4464-8C53-06167F40CC99}. This GUID represents the subgroup that contains the video power settings for a power scheme personality.

<a href="" id="subgroup-name"></a>*subgroup-name*  
A string that specifies the subgroup name of the power setting. If the subgroup is a system-defined subgroup, this entry should not be supplied. If the subgroup is new, this entry is required.

<a href="" id="subgroup-description"></a>*subgroup-description*  
A string that describes to the user the power subgroup. If the subgroup is a system-defined subgroup, this entry should not be supplied. If the subgroup is new, this entry is required.

<a href="" id="subgroup-icon"></a>*subgroup-icon*  
A reference to an icon resource. If the subgroup is a system-defined subgroup, this entry should not be supplied. If the subgroup is new, this entry is required.

An icon resource must be specified as a language-neutral registry value. For information about how to specify a language-neutral registry value, see [Specifying an AddPowerSetting String Entry Value](#specifying-an-addpowersetting-string-entry-value).

<a href="" id="setting"></a>**Setting**  
The **Setting** directive identifies the setting to which all the other entries in the section apply. One **Setting** directive is required in an add-power-setting section and there can only be one **Setting** directive in an add-power-setting section. If an INF file defines more than one setting, each setting must be defined in its own add-power-setting section.

The following are the entries that are associated with a **Setting** directive.

<a href="" id="setting-guid"></a>*setting-guid*  
A required entry that specifies the GUID that represents the power setting. The format of this entry is **{**<em>XXXXXXXX-XXXX-XXXX-XXXXXXXXXXXX</em>**}**, where each "X" is a hexadecimal digit.

For example, the following is a custom GUID value: {BFC0D9E9-549C-483D-AD2A-3D90C98A8B03}.

<a href="" id="setting-name"></a>*setting-name*  
An optional entry that specifies a string that contains the friendly name of the power setting. **Power Options** in Control Panel displays this friendly name to a user.

<a href="" id="setting-description"></a>*setting-description*  
An optional entry that specifies a string that describes to the user the power setting and the effect that the setting has on system power and performance.

<a href="" id="setting-icon"></a>*setting-icon*  
An optional entry that is a reference to an icon resource. An icon resource must be specified by a language-neutral registry value.

For information about how to specify a language-neutral-registry value, see [Specifying an AddPowerSetting String Entry Value](#specifying-an-addpowersetting-string-entry-value).

<a href="" id="value"></a>**Value**  
A **Value** directive defines an allowed value for a power setting. The **Value** directive should be used if the values can best be defined as a set of two or more values, where each value can have a value-specific custom data type. In this situation, an add-power-setting-section should include two or more **Value** directives. A user can select one of these values in **Power Options** in Control Panel to configure a power scheme.

If the allowed power setting values can best be described as incremented set of non-negative integers within a range, use the **ValueRange** directive instead of the **Value** directive to specify the allowed power setting values.

<a href="" id="value-index"></a>*value-index*  
A required entry that specifies a unique index value, which is greater than or equal to zero, and that is used to reference the corresponding setting value. **Power Options** in Control Panel displays power setting values to a user in order of their corresponding index values, from lowest to highest.

<a href="" id="value-name"></a>*value-name*  
A required entry that supplies a string that provides the friendly name for the corresponding setting value. **Power Options** in Control Panel displays the friendly names of the power setting values to a user.

<a href="" id="value-description"></a>*value-description*  
An optional entry that supplies a string that describes to the user the power setting value and the effect that the setting value has on system power and performance.

<a href="" id="value-flags"></a>*value-flags*  
A required entry that specifies the data type of the corresponding value-data entry, as indicated in the following table.

| Flag value | Data type   |
|------------|-------------|
| 0x00000001 | [REG_BINARY](https://docs.microsoft.com/windows/desktop/SysInfo/registry-value-types) |
| 0x00010001 | [REG_DWORD](https://docs.microsoft.com/windows/desktop/SysInfo/registry-value-types)  |
| 0x00000000 | [REG_SZ](https://docs.microsoft.com/windows/desktop/SysInfo/registry-value-types)     |

 

<a href="" id="value-data"></a>*value-data*  
A required entry that supplies the data for the corresponding setting value, the format of which depends on the data type that is specified by corresponding *value-flags* entry, as follows:

-   A [REG_BINARY](https://docs.microsoft.com/windows/desktop/SysInfo/registry-value-types) value can be specified in hexadecimal format by using 0x notation, or as a comma-separated list of paired hexadecimal numbers without the 0x notation.

    For example, the following entries are equivalent: 0xFEDCBA9876543210 and the following comma-separated list of paired hexadecimal digits: FE, DC, BA, 98, 76, 54, 32, 10.

-   A [REG_DWORD](https://docs.microsoft.com/windows/desktop/SysInfo/registry-value-types) value can be specified either in hexadecimal format (by using 0x notation) or in decimal format.
-   A [REG_SZ](https://docs.microsoft.com/windows/desktop/SysInfo/registry-value-types) value can only be expressed as a string enclosed in double quotation marks ("*quoted-string*") or as a %*strkey*% token that is defined in the INF [**Strings**](inf-strings-section.md) section of an INF file.

**Note**  You should not use string values because they cannot be localized. Instead, use values of type [REG_BINARY](https://docs.microsoft.com/windows/desktop/SysInfo/registry-value-types) or [REG_DWORD](https://docs.microsoft.com/windows/desktop/SysInfo/registry-value-types).

 

<a href="" id="valuerange"></a>**ValueRange**  
Use the **ValueRange** directive if the allowed power settings values can best be defined as an incremented sequence of non-negative integer values within a specified range. The power manager validates that a setting that a user selects in **Power Options** in Control Panel is one of these allowed values. The set of allowed values is determined by a minimum allowed value, a maximum allowed value, and an increment between the allowed values within the range. A value is allowed if it satisfies the following:

```cpp
range-minimum-value + k*range-increment
```

where *range-minimum-value* is greater than or equal to zero, *k* and *range-increment* are greater than or equal to one, and the value is less than or equal to *range-maximum-value*. In addition, *range-maximum-value* should be equal to *range-minimum-value* + *k*\**range-increment* for some k.

For example, for a *range-minimum-value* equal to 0, a *range-maximum-value* equal to 10, and a *range-increment* equal to 2, the allowed values are as follows: 0, 2, 4, 6, 8, and 10.

If the allowed power setting values can best be described as a list of values, where each value can have a value-specific custom data type, use the **Value** directive instead of the **ValueRange** directive.

<a href="" id="range-minimum-value"></a>*range-minimum-value*  
A value of type [REG_DWORD](https://docs.microsoft.com/windows/desktop/SysInfo/registry-value-types) that specifies the minimum allowed power setting.

<a href="" id="range-maximum-value"></a>*range-maximum-value*  
A value of type [REG_DWORD](https://docs.microsoft.com/windows/desktop/SysInfo/registry-value-types) that specifies the maximum allowed power setting value. The maximum value must be greater than or equal to minimum-value and should be equal to range-minimum-value + *k\*range-increment*, for some integer *k* that is greater than zero.

<a href="" id="range-increment-"></a>*range-increment*   
A value of type [REG_DWORD](https://docs.microsoft.com/windows/desktop/SysInfo/registry-value-types) that is greater than zero. This value specifies the difference between consecutive values within the inclusive range that is specified by *range-minimum-value* and *range-maximum-value*.

<a href="" id="range-unit-label-"></a>*range-unit-label*   
An optional string that describes the power setting value. The string, together with *setting-name*, informs the user of what type of data to enter.

For example, the string can be used to specify the value units, such as "minutes" or "%" (representing percent).

<a href="" id="default"></a>**Default**  
There are six **Default** directives that must be included in an **AddPowerSetting** section. A **Default** directive specifies the default value for one of the three system-defined power scheme personalities that apply to an AC power state and the three system-defined power scheme personalities that apply to a DC power state.

It is extremely important that the defaults be valid and accurate. If the user does not manually set a power setting, the power manager uses the default value that is specified by the **Default** directive.

<a href="" id="power-scheme-personality-guid"></a>*power-scheme-personality-GUID*  
One of the following GUIDs, which identifies the power scheme that the default value applies to.

| Personality      | GUID                                   |
|------------------|----------------------------------------|
| Power saver      | {A1841308-3541-4FAB-BC81-F71556F20B4A} |
| High performance | {8C5E7FDA-E8BF-4A96-9A85-A6E23A8C635C} |
| Balanced         | {381B4222-F694-41F0-9685-FF5BB260DF2E} |

 

These GUIDs are defined in *Wdm.h*.

<a href="" id="ac-dc-index"></a>*AC/DC-index*  
If *AC/DC-index* is 0, the setting applies to an AC power state and if *AC/DC-index* is 1, the setting applies to a DC power state. A value other than 0 or 1 is not valid.

<a href="" id="default-setting-index-"></a>*default-setting-index*   
If the **Value** directive is used to specify allowed values, *default-setting-index* is the value of the *value-index entry* of the **Value** directive. If the **ValueRange** directive is used to specify allowed values, this entry does not apply.

<a href="" id="default-setting-value-"></a>*default-setting-value*   
If the **ValueRange** directive is used to specify allowed values, *default-setting-value* is one of the allowed values that are specified by the **ValueRange** directive. If the **Value** directive is used to specify allowed values, this entry does not apply.

Remarks
-------

An *add-power-setting-section* name must be unique in an INF file, but it can be referenced by more than one **AddPowerSetting** directive in the same INF file. Each section name must follow the general rules that are described in [General Syntax Rules for INF Files](general-syntax-rules-for-inf-files.md).

The power manager does not automatically remove device power policies after a device is uninstalled. Installation or removal of power settings, values, and defaults can be performed by a co-installer through the system-supplied power setting routines that are defined in *Powrprof.h*. For more information about these power management routines, see the power management reference that is provided with the Microsoft Windows SDK documentation.

In addition, the *Powercfg.exe* command-line tool can be used to change power settings. For information about *Powercfg.exe*, see the Microsoft Help and Support Center.

For more information about how to use the system-defined **.nt**, **.ntx86**, **.ntia64**, and **.ntamd64** extensions, see [Creating INF Files for Multiple Platforms and Operating Systems](creating-inf-files-for-multiple-platforms-and-operating-systems.md).

### Specifying an AddPowerSetting String Entry Value

Except for *value-data* entries of type [REG_SZ](https://docs.microsoft.com/windows/desktop/SysInfo/registry-value-types), all the other string entry values that are supplied with an **AddPowerSetting** directive can be expressed as a string enclosed in double quotation marks ("*quoted-string*"), as a %*strkey*% token that is defined in the INF string section of an INF file, or as language-neutral registry value.

Language-neutral registry values are used to support Windows Multilingual User Interface (MUI) and are specified as follows:

```cpp
"@file-path,-resourceID[;comment]"
```

The entries that specify a language-neutral registry value are as follows:

<a href="" id="file-path"></a>*file-path*  
The fully qualified path of the file that contains the resource.

<a href="" id="resourceid"></a>*resourceID*  
The resource ID of the corresponding resource. In the case of a string, the *resourceID* references a string. In the case of an icon, the *resourceID* references an icon.

<a href="" id="comment"></a>*Comment*  
An optional value that can be used to aid debugging or to provide an additional comment about the setting. In the case of a string resource, the power manager does not combine or display the comment string with specified resource string.

For more information about how to specify language-neutral registry values, see [Rendering Shell and Registry Strings](http://go.microsoft.com/fwlink/p/?linkid=70407).

Examples
--------

The following two examples define power settings that control the brightness of an LCD. The first example shows how to use the **Value** directive to define a minimum, a medium, and a maximum LCD brightness value.

```cpp
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

```cpp
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

[***DDInstall***](inf-ddinstall-section.md)

[***DDInstall*.CoInstallers**](inf-ddinstall-coinstallers-section.md)

[***DDInstall*.HW**](inf-ddinstall-hw-section.md)

[***DDInstall*.Interfaces**](inf-ddinstall-interfaces-section.md)

[***DDInstall*.Services**](inf-ddinstall-services-section.md)

 

 






