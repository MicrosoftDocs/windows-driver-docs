---
title: Installing preview versions of the Windows Driver Kit (WDK)
description: Installation instructions for the latest pre-release version of the Windows Driver Kit (WDK)
keywords:
- Windows Driver Kit
- WDK
- Insider Preview
- Download
- drivers
ms.date: 02/16/2022
---

# Installing preview versions of the Windows Driver Kit (WDK)

This page contains installation instructions for Insider Preview (pre-release) versions of the Windows Driver Kit (WDK). The  download links for the latest pre-release version of the WDK and the EWDK are on  [https://www.microsoft.com/software-download/windowsinsiderpreviewWDK](https://www.microsoft.com/en-us/software-download/windowsinsiderpreviewWDK).  

## Install Windows Driver Kit (WDK) Insider Preview

### 1. Install Visual Studio

* The WDK now supports Visual Studio 2022.  All editions are supported.  The WDK no longer supports Visual Studio 2019.
* Download from [Visual Studio 2022](/visualstudio/releases/2022).
* Select workload: **Development with C++**.
* For Arm64 and Arm64EC drivers, you must additionally install the component: **Individual components -> Compilers, build tools, and runtimes -> Visual C++ compilers and libraries for Arm64/Arm64EC**. Note that the WDK has Spectre mitigation enabled by default but requires Spectre mitigated libraries to be installed with Visual Studio for each architecture you are developing for.

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

As an alternative to the above steps, the EWDK is a standalone self-contained command-line environment for building drivers that includes Build Tools for Visual Studio 2022. See more at [Installing the Enterprise WDK](./develop/using-the-enterprise-wdk.md).

[Get the Enterprise Windows Driver Kit (EWDK) Insider Preview](https://www.microsoft.com/en-us/software-download/windowsinsiderpreviewWDK)

To get started, disable strong name validation by running the following commands from an elevated command prompt:

```console
reg add HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\StrongName\Verification\*,31bf3856ad364e35 /v TestPublicKey /t REG_SZ /d 00240000048000009400000006020000002400005253413100040000010001003f8c902c8fe7ac83af7401b14c1bd103973b26dfafb2b77eda478a2539b979b56ce47f36336741b4ec52bbc51fecd51ba23810cec47070f3e29a2261a2d1d08e4b2b4b457beaa91460055f78cc89f21cd028377af0cc5e6c04699b6856a1e49d5fad3ef16d3c3d6010f40df0a7d6cc2ee11744b5cfb42e0f19a52b8a29dc31b0 /f

reg add HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\StrongName\Verification\*,31bf3856ad364e35 /v TestPublicKey /t REG_SZ /d 00240000048000009400000006020000002400005253413100040000010001003f8c902c8fe7ac83af7401b14c1bd103973b26dfafb2b77eda478a2539b979b56ce47f36336741b4ec52bbc51fecd51ba23810cec47070f3e29a2261a2d1d08e4b2b4b457beaa91460055f78cc89f21cd028377af0cc5e6c04699b6856a1e49d5fad3ef16d3c3d6010f40df0a7d6cc2ee11744b5cfb42e0f19a52b8a29dc31b0 /f
```

Then mount the ISO that you downloaded from the Insider Preview page and select **LaunchBuildEnv** to use the EWDK.