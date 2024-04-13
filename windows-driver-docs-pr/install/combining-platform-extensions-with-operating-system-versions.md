---
title: Combining Platform Extensions with Operating System Versions
description: Provides information on combining platform extensions with operating system versions
ms.date: 06/15/2022
---

# Combining platform extensions with operating system versions

Within the [**INF Manufacturer section**](inf-manufacturer-section.md) of an INF file, you can supply [**INF *Models* sections**](inf-models-section.md) that are specific to various versions of the Windows operating system. These version-specific *Models* sections are identified by using the *TargetOSVersion* decoration.

Within the same INF file, different [**INF *Models* sections**](inf-models-section.md) can be specified for different versions of the operating system. The specified versions indicate target operating system versions with which the INF *Models* sections will be used. If no versions are specified, Windows uses a *Models* section without the *TargetOSVersion* decoration for all versions of all operating systems.

## *TargetOSVersion* decoration format

The following example shows the correct format of the *TargetOSVersion* decoration for Windows XP through Windows 10, version 1511:

**nt**[*Architecture*][**.**[*OSMajorVersion*][**.**[*OSMinorVersion*][**.**[*ProductType*][**.**[*SuiteMask*]]]]]

Starting with Windows 10, version 1607 (Build 14310 and later), the correct format of the *TargetOSVersion* decoration includes *BuildNumber*:

**nt**[*Architecture*][**.**[*OSMajorVersion*][**.**[*OSMinorVersion*][**.**[*ProductType*][**.**[*SuiteMask*]][**.**[*BuildNumber*]]]]]

Each field is defined as follows:

**nt**  
Specifies that the target operating system is NT-based. Windows 2000 and later versions of Windows are all NT-based.

*Architecture*  
Identifies the hardware platform. For more information on architecture platform decorations on *Models* sections, see [Creating INF Files for Multiple Platforms and Operating Systems](creating-inf-files-for-multiple-platforms-and-operating-systems.md).

*OSMajorVersion*  
A number that represents the major version number for the operating system. For a table listing major versions for the Windows operating systems, see *OSMajorVersion* in [INF Manufacturer section](inf-manufacturer-section.md).

*OSMinorVersion*  
A number that represents the minor version number for the operating system. For a table listing minor versions for the Windows operating systems, see *OSMinorVersion* in [INF Manufacturer section](inf-manufacturer-section.md).

*ProductType*  
A number that represents *one* of the VER_NT_*xxxx* flags defined in *Winnt.h*, such as the following:

**0x0000001** (VER_NT_WORKSTATION)

**0x0000002** (VER_NT_DOMAIN_CONTROLLER)

**0x0000003** (VER_NT_SERVER)

If a product type is specified, the INF file will be used only if the operating system matches the specified product type. If the INF file supports multiple product types for a single operating system version, multiple *TargetOSVersion* entries are required.

*SuiteMask*  
A number that represents *a combination of* one or more of the VER_SUITE_*xxxx* flags defined in *Winnt.h*. These flags include the following:

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

If one or more suite mask values are specified, the INF file will be used only if the operating system matches all the specified product suites. If the INF file supports multiple product suite combinations for a single operating system version, multiple *TargetOSVersion* entries are required.

*BuildNumber*  
Specifies the minimum OS build number of the Windows 10 release to which the section applies, starting with build 14310 or later. For a table listing build numbers for the Windows operating systems, see *BuildNumber* in [INF Manufacturer section](inf-manufacturer-section.md).

The build number is assumed to be relative to some specific OS major/minor version only, and may be reset for some future OS major/minor version.

Any build number specified by the *TargetOSVersion* decoration is evaluated only when the OS major/minor version of the *TargetOSVersion* matches the current OS (or AltPlatformInfo) version exactly.  If the current OS version is greater than the OS version specified by the *TargetOSVersion* decoration (OSMajorVersion,OSMinorVersion), the section is considered applicable regardless of the build number specified. Likewise, if the current OS version is less than the OS version specified by the TargetOSVersion decoration, the section is not applicable.

If build number is supplied, the OS version and BuildNumber of the *TargetOSVersion* decoration must both be greater than the OS version and build number of the Windows 10 build 14310 where this decoration was first introduced.  Earlier versions of the operating system without these changes (for example, Windows 10 build 10240) will not parse unknown decorations, so an attempt to target these earlier builds will actually prevent that OS from considering the decoration valid at all.

## How Windows processes *TargetOSVersion* decorations

When you install a driver package on a device, Windows follows these steps to process the [**INF *Models* sections**](inf-models-section.md) within an INF file:

