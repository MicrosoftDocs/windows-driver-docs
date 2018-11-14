---
title: Bug Check 0xEF CRITICAL_PROCESS_DIED
description: The CRITICAL_PROCESS_DIED bug check has a value of 0x000000EF. This indicates that a critical system process died.
ms.assetid: caa18221-6128-4d77-ab61-ef3c28cfba38
keywords: ["(Developer Content) Bug Check 0xEF CRITICAL_PROCESS_DIED", "CRITICAL_PROCESS_DIED"]
ms.author: domars
ms.date: 09/17/2018
topic_type:
- apiref
api_name:
- CRITICAL_PROCESS_DIED
api_type:
- NA
ms.localizationpriority: medium
---

# (Developer Content) Bug Check 0xEF: CRITICAL\_PROCESS\_DIED

This indicates that a critical system process died. A critical process is one that forces the system to bug check if it terminates. This can happen when the state of the process is corrupted or otherwise is damaged. When this happens, as these processes are critical to the operation of Windows, a system bug check occurs as the operating system integrity is in question. 

Built in Windows critical system services include csrss.exe, wininit.exe, logonui.exe, smss.exe, services.exe, conhost.exe, and winlogon.exe. 

A developer can also create a service and set its recovery option to Restart the Computer for more information see [Set up Recovery Actions to Take Place When a Service Fails](https://docs.microsoft.com/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc753662(v=ws.11)).


**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## CRITICAL\_PROCESS\_DIED Parameters


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Parameter</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>1</p></td>
<td align="left"><p>The process object</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>If this is 0, a process died. If this is 1, a thread died.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>Reserved</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>Reserved</p></td>
</tr>
</tbody>
</table>

 

Resolution
----------

Determining the cause of this issues typically requires the use of the debugger to gather additional information. Multiple dump files should be examined to see if this stop code has similar characteristics, such as the code that is running when the stop code appears.

For more information, see [Crash dump analysis using the Windows debuggers (WinDbg)](crash-dump-files.md), [Using the !analyze Extension](using-the--analyze-extension.md) and [!analyze](-analyze.md).

In many cases a user dump is also created before the system bugchecks.  In general, when a user dump is available, it should be examined first to root cause the issue. This is because there are limitations to debugging user mode code from the kernel dump, including paged out/missing data. For more information see, [User-Mode Dump Files](user-mode-dump-files.md). 

Consider using the event log to see if there are errors that occur leading up to this stop code. If there are, these errors can be used to examine specific services or other code to investigate.

If the bug check can be reproduced at will, consider using Time Travel Tracing to record events leading up to the bug check. For more information see, [Time Travel Debugging - Overview](time-travel-debugging-overview.md).

Once information about the code in question is available,  set a breakpoint in the related code before this code is executed and single step forward through the code looking at the values of critical variables that are used to control the code flow.  Carefully examine this area of your code to look for false assumptions or other mistakes. 

Use the second parameter of the bug check to determine if a dying process or thread caused the bug check.

If it is a process, use the [!process](-process.md) command to display information on the process before and after the point of failure to look for abnormal behavior. The [Process explorer](https://docs.microsoft.com/sysinternals/downloads/process-explorer) utility  can used to gather general information about which process are running and parent child relationships.

If it is a thread, consider using the [!thread](-thread.md) command to display information about the thread. For information about threads in kernel mode, see [Changing Contexts](changing-contexts.md). 

For general information on threads and process as well as additional specifics on Windows protected, critical code such as wininit and csrss, see *Windows Internals* by Pavel Yosifovich, Mark E. Russinovich, David A. Solomon, and Alex Ionescu.



**General Troubleshooting Tips**

If you are not able to work with the debugger, these general troubleshooting tips may be helpful.

-   If you recently added hardware to the system, try removing or replacing it. Or check with the manufacturer to see if any patches are available.

-   If new device drivers or system services have been added recently, try removing or updating them. Try to determine what changed in the system that caused the new bug check code to appear.

-   Check the System Log in Event Viewer for additional error messages that might help pinpoint the device or driver that is causing the error. For more information, see [Open Event Viewer](https://windows.microsoft.com/windows/what-information-event-logs-event-viewer#1TC=windows-7). Look for critical errors in the system log that occurred in the same time window as the blue screen.

-   Check with the manufacturer to see if an updated system BIOS or firmware is available.

-   You can try running the hardware diagnostics supplied by the system manufacturer.

-   Confirm that any new hardware that is installed is compatible with the installed version of Windows. For example, you can get information about required hardware at [Windows 10 Specifications](https://www.microsoft.com/windows/windows-10-specifications).

-   Run a virus detection program. Viruses can infect all types of hard disks formatted for Windows, and resulting disk corruption can generate system bug check codes. Make sure the virus detection program checks the Master Boot Record for infections.

-   Use the System File Checker tool to repair missing or corrupted system files. The System File Checker is a utility in Windows that allows users to scan for corruptions in Windows system files and restore corrupted files. Use the following command to run the System File Checker tool (SFC.exe).

    ```console
    SFC /scannow
    ```

    For more information, see [Use the System File Checker tool to repair missing or corrupted system files](https://support.microsoft.com/kb/929833).

-   Look in **Device Manager** to see if any devices are marked with the exclamation point (!). Review the events log displayed in driver properties for any faulting driver. Try updating the related driver.

## <span id="see_also"></span>See also


[Crash dump analysis using the Windows debuggers (WinDbg)](crash-dump-files.md)

[Analyzing a Kernel-Mode Dump File with WinDbg](analyzing-a-kernel-mode-dump-file-with-windbg.md)

 

 




