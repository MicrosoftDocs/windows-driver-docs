---
title: Inf2Cat
description: Inf2Cat (Inf2Cat.exe) is a command-line tool that determines whether a driver package's INF file can be digitally-signed for a specified list of Windows versions.
ms.assetid: 5d85058e-4051-4321-a4c1-b1a71d232b7f
keywords:
- Inf2Cat Driver Development Tools
topic_type:
- apiref
api_name:
- Inf2Cat
api_type:
- NA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Inf2Cat


Inf2Cat (Inf2Cat.exe) is a command-line tool that determines whether a [driver package's](https://msdn.microsoft.com/library/windows/hardware/ff544840) INF file can be digitally-signed for a specified list of Windows versions. If so, Inf2Cat generates the unsigned [catalog files](https://msdn.microsoft.com/library/windows/hardware/ff537872) that apply to the specified Windows versions.

```
    Inf2Cat /driver:
    PackagePath
     /os:
    WindowsVersionList [/nocat] [/verbose] [/?] [other switches]
```

> [!TIP]
> If you see `DriverVer set to a date in the future` when building your driver, change your driver package project settings so that Inf2Cat sets `/uselocaltime`. To do so, use **Configuration Properties->Inf2Cat->General->Use Local Time**. Now both [Stampinf](stampinf-command-options.md) and Inf2Cat use local time.

### <span id="switches_and_arguments"></span><span id="SWITCHES_AND_ARGUMENTS"></span>Switches and Arguments

<span id="_driver_PackagePath"></span><span id="_driver_packagepath"></span><span id="_DRIVER_PACKAGEPATH"></span>**/driver:**<em>PackagePath</em>  
Specifies the path to the directory that contains the INF files for driver packages. If the specified directory contains INF files for multiple driver packages, Inf2Cat will create catalog files for each driver package.

**Note**  You can use the **/drv:** switch in place of the **/driver:** switch.

 

<span id="_nocat"></span><span id="_NOCAT"></span>**/nocat**  
Configures Inf2Cat to verify that the [driver package](https://msdn.microsoft.com/library/windows/hardware/ff544840) complies with the signing requirements for the specified Windows versions, but not to generate a catalog files.

<span id="_os_WindowsVersionList"></span><span id="_os_windowsversionlist"></span><span id="_OS_WINDOWSVERSIONLIST"></span>**/os:**<em>WindowsVersionList</em>  
Configures Inf2Cat to verify that a [driver package's](https://msdn.microsoft.com/library/windows/hardware/ff544840) INF file complies with the signing requirements for the Windows versions that are specified by *WindowsVersionList*. *WindowsVersionList* is a comma-separated list that includes one or more of the following version identifiers.

|Windows version|Version identifier|
|--- |--- |
|Windows 10 x86 Edition|10_X86|
|Windows 10 x64 Edition|10_X64|
|Windows Server 2016|Server10_X64|
|Windows Server 2016 on ARM|Server10_ARM64|
|Windows 8.1 x86 Edition|6_3_X86|
|Windows 8.1 x64 Edition|6_3_X64|
|Windows 8.1 ARM Edition|6_3_ARM|
|Windows Server 2012 R2|Server6_3_X64|
|Windows 8 x64 Edition|8_X64|
|Windows 8 x86 Edition|8_X86|
|Windows 8 ARM Edition|8_ARM|
|Windows Server 2012|Server8_X64|
|Windows Server 2008 R2 x64 Edition|Server2008R2_X64|
|Windows Server 2008 R2 Itanium Edition|Server2008R2_IA64|
|Windows 7 x64 Edition|7_X64|
|Windows 7 x86 Edition|7_X86|
|Windows Server 2008 x64 Edition|Server2008_X64|
|Windows Server 2008 Itanium Edition|Server2008_IA64|
|Windows Server 2008 x86 Edition|Server2008_X86|


 

**Note**  Starting with Windows Server 2008 R2, Windows server operating systems will no longer support x86-based platforms.

 

Inf2Cat ignores the case of the alphabetic characters of the version identifier strings. For example, vista\_x64 and Vista\_X64 are both valid identifiers for Windows Vista x64 Edition.

<span id="_verbose"></span><span id="_VERBOSE"></span>**/verbose**  
Configures Inf2Cat to display detailed information in a command window.

<span id="__"></span>**/?**  
Configures Inf2Cat to display help information in a command window.

<span id="other_switches"></span><span id="OTHER_SWITCHES"></span>*other switches*  
Configures Inf2Cat to add a DRM level catalog attribute or a PE catalog attribute to files, or to add page hashes to files. For more information, use the **/?** switch.

### <span id="comments"></span><span id="COMMENTS"></span>Comments

The Inf2Cat tool replaces the Signability tool that was included in versions of the WDK prior to Windows Vista.

To use Inf2Cat, you must be a member of the Administrators group on the system.

The Inf2Cat tool checks [driver package's](https://msdn.microsoft.com/library/windows/hardware/ff544840) INF files for structural errors and verifies that a driver package can be digitally-signed. A driver package can be signed only if all of the files that are referenced in an INF file are present and the source files are in the correct location. If an INF file cannot be signed or if it contains structural errors, the driver package might not be installed correctly or might incorrectly display a driver signing warning dialog box during installation.

Inf2Cat generates a [catalog file](https://msdn.microsoft.com/library/windows/hardware/ff537872) only if the catalog file is specified in the driver package's INF file and the catalog file applies to one or more of the specified Windows versions. If the [**INF Version section**](https://msdn.microsoft.com/library/windows/hardware/ff547502) of an INF file supplies only a **CatalogFile=**<em>filename.cat</em> directive, that catalog file applies to the entire driver package. To support [cross-platform installations](https://msdn.microsoft.com/library/windows/hardware/ff540206), the INF file should include **CatalogFile.**<em>PlatformExtension</em>**=**<em>unique-filename.cat</em> directives.

For more information about signing a driver package, see [Driver Signing](https://msdn.microsoft.com/library/windows/hardware/ff544865) and [Device and Driver Installation Fundamental Topics](https://msdn.microsoft.com/library/windows/hardware/ff541165).

The Inf2Cat tool is located in the Program Files\\Windows Kits\\8.0\\bin\\x86 or Program Files (x86)\\Windows Kits\\8.0\\bin\\x86 folder of the WDK.

### <span id="examples"></span><span id="EXAMPLES"></span>Examples

In the following example, c:\\MyDriver contains a [driver package](https://msdn.microsoft.com/library/windows/hardware/ff544840) whose INF file is MyInfFile.inf and the INF Version section in the INF file includes only the following **CatalogFile** directive:

```
[Version]
. . .
CatalogFile=MyCatalogFile.cat
. . .
```

For this example, the following Inf2Cat command would verify whether the driver package can be signed for Windows 2000 and for the x86 versions of Windows Vista, Windows Server 2003, and Windows XP. If the package can be signed for these versions, Inf2Cat would create the unsigned catalog file MyCatalogFile.cat.

```
Inf2Cat /driver:C:\MyDriver /os:2000,XP_X86,Server2003_X86,Vista_X86
```

In the following example, c:\\MyDriver contains a [driver package](https://msdn.microsoft.com/library/windows/hardware/ff544840) whose INF file is MyInfFile.inf and the INF **Version** section in the INF file includes only the following two **CatalogFile** directives with platform extensions:

```
[Version]
. . .
CatalogFile.ntx86=MyCatalogFileX86.cat
CatalogFile.ntamd64=MyCatalogFileX64.cat
. . .
```

For this example, the following Inf2Cat command would verify whether the driver package can be signed for Windows 2000 and the x86 versions of Windows Vista, Windows Server 2003, and Windows XP. In addition, the command would verify whether the driver package can be signed for the x64 editions of Windows Vista, Windows Server 2003, and Windows XP. If the package can be signed for all of these versions, Inf2Cat will create the unsigned catalog files MyCatalogFileX86.cat and MyCatalogFileX64.cat.

```
Inf2Cat /driver:C:\MyDriver /os:2000,XP_X86,XP_X64,Server2003_X86,Server2003_X64,Vista_X86,Vista_X64
```

For more information about how to use Inf2Cat to create a catalog file, see [Creating a Catalog File for a PnP Driver Package](https://msdn.microsoft.com/library/windows/hardware/ff540161).

 

 





