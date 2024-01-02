---
title: Install WinDbg
description: Start here for an overview on the Windows debugger and installing WinDbg.
ms.assetid: 938ef180-84de-442f-9b6c-1138c2fc8d5a
keywords: ["Debugging Tools for Windows", "Windows debugging", "Windows Debugger", "Kernel debugging", "Kernel debugger", "WinDbg"]
ms.date: 12/20/2023
ms.topic: article
---

# Install the Windows debugger

WinDbg is a debugger that can be used to analyze crash dumps, debug live user-mode and kernel-mode code, and examine CPU registers and memory.

## :::image type="content" source="images/windbg-logo-35px.png" alt-text="WinDbg logo.":::

This latest version features a more modern user experience with an updated interface, fully fledged scripting capabilities, an extensible debugging data model, built-in Time Travel Debugging (TTD) support, and many additional features.

For more information, see [WinDbg Overview](../debuggercmds/windbg-overview.md).

> [!div class="nextstepaction"]
> [Download WinDbg](https://aka.ms/windbg/download)

Select *Install* and the debugger will download and install.

WinDbg will also periodically check for new versions in the background and autoupdate if necessary.

> [!NOTE]
> Formerly released as *WinDbg Preview* in the Microsoft Store, this version leverages the same underlying engine as *WinDbg (classic)* and supports all the same commands, extensions, and workflows.
>
> To get and stay on the latest release, install WinDbg as described on this page. *WinDbg Preview* will not receive further updates in the Microsoft Store.

### Requirements

- Supported Operating Systems:
  - Windows 11 (all versions)
  - Windows 10 Anniversary Update (version 1607) or newer
- Processor architectures:
  - x64 and ARM64

### Troubleshooting

If you encounter difficulties installing or keeping WinDbg updated, see [Troubleshoot installation issues with the App Installer file](/windows/msix/app-installer/troubleshoot-appinstaller-issues).

If you find any bugs or have a feature request, you can follow the feedback button in the ribbon to go to the [GitHub page](https://aka.ms/windbg/feedback) where you can file a new issue.

## Getting started with WinDbg

To get started with WinDbg, see [Getting Started with Windows Debugging](getting-started-with-windows-debugging.md).

To get started with debugging kernel-mode drivers, see [Debug Universal Drivers - Step by Step Lab (Echo Kernel-Mode)](debug-universal-drivers---step-by-step-lab--echo-kernel-mode-.md). This is a step-by-step lab that shows how to use WinDbg to debug Echo, a sample driver that uses the Kernel-Mode Driver Framework (KMDF).

## Previous versions and related downloads

To debug older versions of Windows, use WinDbg (classic) available with [Debugging Tools for Windows](debugger-download-tools.md).

- [Download the Windows Driver Kit (WDK)](../download-the-wdk.md)

- [Windows Symbol Packages](debugger-download-symbols.md)  

- [Windows Hardware Lab Kit](/windows-hardware/test/hlk/windows-hardware-lab-kit)

- [Download and install the Windows Assessment and Deployment Kit (Windows ADK)](/windows-hardware/get-started/adk-install)

- [Windows Insider - Windows Preview builds](https://insider.windows.com/)
