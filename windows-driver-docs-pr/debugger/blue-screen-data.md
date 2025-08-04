---
title: Analyze Bug Check Stop Code Error Data
description: Learn about bug checks, which provide information when Microsoft Windows encounters a condition that compromises safe system operation and the system halts.
keywords: ["Analyze Bug Check Stop Code Error Data Windows Debugging"]
ms.date: 08/23/2024
topic_type:
- apiref
ms.topic: reference
api_name:
- Analyze Bug Check Stop Code Error Data
api_type:
- NA
---

# Analyze bug check (stop code error) data

> [!NOTE]
> This article is for programmers. If you're a customer who has received a stop code error while using your computer, see [Troubleshoot stop code errors](https://support.microsoft.com/help/14238/windows-10-troubleshoot-blue-screen-errors).

> [!NOTE]
> If you're an IT professional or support agent, see [Advanced troubleshooting for stop code errors](https://support.microsoft.com/help/3106831/) for more information.

## Gather the stop code parameters

Each bug check code has four associated parameters that provide information. The parameters are described in [Bug check code reference](bug-check-code-reference2.md) for each stop code.

There are multiple ways to gather the four stop code parameters.

- Examine the Windows system log in the Event Viewer. The event properties for the bug check will list the four stop code parameters. 

- Load the generated dump file and use the [!analyze](../debuggercmds/-analyze.md) command with the debugger attached. For more information, see [Analyzing a kernel-mode dump file with WinDbg](analyzing-a-kernel-mode-dump-file-with-windbg.md).

- Attach a kernel debugger to the faulting PC. When the stop code occurs, the debugger output will include the four parameters after the stop code hex value.

    ```dbgcmd
    *******************************************************************************
    *                                                                             *
    *                        Bugcheck Analysis                                    *
    *                                                                             *
    *******************************************************************************

    Use !analyze -v to get detailed debugging information.

    BugCheck 9F, {3, ffffe000f38c06a0, fffff803c596cad0, ffffe000f46a1010}

    Implicit thread is now ffffe000`f4ca3040
    Probably caused by : hidusb.sys
    ```

### Bug check symbolic names

[DRIVER_POWER_STATE_FAILURE](bug-check-0x9f--driver-power-state-failure.md) is the bug check symbolic name, with an associated bug check code of 9F. The stop code hex value associated with the bug check symbolic name is listed in the [Bug check code reference](bug-check-code-reference2.md).

### Read bug check information from the debugger

If a debugger is attached, and debugging is enabled on the PC, a bug check will cause the target computer to break into the debugger. In this case, the stop code error might not appear immediately. The full details on this crash will be sent to the debugger and appear in the debugger window. To see this information a second time, use the [.bugcheck (Display bug check data)](../debuggercmds/-bugcheck--display-bug-check-data-.md) command or the [!analyze](../debuggercmds/-analyze.md) extension command. For information on enabling debugging see, [Getting started with WinDbg (Kernel-Mode)](getting-started-with-windbg--kernel-mode-.md).

## Kernel debugging and crash dump analysis

Kernel debugging is especially useful when other troubleshooting techniques fail, or for a recurring problem. Remember to capture the exact text in the bug check information section of the error message. To isolate a complex problem and develop a viable workaround, it's useful to record the exact actions that lead to the failure.

The [!analyze](../debuggercmds/-analyze.md) debug extension displays information about the bug check and can be helpful in determining the root cause.

You can also set a breakpoint in the code leading up to this stop code and attempt to single step forward into the faulting code.

For more information, see the following articles:

[Crash dump analysis using the Windows debuggers (WinDbg)](crash-dump-files.md)

[Analyzing a kernel-mode dump file with WinDbg](analyzing-a-kernel-mode-dump-file-with-windbg.md)

[Using the !analyze extension](using-the--analyze-extension.md) and [!analyze](../debuggercmds/-analyze.md)

[The Defrag Tools shows](/shows/defrag-tools/)

## Use Driver Verifier to gather information

It's estimated that about three quarters of stop code errors are caused by faulting drivers. Driver Verifier is a tool that runs in real time to examine the behavior of drivers. For example, Driver Verifier checks the use of memory resources, such as memory pools. If it finds errors in the execution of driver code, it proactively creates an exception to allow that part of the driver code to be further scrutinized. The driver verifier manager is built into Windows and is available on all Windows PCs. To start the driver verifier manager, enter **Verifier** at a command prompt. You can configure which drivers you would like to verify. The code that verifies drivers adds overhead as it runs, so try to verify the smallest number of drivers as possible. For more information, see [Driver Verifier](../devtest/driver-verifier.md).

## Tips for software engineers

When a bug check occurs as a result of code you've written, you should use the kernel debugger to analyze the problem, and then fix the bugs in your code. For full details, see the individual bug check code in the [Bug check code reference](bug-check-code-reference2.md) section.

However, you might also encounter bug checks that aren't caused by your own code. In this case, you probably won't be able to fix the actual cause of the problem, so your goal should be to work around the problem. If possible, isolate and remove the hardware or software component that's at fault.

Many problems can be resolved through basic troubleshooting procedures, such as verifying instructions, reinstalling key components, and verifying file dates. Also, the Event Viewer, the Sysinternals diagnostic tools, and network monitoring tools might isolate and resolve these issues.

## See also

- [Bug check code reference](bug-check-code-reference2.md)

- [Crash dump analysis using the Windows debuggers (WinDbg)](crash-dump-files.md)

- [Analyzing a kernel-mode dump file with WinDbg](analyzing-a-kernel-mode-dump-file-with-windbg.md)

- [Using the !analyze extension](using-the--analyze-extension.md) and [!analyze](../debuggercmds/-analyze.md)
