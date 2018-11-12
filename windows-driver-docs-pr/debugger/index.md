---
title: Debugging Tools for Windows (WinDbg, KD, CDB, NTSD)
description: Start here for an overview of Debugging Tools for Windows. This tool set includes WinDbg and other debuggers.
ms.assetid: 938ef180-84de-442f-9b6c-1138c2fc8d5a
keywords: ["Debugging Tools for Windows", "Windows debugging", "Windows Debugger", "Kernel debugging", "Kernel debugger", "WinDbg"]
ms.author: domars
ms.date: 02/22/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Debugging Tools for Windows (WinDbg, KD, CDB, NTSD)


Start here for an overview of Debugging Tools for Windows. This tool set includes WinDbg and other debuggers.

## <span id="3_ways_to_get_Debugging_Tools_for_Windows"></span><span id="3_ways_to_get_debugging_tools_for_windows"></span><span id="3_WAYS_TO_GET_DEBUGGING_TOOLS_FOR_WINDOWS"></span>3 ways to get Debugging Tools for Windows

-   **As part of the WDK**

    Debugging Tools for Windows is included in the WDK. You can [get the WDK here](https://docs.microsoft.com/windows-hardware/drivers/download-the-wdk).

   
-   **As a standalone tool set**

    If you want to download only Debugging Tools for Windows, [install the Windows SDK](https://developer.microsoft.com/windows/downloads/windows-10-sdk), and, during the installation, select the **Debugging Tools for Windows** box and clear all the other boxes.


-   **As part of the Windows SDK**

    Install the complete Windows Software Development Kit (SDK). Debugging Tools for Windows is included in the Windows SDK. You can [get the Windows SDK here](https://developer.microsoft.com/windows/downloads/windows-10-sdk).


## <span id="Getting_Started_with_Windows_Debugging"></span><span id="getting_started_with_windows_debugging"></span><span id="GETTING_STARTED_WITH_WINDOWS_DEBUGGING"></span>Getting Started with Windows Debugging


To get started with Windows debugging, see [Getting Started with Windows Debugging](getting-started-with-windows-debugging.md).

To get started with debugging kernel mode drivers, see [Debug Universal Drivers - Step by Step Lab (Echo Kernel-Mode)](debug-universal-drivers---step-by-step-lab--echo-kernel-mode-.md). This is a step by step lab that shows how to use WinDbg to debug the sample KMDF echo driver.

## <span id="Debugging_environments"></span><span id="debugging_environments"></span><span id="DEBUGGING_ENVIRONMENTS"></span>Debugging environments


After you install Visual Studio and the WDK, you'll have six available [debugging environments](debuggers-in-the-debugging-tools-for-windows-package.md). All of these debugging environments provide user interfaces for the same underlying debugging engine, which is implemented in dbgeng.dll. This debugging engine is called the *Windows debugger*, and the six debugging environments are collectively called the *Windows debuggers*.

**Note**  Visual Studio includes its own debugging environment and debugging engine, which together are called the *Visual Studio debugger*. For information on debugging in Visual Studio, see [Visual Studio debugger](https://go.microsoft.com/fwlink/p/?LinkID=238333). If you are looking to debug managed code such as C#, using the Visual Studio debugger is often the easiest way to get started.

 

## <span id="Windows_debuggers"></span><span id="windows_debuggers"></span><span id="WINDOWS_DEBUGGERS"></span>Windows debuggers


The Windows debuggers can run on x86-based, x64-based, or ARM-based processors, and they can debug code that's running on x86-based, x64-based, or ARM-based processors. Sometimes the debugger and the code being debugged run on the same computer, but other times the debugger and the code being debugged run on separate computers. In either case, the computer that's running the debugger is called the *host computer*, and the computer that is being debugged is called the *target computer*. The Windows debuggers support the following versions of Windows for both the host and target computers.

-   Windows 10 and Windows Server 2016

-   Windows 8.1 and Windows Server 2012 R2

-   Windows 8 and Windows Server 2012

-   Windows 7 and Windows Server 2008 R2

## <span id="Symbols_and_Symbol_Files"></span><span id="symbols_and_symbol_files"></span><span id="SYMBOLS_AND_SYMBOL_FILES"></span>Symbols and Symbol Files


Symbol files hold a variety of data which are not actually needed when running the binaries, but are very useful when debugging code. For more information about creating and using symbol files, see [Symbols for Windows debugging (WinDbg, KD, CDB, NTSD)](symbols.md).

## <span id="Blue_Screens_and_crash_dump_files"></span><span id="blue_screens_and_crash_dump_files"></span><span id="BLUE_SCREENS_AND_CRASH_DUMP_FILES"></span>Blue Screens and crash dump files


If Windows stops working and displays a blue screen, the computer has shut down abruptly to protect itself from data loss and displays a bug check code. For more information, see [Bug Checks (Blue Screens)](bug-checks--blue-screens-.md). You analyze crash dump files that are created when Windows shuts down by using WinDbg and other Windows debuggers. For more information, see [Crash dump analysis using the Windows debuggers (WinDbg)](crash-dump-files.md).

## <span id="Tools_and_utilities"></span><span id="tools_and_utilities"></span><span id="TOOLS_AND_UTILITIES"></span>Tools and utilities


In addition to the debuggers, Debugging Tools for Windows includes a set of tools that are useful for debugging. For a full list of the tools, see [Tools Included in Debugging Tools for Windows](extra-tools.md).

## <span id="Additional_documentation"></span><span id="additional_documentation"></span><span id="ADDITIONAL_DOCUMENTATION"></span>Additional documentation


For additional information related to Debugging Tools for Windows, see [Debugging Resources](debugging-resources.md). For information on what's new in Windows 10, see [Debugging Tools for Windows: New for Windows 10](debugging-tools-for-windows--new-for-windows-10.md).

## <span id="In_this_section"></span><span id="in_this_section"></span><span id="IN_THIS_SECTION"></span>In this section


-   [Getting Started with Windows Debugging](getting-started-with-windows-debugging.md)
-   [Debugging Resources](debugging-resources.md)
-   [Debugger Operation](debugger-operation-win8.md)
-   [Debugging Techniques](debugging-techniques.md)
-   [Symbols](symbols.md)
-   [Crash Dump Analysis](crash-dump-files.md)
-   [Bug Checks (Blue Screens)](bug-checks--blue-screens-.md)
-   [Debugger Reference](debugger-reference.md)

 

 





