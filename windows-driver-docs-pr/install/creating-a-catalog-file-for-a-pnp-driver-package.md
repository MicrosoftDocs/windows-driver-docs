---
title: Creating a Catalog File for a PnP Driver Package
description: Creating a Catalog File for a PnP Driver Package
ms.assetid: 2af431f1-a35d-4312-86f6-a928ef4148df
---

# Creating a Catalog File for a PnP Driver Package


To create an unsigned catalog file for a driver package, follow these steps:

1.  Add the required INF **CatalogFile**=*FileName***.Cat** entry or INF **CatalogFile.***PlatformExtension*=*unique-filename***.Cat** entries to the [**INF Version section**](inf-version-section.md) of a [driver package's](driver-packages.md) INF file. For information about how to use platform extensions, see [Cross-Platform INF Files](cross-platform-inf-files.md).

2.  Use the [**Inf2Cat**](https://msdn.microsoft.com/library/windows/hardware/ff547089) tool to verify that the driver package can be signed for the target platforms and to generate the unsigned [catalog files](catalog-files.md) (*.cat* files) that apply to the target platforms.

Use the following Inf2Cat command to create unsigned catalog files:

```
Inf2Cat /driver:DriverPath /os:WindowsVersionList
```

Where:

-   The **/driver:***DriverPath* parameter supplies the name of the directory where the [driver package](driver-packages.md) is located.

-   The **/os:***WindowsVersionList* parameter configures Inf2Cat to verify that the driver package complies with the signing requirements for the Windows versions that are specified by the list of Windows version identifiers.

### Examples

The following examples apply to the toaster [driver package](driver-packages.md) that is located in *c:\\WindDDK\\5739\\src\\general\\toaster\\toastpkg\\toastcd*. The INF file for the toaster package is *Toastpkg.inf* and this INF file contains the following **CatalogFile** directives with platform extensions:

```
[Version]
. . .
CatalogFile.NTx86  = tostx86.cat
CatalogFile.NTIA64 = tostia64.cat
CatalogFile.NTAMD64 = tstamd64.cat
. . .
```

To generate *Tostx86.cat* for specific x86 versions of Windows, specify the Windows versions in *WindowsVersionList*. For example, the following Inf2Cat command verifies that the [driver package](driver-packages.md) can be signed for Windows 2000 and the x86 versions of Windows Vista, Windows Server 2003, and Windows XP.

```
Inf2Cat /driver:c:\WindDDK\5739\src\general\toaster\toastpkg\toastcd /os:2000,XP_X86,Server2003_X86,Vista_X86
```

To generate *Tostamd64.cat* for x64 versions of Windows, specify the Windows versions in *WindowsVersionList*. For example, the following Inf2Cat command verifies that the driver package can be signed for the x64 versions of Windows Vista, Windows Server 2003, and Windows XP.

```
Inf2Cat /driver:c:\WindDDK\5739\src\general\toaster\toastpkg\toastcd /os:XP_X64,Server2003_X64,Vista_X64
```

To generate *Tostamd64.cat* only for Windows Vista x64 Edition, specify only "Vista\_X64" in *WindowsVersionList.* For example, the following Inf2Cat command only verifies that the [driver package](driver-packages.md) can be signed for Windows Vista x64 Edition.

```
Inf2Cat /driver:c:\WindDDK\5739\src\general\toaster\toastpkg\toastcd /os:Vista_X64
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Creating%20a%20Catalog%20File%20for%20a%20PnP%20Driver%20Package%20%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




