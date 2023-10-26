---
title: Download the Windows Driver Kit (WDK)
description: Download instructions for the latest released version of the Windows Driver Kit (WDK)
keywords:
- Windows Driver Kit
- WDK
- Download
- drivers
ms.date: 10/24/2023
---

# Download the Windows Driver Kit (WDK)

> [!NOTE]
> Make sure to use Visual Studio 17.4.1 or newer.  Specifically, driver debugging within Visual Studio does not work from Visual Studio 17.2.0 up until 17.4.1. For more info, see [WDK Known Issues](./wdk-known-issues.md).

The WDK is used to develop, test, and deploy drivers for Windows.

* [Learn what's new in driver development](./what-s-new-in-driver-development.md)
* [Review known issues](./wdk-known-issues.md)

[Join the Windows Insider Program](https://insider.windows.com/) to get [WDK Insider Preview builds](https://aka.ms/wipwdk). For installation instructions for the Windows Insider Preview builds, see [Installing preview versions of the Windows Driver Kit (WDK)](./installing-preview-versions-wdk.md).

Multiple WDKs and EWDKs can be installed concurrently on the same computer and even be part of the same build system. You can run the WDK for Windows 11, version 22H2 (updated Oct 2023) on Windows 7 and later.

To target Windows 8.1, Windows 8, and Windows 7, install an older WDK and an older version of Visual Studio either on the same machine or on a separate machine. For links to older kits, see [Other WDK downloads](./other-wdk-downloads.md).

Certain device-specific stacks (for example graphics) continue to have x86/ARM32 user-mode components to support x86/ARM32 apps.

## ![download icon.](images/download-install.png) Step 1: Install Visual Studio 2022

The WDK requires Visual Studio. For more information about system requirements for Visual Studio, see [Visual Studio 2022 System Requirements](/visualstudio/releases/2022/system-requirements).

The following editions of Visual Studio 2022 support driver development for this release:

* [Download Visual Studio Community 2022](https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=Community&rel=17)
* [Download Visual Studio Professional 2022](https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=Professional&rel=17)
* [Download Visual Studio Enterprise 2022](https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=Enterprise&rel=17)

When you install Visual Studio 2022, select the **Desktop development with C++** workload. Don't worry about the SDK at this point; you install this in step 2 below.

WDK has Spectre mitigation enabled by default but requires Spectre mitigated libraries to be installed with Visual Studio for each architecture you're developing for. Additionally, developing drivers for Arm/Arm64/Arm64EC require the build tools for these architectures to also be installed with Visual Studio. To locate these items, you need to know the latest version of MSVC installed on your system.

To find the latest version of MSVC installed on your system, in **Visual Studio Installer** go to **workload page**, on the right pane under **installation details**, expand **Desktop development with C++** and locate the **MSVC v143 - VS 2022 C++ x64/x86 build tools (Latest)**.

With this information (Latest), go to **Individual components** and search for **Latest**. This returns the tool sets for all architectures, including Spectre mitigated libs. Select the driver architecture you're developing for. 

For example, searching for Latest returns the following:

```console
MSVC v143 - VS 2022 C++ Arm build tools (Latest)
MSVC v143 - VS 2022 C++ Arm Spectre-mitigated libs (Latest)
MSVC v143 - VS 2022 C++ Arm64 build tools (Latest)
MSVC v143 - VS 2022 C++ Arm64 Spectre-mitigated libs (Latest)
MSVC v143 - VS 2022 C++ Arm64EC build tools (Latest - experimental)
MSVC v143 - VS 2022 C++ Arm64EC Spectre-mitigated libs (Latest - experimental)
MSVC v143 - VS 2022 C++ x64/x86 build tools (Latest)
MSVC v143 - VS 2022 C++ x64/x86 Spectre-mitigated libs (Latest)
```

## ![download icon.](images/download-install.png) Step 2: Install SDK

After you've successfully installed Visual Studio, your next step is to download the Windows Software Development Kit (SDK).

* [Download the SDK for Windows 11, version 22H2 (updated Oct 2023)](https://developer.microsoft.com/en-us/windows/downloads/windows-sdk/)

The provided links for the SDK and the WDK have matching build numbers, which is always required for the kits to work together. If you decide to install your own SDK/WDK pair, perhaps for a different Windows version, ensure that the build numbers match.

## ![download icon.](images/download-install.png) Step 3: Install WDK

* [Download WDK for Windows 11, version 22H2 (updated Oct 2023)](https://go.microsoft.com/fwlink/?linkid=2249371)

The WDK Visual Studio extension is included in the default WDK installation.

> [!TIP]
> If you can't find driver project templates in Visual Studio, the WDK Visual Studio extension didn't install properly. To resolve this, run the WDK.vsix file from this location: C:\Program Files (x86)\Windows Kits\10\Vsix\VS2022\10.0.22621.2428\WDK.vsix.

## Enterprise WDK (EWDK)

As an alternative to downloading Visual Studio, the SDK, and the WDK, you can download the EWDK, which is a standalone, self-contained command-line environment for building drivers. It includes Visual Studio Build Tools, the SDK, and the WDK.

You can also use the Visual Studio interface with the build tools provided in the EWDK.

The latest public version of the EWDK contains Visual Studio 2022 Build Tools 17.1.5 and MSVC toolset v14.31.

The EWDK also requires the .NET Framework version 4.7.2. For more information about other requirements for the .NET Framework, see [.NET Framework system requirements](/dotnet/framework/get-started/system-requirements).

### ![download icon.](images/download-install.png) EWDK for Windows 11, version 22H2 (updated Oct 2023) with Visual Studio Build Tools

* [Download the EWDK for Windows 11, version 22H2 (updated Oct 2023)](/legal/windows/hardware/enterprise-wdk-license-2022)

Once you have downloaded the ISO, use these steps to set up your build environment:

1. Mount the EWDK ISO from a drive volume. Network share paths aren't currently supported.
2. Run `LaunchBuildEnv.cmd`.
3. In the environment created in step 2, type **SetupVSEnv**, and then press **Enter**.
4. Launch devenv.exe from the same environment, using the full file path. For example: `"C:\Program Files\Microsoft Visual Studio\2022\%Community|Professional|Enterprise%\Common7\IDE\devenv.exe"`
5. When you're done with the build environment, you may want to eject the ISO.

Note that the Visual Studio major version should match with the version in the EWDK. For example, Visual Studio 2022 works with the EWDK that contain VS17.X build tools. For a list of Visual Studio 2022 version numbers, see [Visual Studio 2022 Releases](/visualstudio/releases/2022/release-history).

## Driver samples for Windows

To download the driver samples, do one of the following:

* Go to the driver samples page on [GitHub](https://github.com/Microsoft/Windows-driver-samples), click **Clone or download**, and then click **Download ZIP**.
* Download the [GitHub Extension for Visual Studio](https://visualstudio.github.com/), and then connect to the GitHub repositories.
* Browse the driver samples on the [Microsoft Samples portal](/samples/browse/?products=windows-wdk).

## Related downloads

* [Download the WDK Insider Preview](https://www.microsoft.com/software-download/windowsinsiderpreviewWDK)
* [Download previous versions of the WDK](other-wdk-downloads.md)
* [Download the Windows Assessment and Deployment Kit (Windows ADK)](/windows-hardware/get-started/adk-install)
* [Download the Windows HLK](/windows-hardware/test/hlk/windows-hardware-lab-kit)
* [Download the Windows Debugging Tools (WinDbg)](./debugger/debugger-download-tools.md)
* [Download Windows Symbol Packages](./debugger/debugger-download-symbols.md)

## See also

* [Windows 11 hardware requirements](/windows/whats-new/windows-11-requirements)
* [Install the WDK using WinGet](./install-the-wdk-using-winget.md)
