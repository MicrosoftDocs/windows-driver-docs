---
title: Installing preview versions of the Windows Driver Kit (WDK)
description: Istallation instructions for the latest pre-release version of the Windows Driver Kit (WDK)
keywords:
- Windows Driver Kit
- WDK
- Insider Preview
- Download
- drivers
ms.date: 08/05/2021
---

# Installing preview versions of the Windows Driver Kit (WDK)

This page contains installation instructions for Insider Preview (pre-release) versions of the Windows Driver Kit (WDK). The  download links for the latest pre-release version of the WDK and the EWDK are on  [https://www.microsoft.com/software-download/windowsinsiderpreviewWDK](https://www.microsoft.com/en-us/software-download/windowsinsiderpreviewWDK).  

For info about the latest **released** versions of the WDK, see [Download the Windows Driver Kit (WDK)](download-the-wdk.md). For downloads of earlier versions of the WDK, see [Other WDK downloads](other-wdk-downloads.md).  

## Install Windows Driver Kit (WDK) Insider Preview

### 1. Install Visual Studio

- The WDK now supports Visual Studio 2019.  All editions are supported.  The WDK no longer supports Visual Studio 2017. 
- Download from [https://visualstudio.microsoft.com/vs/preview/](https://visualstudio.microsoft.com/vs/preview/). 
- Select workload: Development with C++. 
- ARM: To build ARM drivers you must additionally install the component: Individual components -> Compilers, build tools, and runtimes -> Visual C++ compilers and libraries for ARM. 
- ARM64: Currently not supported. 

### 2. Disable strong name validation

The WDK Visual Studio Extensions are currently not strong name signed. Run the following commands from an elevated command prompt to disable strong name validation: 

```cpp
reg add HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\StrongName\Verification\*,31bf3856ad364e35 /v TestPublicKey /t REG_SZ /d 00240000048000009400000006020000002400005253413100040000010001003f8c902c8fe7ac83af7401b14c1bd103973b26dfafb2b77eda478a2539b979b56ce47f36336741b4ec52bbc51fecd51ba23810cec47070f3e29a2261a2d1d08e4b2b4b457beaa91460055f78cc89f21cd028377af0cc5e6c04699b6856a1e49d5fad3ef16d3c3d6010f40df0a7d6cc2ee11744b5cfb42e0f19a52b8a29dc31b0 /f

reg add HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\StrongName\Verification\*,31bf3856ad364e35 /v TestPublicKey /t REG_SZ /d 00240000048000009400000006020000002400005253413100040000010001003f8c902c8fe7ac83af7401b14c1bd103973b26dfafb2b77eda478a2539b979b56ce47f36336741b4ec52bbc51fecd51ba23810cec47070f3e29a2261a2d1d08e4b2b4b457beaa91460055f78cc89f21cd028377af0cc5e6c04699b6856a1e49d5fad3ef16d3c3d6010f40df0a7d6cc2ee11744b5cfb42e0f19a52b8a29dc31b0 /f 
```

### 3. Install SDK Insider Preview 

[Get SDK Insider Preview](https://www.microsoft.com/en-us/software-download/windowsinsiderpreviewSDK)

### 4. Install WDK Insider Preview

[Get WDK Insider Preview](https://www.microsoft.com/en-us/software-download/windowsinsiderpreviewWDK)

> [!Note]   
> During installation you will see the Visual Studio installer install the WDK Visual Studio Extensions. 

## Install Enterprise WDK (EWDK) Insider Preview

The EWDK is a standalone self-contained command-line environment for building drivers.  It includes Build Tools for Visual Studio 2019, the SDK, the WDK and support for ARM64 driver development. See more at [Installing the Enterprise WDK](./develop/using-the-enterprise-wdk.md). 

[Get the Enterprise Windows Driver Kit (EWDK) Insider Preview](https://www.microsoft.com/en-us/software-download/windowsinsiderpreviewWDK)

To get started, disable strong name validation by running the following commands from an elevated command prompt:

```console
reg add HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\StrongName\Verification\*,31bf3856ad364e35 /v TestPublicKey /t REG_SZ /d 00240000048000009400000006020000002400005253413100040000010001003f8c902c8fe7ac83af7401b14c1bd103973b26dfafb2b77eda478a2539b979b56ce47f36336741b4ec52bbc51fecd51ba23810cec47070f3e29a2261a2d1d08e4b2b4b457beaa91460055f78cc89f21cd028377af0cc5e6c04699b6856a1e49d5fad3ef16d3c3d6010f40df0a7d6cc2ee11744b5cfb42e0f19a52b8a29dc31b0 /f

reg add HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\StrongName\Verification\*,31bf3856ad364e35 /v TestPublicKey /t REG_SZ /d 00240000048000009400000006020000002400005253413100040000010001003f8c902c8fe7ac83af7401b14c1bd103973b26dfafb2b77eda478a2539b979b56ce47f36336741b4ec52bbc51fecd51ba23810cec47070f3e29a2261a2d1d08e4b2b4b457beaa91460055f78cc89f21cd028377af0cc5e6c04699b6856a1e49d5fad3ef16d3c3d6010f40df0a7d6cc2ee11744b5cfb42e0f19a52b8a29dc31b0 /f
```

Then mount the ISO that you downloaded from the Insider Preview page and select **LaunchBuildEnv** to use the EWDK.  

## Run-time requirements for the WDK and the EWDK

The WDK requires Visual Studio. For more info about system requirements for Visual Studio, see [Visual Studio 2019 System Requirements](/visualstudio/releases/2019/system-requirements).

In addition, the EWDK requires .NET 4.7.2. For more info about what .NET runs on, see [.NET Framework system requirements](/dotnet/framework/get-started/system-requirements).

You can use the WDK Insider Preview and the EWDK Insider Preview to develop drivers for these operating systems: 

|Client OS|Server OS|
|---|---|
|Windows 10|Windows Server 2016|
|Windows 8.1|Windows Server 2012 R2|
|Windows 8|Windows Server 2012|
|Windows 7|Windows Server 2008 R2 SP1|
