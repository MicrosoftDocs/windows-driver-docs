---
title: Previous WDK versions and other downloads
description: Install versions of the Windows Driver Kit (WDK), the Windows Debugger (WinDBG), and more.
keywords:
- Windows Driver Kit
- previous versions
- WDK
ms.date: 06/16/2025
---

# Other WDK downloads

The Windows Driver Kit (WDK) is used to develop, test, and deploy Windows Drivers. This article contains information about versions of the Windows Driver Kit (WDK), Enterprise WDK (EWDK), and additional downloads for support purposes. To develop drivers, use the latest public versions of the Windows Driver Kit (WDK) and tools, available for download on [Download the Windows Driver Kit (WDK)](./download-the-wdk.md).

To use these earlier versions, you must *first* install the version of Visual Studio that is appropriate for your targeted platform.

## Runtime requirements

Starting with the Windows 11, version 22H2 release of the WDK and EWDK, the kits support:

- Visual Studio 2022 exclusively
- Building and testing kernel-mode drivers for x64 and Arm64
- Building and testing drivers for Windows 10, Windows Server 2016 and later client and server versions
- Side by side (SxS) support with previous WDK/EWDK

Multiple WDKs and EWDKs can be installed concurrently on the same computer and even be part of the same build system. You can run the Windows 11, version 24H2 WDK on Windows 7 and later.

