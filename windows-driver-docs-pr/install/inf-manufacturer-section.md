---
title: INF Manufacturer Section
description: The Manufacturer section identifies the manufacturer of one or more devices that can be installed by using the INF file.
keywords:
- INF Manufacturer Section Device and Driver Installation
topic_type:
- apiref
ms.topic: reference
api_name:
- INF Manufacturer Section
api_type:
- NA
ms.date: 11/02/2023
---

# INF Manufacturer section

The **Manufacturer** section identifies the manufacturer of one or more devices that can be installed by using the INF file.

```inf
[Manufacturer]

manufacturer-identifier
[manufacturer-identifier] 
[manufacturer-identifier] 
...
```

## Entries

_manufacturer-identifier_  
Uniquely identifies a manufacturer and an INF section that contains information that identifies a manufacturer's device models. Each _manufacturer-identifier_ entry must exist on a separate line and use the following format:

```inf
manufacturer-name |
%strkey%=models-section-name |
%strkey%=models-section-name [,TargetOSVersion] [,TargetOSVersion] ...  (Windows XP and later versions of Windows)
```

These entries are defined as follows:

_manufacturer-name_  
Identifies the devices' manufacturer. The INF must also contain a corresponding [**INF _Models_ section**](inf-models-section.md) of the same name. The maximum length of a manufacturer's name, in characters, is LINE_LEN. (An entry specified in this manner cannot be localized.)

_strkey_  
Specifies a token, unique within the INF file that represents the name of a manufacturer. Each such %_strkey_% token must be defined in an [**INF Strings section**](inf-strings-section.md) of the INF file.

_models-section-name_  
Specifies an INF-writer-defined name for the per-manufacturer [**INF _Models_ section**](inf-models-section.md) within the INF file. This value must be unique within the INF file and must follow the general rules for defining section names. For more information about these rules, see [General Syntax Rules for INF Files](general-syntax-rules-for-inf-files.md).

_TargetOSVersion_  
Specifies one or more target operating system versions with which various INF **_Models_** sections can be used. Windows chooses the INF **_Models_** section that most closely matches the operating system version on which it is executing.

For a description of the _TargetOSVersion_ decoration, see the following **Remarks** section, and related info in Example 3 below.

> [!IMPORTANT]
> Starting with Windows Server 2003 SP1, INF files must decorate models-section-name entries in the **INF Manufacturer section**, as well as the associated INF **_Models_** section names, for non-x86 target operating system versions. These platform extensions are not required in INF files for x86-based target operating system versions but are recommended.

## Remarks

Any INF file that installs one or more devices must have a **Manufacturer** section. An IHV/OEM-supplied INF file typically specifies only a single entry in this section. If multiple entries are specified, each entry must be on a separate line of the INF.

Using a %_strkey_%=_models-section-name_ entry simplifies the localization of the INF file for the international market, as described in [Creating International INF Files](creating-international-inf-files.md) and the reference page for the [**INF Strings section**](inf-strings-section.md).

If an INF file specifies one or more entries in the _manufacturer-name_ format, each such entry implicitly specifies the name of the corresponding **_Models_** section elsewhere in the INF.

You can think of each system-supplied INF file's **Manufacturer** section as a table of contents, because this section sets up the installation of every manufacturer's device models for a [device setup class](./overview-of-device-setup-classes.md). Each entry in an INF file's **Manufacturer** section specifies both an easily localizable %_strkey_% token for the name of a manufacturer and a unique-to-the-INF per-manufacturer **_Models_** section name.

The _models-section-name_ entries in the **Manufacturer** section can be decorated to specify target operating system versions. Different [**INF _Models_ sections**](inf-models-section.md) can be specified for different versions of the operating system. The specified versions indicate operating system versions with which the INF **_Models_** sections is used. If no versions are specified, Windows uses a specified **_Models_** section for all versions of all operating systems.

For Windows XP to Windows 10, version 1511, the format of _TargetOSVersion_ decoration is as follows:

```inf
NT[Architecture][.[OSMajorVersion][.[OSMinorVersion][.[ProductType][.SuiteMask]]]]
```

Starting with Windows 10, version 1607 (Build 14310 and later), the format of the _TargetOSVersion_ decoration is as follows:

