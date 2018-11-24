---
title: How to Use Decorations in INF Files for Printer Drivers
description: How to Use Decorations in INF Files for Printer Drivers
ms.assetid: 772e2797-8019-4715-870c-b7cd2b8e65f2
keywords:
- multiple processor architectures WDK printer
- x86-based driver sample WDK printer
- Itanium-based driver sample WDK printer
- undecorated INF WDK printer
- INF files WDK print , decorations
- decorated INF WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# How to Use Decorations in INF Files for Printer Drivers


Printer drivers that run on Windows Server 2003 with SP1 and later, or on the 64-bit version of Windows XP and later, and that target x64 architectures must include a decorated [**INF Models section**](https://msdn.microsoft.com/library/windows/hardware/ff547456) as shown in the following example. However, because the driver might be installed as an additional driver on a version of Windows before Windows Server 2003 with SP1, the INF file must also provide an undecorated INF Models section. It is also recommended that decorations be used to install Itanium-based drivers.

The following examples show how to write an INF file that can be used to install a driver for a single processor architecture.

### x64 Driver Sample

The first example shows how to use an undecorated INF Models section to install an x64 driver on versions of Windows before Windows XP, or on an x86 or Itanium-based machine running Windows XP or Windows Server 2003. The NTamd64 decoration in the second INF Models section causes an x64 driver to be installed on a machine of any processor architecture that is running Windows Server 2003 with SP1 or later.

```cpp
[MANUFACTURER]
%Acme Corp.% = Acme, NTamd64
...

[Acme]
"Acme LaserWhiz 100 PS" = Acme100_x64.PPD, <hardware IDs and compatible IDs for this printer>

[Acme.NTamd64]
"Acme LaserWhiz 100 PS" = Acme100_x64.PPD, <hardware IDs and compatible IDs for this printer>
```

### Itanium-based Driver Sample

The next example shows how to use an undecorated INF Models section to install an Itanium-based driver on versions of Windows before Windows XP, or on an x86 machine running Windows XP or Windows Server 2003 before SP1. The NTia64 decoration in the second INF Models section causes an Itanium-based driver to be installed on a machine of any processor architecture that is running Windows Server 2003 with SP1 or later.

```cpp
[MANUFACTURER]
%Acme Corp.% = Acme, NTia64
...

[Acme]
"Acme LaserWhiz 100 PS" = Acme100_ia64.PPD, <hardware IDs and compatible IDs for this printer>

[Acme.NTia64]
"Acme LaserWhiz 100 PS" = Acme100_ia64.PPD, <hardware IDs and compatible IDs for this printer>
```

### x86 Driver Sample

In the next example, the INF Models section does not require a decoration. It is unnecessary to specify the processor architecture because an undecorated section is assumed to refer to an x86 driver. It is permissible to add an INF Models section with an NTx86 decoration, but keep in mind that you should also include an undecorated INF Models section for versions of Windows before Windows Server 2003 with SP1.

```cpp
[MANUFACTURER]
%Acme Corp.% = Acme
...

[Acme]
"Acme LaserWhiz 100 PS" = Acme100_x86.PPD, <hardware IDs and compatible IDs for this printer>
```

### Supporting Multiple Architectures in a Single INF File

This section shows how to write an INF file that can be used to install printer drivers for multiple processor architectures.

To create an INF file that can be used to install drivers for multiple architectures, write an INF Models section, and then make as many copies of it as necessary so that each architecture that is supported has its own INF Models section. Add the appropriate decoration for each processor architecture to each of the resulting INF Models sections, as shown in the following example.

```cpp
[MANUFACTURER]
%Acme Corp% = Acme, NTamd64, NTia64
...

;; Used to install
;;    - a driver of any architecture type, on a machine running Windows 2000
;;    - a driver of any architecture type, on an x86 machine running Windows XP or Windows Server 2003
;;    - an x86 driver on a machine of any architecture type, running Windows Server 2003 with SP1
[Acme]
%Acme Model 1% = Acme100PS, <hardware IDs and compatible IDs for this printer>

;; Used to install
;;    - an x64 driver on a machine of any architecture type, running Windows Server 2003 with SP1
[Acme.NTamd64]
%Acme Model 1% = Acme100PS, <hardware IDs and compatible IDs for this printer>

;; Used to install
;;    - a driver of any architecture type, on an Itanium-based machine running Windows XP or Windows Server 2003
;;    - an Itanium-based driver on a machine of any architecture type, running Windows Server 2003 with SP1
[Acme.NTia64]
%Acme Model 1% = Acme100PS, <hardware IDs and compatible IDs for this printer>

;; DDInstall Section. 
;; This sample assumes that all three versions of the driver 
;; use the same DDInstall section.
[Acme100PS]
CopyFiles = MyDriverFile.dll, ...

[DestinationDirs]
DefaultDestDir=66000

[SourceDisksNames.x86]
1= %Location%,,,

[SourceDisksFiles.x86]
MyDriverFile.dll = 1,\i386
...

[SourceDisksNames.amd64]
1= %Location%,,,

[SourceDisksFiles.amd64]
MyDriverFile.dll = 1,\amd64
...

[SourceDisksNames.ia64]
1= %Location%,,,

[SourceDisksFiles.ia64]
MyDriverFile.dll = 1,\ia64
...

[Strings]
Acme Corp = "Acme Corporation"
Acme Model 1 = "Acme LaserWhiz 100 PS"
Location = "Acme CD ROM"
```

 

 




