---
title: Windows 11, version 22H2 Support Matrix
description: Page articulates the support matrix for the new Windows Driver Kit (WDK)
keywords:
- Windows Driver Kit
- WDK
- drivers
- Support Matrix
ms.date: 05/23/2022
---

# Windows 11, Version 22H2 Support Matrix

The WDK/EWDK for Windows 11, version 22H2 will align its support matrix to match [Windows 11 new hardware requirements.](https://docs.microsoft.com/en-us/windows/whats-new/windows-11-requirements) 

Windows 11, version 22H2 WDK/EWDK <b>will</b> support: 

* Building and testing Kernel Mode drivers for X64 and ARM64 </br>
* Building and testing drivers for Windows 11 and Windows 10 (x64/arm64 only) </br>
* Side by side (SxS) support with previous WDK/EWDK </br>
 
In addition to the change in OS support, Windows 11, version 22H2 WDK/EWDK will only support running on Visual Studio 2022 release. 

 
Windows 11, version 22H2 WDK/EWDK <b>will not</b> support: 

* Building Kernel Mode drivers for X86 and ARM32 </br>
* Building and testing drivers for Windows 7, Windows 8.0, Windows 8.1, and Windows 10 (x86/arm32) </br>
* Building WDF driver that requires WDF redistributable Co-installers   </br>
* Visual Studio 2019</br>

Notes:

* <b>Features:</b> WDK for Windows 11, version 22H2 is required to take advantage of new features in Windows 11, version 22H2 host OS.  
* <b>Device specific User Mode drivers:</b> Certain device specific stacks (for example graphics) will continue to have x86/arm32 UM components to support x86/arm32 apps.  </br>
* <b>Testing drivers:</b> WDK supports running tests directly in [Visual Studio](https://docs.microsoft.com/en-us/windows-hardware/drivers/develop/testing-a-driver).  The WDK major version must match the target OS major version, this is the same behavior as previously released WDK’s. Meaning Windows 11, version 22H2 WDK will support testing on Windows 11, version 22H2, however Windows 11, version 22H2 WDK will not support testing on Windows 11, version 21H1. </br>
* <b>WDK Side by side support:</b>  Multiple WDKs can be installed SxS and multiple EWDKs can run concurrently on same PC and even be part of same build system. </br>



## SxS Limitations
In a SxS installation of Windows 11, version 22H2 WDK and an older version, if you want to use the older version WDK to build WDF 1.11 driver (most likely because you need to target pre-Win10 OS) msbuild will report failure that it cannot find WDF coinstaller. To work around this limitation, before installing Windows 11, version 22H2 WDK, please backup the folder "\program files (x86)\windows kit\10\redist\wdf" and restore it afterwards. Alternatively, if you have already installed the Windows 11, version 22H2 WDK, please install the MSI file at [WDK 8 redistributable components](https://go.microsoft.com/fwlink/p/?LinkID=253170) on a spare machine, and then copy redist folder to the above folder. Ref: <https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/installation-components-for-kmdf-drivers> 



## FAQ

### Can drivers targeting pre-Win10 OS be built? 

No – you’ll need to install older WDK either on the same machine or on a seated machine. 
  
### Why can’t the WDK continue supporting 32bit/ARM KM drivers?? 
The WDK comes from the same code base as Windows 11. Now that codebase only supports x64 and ARM64, the x86 and ARM kernel mode libraries are no longer produced. As a consequence there is not a natural way to provide a WDK that could build an x86/ARM driver. 
