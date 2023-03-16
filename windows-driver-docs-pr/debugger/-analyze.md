---
title: analyze (WinDbg)
description: Learn how the analyze extension displays the information about the current exception or the bug check.
keywords: ["analyze Windows Debugging"]
ms.date: 12/16/2022
topic_type:
- apiref
ms.topic: reference
api_name:
- analyze
api_type:
- NA
---

# !analyze (WinDbg)

The **!analyze** extension displays information about the current exception or bug check.

**User-Mode**

```dbgcmd
    !analyze [-v[0..99]] [-f | -hang]
    !analyze [-v[0..99]] -xml [-xmi] [-xcs] [-xmf OutputXmlFile]
    !analyze -c [-load KnownIssuesFile | -unload | -help ]
```

**Kernel-Mode**

```dbgcmd    
    !analyze [-v[0..99]] [-f | -hang]
    !analyze -show BugCheckCode [BugParameters]
    !analyze [-v[0..99]] -xml [-xmi] [-xcs] [-xmf OutputXmlFile]
    !analyze -c [-load KnownIssuesFile | -unload | -help ]
```

## General parameters

**-v[0..99]**   

Displays verbose output. You can display more information by specifying a number from 0 to 99. If you don't specify a number, the default value is 1. You can also specify Very Verbose (**-vv**) to display all available information.

For user mode, **-v6** displays what has been discovered globally and on each thread.

**-f**  

Generates the **!analyze** exception output. Use this parameter to see an exception analysis even when the debugger doesn't detect an exception.

**-hang**  

Generates **!analyze** hung-application output. Use this parameter when the target has experienced a bug check or exception. However, an analysis of why an application hung is more relevant to your problem. In kernel mode, **!analyze** **-hang** investigates locks that the system holds and then scans the DPC queue chain. In user mode, **!analyze** **-hang** analyzes the thread stack to determine whether any threads are blocking other threads.

Before you run this extension in user mode, consider changing the current thread to the thread that you think has stopped responding (that is, hung). You should do this change because the exception might have altered the current thread to a different one.

### Show parameter

**-show** `BugCheckCode` `[BugParameters]`  

Displays information about the bug check specified by `BugCheckCode`. `BugParameters` specifies up to four bug check parameters separated by spaces. These parameters enable you to further refine your search.

### Continue execution parameters

**-c**   

Continues execution when the debugger encounters a known issue. If the issue isn't a known issue, the debugger remains broken into the target.

You can use the **-c** option with the following subparameters. These subparameters configure the list of known issues. They don't cause execution to occur by themselves. Until you run **!analyze** **-c** **** **-load** at least one time, **!analyze** **-c** has no effect.

**-load** `KnownIssuesFile`  
Loads the specified known-issues file. `KnownIssuesFile` specifies the path and file name of this file. This file must be in XML format.

The list of known issues in the `KnownIssuesFile` file is used for all later **-c** commands until you use **-c** **-unload**, or until you use **-c** **-load** again (at which point the new data replaces the old data).

**-unload**

Unloads the current list of known issues.

**-help**

Displays help for the **!analyze** **-c** extension commands extension in the [Debugger command window](debugger-command-window.md).

### XML load option parameters

**-xml**

Generates the analysis output in XML format.

**-xmi**

Adds module information to the xml output. This option requires -xml or -xmf.

**-xcs**

Adds the context and call stack frames to the xml output. This option requires -xml or -xmf.

**-xmf** `OutputXmlFile`

Writes the analysis to the specified `OutputXmlFile` in XML format. The file will be overwritten if it already exists. No analysis output will be generated to the console or log unless the -xml option is also specified.

### DLL

ext.dll

### Additional Information

For sample analysis of a user-mode exception and of a kernel-mode stop error (that is, crash), and for more information about how **!analyze** uses the triage.ini file, see [Using the !analyze extension](using-the--analyze-extension.md).

## Remarks

In user mode, **!analyze** displays information about the current exception.

In kernel mode, **!analyze** displays information about the most recent bug check. If a bug check occurs, the **!analyze** display is automatically generated. You can use **!analyze** **-v** to show additional information. If you want to see only the basic bug check parameters, you can use the [.bugcheck (display bug check data)](-bugcheck--display-bug-check-data-.md) command.

For drivers that use User-Mode Driver Framework (UMDF) version 2.15 or later, **!analyze** provides information about UMDF verifier failures and unhandled exceptions. This functionality is available when performing live kernel-mode debugging and when analyzing a user-mode memory dump file. For UMDF driver crashes, **!analyze** attempts to identify the responsible driver.

## See also

- [Using the !analyze extension](using-the--analyze-extension.md)

- [Bug check code reference](bug-check-code-reference2.md)

- [Crash dump analysis using the Windows debuggers (WinDbg)](crash-dump-files.md)

- [Analyzing a kernel-mode dump file with WinDbg](analyzing-a-kernel-mode-dump-file-with-windbg.md)