1. If one or more [**INF *Models* sections**](inf-models-section.md) have the *TargetOS* decoration, Windows selects the INF *Models* section that is closest to the attributes for the host operating system.

    For example, if an INF *Models* section has a *TargetOS* decoration of **ntx86.5.1**, Windows selects that section if the host operating system is running Windows XP or later version of Windows on an x86-based system.

    Similarly, if an [**INF *Models* section**](inf-models-section.md) has a *TargetOS* decoration of **nt.6.0**, Windows selects that section if the host operating system is Windows Vista or later version of Windows on any supported hardware platform.

    If an INF *Models* section has a *TargetOS* decoration of **nt.10.0...14393**, Windows selects that section if the host operating system is running a Windows 10 build equal to or greater than 14393 on any supported hardware platform.

1. If none of the [**INF *Models* sections**](inf-models-section.md) have a *TargetOS* decoration that matches the host operating system, Windows selects the *Models* section that has either a matching platform extension or no platform extension.

    For example, if an INF *Models* section has a platform extension of **ntx86**, Windows selects that section if the host operating system is Microsoft Windows 2000 or later version of Windows on an x86-based system.

1. If Windows cannot find a matching [**INF *Models* section**](inf-models-section.md), it will not install that driver package on the device.

### How *TargetOsVersion* decorations are resolved

When determining the applicable [**INF *Models* sections**](inf-models-section.md), the evaluation is performed per-line within the [**INF Manufacturer section**](inf-manufacturer-section.md), where, for a given OS version, each line may have up to one applicable section.

The below INF excerpt shows an example where [ExampleModelsSection_1.NTamd64.10.0...17134] will be selected on a Windows build number equal to or greater than 17134 , and *both* [ExampleModelsSection_1.NTamd64.10.0...17134] and [ExampleModelsSection_2.NTamd64.10.0...22000] will be selected on a Windows build number equal to or greater than 22000.

```inf
[Manufacturer]
%ManufacturerName% = ExampleModelsSection_1,NTamd64.10.0...17134
%ManufacturerName% = ExampleModelsSection_2,NTamd64.10.0...22000
```

The below INF excerpt shows an example where [ExampleModelsSection_1.NTamd64.10.0...17134] will be selected on a Windows build number equal to or greater than 17134, and [ExampleModelsSection_1.NTamd64.10.0...22000] will be selected on a Windows build number equal to or greater than 22000.

```inf
[Manufacturer]
%ManufacturerName% = ExampleModelsSection_1,NTamd64.10.0...17134,NTamd64.10.0...22000
```

## Sample INF *Models* sections with *TargetOSVersion* decorations

### Apply to a particular OS version and later

This INF excerpt shows how you can specify that a driver package only applies to a particular OS version and later.

```inf
[Manufacturer]
%ManufacturerName% = ExampleModelsSection,NTamd64.10.0...17134

; This driver package applies to Windows 10 1803 (build 17134) and later only

[ExampleModelsSection.NTamd64.10.0...17134]
%DeviceDesc%=ExampleInstallSection,ExampleHardwareId

[ExampleInstallSection]
...
```

### Apply to only a single OS version

This INF excerpt shows how you can specify that a driver package only applies to a single OS version.

```inf
[Manufacturer]
%ManufacturerName% = ExampleModelsSection,NTamd64.10.0...17134,NTamd64.10.0...17763

; This driver package applies to Windows 10 1803 (build 17134)

[ExampleModelsSection.NTamd64.10.0...17134]
%DeviceDesc%=ExampleInstallSection,ExampleHardwareId

; However, this driver package does nothing on Windows 10 1809 (build 17763) and later
[ExampleModelsSection.NTamd64.10.0...17763]
; intentionally left empty

[ExampleInstallSection]
...
```

### Apply to multiple OS versions with different settings

This INF excerpt shows how you can specify that a driver package should go through different installation instructions for different OS versions.

```inf
[Manufacturer]
%ManufacturerName% = ExampleModelsSection,NTamd64.6.1,NTamd64.10.0

; This driver package applies to Windows 7 and later

[ExampleModelsSection.NTamd64.6.1]
%DeviceDesc%=ExampleInstallSection_Win7,ExampleHardwareId

; However, this driver package has different installation instructions on Windows 10 and later

[ExampleModelsSection.NTamd64.10.0]
%DeviceDesc%=ExampleInstallSection_Win10,ExampleHardwareId

[ExampleInstallSection_Win7]
...

[ExampleInstallSection_Win10]
...
```
