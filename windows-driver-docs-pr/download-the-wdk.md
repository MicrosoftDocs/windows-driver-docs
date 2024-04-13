---
title: Download the Windows Driver Kit (WDK)
description: Download instructions for the latest released version of the Windows Driver Kit (WDK)
keywords:
- Windows Driver Kit
- WDK
- Download
- drivers
ms.date: 03/06/2024
---

# Download the Windows Driver Kit (WDK)

The WDK is used to develop, test, and deploy drivers for Windows. The most recent public release is WDK 10.0.22621.

* You can install and run this WDK on Windows 7 and later.
* You can use this kit to build drivers for Windows 10, Windows Server 2016 and later client and server versions.

To target Windows 8.1, Windows 8, and Windows 7, install an older WDK and an older version of Visual Studio either on the same machine or on a separate machine. For links to older kits, see [Other WDK downloads](./other-wdk-downloads.md).

[Join the Windows Insider Program](https://insider.windows.com/) to get [WDK Insider Preview builds](https://aka.ms/wipwdk). For installation instructions for the Windows Insider Preview builds, see [Installing preview versions of the Windows Driver Kit (WDK)](./installing-preview-versions-wdk.md).

## ![download icon for Visual Studio](images/download-install.png) Step 1: Install Visual Studio 2022

The WDK requires Visual Studio. For more information about system requirements for Visual Studio, see [Visual Studio 2022 System Requirements](/visualstudio/releases/2022/system-requirements).

The following editions of Visual Studio 2022 support driver development for this release:

* [Download Visual Studio Community 2022](https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=Community&rel=17)
* [Download Visual Studio Professional 2022](https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=Professional&rel=17)
* [Download Visual Studio Enterprise 2022](https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=Enterprise&rel=17)

When you install Visual Studio 2022, select the **Desktop development with C++** workload, then under Individual Components add:

* MSVC v143 - VS 2022 C++ ARM64/ARM64EC Spectre-mitigated libs (Latest)</br>
* MSVC v143 - VS 2022 C++ x64/x86 Spectre-mitigated libs (Latest)</br>
* C++ ATL for latest v143 build tools with Spectre Mitigations (ARM64/ARM64EC)</br>
* C++ ATL for latest v143 build tools with Spectre Mitigations (x86 & x64)</br>
* C++ MFC for latest v143 build tools with Spectre Mitigations (ARM64/ARM64EC)</br>
* C++ MFC for latest v143 build tools with Spectre Mitigations (x86 & x64)</br>

Hint: Use the Search box to look for "64 latest spectre" (in English installations) or "64 latest" (in non-English installations) to quickly see these components.</br>

![Image showing the six components listed above with checkboxes set](images/installing-VS-components-64-latest-spectre.png)

Note: The **Desktop development with C++** workload selected above also installs the Windows SDK 10.0.22621.

## ![download icon for SDK](images/download-install.png) Step 2: Install SDK

Installing Visual Studio should automatically download the Windows SDK 10.0.22621. In the event that it does not, use the following link:

* [Download Windows SDK 10.0.22621](https://developer.microsoft.com/en-us/windows/downloads/windows-sdk/)

The provided links for the SDK and the WDK have matching build numbers, which is always required for the kits to work together. If you decide to install your own SDK/WDK pair, perhaps for a different Windows version, ensure that the build numbers match. For more details, see [Kit versioning](#kit-versioning).

## ![download icon for WDK](images/download-install.png) Step 3: Install WDK

* [Download WDK 10.0.22621](https://go.microsoft.com/fwlink/?linkid=2249371)

The WDK Visual Studio extension is included in the default WDK installation.

> [!TIP]
> If you can't find driver project templates in Visual Studio, the WDK Visual Studio extension didn't install properly. To resolve this, run the WDK.vsix file from this location: C:\Program Files (x86)\Windows Kits\10\Vsix\VS2022\10.0.22621.2428\WDK.vsix.

## ![download icon for EWDK](images/download-install.png) Enterprise WDK (EWDK)

As an alternative to downloading Visual Studio, the SDK, and the WDK, you can download the EWDK, which is a standalone, self-contained command-line environment for building drivers. It includes Visual Studio Build Tools, the SDK, and the WDK.

The latest public version of the EWDK contains Visual Studio 2022 Build Tools 17.1.5 and MSVC toolset v14.31.

The EWDK also requires the .NET Framework version 4.7.2. For more information about other requirements for the .NET Framework, see [.NET Framework system requirements](/dotnet/framework/get-started/system-requirements).

* [Download EWDK 10.0.22621 with Visual Studio Build Tools](/legal/windows/hardware/enterprise-wdk-license-2022)

Once you have downloaded the ISO, use these steps to set up your build environment:

1. Mount the EWDK ISO from a drive volume. Network share paths aren't currently supported.
2. Run `LaunchBuildEnv.cmd`.
3. In the environment created in step 2, type **SetupVSEnv**, and then press **Enter**.
4. Launch devenv.exe from the same environment, using the full file path. For example: `"C:\Program Files\Microsoft Visual Studio\2022\%Community|Professional|Enterprise%\Common7\IDE\devenv.exe"`
5. When you're done with the build environment, you may want to eject the ISO.

You can optionally use the Visual Studio interface with the build tools provided in the EWDK. To do this, ensure that the Visual Studio major version matches the version of the Visual Studio Build Tools in the EWDK. For example, Visual Studio 2022 works with the EWDK that contain VS17.X build tools. For a list of Visual Studio 2022 version numbers, see [Visual Studio 2022 Releases](/visualstudio/releases/2022/release-history).

## Kit versioning

A full kit build string includes as its last two components, the build number and a QFE (Quick Fix Engineering) value. For example, 10.0.22621.2428 has a build number of 22621, and a QFE value of 2428.

To build a driver, the *build number* of your SDK installation must match the *build number* of your WDK installation. The QFE values does not need to match unless your driver uses functionality that is only available in the headers included with a later QFE.

A quick way to see the full build string for locally installed kits is to go to Windows settings (Win+I), navigate to Apps, then Installed apps, and in the Search box type `kit`. The full build string appears to the right of the kit name. If you navigate to `C:\Program Files (x86)\Windows Kits\10\Include`, note that the QFE shown there is hardcoded to `.0`, so this is not a reliable way to check your QFE identifier. Also note that when you install a kit, the new installation replaces any previously existing installation of the same build number. When you install Visual Studio with the **Desktop development with C++** workload, if the installation payload includes the Windows SDK, the right-hand Summary pane also shows a hardcoded `.0` for QFE.

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
* [Learn what's new in driver development](./what-s-new-in-driver-development.md)
* [Review known issues](./wdk-known-issues.md)
