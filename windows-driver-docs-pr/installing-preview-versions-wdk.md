---
title: Installing preview versions of the Windows Driver Kit (WDK)
description: Istallation instructions for the latest pre-release version of the Windows Driver Kit (WDK)
keywords:
- Windows Driver Kit
- WDK
- Insider Preview
- Download
- drivers
ms.author: eliotgra
ms.date: 07/11/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Installing preview versions of the Windows Driver Kit (WDK)

This page contains installation instructions for Insider Preview (pre-release) versions of the Windows Driver Kit (WDK). You can find the actual downloads for the latest pre-release version of the WDK and the EWDK at [https://www.microsoft.com/en-us/software-download/windowsinsiderpreviewWDK](https://www.microsoft.com/en-us/software-download/windowsinsiderpreviewWDK).  For info about the latest **released** versions of the WDK, see [Download the Windows Driver Kit (WDK)](download-the-wdk.md). For downloads of earlier versions of the WDK, see [Other WDK downloads](other-wdk-downloads.md).  

## Install Windows Driver Kit (WDK) Insider Preview

### 1. Install Visual Studio

- The WDK now supports Visual Studio 2017.  All editions are supported.  The WDK no longer supports Visual Studio 2015. 
- Download from [https://www.visualstudio.com/downloads/](https://www.visualstudio.com/downloads/). 
- Select workload: Development with C++. 
- ARM: To build ARM drivers you must additionally install the component: Individual components -> Compilers, build tools, and runtimes -> Visual C++ compilers and libraries for ARM. 
- ARM64: Currently not supported. 

### 2. Disable strong name validation

The WDK Visual Studio Extensions are currently not strong name signed. Run the following commands from an elevated command prompt to disable strong name validation: 

```
reg add HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\StrongName\Verification\*,31bf3856ad364e35 /v TestPublicKey /t REG_SZ /d 00240000048000009400000006020000002400005253413100040000010001003f8c902c8fe7ac83af7401b14c1bd103973b26dfafb2b77eda478a2539b979b56ce47f36336741b4ec52bbc51fecd51ba23810cec47070f3e29a2261a2d1d08e4b2b4b457beaa91460055f78cc89f21cd028377af0cc5e6c04699b6856a1e49d5fad3ef16d3c3d6010f40df0a7d6cc2ee11744b5cfb42e0f19a52b8a29dc31b0 /f

reg add HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\StrongName\Verification\*,31bf3856ad364e35 /v TestPublicKey /t REG_SZ /d 00240000048000009400000006020000002400005253413100040000010001003f8c902c8fe7ac83af7401b14c1bd103973b26dfafb2b77eda478a2539b979b56ce47f36336741b4ec52bbc51fecd51ba23810cec47070f3e29a2261a2d1d08e4b2b4b457beaa91460055f78cc89f21cd028377af0cc5e6c04699b6856a1e49d5fad3ef16d3c3d6010f40df0a7d6cc2ee11744b5cfb42e0f19a52b8a29dc31b0 /f 
```

### 3. Install SDK Insider Preview 

[Get SDK Insider Preview](https://www.microsoft.com/en-us/software-download/windowsinsiderpreviewWDK)

### 4. Install WDK Insider Preview

[Get WDK Insider Preview](https://www.microsoft.com/en-us/software-download/windowsinsiderpreviewWDK)

> [!Note]   
> During installation you will see the Visual Studio installer install the WDK Visual Studio Extensions. 