```inf
NT[Architecture][.[OSMajorVersion][.[OSMinorVersion][.[ProductType][.[SuiteMask][.[BuildNumber]]]]]
```

Each field is defined as follows:

**NT**  
Specifies the target operating system is NT-based. Windows 2000 and later versions of Windows are all NT-based.

_Architecture_  
Identifies the hardware platform. If specified, this must be **x86**, **ia64**, **amd64**, **arm**, or **arm64**.

Prior to Windows Server 2003 SP1, if _Architecture_ is not specified, the associated INF **_Models_** section can be used with any hardware platform.

Starting with Windows Server 2003 SP1, Architecture must be specified in [**INF _Models_ sections**](inf-models-section.md) names for non-x86 target operating system versions. Architecture is optional in INF **_Models_** section names for x86-based target operating system versions but is recommended.

_OSMajorVersion_  
A number that represents the operating system's major version number. The following table defines the major version for the Windows operating system.

> [!NOTE]
> To differentiate between specific Windows 10 and 11 releases in an INF file, you need to use _BuildNumber_ (see below).

| Windows version | Major version |
|--|--|
| Windows 11 (all releases) | 10 |
| Windows Server 2022 | 10 |
| Windows Server 2019 | 10 |
| Windows Server 2016 | 10 |
| Windows 10 (all releases) | 10 |
| Windows Server 2012 R2 | 6 |
| Windows 8.1 | 6 |
| Windows Server 2012 | 6 |
| Windows 8 | 6 |
| Windows Server 2008 R2 | 6 |
| Windows 7 | 6 |
| Windows Server 2008 | 6 |
| Windows Vista | 6 |
| Windows Server 2003 R2 | 5 |
| Windows Server 2003 | 5 |
| Windows XP | 5 |
| Windows 2000 | 5 |

_OSMinorVersion_  
A number that represents the operating system's minor version number. The following table defines the minor version for the Windows operating system.

| Windows version | Minor version |
|--|--|
| Windows 11 (all releases) | 0 |
| Windows Server 2022 | 0 |
| Windows Server 2019 | 0 |
| Windows Server 2016 | 0 |
| Windows 10 (all releases) | 0 |
| Windows Server 2012 R2 | 3 |
| Windows 8.1 | 3 |
| Windows Server 2012 | 2 |
| Windows 8 | 2 |
| Windows Server 2008 R2 | 1 |
| Windows 7 | 1 |
| Windows Server 2008 | 0 |
| Windows Vista | 0 |
| Windows Server 2003 R2 | 2 |
| Windows Server 2003 | 2 |
| Windows XP | 1 |
| Windows 2000 | 0 |

_ProductType_  
A number that represents one of the VER_NT_xxxx flags defined in _Winnt.h_, such as the following:

**0x0000001** (VER_NT_WORKSTATION)

**0x0000002** (VER_NT_DOMAIN_CONTROLLER)

**0x0000003** (VER_NT_SERVER)

If a product type is specified, the INF file is used only if the operating system matches the specified product type. If the INF supports multiple product types for a single operating system version, multiple _TargetOSVersion_ entries are required.

_SuiteMask_  
A number representing a combination of one or more of the VER_SUITE_xxxx flags defined in _Winnt.h_. These flags include the following:

**0x00000001** (VER_SUITE_SMALLBUSINESS)

**0x00000002** (VER_SUITE_ENTERPRISE)

**0x00000004** (VER_SUITE_BACKOFFICE)

**0x00000008** (VER_SUITE_COMMUNICATIONS)

**0x00000010** (VER_SUITE_TERMINAL)

**0x00000020** (VER_SUITE_SMALLBUSINESS_RESTRICTED)

**0x00000040** (VER_SUITE_EMBEDDEDNT)

**0x00000080** (VER_SUITE_DATACENTER)

**0x00000100** (VER_SUITE_SINGLEUSERTS)

**0x00000200** (VER_SUITE_PERSONAL)

**0x00000400** (VER_SUITE_SERVERAPPLIANCE)

If one or more suite mask values are specified, the INF is used only if the operating system matches all the specified product suites. If the INF supports multiple product suite combinations for a single operating system version, multiple _TargetOSVersion_ entries are required.

_BuildNumber_  
A number that represents the minimum OS build number of the Windows release to which the section is applicable, starting with build 14310 or later.

