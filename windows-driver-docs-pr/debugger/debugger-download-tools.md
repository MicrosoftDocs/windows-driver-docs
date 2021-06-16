---
title: Download Debugging Tools for Windows - WinDbg
description: This page provides downloads for the Windows Debugging tools, such as WinDbg.
keywords: ["Windows Debugging Downloads", "WinDbg", "Download"]
ms.date: 05/01/2020
ms.localizationpriority: High
---

# Download Debugging Tools for Windows

The Windows Debugger (WinDbg) can be used to debug kernel-mode and user-mode code, analyze crash dumps, and examine the CPU registers while the code executes.

To get started with Windows debugging, see [Getting Started with Windows Debugging](getting-started-with-windows-debugging.md).

## ![Small windbg preview logo.](images/windbgx-preview-logo.png) Download WinDbg Preview

WinDbg Preview is a new version of WinDbg with more modern visuals, faster windows, and a full-fledged scripting experience. It is built with the extensible object-orientated debugger data model front and center. WinDbg Preview is using the same underlying engine as WinDbg today, so all the commands, extensions, and workflows still work as they did before.

 - Download WinDbg Preview from the Microsoft Store: [WinDbg Preview](https://www.microsoft.com/store/p/windbg/9pgjgd53tn86).

 - Learn more about installation and configuration in [WinDbg Preview - Installation](./windbg-install-preview.md).

## ![Small classic windbg preview logo.](images/windbg-classic-logo.png) Debugging Tools for Windows 10 (WinDbg)

Get Debugging Tools for Windows (WinDbg) from the SDK: [Windows 10 SDK](https://developer.microsoft.com/windows/downloads/windows-10-sdk). Use the download link on the [Windows 10 SDK](https://developer.microsoft.com/windows/downloads/windows-10-sdk) page, as the Debugging Tools for Windows are not available as part of Visual Studio.

If you just need the Debugging Tools for Windows, and not the Windows Driver Kit (WDK) for Windows 10, you can install the debugging tools as a standalone component from the Windows Software Development Kit (SDK).

In the SDK installation wizard, select **Debugging Tools for Windows**, and deselect all other components.

![sdk download options showing just the debugger box checked.](images/debugger-download-sdk.png)

### Adding the Debugging Tools for Windows if the SDK is already installed

If the Windows SDK is already installed, open **Settings**, navigate to **Apps & features**, select **Windows Software Development Kit**, and then select **Modify** to change the installation to add **Debugging Tools for Windows**.

-------------------

## Looking for the debugging tools for earlier versions of Windows?

To download the debugger tools for previous versions of Windows, you need to download the Windows SDK for the version you are debugging from the
[Windows SDK and emulator archive](https://developer.microsoft.com/windows/downloads/sdk-archive). In the installation wizard of the SDK, select **Debugging Tools for Windows**, and deselect all other components.

## Learn more about the debuggers

Learn more about WinDbg and other debuggers in [Debugging Tools for Windows (WinDbg, KD, CDB, NTSD)](./index.md).

## Looking for related downloads?

- [Download the Windows Driver Kit (WDK)](../download-the-wdk.md)

- [Windows Symbol Packages](debugger-download-symbols.md)  

- [Windows Hardware Lab Kit](/windows-hardware/test/hlk/windows-hardware-lab-kit)

- [Download and install the Windows Assessment and Deployment Kit (Windows ADK)](/windows-hardware/get-started/adk-install)

- [Windows Insider - Windows Preview builds](https://insider.windows.com/)