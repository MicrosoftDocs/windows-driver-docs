---
title: Debugging Tools for Windows
description: This page provides downloads for the Windows Debugging tools, such as WinDbg.
keywords: ["Windows Debugging Downloads", "WinDbg", "Download"]
ms.date: 04/07/2023
---

# Debugging Tools for Windows

In addition to the debuggers such as WinDbg, Debugging Tools for Windows includes a set of tools that are useful for debugging. For a complete list of the tools, see [Tools Included in Debugging Tools for Windows](extra-tools.md).

For directions on how to download and install just the Windows debugger, see [Download and install the WinDbg Windows debugger](index.md).

## Install Debugging Tools for Windows

You can get Debugging Tools for Windows as part of a development kit or as a standalone toolset:

-   **As part of the WDK**

    Debugging Tools for Windows is included in the Windows Driver Kit (WDK). To get the WDK, see [Download the Windows Driver Kit (WDK)](../download-the-wdk.md).

-   **As part of the Windows SDK**
 
    Debugging Tools for Windows is included in the Windows Software Development Kit (SDK). To download the installer or an ISO image, see [Windows SDK](https://developer.microsoft.com/windows/downloads/windows-sdk) on Windows Dev Center.

-   **As a standalone toolset**

    You can install the Debugging Tools for Windows alone, without the Windows SDK or WDK, by starting the installation of the Windows SDK and then selecting only **Debugging Tools for Windows** in the list of features to install (and clearing the selection of all other features). To download the installer or an ISO image, see [Windows SDK](https://developer.microsoft.com/windows/downloads/windows-10-sdk) on Windows Dev Center.

## Debugging environments

If your computer has Visual Studio and the WDK installed, then you have six available debugging environments. For descriptions of these environments, see [Debugging Environments](debuggers-in-the-debugging-tools-for-windows-package.md).

All of these debugging environments provide user interfaces for the same underlying debugging engine, which is implemented in the Windows Symbolic Debugger Engine (Dbgeng.dll). This debugging engine is also called the *Windows debugger*, and the six debugging environments are collectively called the *Windows debuggers*.

> [!NOTE]
> Visual Studio includes its own debugging environment and debugging engine, which together are called the *Visual Studio debugger*. For information on debugging in Visual Studio, see [Debugging in Visual Studio](/visualstudio/debugger/). For debugging managed code, such as C#, using the Visual Studio debugger is often the easiest way to get started.

## Windows debuggers

The Windows debuggers can run on x86-based, x64-based, or Arm-based processors, and they can debug code that is running on those same architectures. Sometimes the debugger and the code being debugged run on the same computer, but other times the debugger and the code being debugged run on separate computers. In either case, the computer that is running the debugger is called the *host computer*, and the computer that is being debugged is called the *target computer*. The Windows debuggers support the following versions of Windows for both the host and target computers.

## Command line debuggers

There are four command line debuggers that are available for specialized environments and for those that prefer a command line interface.

### KD and NTKD

KD and NTKD are identical in every way, except that NTKD spawns a new text window when it is started, whereas KD inherits the Command Prompt window from which it was invoked. For more information, see [Debugging Using KD and NTKD](debugging-using-kd-and-ntkd.md).

### CDB and NTSD

Also available are the Microsoft Console Debugger (CDB) and Microsoft NT Symbolic Debugger (NTSD). For more information, see [Debugging Using CDB and NTSD](debugging-using-cdb-and-ntsd.md).

## Symbols and symbol files

Symbol files store a variety of data that are not required when running the executable binaries, but symbol files are very useful when debugging code. For more information about creating and using symbol files, see [Symbols for Windows debugging](symbols.md).

## Blue screens and crash dump files

If Windows stops working and displays a blue screen, the computer has shut down abruptly to protect itself from data loss and displays a bug check code. For more information, see [Bug Checks (Blue Screens)](bug-checks--blue-screens-.md). You can analyze crash dump files that are created when Windows shuts down by using WinDbg and other Windows debuggers. For more information, see [Crash dump analysis using the Windows debuggers (WinDbg)](crash-dump-files.md).

## Looking for the debugging tools for earlier versions of Windows?

To download the debugger tools for previous versions of Windows, you need to download the Windows SDK for the version you are debugging from the
[Windows SDK and emulator archive](https://developer.microsoft.com/windows/downloads/sdk-archive). In the installation wizard of the SDK, select **Debugging Tools for Windows**, and deselect all other components.

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
