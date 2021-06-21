---
title: Download the Windows Driver Kit (WDK)
description: Download instructions for the latest released version of the Windows Driver Kit (WDK)
keywords:
- Windows Driver Kit
- WDK
- Download
- drivers
ms.date: 08/17/2020
ms.localizationpriority: medium
ms.custom: 19H1
---

# Download the Windows Driver Kit (WDK)

The WDK is used to develop, test, and deploy Windows drivers.

* [Learn what's new in driver development](what-s-new-in-driver-development.md)
* [Review known issues](wdk-known-issues.md)

[Join the Windows Insider Program](https://insider.windows.com/) to get [WDK Insider Preview builds](https://www.microsoft.com/software-download/windowsinsiderpreviewWDK). For installation instructions for the Windows Insider Preview builds, see [Installing preview versions of the Windows Driver Kit (WDK)](installing-preview-versions-wdk.md).

## Runtime requirements: WDK for Windows Server 2022

You can run the WDK for Windows Server 2022 on Windows 7 and later, and use it to develop drivers for these operating systems:

|Client OS|Server OS|
|-|-|
|Windows 10|Windows Server 2022, Windows Server 2019, Windows Server 2016|
|Windows 8.1|Windows Server 2012 R2|
|Windows 8|Windows Server 2012|
|Windows 7|Windows Server 2008 R2 SP1|

## WDK for Windows Server 2022

### ![download icon.](images/download-install.png) Step 1: Install Visual Studio 2019

The WDK requires Visual Studio. For more information about system requirements for Visual Studio, see [Visual Studio 2019 System Requirements](/visualstudio/releases/2019/system-requirements).

The following editions of Visual Studio 2019 support driver development for this release:

* [Download Visual Studio Community 2019](https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=Community&rel=16)
* [Download Visual Studio Professional 2019](https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=Professional&rel=16)
* [Download Visual Studio Enterprise 2019](https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=Enterprise&rel=16)

When you install Visual Studio 2019, select the **Desktop development with C++** workload. The Windows 10 Software Development Kit (SDK) is automatically included, and is displayed in the right-hand **Summary** pane. Note that the version of the SDK that is compatible with the WDK for Windows Server 2022 may not be the default SDK. To get the compatible version of the SDK please use the link in step 1.5 below. 

WDK has Spectre mitigation enabled by default but requires spectre mitigated libraries to be installed with Visual Studio for each architecture you are developing for. Additionally, developing drivers for ARM/ARM64 require the build tools for these architectures to also be installed with Visual Studio. To locate these items you will need to know the latest version of MSVC installed on your system.

To find the latest version of MSVC installed on your system, in **Visual Studio Installer** go to **workload page**, on the right pane under **installation details**, expand **Desktop development with C++** and locate the **MSVC v142 - VS 2019 C++ x64/x86 build tools (V14.xx)** - note where **xx** should be the highest version available.

With this information (v14.xx), go to **Individual components** and search for **v14.xx**. This will return the tool sets for all architectures, including Spectre mitigated libs. Select the driver architecture you are developing for. Alternatively you can search for 'Latest' and the most recent version of MSVC will be displayed to select.

For example, searching for Latest returns the following:

```console
MSVC v142 - VS 2019 C++ ARM build tools (Latest)
MSVC v142 - VS 2019 C++ ARM Spectre-mitigated libs (Latest)
MSVC v142 - VS 2019 C++ ARM64 build tools (Latest)
MSVC v142 - VS 2019 C++ ARM64 Spectre-mitigated libs (Latest)
MSVC v142 - VS 2019 C++ x64/x86 build tools (Latest)
MSVC v142 - VS 2019 C++ x64/x86 Spectre-mitigated libs (Latest)
```

### ![download icon.](images/download-install.png) Step 1.5 Install Windows SDK, version 2104 (Build 10.0.20348.0)
* [Download SDK for Windows 10, version 2104 (Build 10.0.20348.0)](https://go.microsoft.com/fwlink/?linkid=2164360)

This SDK is strongly recommended and will eventually be made available through Visual Studio


### ![download icon.](images/download-install.png) Step 2: Install WDK for Windows Server 2022

* [Download WDK for Windows Server 2022](https://go.microsoft.com/fwlink/?linkid=2164149)

The WDK Visual Studio extension is included in the default WDK installation.

> [!TIP]
> If you can't find driver project templates in Visual Studio, the WDK Visual Studio extension didn't install properly. To resolve this, run the WDK.vsix file from this location: C:\Program Files (x86)\Windows Kits\10\Vsix\VS2019\WDK.vsix.

## Enterprise WDK (EWDK) for Windows Server 2022

The EWDK is a standalone, self-contained command-line environment for building drivers. It includes the Visual Studio Build Tools, the SDK, and the WDK.  The latest public version of the EWDK contains Visual Studio 2019 Build Tools 16.9.2 and MSVC toolset v14.28.  To get started, mount the ISO and run **LaunchBuildEnv**.

The EWDK also requires the .NET Framework version 4.7.2. For more information about other requirements for the .NET Framework, see [.NET Framework system requirements](/dotnet/framework/get-started/system-requirements).

### ![download icon.](images/download-install.png) EWDK with Visual Studio Build Tools

* [Download the EWDK for Windows Windows Server 2022](/legal/windows/hardware/enterprise-wdk-license-2019)

> You can use the Visual Studio interface with the build tools provided in the EWDK.
>
>1.	Mount the EWDK ISO.
>2.	Run `LaunchBuildEnv.cmd`.
>3.	In the environment created in step 2, type **SetupVSEnv**, and then press **Enter**.
>4.	Launch devenv.exe from the same environment, using the full file path. 
>Example: `"C:\Program Files (x86)\Microsoft Visual Studio\2019\\%Community|Professional|Enterprise%\Common7\IDE\devenv.exe"`
>
>Note that the Visual Studio major version should match with the version in the EWDK. For example, Visual Studio 2019 works with the EWDK that contain VS16.X build tools. 

<br>



## Runtime requirements: WDK for Windows 10, version 2004

You can run the Windows 10, version 2004 WDK on Windows 7 and later, and use it to develop drivers for these operating systems:

|Client OS|Server OS|
|-|-|
|Windows 10|Windows Server 2019, Windows Server 2016|
|Windows 8.1|Windows Server 2012 R2|
|Windows 8|Windows Server 2012|
|Windows 7|Windows Server 2008 R2 SP1|

## WDK for Windows 10, version 2004

### ![download icon.](images/download-install.png) Step 1: Install Visual Studio 2019

The WDK requires Visual Studio. For more information about system requirements for Visual Studio, see [Visual Studio 2019 System Requirements](/visualstudio/releases/2019/system-requirements).

The following editions of Visual Studio 2019 support driver development for this release:

* [Download Visual Studio Community 2019](https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=Community&rel=16)
* [Download Visual Studio Professional 2019](https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=Professional&rel=16)
* [Download Visual Studio Enterprise 2019](https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=Enterprise&rel=16)

When you install Visual Studio 2019, select the **Desktop development with C++** workload. The Windows 10 Software Development Kit (SDK) is automatically included, and is displayed in the right-hand **Summary** pane. Note that the version of the SDK that is compatible with the WDK for Windows 10, version 2004 may not be the default SDK. To select the correct SDK:

In **Visual Studio Installer**, on the **Individual components** tab, search for Windows 10 SDK (10.0.19041.0), select this version and continue with install. Note that Visual Studio will automatically install Windows 10 SDK (10.0.19041.1) on your machine.

If you already have Visual Studio 2019 installed, you can install the **Windows 10 SDK (10.0.19041.1)** by using the **Modify** button in Visual Studio install.

WDK has Spectre mitigation enabled by default but requires spectre mitigated libraries to be installed with Visual Studio for each architecture you are developing for. Additionally, developing drivers for ARM/ARM64 require the build tools for these architectures to also be installed with Visual Studio. To locate these items you will need to know the latest version of MSVC installed on your system.

To find the latest version of MSVC installed on your system, in **Visual Studio Installer** go to **workload page**, on the right pane under **installation details**, expand **Desktop development with C++** and locate the **MSVC v142 - VS 2019 C++ x64/x86 build tools (V14.xx)** - note where **xx** should be the highest version available.

With this information (v14.xx), go to **Individual components** and search for **v14.xx**. This will return the tool sets for all architectures, including Spectre mitigated libs. Select the driver architecture you are developing for.

For example, searching for v14.25 returns the following:

```console
MSVC v142 - VS 2019 C++ ARM build tools (v14.25)
MSVC v142 - VS 2019 C++ ARM Spectre-mitigated libs (v14.25)
MSVC v142 - VS 2019 C++ ARM64 build tools (v14.25)
MSVC v142 - VS 2019 C++ ARM64 Spectre-mitigated libs (v14.25)
MSVC v142 - VS 2019 C++ x64/x86 build tools (v14.25)
MSVC v142 - VS 2019 C++ x64/x86 Spectre-mitigated libs (v14.25)
```

### ![download icon.](images/download-install.png) Step 1.5 Install Refreshed Windows SDK 10.0.19041.685 for Windows 10, version 2004
* [Download SDK for Windows 10, version 2004](https://aka.ms/windowssdk)

This SDK is strongly recommended and will eventually be made available through Visual Studio


### ![download icon.](images/download-install.png) Step 2: Install Refreshed WDK for Windows 10, version 2004

* [Download WDK for Windows 10, version 2004](https://go.microsoft.com/fwlink/?linkid=2128854)

The WDK Visual Studio extension is included in the default WDK installation.

> [!TIP]
> If you can't find driver project templates in Visual Studio, the WDK Visual Studio extension didn't install properly. To resolve this, run the WDK.vsix file from this location: C:\Program Files (x86)\Windows Kits\10\Vsix\VS2019\WDK.vsix.

## Enterprise WDK (EWDK) for Windows 10, version 2004

The EWDK is a standalone, self-contained command-line environment for building drivers. It includes the Visual Studio Build Tools, the SDK, and the WDK.  The latest public version of the EWDK contains Visual Studio 2019 Build Tools 16.7.0 and MSVC toolset v14.23.  To get started, mount the ISO and run **LaunchBuildEnv**.

The EWDK also requires the .NET Framework version 4.7.2. For more information about other requirements for the .NET Framework, see [.NET Framework system requirements](/dotnet/framework/get-started/system-requirements).

### ![download icon.](images/download-install.png) EWDK with Visual Studio Build Tools

* [Download the EWDK for Windows 10, version 2004](/legal/windows/hardware/enterprise-wdk-license-2019)

> You can use the Visual Studio interface with the build tools provided in the EWDK.
>
>1.	Mount the EWDK ISO.
>2.	Run `LaunchBuildEnv.cmd`.
>3.	In the environment created in step 2, type **SetupVSEnv**, and then press **Enter**.
>4.	Launch devenv.exe from the same environment, using the full file path. 
>Example: `"C:\Program Files (x86)\Microsoft Visual Studio\2019\\%Community|Professional|Enterprise%\Common7\IDE\devenv.exe"`
>
>Note that the Visual Studio major version should match with the version in the EWDK. For example, Visual Studio 2019 works with the EWDK that contain VS16.X build tools. 



## Driver samples for Windows 10

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
