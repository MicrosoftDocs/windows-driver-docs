---
title: Debugging OCA minidump files
description: Online Crash Analysis (OCA) is the reporting facility for Windows Error Reporting (WER) information. Your company can use OCA crash dumps to analyze customer problems.
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# Debugging OCA minidump files

Online Crash Analysis (OCA) is the reporting facility for [Windows Error Reporting (WER)](/windows/desktop/wer/windows-error-reporting) information. Your company can use OCA crash dumps to analyze customer problems.

## Analyze dump files

Dump files are a snapshot of the state of the computer (or process) at the time of the crash.

To analyze this data, a developer must use a debugger that can read user minidump files. The debugger must also have access to both the images and symbols that match the contents of the dump file. Most developers are aware of the need to use matching symbols when debugging a live crash. However, when debugging a minidump, matching images must also be available for the debugger.

Matching images must be available because minidump files store very little information; they store only some of the volatile information at the time of the crash. They do not store the basic code streams that the computer loaded into memory. Instead, to save space, the minidump file stores only the name and time stamp of the images loaded on the crashing computer.

To examine the code that was running on the crashing computer, the debugger must be given access to the same binaries that the crashing computer was running. The debugger uses the name and time stamp stored in the minidump file to uniquely match and load the binaries when the developer wants to debug the crash.

After the images and symbols are loaded in the debugger, you can analyze the state of the system at the time of the crash, including data that was saved after the crash occurred. The minidump does not, however, reproduce the steps that led to the specific failure. Finding the root cause requires analyzing the driver's source code to determine what code path may have led to the failure. Experience has shown that a large percentage of failures can be understood and addressed by analyzing dump files and source code.

## Use symbols to match executable code with source code

The best way to access matching images and symbols is to use the Microsoft symbol server. Symbols are data that enable the debugger to map the executable code back to the source code. When you build a program, the program's symbols are usually stored in symbol files. When a debugger analyzes a program, it needs to access the program's symbols.

Symbol files can include any or all of the following:

- The names and addresses of all functions.
- All data type, structure, and class definitions.
- The names, data types, and addresses of global variables.
- The names, data types, addresses, and scopes of local variables.
- The line number in the source code that corresponds to each binary instruction.

The Windows Driver Kit (WDK) includes tools that can be used to reduce the number of symbols in a symbol file. The symbol files that contain all of the source-level information are called full symbol files. The symbol files with reduced information are called stripped symbol files. For more information, see [BinPlace](../devtest/binplace.md).

Because symbol data is crucial for getting meaningful crash information from Windows Error Report (WER) data, we encourage you to submit your symbols when you submit drivers to be signed. When symbols are submitted, they are stored on a server that synchronizes symbol data with the associated WER processes. With this storage process, you can easily categorize the crashes reported in the minidump files and ultimately receive better data back from Microsoft.

Microsoft provides a symbol server on the Internet that you can use to analyze the Windows modules that are present in minidump files. The server includes stripped symbol files for Windows and a few other products. Microsoft has added the binaries for Windows XP and Windows Server 2003. You can use the Internet symbol server and the Debugging Tools for Windows to analyze minidump files.

## Integrate WER into applications

For more information on integrating WER into applications, see [Using WER](/windows/desktop/wer/using-wer).

## Related topics

[Advanced Driver Debugging \[336 KB\] \[PPT\]](https://download.microsoft.com/download/f/0/5/f05a42ce-575b-4c60-82d6-208d3754b2d6/adv-drv_debug.ppt)

[WDK and WinDbg downloads](../download-the-wdk.md)

[Driver Debugging Basics \[WinHEC 2007; 633 KB\] \[PPT\]](https://download.microsoft.com/download/a/f/d/afdfd50d-6eb9-425e-84e1-b4085a80e34e/dvr-t410_wh07.pptx)

[How to read the small memory dump file that is created by Windows if a crash occurs](https://support.microsoft.com/help/315263/how-to-read-the-small-memory-dump-file-that-is-created-by-windows-if-a)

[Resource-Definition Statements](/windows/desktop/menurc/resource-definition-statements)

[Windows Error Reporting](/windows/desktop/wer/windows-error-reporting)

[VERSIONINFO resource](/windows/desktop/menurc/versioninfo-resource)