The build number is assumed to be relative to some specific OS major/minor version only, and may be reset for some future OS major/minor version.

Any build number specified by the _TargetOSVersion_ decoration is evaluated only when the OS major/minor version of the _TargetOSVersion_ matches the current OS (or AltPlatformInfo) version exactly.  If the current OS version is greater than the OS version specified by the _TargetOSVersion_ decoration (OSMajorVersion,OSMinorVersion), the section is considered applicable regardless of the build number specified. Likewise, if the current OS version is less than the OS version specified by _TargetOSVersion_ decoration, the section is not applicable.

If build number is supplied, the OS version and BuildNumber of the _TargetOSVersion_ decoration must both be greater than the OS version and build number of the Windows 10 build 14310 where this decoration was first introduced.  Earlier versions of the operating system without these changes (for example, Windows 10 build 10240) will not parse unknown decorations, so an attempt to target these earlier builds will actually prevent that OS from considering the decoration valid at all.

The following table defines the build number for the Windows operating system.

| Windows version | Build number |
|--|--|
| Windows 11 version 23H2 | 22631 |
| Windows 11 version 22H2 | 22621 |
| Windows 11 version 21H2 | 22000 |
| Windows Server 2022 | 20348 |
| Windows 10 version 22H2 | 19045 |
| Windows 10 version 21H2 | 19044 |
| Windows 10 version 21H1 | 19043 |
| Windows 10 version 20H2 | 19042 |
| Windows 10 version 2004 | 19041 |
| Windows 10 version 1909 | 18363 |
| Windows 10 version 1903 | 18362 |
| Windows Server 2019 | 17763 |
| Windows 10 version 1809 | 17763 |
| Windows 10 version 1803 | 17134 |
| Windows 10 version 1709 | 16299 |
| Windows 10 version 1703 | 15063 |
| Windows Server 2016 | 14393 |
| Windows 10 version 1607 | 14393 |

For more information about the _TargetOSVersion_ decoration, see [Combining Platform Extensions with Operating System Versions](combining-platform-extensions-with-operating-system-versions.md).

> [!IMPORTANT]
> We highly recommend that you always decorate _models-section-name_ entries in the **Manufacturer** and [**_Models_**](inf-models-section.md) sections with platform extensions for target operating systems of Windows XP or later versions of Windows. For x86-based hardware platforms, you should avoid the use of the **.NT** platform extension and use **.NTx86** instead.

If your INF contains **Manufacturer** section entries with decorations, it must also include [**INF _Models_ sections**](inf-models-section.md) with names that match the operating system decorations. For example, if an INF contains the following **Manufacturer** section:

**%FooCorp%=FooMfg, NTx86....0x80, NTamd64**

Then the INF must also contain [**INF _Models_ sections**](inf-models-section.md) with the following names:

- **[FooMfg.NTx86....0x80]**

    This name applies to the Data Center suite of Windows XP and later versions of Windows on x86-based hardware platforms.

- **[FooMfg.NTamd64]**

    This name applies to all product types and suites of Windows XP and later versions of Windows on x64-based hardware platforms.

During installation, Windows selects an [**INF _Models_ section**](inf-models-section.md) in the following way:

1. If Windows is running in an x86-based version of the operating system (Windows XP or later versions) that includes the Data Center product suite, Windows selects the **[FooMfg.NTx86....0x80]** **_Models_** section.

1. If Windows is running in an x64-based version of the operating system (Windows XP or later versions) for any product suite, Windows selects the **[FooMfg.NTamd64]** **_Models_** section.

If the INF is intended for use with operating system versions earlier than Windows XP, it must also contain an undecorated **_Models_** section named **[FooMfg]**.

If an INF supports multiple manufacturers, these rules must be followed for each manufacturer.

The following are additional examples of _TargetOSVersion_ decorations:

- **%FooCorp% = FooMfg, NTx86**

    In this example, the resultant INF **_Models_** section name is **[FooMfg.NTx86]**, and is applicable for any x86 version of the operating system (Windows XP or later).

- **%FooCorp% = FooMfg, NT.7.8**

    In this example, for version 7.8 and later of the operating system, the resultant INF **_Models_** section name is **[FooMfg.NT.7.8]**. For earlier versions of the operating system such as Windows XP, **[FooMfg.NT]** is used.

