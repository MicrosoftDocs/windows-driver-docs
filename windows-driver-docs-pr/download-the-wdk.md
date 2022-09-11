---
title: Download the Windows Driver Kit (WDK)
description: Download instructions for the latest released version of the Windows Driver Kit (WDK)
keywords:
- Windows Driver Kit
- WDK
- Download
- drivers
ms.date: 08/22/2022
---

# Download the Windows Driver Kit (WDK)

> [!NOTE]
> If you installed the original Windows 11, version 22H2 WDK between May and August 2022 (version 10.0.22621.1), you may see the following error message when you start Visual Studio with the WDK.
> * The service ‘Microsoft.VisualStudio.Shell.Interop.SVsUIShell’ must be installed for this feature to work. Ensure that this service is available.
>
> You can either safely dismiss this message, or you can uninstall the WDK and then reinstall the WDK (updated August 19, 2022 to version 10.0.22621.382) using the WDK download link below.
>
> It is still not possible to debug drivers within the Visual Studio interface when using Visual Studio 2022 version 17.2.0 and the Windows 11, version 22H2 WDK (version 10.0.22621.382). To work around the problem, debug with WinDbg or use a version of Visual Studio earlier than 17.2.0. The following error message is related to this issue:
> * The 'Microsoft.Windows.Tools.WinIDE.Debugger.DebuggerPackage, DebuggerPackage, Version=10.0.0.0, Culture=neutral, PublicKeyToken=null' package did not load correctly.

The WDK is used to develop, test, and deploy drivers for Windows.

* [Learn what's new in driver development](./what-s-new-in-driver-development.md)
* [Review known issues](./wdk-known-issues.md)

[Join the Windows Insider Program](https://insider.windows.com/) to get [WDK Insider Preview builds](https://aka.ms/wipwdk). For installation instructions for the Windows Insider Preview builds, see [Installing preview versions of the Windows Driver Kit (WDK)](./installing-preview-versions-wdk.md).

Starting with the Windows 11, version 22H2 release of the WDK and EWDK, the kits support:

* Visual Studio 2022 exclusively
* Building and testing kernel-mode drivers for x64 and Arm64
* Building and testing drivers for Windows 10, Windows Server 2016 and later client and server versions
* Side by side (SxS) support with previous WDK/EWDK

Multiple WDKs and EWDKs can be installed concurrently on the same computer and even be part of same build system. You can run the Windows 11, version 22H2 WDK on Windows 7 and later.

To target Windows 8.1, Windows 8, and Windows 7, you will need to install an older WDK and an older version of Visual Studio either on the same machine or on a separate machine. For links to older kits, see [Other WDK downloads](./other-wdk-downloads.md).

Certain device-specific stacks (for example graphics) continue to have x86/ARM32 user-mode components to support x86/ARM32 apps.

Starting with this release, WDF redistributable co-installers are no longer supported.

> [!NOTE]
> On a computer that has both the Windows 11, version 22H2 WDK and an older WDK, when building a WDF 1.11 driver, msbuild fails because it cannot find the WDF coinstaller. To fix this problem, before installing Windows 11, version 22H2 WDK, back up the folder `\Program files (x86)\windows kit\10\redist\wdf` and restore it afterwards. Alternatively, if you have already installed the Windows 11, version 22H2 WDK, install the MSI file at [WDK 8 redistributable components](https://go.microsoft.com/fwlink/p/?LinkID=253170) on a separate computer and copy the `redist` folder to the above folder. For more information, see [Redistributable Framework Components](./wdf/installation-components-for-kmdf-drivers.md).

## Download and install the Windows 11, version 22H2 WDK

### ![download icon.](images/download-install.png) Step 1: Install Visual Studio 2022

The WDK requires Visual Studio. For more information about system requirements for Visual Studio, see [Visual Studio 2022 System Requirements](/visualstudio/releases/2022/system-requirements).

The following editions of Visual Studio 2022 support driver development for this release:

* [Download Visual Studio Community 2022](https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=Community&rel=17)
* [Download Visual Studio Professional 2022](https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=Professional&rel=17)
* [Download Visual Studio Enterprise 2022](https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=Enterprise&rel=17)

When you install Visual Studio 2022, select the **Desktop development with C++** workload. The Windows 11, version 22H2 Software Development Kit (SDK) that is compatible with the Windows 11, version 22H2 WDK is not included in Visual Studio. Please use the SDK download link in step 2 below.

WDK has Spectre mitigation enabled by default but requires Spectre mitigated libraries to be installed with Visual Studio for each architecture you are developing for. Additionally, developing drivers for Arm/Arm64/Arm64EC require the build tools for these architectures to also be installed with Visual Studio. To locate these items, you will need to know the latest version of MSVC installed on your system.

To find the latest version of MSVC installed on your system, in **Visual Studio Installer** go to **workload page**, on the right pane under **installation details**, expand **Desktop development with C++** and locate the **MSVC v143 - VS 2022 C++ x64/x86 build tools (Latest)**.

With this information (Latest), go to **Individual components** and search for **Latest**. This will return the tool sets for all architectures, including Spectre mitigated libs. Select the driver architecture you are developing for. 

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

### ![download icon.](images/download-install.png) Step 2: Install Windows 11, version 22H2 SDK

* [Download Windows 11, version 22H2 SDK](https://developer.microsoft.com/en-us/windows/downloads/windows-sdk/)

This SDK must be installed separately until available through Visual Studio

### ![download icon.](images/download-install.png) Step 3: Install Windows 11, version 22H2 WDK

* [Download WDK for Windows 11, version 22H2 ](https://go.microsoft.com/fwlink/?linkid=2196230)

The WDK Visual Studio extension is included in the default WDK installation.

> [!TIP]
> If you can't find driver project templates in Visual Studio, the WDK Visual Studio extension didn't install properly. To resolve this, run the WDK.vsix file from this location: C:\Program Files (x86)\Windows Kits\10\Vsix\VS2022\10.0.22621.382\WDK.vsix.

## Enterprise WDK (EWDK)

The EWDK is a standalone, self-contained command-line environment for building drivers. It includes Visual Studio Build Tools, the SDK, and the WDK.  The latest public version of the EWDK contains Visual Studio 2022 Build Tools 17.1.5 and MSVC toolset v14.31.  To get started, mount the ISO and run **LaunchBuildEnv**.

The EWDK also requires the .NET Framework version 4.7.2. For more information about other requirements for the .NET Framework, see [.NET Framework system requirements](/dotnet/framework/get-started/system-requirements).

### ![download icon.](images/download-install.png) Windows 11, version 22H2 EWDK with Visual Studio Build Tools

* [Download the Windows 11, version 22H2 EWDK](/legal/windows/hardware/enterprise-wdk-license-2022)

> You can use the Visual Studio interface with the build tools provided in the EWDK.
>
>1.    Mount the EWDK ISO.
>2.    Run `LaunchBuildEnv.cmd`.
>3.    In the environment created in step 2, type **SetupVSEnv**, and then press **Enter**.
>4.    Launch devenv.exe from the same environment, using the full file path. 
>Example: `"C:\Program Files\Microsoft Visual Studio\2022\%Community|Professional|Enterprise%\Common7\IDE\devenv.exe"`
>
>Note that the Visual Studio major version should match with the version in the EWDK. For example, Visual Studio 2022 works with the EWDK that contain VS17.X build tools. For a list of Visual Studio 2022 version numbers, see [Visual Studio 2022 Releases](/visualstudio/releases/2022/release-history).

<br>


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
