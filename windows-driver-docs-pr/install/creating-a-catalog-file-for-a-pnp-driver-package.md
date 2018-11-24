---
title: Creating a Catalog File for a PnP Driver Package
description: Creating a Catalog File for a PnP Driver Package
ms.assetid: 2af431f1-a35d-4312-86f6-a928ef4148df
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Creating a Catalog File for a PnP Driver Package


To create an unsigned catalog file for a driver package, follow these steps:

1. Add the required INF **CatalogFile**=<em>FileName</em>**.Cat** entry or INF **CatalogFile.**<em>PlatformExtension</em>=<em>unique-filename</em>**.Cat** entries to the [**INF Version section**](inf-version-section.md) of a [driver package's](driver-packages.md) INF file. For information about how to use platform extensions, see [Cross-Platform INF Files](cross-platform-inf-files.md).

2. Use the [**Inf2Cat**](https://msdn.microsoft.com/library/windows/hardware/ff547089) tool to verify that the driver package can be signed for the target platforms and to generate the unsigned [catalog files](catalog-files.md) (*.cat* files) that apply to the target platforms.

Use the following Inf2Cat command to create unsigned catalog files:

```cpp
Inf2Cat /driver:DriverPath /os:WindowsVersionList
```

Where:

- The **/driver:**<em>DriverPath</em> parameter supplies the name of the directory where the [driver package](driver-packages.md) is located.

- The **/os:**<em>WindowsVersionList</em> parameter configures Inf2Cat to verify that the driver package complies with the signing requirements for the Windows versions that are specified by the list of Windows version identifiers.

### Examples

The following examples apply to the toaster [driver package](driver-packages.md) that is located in *c:\\WindDDK\\5739\\src\\general\\toaster\\toastpkg\\toastcd*. The INF file for the toaster package is *Toastpkg.inf* and this INF file contains the following **CatalogFile** directives with platform extensions:

```cpp
[Version]
. . .
CatalogFile.NTx86  = tostx86.cat
CatalogFile.NTIA64 = tostia64.cat
CatalogFile.NTAMD64 = tstamd64.cat
. . .
```

To generate *Tostx86.cat* for specific x86 versions of Windows, specify the Windows versions in *WindowsVersionList*. For example, the following Inf2Cat command verifies that the [driver package](driver-packages.md) can be signed for Windows 2000 and the x86 versions of Windows Vista, Windows Server 2003, and Windows XP.

```cpp
Inf2Cat /driver:c:\WindDDK\5739\src\general\toaster\toastpkg\toastcd /os:2000,XP_X86,Server2003_X86,Vista_X86
```

To generate *Tostamd64.cat* for x64 versions of Windows, specify the Windows versions in *WindowsVersionList*. For example, the following Inf2Cat command verifies that the driver package can be signed for the x64 versions of Windows Vista, Windows Server 2003, and Windows XP.

```cpp
Inf2Cat /driver:c:\WindDDK\5739\src\general\toaster\toastpkg\toastcd /os:XP_X64,Server2003_X64,Vista_X64
```

To generate *Tostamd64.cat* only for Windows Vista x64 Edition, specify only "Vista_X64" in *WindowsVersionList.* For example, the following Inf2Cat command only verifies that the [driver package](driver-packages.md) can be signed for Windows Vista x64 Edition.

```cpp
Inf2Cat /driver:c:\WindDDK\5739\src\general\toaster\toastpkg\toastcd /os:Vista_X64
```

 

 





