---
title: Using INX Files to Create INF Files
description: Using INX Files to Create INF Files
ms.assetid: b49f8fed-c2b5-46e2-aeaf-e09231fa1578
keywords: ["INX files WDK KMDF", "Build utility WDK KMDF", "Stampinf WDK KMDF", "KMDF WDK , INX files", "Kernel-Mode Driver Framework WDK , INX files"]
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

```
[Manufacturer]
%StdMfg%=Standard,NT$ARCH$
```

<a href="" id="-kmdfcoinstallerversion-"></a>$KMDFCOINSTALLERVERSION$  
If you use the [Stampinf](https://msdn.microsoft.com/library/windows/hardware/ff552786) tool's -*k* option, Stampinf replaces this variable with a string that represents a specific version of the KMDF co-installer. You can use the $KMDFCOINSTALLERVERSION$ variable when you specify the framework's co-installer within an INF file, such as within an [**INF DDInstall.CoInstallers section**](https://msdn.microsoft.com/library/windows/hardware/ff547321), as follows:

```
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

```
KmdfLibraryVersion = $KMDFVERSION$
```

<a href="" id="-umdfcoinstallerversion-"></a>$UMDFCOINSTALLERVERSION$  
```
[SourceDisksFiles]
WudfUpdate_$UMDFCOINSTALLERVERSION$.dll=1

[CoInstallers_CopyFiles]
WudfUpdate_$UMDFCOINSTALLERVERSION$.dll

[CoInstallers_AddReg]
HKR,,CoInstallers32,0x00010000,"WUDFUpdate_$UMDFCOINSTALLERVERSION$.dll"
```

<a href="" id="-umdfversion-"></a>$UMDFVERSION$  
```
[UMDFYourDriver_Install]
UmdfLibraryVersion=$UMDFVERSION$
```

[Stampinf](https://msdn.microsoft.com/library/windows/hardware/ff552786) also supports a -*u* option to replace UMDF string variables in an INX file. If your driver package includes both UMDF-based drivers and KMDF-based drivers, you can use the -*k* and -*u* options with a single Stampinf command and a single INX file.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Using%20INX%20Files%20to%20Create%20INF%20Files%20%20RELEASE:%20%283/24/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




