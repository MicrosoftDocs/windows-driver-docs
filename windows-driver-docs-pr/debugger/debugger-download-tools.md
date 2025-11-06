---
title: Debugging Tools for Windows SDK and WDK
description: Learn how to download and install Debugging Tools for Windows, including WinDbg, to debug applications and analyze crash dumps. Get started today.
keywords: ["Windows Debugging Downloads", "WinDbg", "Download"]
ms.date: 11/03/2025
ms.topic: concept-article
---

# Debugging Tools for Windows SDK and WDK

Debugging Tools for Windows is a comprehensive suite of debugging utilities that helps developers diagnose and resolve issues in Windows applications and drivers. This powerful toolset includes WinDbg, command-line debuggers, and specialized tools for analyzing crash dumps and system failures. With these tools, you can efficiently troubleshoot and fix complex software problems. For a complete list of the tools, see [Tools Included in Debugging Tools for Windows](extra-tools.md).

You can get Debugging Tools for Windows through multiple channels: as part of the Windows Driver Kit (WDK), bundled with the Windows Software Development Kit (SDK), or as a standalone installation. For directions on how to download and install just the Windows debugger, see [Download and install the WinDbg Windows debugger](index.md).

## Install Debugging Tools for Windows

You can get Debugging Tools for Windows as part of a development kit or as a standalone toolset:

- **As part of the WDK**

    Debugging Tools for Windows is included in the Windows Driver Kit (WDK). To get the WDK, see [Download the Windows Driver Kit (WDK)](../download-the-wdk.md).

- **As part of the Windows SDK**

    Debugging Tools for Windows is included in the Windows Software Development Kit (SDK). To download the installer or an ISO image, see [Windows SDK](https://developer.microsoft.com/windows/downloads/windows-sdk) on Windows Dev Center.

- **As a standalone toolset**

    You can install the Debugging Tools for Windows alone, without the Windows SDK or WDK, by starting the installation of the Windows SDK and then selecting only **Debugging Tools for Windows** in the list of features to install (and clearing the selection of all other features). To download the installer or an ISO image, see [Windows SDK](https://developer.microsoft.com/windows/downloads/windows-10-sdk) on Windows Dev Center.

## Debugging environments

If your computer has Visual Studio and the WDK installed, you have six available debugging environments. For descriptions of these environments, see [Debugging Environments](debuggers-in-the-debugging-tools-for-windows-package.md).

All of these debugging environments provide user interfaces for the same underlying debugging engine, which is implemented in the Windows Symbolic Debugger Engine (Dbgeng.dll). This debugging engine is also called the *Windows debugger*, and the six debugging environments are collectively called the *Windows debuggers*.

> [!NOTE]
> Visual Studio includes its own debugging environment and debugging engine, which together are called the *Visual Studio debugger*. For information on debugging in Visual Studio, see [Debugging in Visual Studio](/visualstudio/debugger/). For debugging managed code, such as C#, using the Visual Studio debugger is often the easiest way to get started.

## Windows debuggers

The Windows debuggers can run on x86-based, x64-based, or Arm-based processors, and they can debug code that runs on those same architectures. Sometimes the debugger and the code being debugged run on the same computer, but other times the debugger and the code being debugged run on separate computers. In either case, the computer that runs the debugger is called the *host computer*, and the computer that is being debugged is called the *target computer*. The Windows debuggers support the following versions of Windows for both the host and target computers.

## Command line debuggers

Four command line debuggers are available for specialized environments and for those who prefer a command line interface.

### KD and NTKD

KD and NTKD are identical in every way, except that NTKD spawns a new text window when it starts, whereas KD inherits the Command Prompt window from which it was invoked. For more information, see [Debugging Using KD and NTKD](debugging-using-kd-and-ntkd.md).

### CDB and NTSD

Also available are the Microsoft Console Debugger (CDB) and Microsoft NT Symbolic Debugger (NTSD). For more information, see [Debugging Using CDB and NTSD](debugging-using-cdb-and-ntsd.md).

## Symbols and symbol files

Symbol files store a variety of data that aren't required when running the executable binaries, but symbol files are very useful when debugging code. For more information about creating and using symbol files, see [Symbols for Windows debugging](symbols.md).

## Blue screens and crash dump files

If Windows stops working and displays a blue screen, the computer shuts down abruptly to protect itself from data loss and displays a bug check code. For more information, see [Bug Checks (Blue Screens)](bug-checks--blue-screens-.md). You can analyze crash dump files that Windows creates when it shuts down by using WinDbg and other Windows debuggers. For more information, see [Crash dump analysis using the Windows debuggers (WinDbg)](crash-dump-files.md).

## Looking for the debugging tools for earlier versions of Windows?

To download the debugger tools for previous versions of Windows, you need to download the Windows SDK for the version you're debugging from the [Windows SDK and emulator archive](https://developer.microsoft.com/windows/downloads/sdk-archive). In the installation wizard of the SDK, select **Debugging Tools for Windows**, and deselect all other components.

## Learn more about the debuggers

Learn more about WinDbg in [Download and install the WinDbg Windows debugger](./index.md).

To get started with Windows debugging, see [Getting Started with Windows Debugging](getting-started-with-windows-debugging.md).

For additional information related to Debugging Tools for Windows, see [Debugging Resources](debugging-resources.md).

## Looking for other downloads?

- [Download the Windows Driver Kit (WDK)](../download-the-wdk.md)
- [Windows Symbol Packages](debugger-download-symbols.md)
- [Windows Hardware Lab Kit](/windows-hardware/test/hlk/windows-hardware-lab-kit)
- [Download and install the Windows Assessment and Deployment Kit (Windows ADK)](/windows-hardware/get-started/adk-install)
- [Windows Insider - Windows Preview builds](https://insider.windows.com/)
