---
title: Inf2Cat
description: Inf2Cat (Inf2Cat.exe) is a command-line tool that determines whether a driver package's INF file can be digitally-signed for a specified list of Windows versions.
keywords:
- Inf2Cat Driver Development Tools
topic_type:
- apiref
ms.topic: reference
api_name:
- Inf2Cat
api_type:
- NA
ms.date: 05/31/2023
---

# Inf2Cat

Inf2Cat (Inf2Cat.exe) is a command-line tool that determines whether a [driver package's](../install/driver-packages.md) INF file can be digitally-signed for a specified list of Windows versions. If so, Inf2Cat generates the unsigned [catalog files](../install/catalog-files.md) that apply to the specified Windows versions.

```command
    Inf2Cat /driver:
    PackagePath
     /os:
    WindowsVersionList [/nocat] [/verbose] [/?] [other switches]
```

The Inf2Cat tool is located in the Program Files\\Windows Kits\\8.0\\bin\\x86 or Program Files (x86)\\Windows Kits\\8.0\\bin\\x86 folder of the WDK.

## Troubleshooting

If you see `DriverVer set to a date in the future` when building your driver, change your driver package project settings so that Inf2Cat sets `/uselocaltime`. To do so, use **Configuration Properties->Inf2Cat->General->Use Local Time**. Now both [Stampinf](stampinf-command-options.md) and Inf2Cat use local time.

If you see `An attempt was made to load a program with an incorrect format. (Exception from HRESULT: 0x8007000B) Signability test failed.`, try one of these workarounds:

1. Set the project's inf2cat settings to `/nocat` and run inf2cat manually.
2. Delete `inf2cat.exe.manifest` from the `\x86` folder of the active WDK to cause the tool to run in Visual Studio.

## Switches and Arguments

### /driver:*PackagePath*

Specifies the path to the directory that contains the INF files for driver packages. If the specified directory contains INF files for multiple driver packages, Inf2Cat will create catalog files for each driver package.

> [!NOTE]
> You can use the **/drv:** switch in place of the **/driver:** switch.

### /nocat

Configures Inf2Cat to verify that the [driver package](../install/driver-packages.md) complies with the signing requirements for the specified Windows versions, but not to generate a catalog files.

### /os:*WindowsVersionList*
  
Configures Inf2Cat to verify that a [driver package's](../install/driver-packages.md) INF file complies with the signing requirements for the Windows versions that are specified by *WindowsVersionList*. *WindowsVersionList* is a comma-separated list that includes one or more of the following version identifiers.

|Windows version|Version identifier|
|--- |--- |
|Windows 11, version 22H2 x64 Edition|10_NI_X64|
|Windows 11, version 22H2 Arm64 Edition|10_NI_ARM64|
|Windows 11, version 21H2 x64 Edition|10_CO_X64|
|Windows 11, version 21H2 Arm64 Edition|10_CO_ARM64|
|Windows Server 2022 x64 Edition|ServerFE_X64|
|Windows Server 2022 Arm64 Edition|ServerFE_ARM64|
|Windows 10, version 22H2, 21H2, 21H1, 20H2, 2004 x86 Edition|10_VB_X86|
|Windows 10, version 22H2, 21H2, 21H1, 20H2, 2004 x64 Edition|10_VB_X64|
|Windows 10, version 22H2, 21H2, 21H1, 20H2, 2004 Arm64 Edition|10_VB_ARM64|
|Windows 10, version 1909, 1903 x86 Edition|10_19H1_X86|
|Windows 10, version 1909, 1903 x64 Edition|10_19H1_X64|
|Windows 10, version 1909, 1903 Arm64 Edition|10_19H1_ARM64|
|Windows 10, version 1809 x86 Edition|10_RS5_X86|
|Windows 10, version 1809 x64 Edition|10_RS5_X64|
|Windows 10, version 1809 Arm64 Edition|10_RS5_ARM64|
|Windows Server 2019 x64 Edition|ServerRS5_X64|
|Windows Server 2019 Arm64 Edition|ServerRS5_ARM64|
|Windows 10, version 1803 x86 Edition|10_RS4_X86|
|Windows 10, version 1803 x64 Edition|10_RS4_X64|
|Windows 10, version 1803 Arm64 Edition|10_RS4_ARM64|
|Windows 10, version 1709 x86 Edition|10_RS3_X86|
|Windows 10, version 1709 x64 Edition|10_RS3_X64|
|Windows 10, version 1709 Arm64 Edition|10_RS3_ARM64|
|Windows 10, version 1703 x86 Edition|10_RS2_X86|
|Windows 10, version 1703 x64 Edition|10_RS2_X64|
|Windows 10, version 1607 x86 Edition|10_AU_X86|
|Windows 10, version 1607 x64 Edition|10_AU_X64|
|Windows Server 2016 x64 Edition|SERVER2016_X64|
|Windows 10 x86 Edition|10_X86|
|Windows 10 x64 Edition|10_X64|
|Windows Server 2016|Server10_X64|
|Windows Server 2016 on Arm|Server10_ARM64|

> [!NOTE]
> Starting with Windows Server 2008 R2, Windows server operating systems will no longer support x86-based platforms.

Inf2Cat ignores the case of the alphabetic characters of the version identifier strings. For example, 10\_NI\_X64 and 10\_ni\_X64  are both valid identifiers for Windows 11, version 22H2 x64 Edition.

### /uselocaltime

Use local timezone while running driver timestamp verification tests. By default UTC is used.

### /verbose

Configures Inf2Cat to display detailed information in a command window.

### /?

Configures Inf2Cat to display help information in a command window.

### /drm

*Deprecated command line argument.*  
Add drm signature attribute in .inf file to add drm signature attribute.

### /pe

*Deprecated command line argument.*  
Add petrust signature attribute in .inf file to add petrust signature attribute.

### /pageHashes

Include page hashes with files.  Optionally followed by a list of files.

## Comments

The Inf2Cat tool checks [driver package's](../install/driver-packages.md) INF files for structural errors and verifies that a driver package can be digitally-signed. A driver package can be signed only if all of the files that are referenced in an INF file are present and the source files are in the correct location. If an INF file cannot be signed or if it contains structural errors, the driver package might not be installed correctly or might incorrectly display a driver signing warning dialog box during installation.

Inf2Cat generates a [catalog file](../install/catalog-files.md) only if the catalog file is specified in the driver package's INF file and the catalog file applies to one or more of the specified Windows versions. If the [**INF Version section**](../install/inf-version-section.md) of an INF file supplies only a CatalogFile=*filename.cat* directive, that catalog file applies to the entire driver package. To support [cross-platform installations](../install/creating-inf-files-for-multiple-platforms-and-operating-systems.md), the INF file should include CatalogFile.*PlatformExtension*=*unique-filename.cat* directives.

For more information about signing a driver package, see [Driver Signing](../install/driver-signing.md).

To use Inf2Cat, you must be a member of the Administrators group on the system.

## Examples

In the following example, c:\\MyDriver contains a [driver package](../install/driver-packages.md) whose INF file is MyInfFile.inf and the INF Version section in the INF file includes only the following **CatalogFile** directive:

```command
[Version]
. . .
CatalogFile=MyCatalogFile.cat
. . .
```

For this example, the following Inf2Cat command would verify whether the driver package can be signed for Windows 10, version 21H2, 21H1, 20H2, 2004 x64 Edition and for Windows 11, version 21H2 x64 Edition. If the package can be signed for these versions, Inf2Cat would create the unsigned catalog file MyCatalogFile.cat.

```command
Inf2Cat /driver:C:\MyDriver /os:10_VB_X64,10_CO_X64 
```

In the following example, c:\\MyDriver contains a [driver package](../install/driver-packages.md) whose INF file is MyInfFile.inf and the INF **Version** section in the INF file includes only the following two **CatalogFile** directives with platform extensions:

```command
[Version]
. . .
CatalogFile.ntx86=MyCatalogFileX86.cat
CatalogFile.ntamd64=MyCatalogFileX64.cat
. . .
```

For this example, the following Inf2Cat command would verify whether the driver package can be signed for Windows 10, version 1809 x86 Edition and X64 Edition. In addition it checks if it can be signed by Windows Windows 10, version 1909, 1903 x86 Edition and X64 Edition. If the package can be signed for all of these versions, Inf2Cat will create the unsigned catalog files MyCatalogFileX86.cat and MyCatalogFileX64.cat.

```command
Inf2Cat /driver:C:\MyDriver /os:10_RS5_X86,10_RS5_X64,10_19H1_X86,10_19H1_X64 
```

For more information about how to use Inf2Cat to create a catalog file, see [Creating a Catalog File for a PnP Driver Package](../install/creating-a-catalog-file-for-a-pnp-driver-package.md).
