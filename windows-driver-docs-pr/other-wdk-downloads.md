---
title: Previous WDK versions and other downloads
description: Install versions of the Windows Driver Kit (WDK), the Windows Debugger (WinDBG), and more.
keywords:
- Windows Driver Kit
- previous versions
- WDK
ms.date: 06/19/2025
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

Table below indicates which Visual Studio version is required for the different releases of the WDK.

## Step 2: Install the Windows SDK

The WDK requires SDK. If your development targets systems that run Windows 11, then you should mostly be fine by installing the SDK included in the Visual Studio under Desktop Development with C++ workload. The table below indicates which SDK version is required for the different releases of the WDK. As a general rule of thumb, the installed SDK version should match with the WDK version you are using.

## Step 3: Install the WDK

The WDK is integrated with Visual Studio and Debugging Tools for Windows (WinDbg). This integrated environment gives you the tools you need to develop, build, package, deploy, test, and debug drivers.

> [!NOTE]
> The WDK VSIX is now shipped as a Visual Studio individual component. The WDK VSIX is no longer available through the MSI installation process. Instead, use the Visual Studio Installer to install the WDK VSIX. This installation method is required for WDK integration in Visual Studio.
>
> Starting April 13, 2025, Microsoft no longer distributes older kits. We provide download links only for the latest version of the Windows Driver Kit. The latest published Windows Driver Kit supports driver development for Windows 10, Windows Server 2016, and later versions of each Windows variant. For details, see [Building Drivers for Previous OS Release Using the Latest WDK](https://techcommunity.microsoft.com/blog/windowsdriverdev/building-drivers-for-previous-os-releases-using-the-latest-windows-driver-kit-wd/4374910). If you need further assistance, contact [Microsoft WDK Feedback](mailto:wdkfeedback@microsoft.com).


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

Table below indicates which Visual Studio version is required for the different releases of the WDK.

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
