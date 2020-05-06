---
title: Download the Windows Driver Kit (WDK)
description: Download instructions for the latest released version of the Windows Driver Kit (WDK)
ms.assetid: 7b5e253b-3bcd-41e3-a646-0f95ce416f87
keywords:
- Windows Driver Kit
- WDK
- Download
- drivers
ms.date: 03/16/2020
ms.localizationpriority: medium
ms.custom: 19H1
---

# Download the Windows Driver Kit (WDK)

The WDK is used to develop, test, and deploy Windows drivers.

* [Learn what's new in driver development](what-s-new-in-driver-development.md)
* [Review known issues](https://go.microsoft.com/fwlink/?linkid=872986)

[Join the Windows Insider Program](https://insider.windows.com/) to get [WDK Insider Preview builds](https://www.microsoft.com/en-us/software-download/windowsinsiderpreviewWDK). For installation instructions for the Windows Insider Preview builds, see [Installing preview versions of the Windows Driver Kit (WDK)](installing-preview-versions-wdk.md).

## WDK for Windows 10, version 1903

### ![download icon](images/download-install.png) Step 1: Install Visual Studio 2019

The WDK requires Visual Studio. For more information about system requirements for Visual Studio, see [Visual Studio 2019 System Requirements](https://docs.microsoft.com/visualstudio/releases/2019/system-requirements). 

The following editions of Visual Studio 2019 support driver development for this release:

* [Download Visual Studio Community 2019](https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=Community&rel=16)
* [Download Visual Studio Professional 2019](https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=Professional&rel=16)
* [Download Visual Studio Enterprise 2019](https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=Enterprise&rel=16)

When you install Visual Studio 2019, select the **Desktop development with C++** workload. The Windows 10 Software Development Kit (SDK) is automatically included, and is displayed in the right-hand **Summary** pane. Note that the version of the SDK that is compatible with the WDK for Windows 10, version 1903 may not be the default SDK. To select the correct SDK:

1. In **Visual Studio Installer**, on the **Workloads** tab, under **Installation Details**, expand **Universal Windows Platform development**.
1. Under **Optional**, select **Windows 10 SDK (10.0.18362.0)**.
1. Continue with the install.

If you already have Visual Studio 2019 installed, you can install the Windows 10 SDK (10.0.18362.0) by using the **Modify** button in Visual Studio install.

Verify that you have correct version of MSVC v142 build tools for x86/x64 installed by 
1. Choose **Individual components**
1. Under **Compilers, build tools, and runtimes**, options **MSVC v142 - VS 2019 C++ x64/x86 build tools (v14.21)** should be checked and if not please go ahead and check it.
1. If later versions of MSVC build tools are already installed then you would need to set the MSVC version in Project's Properties inside VS. Go to **Configuration Properties** then **Advanced** then set **MSVC Toolset Version** to **14.21.XXXX**. If you want to use command line then follow this [VS Link](https://docs.microsoft.com/cpp/build/building-on-the-command-line?view=vs-2019).

For ARM/ARM64 driver development: 

1. Choose **Individual components**. 
1. Under **Compilers, build tools, and runtimes**, select **MSVC v142 - VS 2019 C++ ARM build tools (v14.21)** and **MSVC v142 - VS 2019 C++ ARM64 build tools (v14.21)**.

You will need to install Spectre mitigated libraries for each architecture you intend to build drivers for. Go to **Individual Components** tab and under heading **Compilers, build tools, and runtimes**:
  * For x86 and x64 select **MSVC v142 - VS 2019 C++ x64/x86 Spectre-mitigated libs (v14.21)**.
  * For ARM select **MSVC v142 - VS 2019 C++ ARM Spectre-mitigated libs (v14.21)**.
  * For ARM64 select **MSVC v142 - VS 2019 C++ ARM64 Spectre-mitigated libs (v14.21)**.

### ![download icon](images/download-install.png) Step 2: Install WDK for Windows 10, version 1903

* [Download WDK for Windows 10, version 1903](https://go.microsoft.com/fwlink/?linkid=2085767)

The WDK installation will by default install the WDK Visual Studio extension. 

## Enterprise WDK (EWDK) for Windows 10, version 1903

The EWDK is a standalone, self-contained command-line environment for building drivers. It includes the Visual Studio Build Tools, the SDK, and the WDK.  The latest public version of the EWDK contains Visual Studio 2019 Build Tools 16.0.0.  To get started, mount the ISO and run **LaunchBuildEnv**.

The EWDK also requires the .NET Framework version 4.7.2. For more information about other requirements for the .NET Framework, see [.NET Framework system requirements](https://docs.microsoft.com/dotnet/framework/get-started/system-requirements).

### ![download icon](images/download-install.png) EWDK with Visual Studio Build Tools

* [Download the EWDK for Windows 10, version 1903](https://docs.microsoft.com/legal/windows/hardware/enterprise-wdk-license-2019)

## Additional information

### Release notes and runtime requirements

You can use the WDK to develop drivers for these operating systems:

|Client OS|Server OS|
|-|-|
|Windows 10|Windows Server 2019, Windows Server 2016|
|Windows 8.1|Windows Server 2012 R2|
Windows 8|Windows Server 2012|
Windows 7|Windows Server 2008 R2 SP1|

### Universal Windows driver samples

To download universal Windows driver samples, do one of the following:

* Go to the driver samples page on [GitHub](https://github.com/Microsoft/Windows-driver-samples), click **Clone or download**, and then click **Download ZIP**.
* Download the [GitHub Extension for Visual Studio](https://visualstudio.github.com/), and then connect to the GitHub repositories.
* Browse the driver samples on the [Microsoft Samples portal](https://docs.microsoft.com/samples/browse/?products=windows-wdk).

## Related downloads

* [Download the WDK Insider Preview](https://www.microsoft.com/en-us/software-download/windowsinsiderpreviewWDK)
* [Download previous versions of the WDK](other-wdk-downloads.md)
* [Download the Windows Assessment and Deployment Kit (Windows ADK)](https://docs.microsoft.com/windows-hardware/get-started/adk-install)
* [Download the Windows HLK](https://docs.microsoft.com/windows-hardware/test/hlk/windows-hardware-lab-kit)
* [Download the Windows Debugging Tools (WinDbg)](https://docs.microsoft.com/windows-hardware/drivers/debugger/debugger-download-tools)
* [Download Windows Symbol Packages](https://docs.microsoft.com/windows-hardware/drivers/debugger/debugger-download-symbols)
