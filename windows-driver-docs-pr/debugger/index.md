---
title: Debugging Tools for Windows (WinDbg, KD, CDB, NTSD)
description: Start here for an overview of Debugging Tools for Windows. This tool set includes WinDbg and other debuggers.
ms.assetid: 938ef180-84de-442f-9b6c-1138c2fc8d5a
keywords: ["Debugging Tools for Windows", "Windows debugging", "Windows Debugger", "Kernel debugging", "Kernel debugger", "WinDbg"]
ms.date: 02/22/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Debugging Tools for Windows (WinDbg, KD, CDB, NTSD)

Start here for an overview of Debugging Tools for Windows. This tool set includes WinDbg and other debuggers.


## <span id="3_ways_to_get_Debugging_Tools_for_Windows"></span><span id="3_ways_to_get_debugging_tools_for_windows"></span><span id="3_WAYS_TO_GET_DEBUGGING_TOOLS_FOR_WINDOWS"></span>Install Debugging Tools for Windows

You can get Debugging Tools for Windows as part of a development kit or as a standalone tool set:

-   **As part of the WDK**

    Debugging Tools for Windows is included in the Windows Driver Kit (WDK). To get the WDK, see [Download the Windows Driver Kit (WDK)](../download-the-wdk.md).


-   **As part of the Windows SDK**

    Debugging Tools for Windows is included in the Windows Software Development Kit (SDK). To download the installer or an ISO image, see [Windows 10 SDK](https://developer.microsoft.com/windows/downloads/windows-10-sdk) on Windows Dev Center.


-   **As a standalone tool set**

    You can install the Debugging Tools for Windows alone, without the Windows SDK or WDK, by starting installation of the Windows SDK and then selecting only **Debugging Tools for Windows** in the list of features to install (and clearing the selection of all other features). To download the installer or an ISO image, see [Windows 10 SDK](https://developer.microsoft.com/windows/downloads/windows-10-sdk) on Windows Dev Center.


## <span id="Getting_Started_with_Windows_Debugging"></span><span id="getting_started_with_windows_debugging"></span><span id="GETTING_STARTED_WITH_WINDOWS_DEBUGGING"></span>Get started with Windows Debugging

To get started with Windows debugging, see [Getting Started with Windows Debugging](getting-started-with-windows-debugging.md).

To get started with debugging kernel-mode drivers, see [Debug Universal Drivers - Step by Step Lab (Echo Kernel-Mode)](debug-universal-drivers---step-by-step-lab--echo-kernel-mode-.md). This is a step-by-step lab that shows how to use WinDbg to debug Echo, a sample driver that uses the Kernel-Mode Driver Framework (KMDF).


## <span id="Debugging_environments"></span><span id="debugging_environments"></span><span id="DEBUGGING_ENVIRONMENTS"></span>Debugging environments

If your computer has Visual Studio and the WDK installed, then you have six available debugging environments. For descriptions of these environments, see [Debugging Environments](debuggers-in-the-debugging-tools-for-windows-package.md).

All of these debugging environments provide user interfaces for the same underlying debugging engine, which is implemented in the Windows Symbolic Debugger Engine (Dbgeng.dll). This debugging engine is also called the *Windows debugger*, and the six debugging environments are collectively called the *Windows debuggers*.

> [!NOTE]
> Visual Studio includes its own debugging environment and debugging engine, which together are called the *Visual Studio debugger*. For information on debugging in Visual Studio, see [Debugging in Visual Studio](/visualstudio/debugger/). For debugging managed code, such as C#, using the Visual Studio debugger is often the easiest way to get started.


## <span id="Windows_debuggers"></span><span id="windows_debuggers"></span><span id="WINDOWS_DEBUGGERS"></span>Windows debuggers

The Windows debuggers can run on x86-based, x64-based, or ARM-based processors, and they can debug code that is running on those same architectures. Sometimes the debugger and the code being debugged run on the same computer, but other times the debugger and the code being debugged run on separate computers. In either case, the computer that is running the debugger is called the *host computer*, and the computer that is being debugged is called the *target computer*. The Windows debuggers support the following versions of Windows for both the host and target computers.

-   Windows 10 and Windows Server 2016
-   Windows 8.1 and Windows Server 2012 R2
-   Windows 8 and Windows Server 2012
-   Windows 7 and Windows Server 2008 R2


## <span id="Symbols_and_Symbol_Files"></span><span id="symbols_and_symbol_files"></span><span id="SYMBOLS_AND_SYMBOL_FILES"></span>Symbols and symbol files

Symbol files store a variety of data that are not required when running the executable binaries, but symbol files are very useful when debugging code. For more information about creating and using symbol files, see [Symbols for Windows debugging (WinDbg, KD, CDB, NTSD)](symbols.md).


## <span id="Blue_Screens_and_crash_dump_files"></span><span id="blue_screens_and_crash_dump_files"></span><span id="BLUE_SCREENS_AND_CRASH_DUMP_FILES"></span>Blue screens and crash dump files

If Windows stops working and displays a blue screen, the computer has shut down abruptly to protect itself from data loss and displays a bug check code. For more information, see [Bug Checks (Blue Screens)](bug-checks--blue-screens-.md). You analyze crash dump files that are created when Windows shuts down by using WinDbg and other Windows debuggers. For more information, see [Crash dump analysis using the Windows debuggers (WinDbg)](crash-dump-files.md).


## <span id="Tools_and_utilities"></span><span id="tools_and_utilities"></span><span id="TOOLS_AND_UTILITIES"></span>Tools and utilities

In addition to the debuggers, Debugging Tools for Windows includes a set of tools that are useful for debugging. For a full list of the tools, see [Tools Included in Debugging Tools for Windows](extra-tools.md).


## <span id="Additional_documentation"></span><span id="additional_documentation"></span><span id="ADDITIONAL_DOCUMENTATION"></span>Additional documentation

For additional information related to Debugging Tools for Windows, see [Debugging Resources](debugging-resources.md). For information on what's new in Windows 10, see [Debugging Tools for Windows: New for Windows 10](debugging-tools-for-windows--new-for-windows-10.md).