The latest Windows 11 WDK release can be used to develop drivers for lower level client and server operating system. See [Building Driver for Previous OS Release Using the Latest Windows Driver Kits](https://techcommunity.microsoft.com/blog/windowsdriverdev/building-drivers-for-previous-os-releases-using-the-latest-windows-driver-kit-wd/4374910) for details

For links to older kits, see the table in Step 2 below.

Certain device-specific stacks such as graphics continue to have x86/ARM32 user-mode components to support x86/ARM32 apps.

Additionally, starting with Windows 11, version 22H2 release of the WDK and EWDK, WDF redistributable coinstallers are no longer supported. To learn how to work around this change, see [WDK Known Issues](./wdk-known-issues.md).

## Step 1: Install Visual Studio

The WDK requires Visual Studio. For more information about system requirements for Visual Studio, see [Visual Studio 2022 System Requirements](/visualstudio/releases/2022/system-requirements).

The following table indicates which Visual Studio version is required for the different releases of the WDK.

| Targeted versions of Windows | Editions of Visual Studio |
|--|--|
| Windows 11, version 24H2<br/>Windows 11, version 23H2<br/>Windows 11, version 22H2 | [Visual Studio Community 2022](https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=Community&rel=17) <br/> [Visual Studio Professional 2022](https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=Professional&rel=17) <br/> [Visual Studio Enterprise 2022](https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=Enterprise&rel=17) |
| Windows 11, version 21H2<br/>Windows Server 2022 <br/>Windows 10, version 2004 <br/>Windows 10, version 1903 | [Visual Studio Community 2019](https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=Community&rel=16) <br/>[Visual Studio Professional 2019](https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=Professional&rel=16) <br/>[Visual Studio Enterprise 2019](https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=Enterprise&rel=16) |
| Windows 10, version 1809 <br/>Windows 10, version 1803 <br/>Windows 10, version 1709 | [Visual Studio Community 2017](https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=Community&rel=15) <br/>[Visual Studio Professional 2017](https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=Professional&rel=15) <br/>[Visual Studio Enterprise 2017](https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=Enterprise&rel=15) |
| Windows 10, version 1703 <br/>Windows 10, version 1607 | [Visual Studio Express 2015 for Desktop](https://go.microsoft.com/fwlink/?linkid=875331) <br/>[Visual Studio Community 2015](https://go.microsoft.com/fwlink/p/?LinkId=534599) <br/>[Visual Studio Professional 2015](https://go.microsoft.com/fwlink/p/?LinkId=619628) <br/>[Visual Studio Enterprise 2015](https://go.microsoft.com/fwlink/p/?LinkId=619629) |
| Windows 8.1 Update <br/>Windows 8.1 | [Visual Studio 2013](https://go.microsoft.com/fwlink/?linkid=875331) |
| Windows 8 | [Visual Studio Professional 2012](https://go.microsoft.com/fwlink/p/?LinkID=255976) <br/>[Visual Studio Ultimate 2012](https://go.microsoft.com/fwlink/p/?LinkID=255982) |

For information on which options to select when installing Visual Studio, see [Download the Windows Driver Kit](./download-the-wdk.md).

### Install the Windows SDK to target Windows 10, versions 1607 and 1703

If your development targets systems that run Windows 10, version 1607 or Windows 10, version 1703, you should install Visual Studio 2015, and then also download and install the version of the Windows SDK for the targeted version of Windows 10, as identified in the following table.

| Targeted versions of Windows | Version of Windows SDK |
|--|--|
| Windows 10, version 1703 | [Windows SDK for Windows 10.0.15063.468](https://go.microsoft.com/fwlink/p/?LinkID=845298) |
| Windows 10, version 1607 | [Windows SDK for Windows 10.0.14393.795](https://go.microsoft.com/fwlink/p/?LinkId=838916) |
| Windows 8.1 | [Windows SDK for Windows 8.1](https://go.microsoft.com/fwlink/p/?LinkId=323507) |
| Windows 8 | [Windows SDK for Windows 8](https://go.microsoft.com/fwlink/p/?LinkId=226658) |

The Windows SDK wasn't included in Visual Studio 2015, so you must install the SDK separately. Later versions of Visual Studio include the Windows SDK.

## Step 2: Install the WDK

The WDK is integrated with Visual Studio and Debugging Tools for Windows (WinDbg). This integrated environment gives you the tools you need to develop, build, package, deploy, test, and debug drivers.

> [!NOTE]
> The WDK VSIX isn't shipped as a Visual Studio individual component. The WDK is also not available through the MSI installation process. Instead, use the Visual Studio Installer to install the WDK. This installation method is required for WDK integration in Visual Studio.
>
> Starting April 13, 2025, Microsoft no longer distributes older kits. We provide download links only for the latest version of the Windows Driver Kit. The latest published Windows Driver Kit supports driver development for Windows 10, Windows Server 2016, and later versions of each Windows variant. For details, see [Building Drivers for Previous OS Release Using the Latest WDK](https://techcommunity.microsoft.com/blog/windowsdriverdev/building-drivers-for-previous-os-releases-using-the-latest-windows-driver-kit-wd/4374910). If you need further assistance, contact [Microsoft WDK Feedback](mailto:wdkfeedback@microsoft.com).

| Released with | WDK and related downloads |
|--|--|
| Windows 11, Version 24H2 | [WDK 10.0.26100.4202](https://go.microsoft.com/fwlink/?linkid=2324617) |
| Windows 11, Version 23H2 | Permanently unavailable |
| Windows 11, version 22H2 | Permanently unavailable |
| Windows 11, version 21H2 | Permanently unavailable |
| Windows Server 2022 | Permanently unavailable |
| Windows 10, version 2004 | Permanently unavailable |
| Windows 10, version 1903 | Permanently unavailable |
| Windows 10, version 1809<br>Windows Server 2019 | Permanently unavailable |
| Windows 10, version 1607<br>Windows Server 2016 | Permanently unavailable |
| Windows 8.1 Update | WDK 8.1 Update (English only) - permanently unavailable<br/>WDK 8.1 Update Test Pack (English only) - permanently unavailable <br/>[WDK 8.1 Samples](https://go.microsoft.com/fwlink/p/?LinkId=618052)  <br/><br/>**NOTE:** You can use any WDK from Windows 10, version 1607 through Windows 11, version 21H2 to build drivers for Windows 8.1. |
| Windows 8 | [WDK 8 Samples](https://go.microsoft.com/fwlink/p/?LinkId=616509) |

> [!NOTE]
>Review [Hardware development kits for Windows 10, Version 2004 (10.0.19041.1)](https://social.msdn.microsoft.com/Forums/en-US/96c770a9-19a3-42d0-8d0e-bd200285d980/hardware-development-kits-for-windows-10-version-2004?forum=wdk), which addresses a bug with ExAllocatePoolZero.

> [!IMPORTANT]
> If you have installed the WDK for Windows 10, version 1703 on a system that had the WDK for Windows 10, version 1607 installed, some files from the earlier version of the WDK might have been removed.

To restore these files:

1. On the Start menu, enter **Apps & features** in the search box, and select **Apps & features** from the results.
1. Find **Windows Driver Kit - Windows 10.0.15063.0** in the list of **Apps & Features**, and then select the program.
1. Select **Modify**, select **Repair**, and then follow the directions on the screen.
1. The files will be restored.

## Install the EWDK

The Enterprise WDK (EWDK) is a standalone, self-contained, command-line environment for building drivers and basic Win32 test applications. It includes the Visual Studio Build Tools, the SDK, and the WDK. This environment doesn't include all the features available in Visual Studio, such as the integrated development environment (IDE).

Using the EWDK requires .NET Framework 4.7.2. For more information about which systems run this version of the framework, see [.NET Framework system requirements](/dotnet/framework/get-started/system-requirements). For links to download the .NET Framework, see [.NET Framework system requirements](/dotnet/framework/get-started/system-requirements).

For more information about the EWDK, see [Using the Enterprise WDK](./develop/using-the-enterprise-wdk.md).

| Versions of Windows | EWDK |
|--|--|
| Windows 11, version 24H2 | [Windows 11, version 24H2 (released March 14, 2025) EWDK](/legal/windows/hardware/enterprise-wdk-license-2022) |
| Windows 11, version 24H2 | [Windows 11, version 24H2 (released November 27, 2024) EWDK](/legal/windows/hardware/enterprise-wdk-license-2022) |
| Windows 11, version 24H2 | [Windows 11, version 24H2 (released November 4, 2024) EWDK](/legal/windows/hardware/enterprise-wdk-license-2022) |
| Windows 11, version 24H2 | [Windows 11, version 24H2 (released October 2024) EWDK](/legal/windows/hardware/enterprise-wdk-license-2022) |
| Windows 11, version 24H2 | [Windows 11, version 24H2 (released September 2024) EWDK](/legal/windows/hardware/enterprise-wdk-license-2022) |
| Windows 11, version 24H2 | [Windows 11, version 24H2 (released May 2024) EWDK](/legal/windows/hardware/enterprise-wdk-license-2022) |
| Windows 11, version 22H2 | [Windows 11, version 22H2 (released May 2023) EWDK](/legal/windows/hardware/enterprise-wdk-license-2022) |
| Windows 11, version 21H2 | [Windows 11, version 21H2 EWDK](/legal/windows/hardware/enterprise-wdk-license-2019-New) |
| Windows Server 2022 | [EWDK for Windows Windows Server 2022](/legal/windows/hardware/enterprise-wdk-license-2019) |
| Windows 10, version 2004 | [EWDK for Windows 10, version 2004](/legal/windows/hardware/enterprise-wdk-license-2019) |
| Windows 10, version 1903 | [EWDK for Windows 10, version 1903](/legal/windows/hardware/enterprise-wdk-license-2019) |
| Windows 10, version 1809 | [EWDK for Windows 10, version 1809](/legal/windows/hardware/enterprise-wdk-license-2017) |
| Windows 10, version 1803 | [EWDK for Windows 10, version 1803](/legal/windows/hardware/enterprise-wdk-license-2017) |
| Windows 10, version 1709 | [EWDK for Visual Studio with Build Tools 15.6](/legal/windows/hardware/enterprise-wdk-license-2017) (Recommended) <br/>[EWDK for Visual Studio with Build Tools 15.4](/legal/windows/hardware/enterprise-wdk-license-2017) <br/>[EWDK for Visual Studio with Build Tools 15.2](/legal/windows/hardware/enterprise-wdk-license-2017) |
| Windows 10, version 1703 | [EWDK for Windows 10, version 1703](/legal/windows/hardware/enterprise-wdk-license-2015) |

> [!NOTE]
> Information the user should notice even if skimmingStarting in Windows 10 version 1709, the EWDK is ISO-based. To get started, download and mount the ISO, and then run **LaunchBuildEnv**.

## Optional: Install updated test certificates for HAL extensions

To work with HAL Extensions, prepare your development system, running Windows 10, version 1709 or a later version of Windows 10. Also install the WDK or the EWDK, and then install the updated version of the **Windows OEM HAL Extension Test Cert 2017 (TEST ONLY)**, available for download as a ZIP file: [HAL_Extension_Test_Cert_2017.zip](https://go.microsoft.com/fwlink/?linkid=872294).

For more information about using this updated certificate, see [Update for "Windows OEM HAL Extension Test Cert 2017 (TEST ONLY)" test certificate](https://support.microsoft.com/help/4131991/update-for-windows-oem-hal-extension-test-cert-2017-test-only-test-cer) on Windows Support.

## Optional: Install WinDbg

WinDbg is the latest version of WinDbg with more modern visuals, faster windows, a full-fledged scripting experience, built with the extensible debugger data model front and center. Formerly known as *WinDbg Preview*, it supports Windows 10 and Windows 11.

For download links and more information about WinDbg, see [Download and install the WinDbg Windows debugger](./debugger/index.md) and [Debugging Tools for Windows](./debugger/debugger-download-tools.md).

### Related downloads

- [Download the Windows Assessment and Deployment Kit (Windows ADK)](/windows-hardware/get-started/adk-install)
- [Download the Windows HLK, HCK, or Logo Kit](/windows-hardware/test/hlk/windows-hardware-lab-kit)
- [Download the debugging Tools for Windows (WinDbg)](./debugger/debugger-download-tools.md)
- [Download Windows Symbol Packages](./debugger/debugger-download-symbols.md)
- [Download the WDK Insider Preview](https://www.microsoft.com/software-download/windowsinsiderpreviewWDK)
