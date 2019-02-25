---
title: Using INX Files to Create INF Files
description: Using INX Files to Create INF Files
ms.assetid: b49f8fed-c2b5-46e2-aeaf-e09231fa1578
keywords:
- INX files WDK KMDF
- Build utility WDK KMDF
- Stampinf WDK KMDF
- KMDF WDK , INX files
- Kernel-Mode Driver Framework WDK , INX files
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using INX Files to Create INF Files


An *INX file* is an INF file that contains string variables that represent version information. When you build your driver using Microsoft Visual Studio, the build process runs the [Stampinf](https://msdn.microsoft.com/library/windows/hardware/ff552786) tool to replace the string variables in INX files with text strings that represent a specific hardware architecture or a framework version. You can also manually run the Stampinf tool, which is located in the *bin* subdirectory of the WDK.

If you create INX files for your drivers, you do not have to maintain multiple version-specific INF files. Instead, you can create a single INX file and use Visual Studio or Stampinf to generate version-specific INF files when you need them.

To modify Stampinf properties within Visual Studio, open the Property Pages for your driver package project. Right-click the package project in Solution Explorer and select **Properties**. In the Property Pages for the package, click **Configuration Properties**, and then **StampInf**.

You can also manually run the Stampinf tool, which is located in the *bin* subdirectory of the WDK.

The WDK includes INX files for all the KMDF and UMDF sample drivers.

INX files can contain the following string variables:

<a href="" id="-arch-"></a>$ARCH$  
Stampinf replaces this variable with an architecture-specific string. For example, if you are using an x86 build environment, the tool replaces $ARCH$ with "x86". You can use the $ARCH$ string wherever you need to specify a specific architecture within an INF file, such as within an [**INF Manufacturer section**](https://msdn.microsoft.com/library/windows/hardware/ff547454), as follows:

```cpp
[Manufacturer]
%StdMfg%=Standard,NT$ARCH$
```

<a href="" id="-kmdfcoinstallerversion-"></a>$KMDFCOINSTALLERVERSION$  
If you use the [Stampinf](https://msdn.microsoft.com/library/windows/hardware/ff552786) tool's -*k* option, Stampinf replaces this variable with a string that represents a specific version of the KMDF co-installer. You can use the $KMDFCOINSTALLERVERSION$ variable when you specify the framework's co-installer within an INF file, such as within an [**INF DDInstall.CoInstallers section**](https://msdn.microsoft.com/library/windows/hardware/ff547321), as follows:

```cpp
[ECHO_Device.NT.CoInstallers]
AddReg=ECHO_Device_CoInstaller_AddReg
CopyFiles=ECHO_Device_CoInstaller_CopyFiles

[ECHO_Device_CoInstaller_AddReg]
HKR,,CoInstallers32,0x00010000, "WdfCoInstaller$KMDFCOINSTALLERVERSION$.dll,WdfCoInstaller"

[ECHO_Device_CoInstaller_CopyFiles]
WdfCoInstaller$KMDFCOINSTALLERVERSION$.dll
```

<a href="" id="-kmdfversion-"></a>$KMDFVERSION$  
If you set the **KMDF Version Number** property in Visual Studio (or use the [Stampinf](https://msdn.microsoft.com/library/windows/hardware/ff552786) tool's -*k* option), Stampinf replaces this variable with a string that represents a specific version of KMDF. You can use the $KMDFVERSION$ variable when you specify the framework's version within an INF file, such as when you specify the [KmdfLibraryVersion](installing-the-framework-s-co-installer.md) directive, as follows:

```cpp
KmdfLibraryVersion = $KMDFVERSION$
```

<a href="" id="-umdfcoinstallerversion-"></a>$UMDFCOINSTALLERVERSION$  
```cpp
[SourceDisksFiles]
WudfUpdate_$UMDFCOINSTALLERVERSION$.dll=1

[CoInstallers_CopyFiles]
WudfUpdate_$UMDFCOINSTALLERVERSION$.dll

[CoInstallers_AddReg]
HKR,,CoInstallers32,0x00010000,"WUDFUpdate_$UMDFCOINSTALLERVERSION$.dll"
```

<a href="" id="-umdfversion-"></a>$UMDFVERSION$  
```cpp
[UMDFYourDriver_Install]
UmdfLibraryVersion=$UMDFVERSION$
```

[Stampinf](https://msdn.microsoft.com/library/windows/hardware/ff552786) also supports a -*u* option to replace UMDF string variables in an INX file. If your driver package includes both UMDF-based drivers and KMDF-based drivers, you can use the -*k* and -*u* options with a single Stampinf command and a single INX file.

 

 





