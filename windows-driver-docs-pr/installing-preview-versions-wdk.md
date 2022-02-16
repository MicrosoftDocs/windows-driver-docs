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


## Supported Configurations

Starting with the February 2022 Windows Insider Preview (WIP) release of the WDK and EWDK, the kits support:

* Visual Studio 2022 exclusively
* Building and testing kernel-mode drivers for x64 and ARM64
* Building and testing drivers for Windows 11 and Windows 10
* Side by side (SxS) support with previous WDK/EWDK

> [!NOTE]
> The following are not supported:
> * Visual Studio 2019
> * Building kernel-mode drivers for x86 and ARM32
> * Building and testing drivers for Windows 7, Windows 8, Windows 8.1
> * Building WDF drivers that require WDF redistributable co-installers

**Notes**

* Device-specific user-mode drivers: Certain device-specific stacks (for example graphics) will continue to have x86/ARM32 user-mode components to support x86/ARM32 apps.
* Testing drivers: As with previous driver kits, WDK continues to support running tests directly in Visual Studio. The WDK major version must match the target OS major version. For details, see [Testing a Driver](/windows-hardware/drivers/develop/testing-a-driver).


**FAQ**

Q. Can drivers targeting  Windows 8.1, Windows 8, and Windows 7 be built?

A. No – you will need to install an older WDK and an older version of Visual Studio either on the same machine or on a separate machine.

Q. Why can't the WDK continue supporting 32 bit/ARM kernel-mode drivers?

A. The WDK comes from the same code base as Windows 11. Now that the codebase only supports x64 and ARM64, the x86 and ARM kernel mode libraries are no longer produced.

For info about the latest **released** versions of the WDK, see [Download the Windows Driver Kit (WDK)](download-the-wdk.md). For downloads of earlier versions of the WDK, see [Other WDK downloads](other-wdk-downloads.md).  

## Install Windows Driver Kit (WDK) Insider Preview

### 1. Install Visual Studio

* The WDK now supports Visual Studio 2022.  All editions are supported.  The WDK no longer supports Visual Studio 2019.
* Download from [Visual Studio 2022](/visualstudio/releases/2022).
* Select workload: **Development with C++**.
* For ARM64 and ARM64EC drivers, you must additionally install the component: **Individual components -> Compilers, build tools, and runtimes -> Visual C++ compilers and libraries for ARM64/ARM64EC**. Note that the WDK has Spectre mitigation enabled by default but requires Spectre mitigated libraries to be installed with Visual Studio for each architecture you are developing for.

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
