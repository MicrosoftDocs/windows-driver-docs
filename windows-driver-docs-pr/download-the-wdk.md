---
title: Download the Windows Driver Kit (WDK)
description: Download instructions for the latest released version of the Windows Driver Kit (WDK)
ms.assetid: 7b5e253b-3bcd-41e3-a646-0f95ce416f87
keywords:
- Windows Driver Kit
- WDK
- Download
- drivers
ms.date: 08/06/2018
ms.localizationpriority: medium
---

# Download the Windows Driver Kit (WDK)

The WDK is used to develop, test, and deploy Windows drivers. The latest public version of WDK is available below. 

Join the Windows Insider Program to get [WDK Insider Preview builds](https://www.microsoft.com/software-download/windowsinsiderpreviewWDK). For installation instructions for the Windows Insider Preview builds, see [Installing preview versions of the Windows Driver Kit (WDK)](installing-preview-versions-wdk.md).

* [Learn what's new in driver development](what-s-new-in-driver-development.md) 
* [Review known issues](https://go.microsoft.com/fwlink/?linkid=872986)

## WDK for Windows 10, version 1809

### ![download icon](images/download-install.png) Step 1: Install Visual Studio 2017 
The following editions of Visual Studio 2017 support driver development: 

* [Download Visual Studio Community 2017](https://www.visualstudio.com/thank-you-downloading-visual-studio/?sku=Community&rel=15)
* [Download Visual Studio Professional 2017](https://www.visualstudio.com/thank-you-downloading-visual-studio/?sku=Professional&rel=15) 
* [Download Visual Studio Enterprise 2017](https://www.visualstudio.com/thank-you-downloading-visual-studio/?sku=Enterprise&rel=15)

When you install Visual Studio, select the **Desktop development with C++** workload. The Windows 10 Software Development Kit (SDK) is automatically included, and is displayed in the right-hand **Summary** pane. 

For ARM/ARM64 driver development, choose **Individual components** and under **Compilers, build tools, and runtimes** select **Visual C++ compilers and libraries for ARM/ARM64**.


### ![download icon](images/download-install.png) Step 2: Install WDK for Windows 10, version 1809

* [Download WDK for Windows 10, version 1809](https://go.microsoft.com/fwlink/?linkid=2026156) 

New as of 1709 release: The WDK installation will by default install the WDK Visual Studio extension. This must be done in order for WDK VS integration to work. 

## Enterprise WDK for Windows 10, version 1809 (EWDK) 

The EWDK is a standalone self-contained command-line environment for building drivers. It includes the Visual Studio Build Tools, the SDK, and the WDK.  The latest public version of the EWDK contains Visual Studio Build Tools 15.8.9.  To get started, mount the ISO and run **LaunchBuildEnv**. 

### ![download icon](images/download-install.png) EWDK with Visual Studio Build Tools 15.8.9 (Recommended)

* [Download EWDK for Windows 10, version 1809](https://developer.microsoft.com/windows/hardware/license-terms-EWDK)


### ![download icon](images/download-install.png) EWDK with Visual Studio Build Tools 15.8

* [Download EWDK for Windows 10, version 1809](https://developer.microsoft.com/windows/hardware/license-terms-EWDK)

## Additional information

### Release notes and run-time requirements

WDK requires Visual Studio, for more information more info on system requirements for Visual Studio please review [Visual Studio 2017 System Requirements](https://www.visualstudio.com/productinfo/vs2017-system-requirements-vs). 

EWDK will additionally need .NET 4.6.1, for more information on what .NET runs on please review [.NET Framework system requirements](https://docs.microsoft.com/dotnet/framework/get-started/system-requirements). 

You can use the WDK to develop drivers for these operating systems: 

|Client OS|Server OS|
|-|-|
|Windows 10|Windows Server 2019, Windows Server 2016|
|Windows 8.1|Windows Server 2012 R2|
Windows 8|Windows Server 2012|
Windows 7|Windows Server 2008 R2 SP1|

### Universal Windows driver samples

To get universal Windows driver samples, do one of the following: 
* Go to the driver samples page on [GitHub](https://github.com/Microsoft/Windows-driver-samples) and click **Clone or download > Download ZIP** on the right side of the page. 
* Download the [GitHub Extension for Visual Studio](https://visualstudio.github.com/) to connect to the GitHub repositories. 
* [Learn more about what's new for driver samples](https://developer.microsoft.com/windows/hardware/drivers-code-samples). 

## Related downloads
* [Download the WDK Insider Preview](https://www.microsoft.com/software-download/windowsinsiderpreviewWDK)
* [Download previous versions of the WDK](other-wdk-downloads.md)
* [Download the Windows Assessment and Deployment Kit (Windows ADK)](https://developer.microsoft.com/windows/hardware/windows-assessment-deployment-kit)
* [Download the Windows HLK, HCK, or Logo Kit](https://developer.microsoft.com/windows/hardware/windows-hardware-lab-kit)
* [Download the debugging Tools for Windows (WinDbg)](https://developer.microsoft.com/windows/hardware/download-windbg)
* [Download Windows Symbol Packages](https://developer.microsoft.com/windows/hardware/download-symbols)

