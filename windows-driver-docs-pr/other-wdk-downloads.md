---
title: Previous WDK versions and other downloads
description: Install versions of the Windows Driver Kit (WDK), the Windows Debugger (WinDBG), and more.
ms.assetid: e07d9f05-f8d0-46e5-82e6-c23baa614bb1
keywords:
- Windows Driver Kit
- previous versions
- WDK
ms.date: 05/07/2018
ms.localizationpriority: medium
---
<!-- This is in branch "v-gmoor-other-wdk-downloads-2" -->
# Other WDK downloads

This topic contains information about earlier versions of the Windows Driver Kit (WDK), Enterprise WDK (EWDK), and additional downloads for support purposes. To develop drivers, use the latest public versions of the Windows Driver Kit (WDK) and tools, available for download on [Download the Windows Driver Kit (WDK)](download-the-wdk.md).


The Windows Driver Kit (WDK) is used to develop, test, and deploy
Windows drivers. To develop drivers, use the latest public versions of
the Windows Driver Kit (WDK) and tools, available for download on
[Download the Windows Driver Kit (WDK)](download-the-wdk.md).

This topic contains information about earlier versions of the WDK, the
Enterprise WDK (EWDK), and additional downloads for support purposes. To
use these earlier versions, you must *first* install the version of
Visual Studio that is appropriate for your targeted platform.


## Step 1: Install Visual Studio

Development of drivers is supported for specific versions of Visual
Studio. To develop a driver for a specific version of Windows, you must
use one of the versions of Visual Studio that are identified (and linked
for download) in the following table.

