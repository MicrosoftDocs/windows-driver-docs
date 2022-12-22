---
title: Bug check 0xEF CRITICAL_PROCESS_DIED
description: Learn how the CRITICAL_PROCESS_DIED bug check has a value of 0x000000EF and indicates that a critical system process died.
keywords: ["Bug Check 0xEF CRITICAL_PROCESS_DIED", "CRITICAL_PROCESS_DIED"]
ms.date: 12/16/2022
topic_type:
- apiref
api_name:
- CRITICAL_PROCESS_DIED
api_type:
- NA
---

# Bug check 0xEF: CRITICAL_PROCESS_DIED

The `CRITICAL_PROCESS_DIED` bug check has a value of 0x000000EF. This check indicates that a critical system process terminated. A critical process forces the system to bug check if the system terminates. This check happens when the state of the process is corrupted or damaged. When the corruption or damage happens, as these processes are critical to the operation of Windows, a system bug check occurs as the operating system integrity is in question.

Built-in Windows critical system services include csrss.exe, wininit.exe, logonui.exe, smss.exe, services.exe, conhost.exe, and winlogon.exe.

A developer can also create a service and set its recovery option to **Restart the Computer**. For more information, see [Set up recovery actions to take place when a service fails](/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc753662(v=ws.11)).

> [!IMPORTANT]
> This topic is for programmers. If you're a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).

## CRITICAL_PROCESS_DIED parameters

| Parameter | Description |
|---|---|
| 1 | The process object |
| 2 | If 0, a process terminated. If 1, a thread terminated. |
| 3 | Reserved |
| 4 | Reserved |

## Resolution

Determining the cause of this issue typically requires the use of the debugger to gather additional information. You should examine multiple dump files to see if this stop code has similar characteristics, such as the code that's running when the stop code appears.

For more information, see [Crash dump analysis using the Windows debuggers (WinDbg)](crash-dump-files.md), [Using the !analyze extension](using-the--analyze-extension.md) and [!analyze](-analyze.md).

In many cases, a user dump is also created before the system bug checks. In general, when a user dump is available, that dump should be examined first to find the root cause of the issue. There are limitations to debugging user mode code from the kernel dump, including paged out/missing data. For more information, see [User-Mode dump files](user-mode-dump-files.md).

Consider using the event log to see if there are errors that occur leading up to this stop code. If there are, these errors can be used to examine specific services or other code to investigate.

Once information about the code in question is available, set a breakpoint in the related code before this code is executed. From there, single-step forward through the code, looking at the values of critical variables that are used to control the code flow. Carefully examine this area of your code to look for false assumptions or other mistakes.

Use the second parameter of the bug check to determine if a dying process or thread caused the bug check.

If it's a process, use the [!process](-process.md) command to display information on the process before and after the point of failure to look for abnormal behavior. The [Process explorer](/sysinternals/downloads/process-explorer) utility can gather general information about parent child relationships and which processes are running.

If it's a thread, consider using the [!thread](-thread.md) command to display information about the thread. For information about threads in kernel mode, see [Changing Contexts](changing-contexts.md).

For general information on threads, processes, and other specifics on Windows protected critical code, such as wininit and csrss, see *Windows Internals* by Pavel Yosifovich, Mark E. Russinovich, David A. Solomon, and Alex Ionescu.

## General troubleshooting tips

If you're not able to work with the debugger, these general troubleshooting tips may be helpful.

- If you recently added hardware to the system, try removing or replacing that hardware. You can also check with the manufacturer to see if any patches are available.

- If new device drivers or system services have been added recently, try removing or updating them. Try to determine what changed in the system that caused the new bug check code to appear.

- Check the System Log in Event Viewer for other error messages that might help pinpoint the device or driver that's causing the error. For more information, see [Open Event Viewer](https://support.microsoft.com/hub/4338813/windows-help#1TC=windows-7). Look for critical errors in the system log that occurred in the same time window as the blue screen.

- Check with the manufacturer to see if an updated system BIOS or firmware is available.

- Try running the hardware diagnostics supplied by the system manufacturer.

- Confirm that any new hardware that's installed is compatible with the installed version of Windows. For example, you can get information about required hardware at [Windows 10 specifications](https://www.microsoft.com/windows/windows-10-specifications).

- Run a virus detection program. Viruses can infect all types of hard disks formatted for Windows. Resulting disk corruption can generate system bug check codes. Make sure the virus detection program checks the Master Boot Record for infections.

- Use the **System File Checker** tool to repair missing or corrupted system files. The **System File Checker** is a utility in Windows that allows users to scan for corruptions in Windows system files and restore corrupted files. Use the following command to run the **System File Checker** tool (SFC.exe).

    ```console
    SFC /scannow
    ```

    For more information, see [Use the System File Checker tool to repair missing or corrupted system files](https://support.microsoft.com/help/929833/use-the-system-file-checker-tool-to-repair-missing-or-corrupted-system).

- Look in **Device Manager** to see if any devices are marked with the exclamation point (!). Review the events log displayed in driver properties for any faulting driver. Try updating the related driver.

## See also

- [Crash dump analysis using the Windows debuggers (WinDbg)](crash-dump-files.md)

- [Analyzing a kernel-mode dump file with WinDbg](analyzing-a-kernel-mode-dump-file-with-windbg.md)
