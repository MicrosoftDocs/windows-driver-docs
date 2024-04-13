---
title: Using INX Files to Create INF Files
description: Using INX Files to Create INF Files
keywords:
- INX files WDK KMDF
- Build utility WDK KMDF
- Stampinf WDK KMDF
- KMDF WDK , INX files
- Kernel-Mode Driver Framework WDK , INX files
ms.date: 05/07/2022
---

# Using INX Files to Create INF Files

When you're writing a Windows driver, instead of maintaining multiple version-specific INF files, you can create a single INX file and use Microsoft Visual Studio or the [Stampinf](../devtest/stampinf.md) tool to generate version-specific INF files when you need them.

An *INX file* is like an INF file, but it contains string variables that represent version information.

When you build your driver using  Visual Studio, the build process runs Stampinf to replace the string variables in INX files with text strings that represent a specific hardware architecture or a framework version. You can also manually run Stampinf, which is located in the *bin* subdirectory of the WDK.

To modify Stampinf properties within Visual Studio:

1. Open the Property Pages for your driver package project.
1. Right-click the package project in Solution Explorer and select **Properties**.
1. In the Property Pages for the package, click **Configuration Properties**, and then **StampInf**.

The WDK includes INX files for all the KMDF and UMDF sample drivers.

You can use the following string variables in an INX file:

*$ARCH$*
<ul>
Stampinf replaces this variable with an architecture-specific string. For example, if you are using an x86 build environment, the tool replaces $ARCH$ with "x86". You can use the $ARCH$ string wherever you need to specify a specific architecture within an INF file, such as within an [**INF Manufacturer section**](../install/inf-manufacturer-section.md), as follows:

<pre>
[Manufacturer]
%StdMfg%=Standard,NT$ARCH$
</pre>
</ul>

*$KMDFCOINSTALLERVERSION$*
<ul>
If you use the [Stampinf](../devtest/stampinf.md) tool's -*k* option, Stampinf replaces this variable with a string that represents a specific version of the KMDF co-installer. You can use the $KMDFCOINSTALLERVERSION$ variable when you specify the framework's co-installer within an INF file, such as within an [**INF DDInstall.CoInstallers section**](../install/inf-ddinstall-coinstallers-section.md), as follows:

<pre>
[ECHO_Device.NT.CoInstallers]
AddReg=ECHO_Device_CoInstaller_AddReg
CopyFiles=ECHO_Device_CoInstaller_CopyFiles

[ECHO_Device_CoInstaller_AddReg]
HKR,,CoInstallers32,0x00010000, "WdfCoInstaller$KMDFCOINSTALLERVERSION$.dll,WdfCoInstaller"

[ECHO_Device_CoInstaller_CopyFiles]
WdfCoInstaller$KMDFCOINSTALLERVERSION$.dll
</pre>
</ul>

*$KMDFVERSION$*
<ul>
If you set the **KMDF Version Number** property in Visual Studio (or use the [Stampinf](../devtest/stampinf.md) tool's -*k* option), Stampinf replaces this variable with a string that represents a specific version of KMDF. You can use the $KMDFVERSION$ variable when you specify the framework's version within an INF file, such as when you specify the [KmdfLibraryVersion](installing-the-framework-s-co-installer.md) directive, as follows:

<pre>
KmdfLibraryVersion = $KMDFVERSION$
</pre>
</ul>

*$UMDFCOINSTALLERVERSION$*
<ul>
<pre>
[SourceDisksFiles]
WudfUpdate_$UMDFCOINSTALLERVERSION$.dll=1

[CoInstallers_CopyFiles]
WudfUpdate_$UMDFCOINSTALLERVERSION$.dll

[CoInstallers_AddReg]
HKR,,CoInstallers32,0x00010000,"WUDFUpdate_$UMDFCOINSTALLERVERSION$.dll"
</pre>
</ul>

*$UMDFVERSION$*
<ul>
<pre>
[UMDFYourDriver_Install]
UmdfLibraryVersion=$UMDFVERSION$
</pre>
</ul>

[Stampinf](../devtest/stampinf.md) also supports a -*u* option to replace UMDF string variables in an INX file. If your driver package includes both UMDF-based drivers and KMDF-based drivers, you can use the -*k* and -*u* options with a single Stampinf command and a single INX file.