| Versions of Windows      | Edition(s) of Visual Studio            |
|--------------------------|----------------------------------------|
| Windows 10, version 1803 <br/>Windows 10, version 1709 | [Visual Studio Community 2017](https://www.visualstudio.com/thank-you-downloading-visual-studio/?sku=Community&rel=15) <br/>[Visual Studio Professional 2017](https://www.visualstudio.com/thank-you-downloading-visual-studio/?sku=Professional&rel=15) <br/>[Visual Studio Enterprise 2017](https://www.visualstudio.com/thank-you-downloading-visual-studio/?sku=Enterprise&rel=15) |
| Windows 10, version 1703 <br/>Windows 10, version 1607 | [Visual Studio Express 2015 for Desktop](https://go.microsoft.com/fwlink/?linkid=875331) <br/>[Visual Studio Community 2015](https://go.microsoft.com/fwlink/p/?LinkId=534599) <br/>[Visual Studio Professional 2015](https://go.microsoft.com/fwlink/p/?LinkId=619628) <br/>[Visual Studio Enterprise 2015](https://go.microsoft.com/fwlink/p/?LinkId=619629) |
| Windows 8.1 Update <br/>Windows 8.1 | [Visual Studio 2013](https://go.microsoft.com/fwlink/?linkid=875331) |
| Windows 8                | [Visual Studio Professional 2012](https://go.microsoft.com/fwlink/p/?LinkID=255976) <br/>[Visual Studio Ultimate 2012](https://go.microsoft.com/fwlink/p/?LinkID=255982) |


### Configure Visual Studio for Windows 10, versions 1709 and 1803

When you install Visual Studio, select the **Desktop development with
C++** workload. The Windows 10 Software Development Kit (SDK) is
automatically included and is displayed in the right-hand **Summary**
pane.

To develop drivers for ARM/ARM64, choose **Individual components** and
under **Compilers, build tools, and runtimes** select **Visual C++
compilers and libraries for ARM/ARM64**.

### Install Windows SDK for Windows 10, version 1703

For systems that run Windows 10, version 1703, also download and install the Windows SDK: [Windows SDK for Windows 10, version 1703](https://go.microsoft.com/fwlink/p/?LinkID=845298).


## Step 2: Install the WDK

The WDK is integrated with Visual Studio and Debugging Tools for Windows
(WinDbg). This integrated environment gives you the tools you need to
develop, build, package, deploy, test, and debug drivers.

> [!Note]
> Starting with Windows 10, version 1709, installing the WDK
> will by default install the WDK extensions for Visual Studio. These
> extensions are required for integration of the WDK with Visual Studio.

| Versions of Windows      | WDK and related downloads                       |
|--------------------------|-------------------------------------------------|
| Windows 10, version 1803 | [WDK for Windows 10, version 1803](https://go.microsoft.com/fwlink/?linkid=873060) |
| Windows 10, version 1709 | [WDK for Windows 10, version 1709](https://go.microsoft.com/fwlink/p/?linkid=859232) |
| Windows 10, version 1703 | [WDK for Windows 10, version 1703](https://go.microsoft.com/fwlink/p/?LinkID=845980) |
| Windows 10, version 1607 | [WDK for Windows 10, version 1607](https://go.microsoft.com/fwlink/p/?LinkId=526733)                |
| Windows 8.1 Update       | [WDK 8.1 Update](https://go.microsoft.com/fwlink/p/?LinkId=393659) (English only) <br/>[WDK 8.1 Update Test Pack](https://go.microsoft.com/fwlink/p/?LinkID=393660) (English only) <br/>[WDK 8.1 Samples](https://code.msdn.microsoft.com/windowshardware/Windows-Driver-Kit-WDK-81-cf35e953) |
| Windows 8                | [WDK 8](https://go.microsoft.com/fwlink/p/?LinkID=324284) (English only) <br/>[WDK 8 redistributable components](https://go.microsoft.com/fwlink/p/?LinkID=253170) (English only) <br/>[WDK 8 Samples](https://code.msdn.microsoft.com/windowshardware/Windows-Driver-Kit-WDK-80-e3161626) |
| Windows XP <br/>Windows Server 2003 | [WDK 7.1.0](https://www.microsoft.com/download/confirmation.aspx?id=11800) |


### Notes for Windows 8.1 Update

#### WinDbg for Windows 8.1

Debugging Tools for Windows (WinDbg) are included in the WDK 8.1 Update,
but you can also install them as a standalone component from the Windows
8.1 SDK. In the installation wizard, select Debugging Tools for Windows,
and clear all other components. Get WinDbg as part of Windows 8.1 SDK,
which you can download from [Windows SDK and emulator archive](https://developer.microsoft.com/en-us/windows/downloads/sdk-archive).
<!--edit:  Preceding link for the Windows 8.1 SDK is a change and update for an old, dead link. -->

#### Remote Debugging client for Windows 8.1

With the Windows Remote Debugging client, you can work remotely with
developers from Microsoft, over the internet, to debug kernel-mode
failures using the kernel debugger. For more information about remote debugging,
see [Remote Debugging](https://docs.microsoft.com/windows-hardware/drivers/debugger/remote-debugging).

-   [Download the Remote Debugging client](https://go.microsoft.com/fwlink/p/?LinkId=316921) (English only)
<!--edit: Preceding link for the Remote Debugging client for Windows 8.1 is dead, and I haven't yet found a working replacement, unless one of these applies: https://docs.microsoft.com/en-us/visualstudio/debugger/remote-debugging?view=vs-2017#download-and-install-the-remote-tools -->


## Optional: Install the EWDK

The EWDK is a standalone, self-contained, command-line environment for
building drivers and basic Win32 test applications. It includes the
Visual Studio Build Tools, the SDK, and the WDK. This environment
doesn't include all the features available in Visual Studio, such as
the integrated development environment (IDE).

For more information about the EWDK, see [Using the Enterprise WDK 10](https://docs.microsoft.com/en-us/windows-hardware/drivers/develop/using-the-enterprise-wdk).

| Versions of Windows               | EWDK                              |
|-----------------------------------|-----------------------------------|
| Windows 10, version 1803          | [EWDK for Windows 10, version 1803](https://developer.microsoft.com/windows/hardware/license-terms-EWDK) |
| Windows 10, version 1709          | [EWDK for Visual Studio with Build Tools 15.6](https://developer.microsoft.com/windows/hardware/license-terms-enterprise-wdk-1709-VS15-6) (Recommended) <br/>[EWDK for Visual Studio with Build Tools 15.4](https://developer.microsoft.com/windows/hardware/license-terms-enterprise-wdk-1709-VS15-4) <br/>[EWDK for Visual Studio with Build Tools 15.2](https://developer.microsoft.com/windows/hardware/license-terms-enterprise-wdk-1709) |
| Windows 10, version 1703          | [EWDK for Windows 10, version 1703](https://developer.microsoft.com/windows/hardware/license-terms-enterprise-wdk-1703) |

> [!Note]
> Starting in Windows 10 version 1709, the EWDK is ISO-based. To get started, download and mount the ISO, then run **LaunchBuildEnv**.


## Standalone tools for debugging Windows XP and Windows Vista

If you're debugging Windows XP, Windows Server 2003, Windows Vista, or
Windows Server 2008 (or using one of these operating systems to run
Debugging Tools for Windows), you need to use the Windows 7 release of
the debugging tools. It's included in the SDK for Windows 7 and .NET
Framework 4.0.

> [!IMPORTANT]
> Newer versions of the Visual C++ 2010 Redistributable
> can cause issues when you install the SDK for Windows 7. For more
> information, see support for the Windows SDK.

Get the standalone debugging tools for Windows XP by first downloading
the Windows 7 SDK: Microsoft Windows SDK for Windows 7 and .NET
Framework 4.

To install the Debugging Tools for Windows as a standalone component,
start the SDK installer, and in the installation wizard, select
**Debugging Tools for Windows**, and clear all other components.



<!-- Old content follows...

Downloads for Windows 10, version 1803
--------------------------------------

### WDK for Windows 10, version 1803

#### Step 1: Install Visual Studio 2017

The following editions of Visual Studio 2017 support driver development:

-   [Download Visual Studio Community
    2017](https://www.visualstudio.com/thank-you-downloading-visual-studio/?sku=Community&rel=15)

-   [Download Visual Studio Professional
    2017](https://www.visualstudio.com/thank-you-downloading-visual-studio/?sku=Professional&rel=15)

-   [Download Visual Studio Enterprise
    2017](https://www.visualstudio.com/thank-you-downloading-visual-studio/?sku=Enterprise&rel=15)

When you install Visual Studio, select the **Desktop development with
C++** workload. The Windows 10 Software Development Kit (SDK) is
automatically included, and is displayed in the right-hand **Summary**
pane.

For ARM/ARM64 driver development, choose **Individual components** and
under **Compilers, build tools, and runtimes** select **Visual C++
compilers and libraries for ARM/ARM64**.

#### Step 2: Install WDK for Windows 10, version 1803

-   [Download WDK for Windows 10, version
    1803](https://go.microsoft.com/fwlink/?linkid=873060)

New as of 1709 release: The WDK installation will by default install the
WDK Visual Studio extension. This must be done in order for WDK VS
integration to work.

### Enterprise WDK (EWDK) for Windows 10, version 1803

The EWDK is a standalone self-contained command-line environment for
building drivers. It includes the Visual Studio Build Tools, the SDK,
and the WDK. The latest public version of the EWDK contains Visual
Studio Build Tools 15.7. To get started, mount the ISO and run
**LaunchBuildEnv**.

#### EWDK with Visual Studio Build Tools 15.7

-   [Download EWDK for Windows 10, version
    1803](https://developer.microsoft.com/windows/hardware/license-terms-EWDK)

### Release notes and run-time requirements

WDK requires Visual Studio, for more information more info on system
requirements for Visual Studio please review [Visual Studio 2017 System
Requirements](https://www.visualstudio.com/productinfo/vs2017-system-requirements-vs).

EWDK will additionally need .NET 4.6.1, for more information on what
.NET runs on please review [.NET Framework system
requirements](https://docs.microsoft.com/dotnet/framework/get-started/system-requirements).

To work with HAL Extensions, download and install the updated [Windows
OEM HAL Extension Test Cert 2017 (TEST
ONLY)](https://go.microsoft.com/fwlink/?linkid=872294) certificate after
preparing your environment for development. [Learn
more](https://support.microsoft.com/help/4131991)

Downloads for Windows 10, version 1709
--------------------------------------

### WDK for Windows 10, version 1709

#### Step 1: Install Visual Studio 2017

The following editions of Visual Studio 2017 support driver development:

-   [Download Visual Studio Community
    2017](https://www.visualstudio.com/thank-you-downloading-visual-studio/?sku=Community&rel=15)

-   [Download Visual Studio Professional
    2017](https://www.visualstudio.com/thank-you-downloading-visual-studio/?sku=Professional&rel=15)

-   [Download Visual Studio Enterprise
    2017](https://www.visualstudio.com/thank-you-downloading-visual-studio/?sku=Enterprise&rel=15)

When you install Visual Studio, select the **Desktop development with
C++** workload. The Windows 10 Software Development Kit (SDK) is
automatically included, and is displayed in the right-hand **Summary**
pane.

For ARM/ARM64 driver development, choose **Individual components** and
under **Compilers, build tools, and runtimes** select **Visual C++
compilers and libraries for ARM/ARM64**.

#### Step 2: Install WDK for Windows 10, version 1709

-   [Download WDK for Windows 10, version
    1709](https://go.microsoft.com/fwlink/p/?linkid=859232)

New for this release: The WDK installation will by default install the
WDK Visual Studio extension. This must be done in order for integration
of the WDK with Visual Studio to work.

### Enterprise WDK (EWDK) for Windows 10, version 1709

The EWDK is a standalone self-contained command-line environment for
building drivers. It includes the Visual Studio Build Tools, the SDK,
and the WDK. The latest public version of the EWDK contains Visual
Studio Build Tools 15.6.

#### EWDK with Visual Studio Build Tools 15.6 (Recommended)

-   [Download EWDK for Windows 10, version
    1709](https://developer.microsoft.com/windows/hardware/license-terms-enterprise-wdk-1709-VS15-6)

#### EWDK with Visual Studio Build Tools 15.4

-   [Download EWDK for Windows 10, version
    1709](https://developer.microsoft.com/windows/hardware/license-terms-enterprise-wdk-1709-VS15-4)

#### EWDK with Visual Studio Build Tools 15.2

-   [Download EWDK for Windows 10, version
    1709](https://developer.microsoft.com/windows/hardware/license-terms-enterprise-wdk-1709)

To get started, mount the ISO and run **LaunchBuildEnv**.


# OLD CONTENT FOLLOWS (but may also precede)

## Downloads for Windows 10, version 1803

### WDK for Windows 10, version 1803

#### Step 1: Install Visual Studio 2017
The following editions of Visual Studio 2017 support driver development:

* [Download Visual Studio Community 2017](https://www.visualstudio.com/thank-you-downloading-visual-studio/?sku=Community&rel=15)
* [Download Visual Studio Professional 2017](https://www.visualstudio.com/thank-you-downloading-visual-studio/?sku=Professional&rel=15)
* [Download Visual Studio Enterprise 2017](https://www.visualstudio.com/thank-you-downloading-visual-studio/?sku=Enterprise&rel=15)

When you install Visual Studio, select the **Desktop development with C++** workload. The Windows 10 Software Development Kit (SDK) is automatically included, and is displayed in the right-hand **Summary** pane.

For ARM/ARM64 driver development, choose **Individual components** and under **Compilers, build tools, and runtimes** select **Visual C++ compilers and libraries for ARM/ARM64**.


#### Step 2: Install WDK for Windows 10, version 1803

* [Download WDK for Windows 10, version 1803](https://go.microsoft.com/fwlink/?linkid=873060)

New as of 1709 release: The WDK installation will by default install the WDK Visual Studio extension. This must be done in order for WDK VS integration to work.

### Enterprise WDK (EWDK) for Windows 10, version 1803

The EWDK is a standalone self-contained command-line environment for building drivers. It includes the Visual Studio Build Tools, the SDK, and the WDK.  The latest public version of the EWDK contains Visual Studio Build Tools 15.7. To get started, mount the ISO and run **LaunchBuildEnv**.

#### EWDK with Visual Studio Build Tools 15.7

* [Download EWDK for Windows 10, version 1803](https://developer.microsoft.com/windows/hardware/license-terms-EWDK)

### Release notes and run-time requirements

WDK requires Visual Studio, for more information more info on system requirements for Visual Studio please review [Visual Studio 2017 System Requirements](https://www.visualstudio.com/productinfo/vs2017-system-requirements-vs).

EWDK will additionally need .NET 4.6.1, for more information on what .NET runs on please review [.NET Framework system requirements](https://docs.microsoft.com/dotnet/framework/get-started/system-requirements).

To work with HAL Extensions, download and install the updated [Windows OEM HAL Extension Test Cert 2017 (TEST ONLY)](https://go.microsoft.com/fwlink/?linkid=872294) certificate after preparing your environment for development.  [Learn more](https://support.microsoft.com/help/4131991)


## Downloads for Windows 10, version 1709

### WDK for Windows 10, version 1709

#### Step 1: Install Visual Studio 2017
The following editions of Visual Studio 2017 support driver development:

* [Download Visual Studio Community 2017](https://www.visualstudio.com/thank-you-downloading-visual-studio/?sku=Community&rel=15)
* [Download Visual Studio Professional 2017](https://www.visualstudio.com/thank-you-downloading-visual-studio/?sku=Professional&rel=15)
* [Download Visual Studio Enterprise 2017](https://www.visualstudio.com/thank-you-downloading-visual-studio/?sku=Enterprise&rel=15)

When you install Visual Studio, select the **Desktop development with C++** workload. The Windows 10 Software Development Kit (SDK) is automatically included, and is displayed in the right-hand **Summary** pane.

For ARM/ARM64 driver development, choose **Individual components** and under **Compilers, build tools, and runtimes** select **Visual C++ compilers and libraries for ARM/ARM64**.


#### Step 2: Install WDK for Windows 10, version 1709

* [Download WDK for Windows 10, version 1709](https://go.microsoft.com/fwlink/p/?linkid=859232)

New for this release: The WDK installation will by default install the WDK Visual Studio extension. This must be done in order for integration of the WDK with Visual Studio to work.

### Enterprise WDK (EWDK) for Windows 10, version 1709

The EWDK is a standalone self-contained command-line environment for building drivers. It includes the Visual Studio Build Tools, the SDK, and the WDK.  The latest public version of the EWDK contains Visual Studio Build Tools 15.6.

#### EWDK with Visual Studio Build Tools 15.6 (Recommended)

* [Download EWDK for Windows 10, version 1709](https://developer.microsoft.com/windows/hardware/license-terms-enterprise-wdk-1709-VS15-6)

#### EWDK with Visual Studio Build Tools 15.4

* [Download EWDK for Windows 10, version 1709](https://developer.microsoft.com/windows/hardware/license-terms-enterprise-wdk-1709-VS15-4)

#### EWDK with Visual Studio Build Tools 15.2

* [Download EWDK for Windows 10, version 1709](https://developer.microsoft.com/windows/hardware/license-terms-enterprise-wdk-1709)

To get started, mount the ISO and run **LaunchBuildEnv**.


## Downloads for Windows 10, version 1703

### WDK for Windows 10, version 1703

#### Install Visual Studio 2015

> [!IMPORTANT]
> WDK for Windows 10, version 1703, is not compatible with Visual Studio 2017. Use Visual Studio 2015 for driver development with this version of the WDK.

These editions of Visual Studio 2015 support driver development.

* [Download Visual Studio Express 2015 for Desktop](https://go.microsoft.com/fwlink/?linkid=875331)
* [Download Visual Studio Community 2015](https://go.microsoft.com/fwlink/p/?LinkId=534599)
* [Download Visual Studio Professional 2015](https://go.microsoft.com/fwlink/p/?LinkId=619628)
* [Download Visual Studio Enterprise 2015](https://go.microsoft.com/fwlink/p/?LinkId=619629)

#### Install Windows SDK for Windows 10, version 1703

* [Download the Windows SDK for Windows 10, version 1703](https://go.microsoft.com/fwlink/p/?LinkID=845298)

#### Install WDK for Windows 10, version 1703

* [Download the WDK for Windows 10, version 1703](https://go.microsoft.com/fwlink/p/?LinkID=845980)

> [!IMPORTANT]
> If you install the WDK, you will not be able to develop Modern Applications.

> [!IMPORTANT]
> If you have installed WDK for Windows 10, version 1607, some WDK files get removed when installing the WDK for Windows 10, version 1703, on top of the WDK for Windows 10, version 1607. To restore these files:
> 1. On the Start menu, enter **Apps & features** in the search box, and select **Apps & features** from the results.
> 2. Find **Windows Driver Kit - Windows 10.0.15063.0** in the list of **Apps & Features**, and then select the program.
> 3. Select **Modify**, select **Repair**, and then follow the directions on the screen.
> 4. The files will be restored.

### EWDK for Windows 10, version 1703

You can also install the EWDK to build drivers and basic Win32 test applications in a command-line build environment. This environment doesn't include all the features available in Visual Studio, such as the integrated development environment (IDE), so you'll need to use a code editor of your choice.

* [Learn more about the EWDK](https://go.microsoft.com/fwlink/p/?LinkId=846040)
* [Download EWDK for Windows 10, version 1703](https://developer.microsoft.com/windows/hardware/license-terms-enterprise-wdk-1703)


## Downloads for Windows 10, version 1607

### WDK for Windows 10, version 1607

1. Run Windows Update.
2. Install the version of Visual Studio 2015 that best suits your development needs.

    * [Download Visual Studio Express 2015 for Desktop](https://go.microsoft.com/fwlink/?linkid=875331)
    * [Download Visual Studio Community 2015](https://go.microsoft.com/fwlink/p/?LinkId=534599)
    * [Download Visual Studio Professional 2015](https://go.microsoft.com/fwlink/p/?LinkId=619628)
    * [Download Visual Studio Enterprise 2015](https://go.microsoft.com/fwlink/p/?LinkId=619629)

3. During installation, select the **Typical for Windows 10 Developers** option.
4. Follow the prompts to complete the installation.
5. [Install the WDK for Windows 10, version 1607](https://go.microsoft.com/fwlink/p/?LinkId=526733)
**OR**
[Install the EWDK 1607](https://developer.microsoft.com/windows/hardware/license-terms-enterprise-wdk)


## Downloads for Windows 8.1

### WDK 8.1 Update (for Windows 8.1, 8, and 7 drivers)

WDK 8.1 Update has tools to build, test, debug, and deploy drivers for Windows 8.1 Update, Windows 8.1, Windows 8, and Windows 7. When you have the WDK, we recommend that you install the WDK 8.1 Update Test Pack. It has the tests for device fundamentals, graphics, imaging, mobile broadband (CDMA, GSM, WLAN), sensors, and other utilities.

> [!IMPORTANT]
> Before installing WDK 8.1 Update, you need to install Visual Studio 2013.

1. [Download Visual Studio 2013](https://go.microsoft.com/fwlink/?linkid=875331)
2. [Download WDK 8.1 Update](https://go.microsoft.com/fwlink/p/?LinkId=393659) (English only)
3. [Download the WDK 8.1 Update Test Pack](https://go.microsoft.com/fwlink/p/?LinkID=393660) (English only)
4. [Get driver samples for Windows 8.1](https://code.msdn.microsoft.com/windowshardware/Windows-Driver-Kit-WDK-81-cf35e953)

### WinDbg for Windows 8.1
Debugging Tools for Windows (WinDbg) are included in the WDK 8.1 Update, but you can also install them as a standalone component from the Windows 8.1 SDK. In the installation wizard, select Debugging Tools for Windows, and clear all other components.

* [Get (WinDbg) as part of Windows 8.1 SDK](https://www.microsoft.com/click/services/Redirect2.ashx?CR_EAC=300135395) (English only)

### Remote Debugging client for Windows 8.1
With the Windows Remote Debugging client, you can work remotely with developers from Microsoft, over the internet, to debug kernel-mode failures using the kernel debugger.
* [Learn more and prepare for remote debugging.](https://docs.microsoft.com/windows-hardware/drivers/debugger/remote-debugging)
* [Download the Remote Debugging client](https://go.microsoft.com/fwlink/p/?LinkId=316921) (English only)  


## Downloads for Windows 8

### WDK 8
WDK 8 enables you to migrate earlier drivers to WDK 8.1 Update and Visual Studio 2013. Microsoft does not support WDK 8 and will make no further updates to this kit. You should use the latest versions of the WDK and Visual Studio to build drivers for Windows.

> [!IMPORTANT]
> You must install [Visual Studio Professional 2012](https://go.microsoft.com/fwlink/p/?LinkID=255976) or [Visual Studio Ultimate 2012](https://go.microsoft.com/fwlink/p/?LinkID=255982) before you install WDK 8.

1. [Download WDK 8 (English only)](https://go.microsoft.com/fwlink/p/?LinkID=324284)
2. [Download the WDK 8 redistributable components](https://go.microsoft.com/fwlink/p/?LinkID=253170) (English only)
3. [Get driver samples for Windows 8](https://code.msdn.microsoft.com/windowshardware/Windows-Driver-Kit-WDK-80-e3161626)


## Downloads for Windows XP

### WDK 7.1.0 (for Windows XP drivers)
Developing a driver for Windows XP or Windows Server 2003? WDK 7.1.0 has the tools, code samples, docs, compilers, headers, and libraries that you can use to create drivers for these operating systems.

* [Download WDK 7.1.0](https://www.microsoft.com/download/confirmation.aspx?id=11800) (English only)

### Standalone debugging tools for debugging Windows XP and Windows Vista
If you're debugging Windows XP, Windows Server 2003, Windows Vista, or Windows Server 2008 (or using one of these operating systems to run Debugging Tools for Windows), you need to use the Windows 7 release of the debugging tools. It's included in the SDK for Windows 7 and .NET Framework 4.0. To install the Debugging Tools for Windows as a standalone component, in the SDK installation wizard, select Debugging Tools for Windows, and clear all other components.

> [!IMPORTANT]
> Newer versions of the Visual C++ 2010 Redistributable can cause issues when you install the SDK for Windows 7. For more information, see [support for the Windows SDK](https://support.microsoft.com/kb/2717426).

* [Get the standalone debugging tools for Windows XP as part of Windows 7 SDK](https://www.microsoft.com/download/confirmation.aspx?id=8279)


...old content ends.-->

### Related downloads
* [Download the Windows Assessment and Deployment Kit (Windows ADK)](https://developer.microsoft.com/windows/hardware/windows-assessment-deployment-kit)
* [Download the Windows HLK, HCK, or Logo Kit](https://developer.microsoft.com/windows/hardware/windows-hardware-lab-kit)
* [Download the debugging Tools for Windows (WinDbg)](https://developer.microsoft.com/windows/hardware/download-windbg)
* [Download Windows Symbol Packages](https://developer.microsoft.com/windows/hardware/download-symbols)
* [Download the WDK Insider Preview](https://www.microsoft.com/software-download/windowsinsiderpreviewWDK)
