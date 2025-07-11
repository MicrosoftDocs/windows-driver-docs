---
title: Install Preview Versions Windows Driver Kit (WDK)
description: Get installation instructions for the latest prerelease version of the Windows Driver Kit (WDK) and Enterprise Windows Driver Kit (EWDK).
keywords:
- Windows Driver Kit
- WDK
- Insider Preview
- Download
- drivers
ms.date: 07/14/2025
ms.topic: concept-article
---

# Installing preview versions of the Windows Driver Kit (WDK)

This article provides installation instructions for Insider Preview (prerelease) versions of the Windows Driver Kit (WDK). 

You can follow procedures to [install the WDK Insider Preview](#install-the-wdk-insider-preview) or the [Enterprise WDK (EWDK)](#install-the-ewdk-insider-preview).

The download links for the latest prerelease version of the WDK and the EWDK are available at [Windows Insider Preview Downloads](https://www.microsoft.com/en-us/software-download/windowsinsiderpreviewWDK).

## Install the WDK Insider Preview

This procedure installs the WDK Insider Preview. You install Visual Studio with the C++ workload, disable strong-name validation, and install the preview versions of the SDK and WDK.

### Step 1. Install Visual Studio

To install Visual Studio and the necessary workload or component, follow these steps:

1. Download [Visual Studio 2022](/visualstudio/releases/2022).

   The WDK supports Visual Studio 2022, all editions. The WDK no longer supports Visual Studio 2019.

1. Select the **Development with C++** workload.

   For Arm64 and Arm64EC drivers, install an extra component: **Individual components > Compilers, build tools, and runtimes > Visual C++ compilers and libraries for Arm64/Arm64EC**. The WDK has Spectre mitigation enabled by default, but requires Spectre mitigated libraries installed with Visual Studio for each development architecture.

### Step 2. Disable strong name validation

The WDK Visual Studio Extensions are currently not strong-name signed. To disable strong name validation, run the following commands from an elevated command prompt:

```cpp
reg add HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\StrongName\Verification\*,31bf3856ad364e35 /v TestPublicKey /t REG_SZ /d 00240000048000009400000006020000002400005253413100040000010001003f8c902c8fe7ac83af7401b14c1bd103973b26dfafb2b77eda478a2539b979b56ce47f36336741b4ec52bbc51fecd51ba23810cec47070f3e29a2261a2d1d08e4b2b4b457beaa91460055f78cc89f21cd028377af0cc5e6c04699b6856a1e49d5fad3ef16d3c3d6010f40df0a7d6cc2ee11744b5cfb42e0f19a52b8a29dc31b0 /f

reg add HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\StrongName\Verification\*,31bf3856ad364e35 /v TestPublicKey /t REG_SZ /d 00240000048000009400000006020000002400005253413100040000010001003f8c902c8fe7ac83af7401b14c1bd103973b26dfafb2b77eda478a2539b979b56ce47f36336741b4ec52bbc51fecd51ba23810cec47070f3e29a2261a2d1d08e4b2b4b457beaa91460055f78cc89f21cd028377af0cc5e6c04699b6856a1e49d5fad3ef16d3c3d6010f40df0a7d6cc2ee11744b5cfb42e0f19a52b8a29dc31b0 /f
```

### Step 3. Install SDK Insider Preview 

Install the SDK Insider Preview by following the instructions at [Get the SDK Insider Preview](https://www.microsoft.com/software-download/windowsinsiderpreviewSDK).

### Step 4. Complete the WDK install

Complete the installation of the WDK Insider Preview by following the instructions at [Get the WDK Insider Preview](https://www.microsoft.com/software-download/windowsinsiderpreviewWDK)

> [!Note]
> During the installation, Visual Studio installs the WDK Visual Studio Extensions. For more information, see [Download the Windows Driver Kit](download-the-wdk.md#download-icon-for-wdk-step-3-install-wdk).

## Install the EWDK Insider Preview

An alternate approach is to install the EWDK Insider Preview. The EWDK is a standalone self-contained command-line environment for building drivers that includes Build Tools for Visual Studio 2022. For more information, see [Using the Enterprise WDK](develop/using-the-enterprise-wdk.md).

To install the EWDK Insider Preview, follow these steps:

### Step 1. Get the EWDK Insider Preview

Start by following the instructions in [Get the EWDK Insider Preview](https://www.microsoft.com/software-download/windowsinsiderpreviewWDK).

### Step 2. Turn off strong name validation

To disable strong name validation for the WDK Extensions, run the following commands from an elevated command prompt:

```cpp
reg add HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\StrongName\Verification\*,31bf3856ad364e35 /v TestPublicKey /t REG_SZ /d 00240000048000009400000006020000002400005253413100040000010001003f8c902c8fe7ac83af7401b14c1bd103973b26dfafb2b77eda478a2539b979b56ce47f36336741b4ec52bbc51fecd51ba23810cec47070f3e29a2261a2d1d08e4b2b4b457beaa91460055f78cc89f21cd028377af0cc5e6c04699b6856a1e49d5fad3ef16d3c3d6010f40df0a7d6cc2ee11744b5cfb42e0f19a52b8a29dc31b0 /f

reg add HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\StrongName\Verification\*,31bf3856ad364e35 /v TestPublicKey /t REG_SZ /d 00240000048000009400000006020000002400005253413100040000010001003f8c902c8fe7ac83af7401b14c1bd103973b26dfafb2b77eda478a2539b979b56ce47f36336741b4ec52bbc51fecd51ba23810cec47070f3e29a2261a2d1d08e4b2b4b457beaa91460055f78cc89f21cd028377af0cc5e6c04699b6856a1e49d5fad3ef16d3c3d6010f40df0a7d6cc2ee11744b5cfb42e0f19a52b8a29dc31b0 /f
```

### Step 3. Mount the ISO and start the EWDK

Mount the ISO that you downloaded from the Insider Preview page, and select **LaunchBuildEnv** to use the EWDK.

### Step 4. Complete the EWDK install

Complete the installation of the EWDK Insider Preview by following the instructions at [Get the EWDK Insider Preview](https://www.microsoft.com/software-download/windowsinsiderpreviewWDK).
