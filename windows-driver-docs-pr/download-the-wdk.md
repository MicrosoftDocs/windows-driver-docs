---
title: Download the Windows Driver Kit (WDK)
description: Download instructions for the latest released version of the Windows Driver Kit (WDK)
ms.assetid: 
keywords:
- Windows Driver Kit
- WDK
- Download
- drivers
ms.author: windowsdriverdev
ms.date: 02/02/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Download the Windows Driver Kit (WDK)

The WDK is used to develop, test, and deploy Windows drivers. The latest public version of WDK is available below. Join the Windows Insider Program to get [WDK Insider Preview builds](https://www.microsoft.com/software-download/windowsinsiderpreviewWDK). 

[Learn what's new in driver development](what-s-new-in-driver-development.md) 

[Review known issues](https://go.microsoft.com/fwlink/p/?LinkId=859628)

## WDK for Windows 10, version 1709

### Step 1: Install Visual Studio 2017
The following editions of Visual Studio 2017 support driver development: 

<!-- Insert 3 VS download buttons HERE -->

When you install Visual Studio, select the **Desktop development with C++** workload. The Windows 10 Software Development Kit (SDK) is automatically included, and is displayed in the right-hand **Summary** pane. 

For ARM/ARM64 driver development, choose **Individual components** and under **Compilers, build tools, and runtimes** select **Visual C++ compilers and libraries for ARM/ARM64**.

### Step 2: Install WDK for Windows 10, version 1709

<!-- Insert Download Now button --> 

New for this release: The WDK installation will by default install the WDK Visual Studio extension. This must be done in order for WDK VS integration to work. 

## Enterprise WDK for Windows 10, version 1709 (EWDK) 

The EWDK is a standalone self-contained command-line environment for building drivers. It includes the Visual Studio Build Tools, the SDK, and the WDK. There are two versions available: 

EWDK with Visual Studio Build Tools 15.4 (Recommended)

<!-- Insert Download Now button --> 

EWDK with Visual Studio Build Tools 15.2

<!-- Insert Download Now button --> 

To get started, mount the ISO and run **LaunchBuildEnv**.

## Additional information

### Release notes and run-time requirements

WDK requires Visual Studio, for more information more info on system requirements for Visual Studio please review [Visual Studio 2017 System Requirements](https://www.visualstudio.com/productinfo/vs2017-system-requirements-vs). 

EWDK will additionally need .NET 4.6.1, for more information on what .NET runs on please review [.NET Framework system requirements](https://docs.microsoft.com/dotnet/framework/get-started/system-requirements). 

You can use the WDK to develop drivers for these operating systems: 

|CLient OS|Server OS|
|-|-|
|Windows 10|Windows Server 2016|
|Windows 8.1|Windows Server 2012 R2|
Windows 8|Windows Server 2012|
Windows 7|Windows Server 2008 R2 SP1|

### Universal Windows driver samples

To get universal Windows driver samples, do one of the following: 
* Go to the driver samples page on [GitHub](https://github.com/Microsoft/Windows-driver-samples) and click **Clone or download > Download ZIP** on the right side of the page. 
Download the [GitHub Extension for Visual Studio](https://visualstudio.github.com/) to connect to the GitHub repositories. 

[Learn more about what's new for driver samples](https://developer.microsoft.com/windows/hardware/drivers-code-samples). 