Setup's selection of which INF **_Models_** section to use is based on the following rules:

- If the INF contains [**INF _Models_ sections**](inf-models-section.md) for several major or minor operating system version numbers, Windows uses the section with the highest version numbers that are not higher than the operating system version on which the installation is taking place.

- If the INF **_Models_** sections that match the operating system version also include product type and/or product suite decorations, Windows selects the section that most closely matches the running operating system.

Suppose, for example, Windows is executing on Windows XP (version 5.1), without the Data Center product suite, and it finds the following entry in a **Manufacturer** section:

**%FooCorp%=FooMfg, NT, NT.5, NT.5.5, NT....0x80**

In this case, Windows looks for an [**INF _Models_ section**](inf-models-section.md) named **[FooMfg.NT.5]**. Windows also uses the **[FooMfg.NT.5]** section if it is executing on a Datacenter version of Windows XP, because a specific version number takes precedence over the product type and suite mask.

If you want an INF to explicitly exclude a specific operating system version, product type, or suite, create an empty [**INF _Models_ section**](inf-models-section.md). For example, an empty section named **[FooMfg.NTx86.6.0]** prohibits installation on x86-based operating system versions 6.0 and higher.

## Examples

This example shows a **Manufacturer** section typical to an INF for a single IHV.

```inf
[Manufacturer]
%Mfg%=Contoso,NTamd64        ; Models section == Contoso

[Contoso.NTamd64]

; ...
[Strings]
Mfg = "Contoso, Ltd."
```

The next example shows part of a **Manufacturer** section typical to an INF for a device-class-specific installer:

```inf
[Manufacturer]
%CONTOSO%=Contoso_Section,NTamd64
; several entries omitted here for brevity
%FABRIKAM%=Fabrikam_Section,NTamd64
%ADATUM%=Adatum_Section,NTamd64
```

The following example shows a **Manufacturer** section that is specific to x86 platforms, Windows XP and later:

```inf
[Manufacturer]
%foo%=foosec,NTx86.5.1

[foosec.NTx86.5.1]
```

The following example shows a **Manufacturer** section that is specific to x64 platforms, Windows 10 build 14393 and later:

```inf
[Manufacturer]
%foo%=foosec,NTamd64.10.0...14393

[foosec.NTamd64.10.0...14393]
```

The following two examples show skeletal INF files with a variety of OS-specific INF _Models_ sections:

Example 1:

```inf
[Manufacturer]
%MyName% = MyName,NTx86.5.1
.
[MyName]
%MyDev% = InstallA,hwid
.
[MyName.NTx86.5.1]
%MyDev% = InstallB,hwid
.
[InstallA]   ; Windows 2000 
.
.
[InstallB]   ; Windows XP and later, x86 only
.
```

Example 2:

```inf
[Manufacturer]
%MyName% = MyName,NTx86.6.0,NTx86.5.1,
.
[MyName.NTx86.6.0] ; Empty section, so this INF does not support
.                  ; NT 6.0 and later.
.
[MyName.NTx86.5.1] ; Used for NT 5.1 and later
.                  ; (but not NT 6.0 and later due to the NTx86.6.0 entry)
%MyDev% = InstallB,hwid
.
[MyName]           ; Empty section, so this INF does not support
.                  ; Win2000
.
```

Example 3:

```inf
[Manufacturer]
%MyMfg% = MyMfg, NTamd64.6.1, NTamd64.10.0, NTamd64.10.0...14310
.
[MyMfg.NTamd64.6.1]          ; Used for Windows 7 and later
.                            ; (but not for Windows 10 and later due to the NT.10.0 entry)
.
[MyMfg.NTamd64.10.0]         ; Used for Windows 10
.                            ; (but not for Windows 10 build 14393 and later due to the NT.10.0...14393 entry)
.
[MyMfg.NTamd64.10.0...14393] ; Used for Windows 10 build 14393 and later
.
.
```

> [!NOTE]
> When specifying multiple TargetOSVersions, string them together in one entry as seen in this example.  Do not represent each target as a separate entry.

## See also

[Combining platform extensions with operating system versions](combining-platform-extensions-with-operating-system-versions.md)

[**_Models_**](inf-models-section.md)

[**Strings**](inf-strings-section.md)
