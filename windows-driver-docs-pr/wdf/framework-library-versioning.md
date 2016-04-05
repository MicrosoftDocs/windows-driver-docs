---
title: Framework Library Versioning
description: In this topic, you'll learn about the naming conventions for the file names of the Kernel-Mode Driver Framework (KMDF) library and the User-Mode Driver Framework (UMDF) library.
ms.assetid: 51db6f3c-45cb-46a7-9dd4-2bab67893fea
keywords: ["kernel-mode drivers WDK KMDF , library versions", "KMDF WDK , library versions", "Kernel-Mode Driver Framework WDK , library versions", "library WDK KMDF", "version numbers WDK KMDF", "major version numbers WDK KMDF", "minor version numbers WDK KMDF"]
---

# Framework Library Versioning


In this topic, you'll learn about the naming conventions for the file names of the Kernel-Mode Driver Framework (KMDF) library and the User-Mode Driver Framework (UMDF) library.

## KMDF


A major version number and a minor version number are assigned to each version of the KMDF library. The library's file name contains the major version number. The file name's format is:

**Wdf**&lt;*MajorVersionNumber*&gt;**000.sys**

The major version number uses two characters. For example, the file name for version 1.0 of the library is *Wdf01000.sys*. Versions 1.9, 1.11, and so on are also named *Wdf01000.sys*, and each new minor version of the library file overwrites the previous version of the file.

If you built your driver using a version of the KMDF library that is more recent than the version of the framework that is on the system, then the latter must be updated. For information about updating the framework library, see [Redistributable Framework Components](installation-components-for-kmdf-drivers.md).

(Note that the framework co-installer's file name includes both the major and minor version numbers. For more information about co-installer file names, see [Using the KMDF Co-installer](installing-the-framework-s-co-installer.md).)

When you build your driver, the MSBuild utility links the driver with a stub file that contains the version number of the library that the MSBuild utility used. When the operating system loads your driver, the framework's loader checks the version information in your driver's stub to determine if the driver will run with the version of the framework library that is on the system.

To determine the version of the library that your driver is running with, the driver can call [**WdfDriverIsVersionAvailable**](https://msdn.microsoft.com/library/windows/hardware/ff547190) or [**WdfDriverRetrieveVersionString**](https://msdn.microsoft.com/library/windows/hardware/ff547211).

For information about the release history of the KMDF library, see [KMDF Version History](kmdf-version-history.md).

## UMDF


As with KMDF, the major version number of the UMDF library uses two characters. However, the major version number only appears in the UMDF library file name starting with UMDF version 2.0.

For UMDF version 2.0, the file name of the UMDF library is *Wudfx02000.dll*.

For UMDF version 1.*x*, the file name of the UMDF library is *Wudfx.dll*.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Framework%20Library%20Versioning%20%20RELEASE:%20%284/5/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




