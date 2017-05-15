---
title: (Developer Content) Bug Check 0xEF CRITICAL\_PROCESS\_DIED
description: The CRITICAL\_PROCESS\_DIED bug check has a value of 0x000000EF. This indicates that a critical system process died.
ms.assetid: caa18221-6128-4d77-ab61-ef3c28cfba38
keywords: ["(Developer Content) Bug Check 0xEF CRITICAL_PROCESS_DIED", "CRITICAL_PROCESS_DIED"]
topic_type:
- apiref
api_name:
- CRITICAL_PROCESS_DIED
api_type:
- NA
---

# (Developer Content) Bug Check 0xEF: CRITICAL\_PROCESS\_DIED


The CRITICAL\_PROCESS\_DIED bug check has a value of 0x000000EF. This indicates that a critical system process died.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](http://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

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
<td align="left"><p>Reserved</p></td>
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

Use the event log to see if there are higher level events that occur leading up to this stop code.

These general troubleshooting tips may be helpful.

-   If you recently added hardware to the system, try removing or replacing it. Or check with the manufacturer to see if any patches are available.

-   If new device drivers or system services have been added recently, try removing or updating them. Try to determine what changed in the system that caused the new bug check code to appear.

-   Check the System Log in Event Viewer for additional error messages that might help pinpoint the device or driver that is causing the error. For more information, see [Open Event Viewer](http://windows.microsoft.com/windows/what-information-event-logs-event-viewer#1TC=windows-7). Look for critical errors in the system log that occurred in the same time window as the blue screen.

-   Check with the manufacturer to see if an updated system BIOS or firmware is available.

-   You can try running the hardware diagnostics supplied by the system manufacturer.

-   Confirm that any new hardware that is installed is compatible with the installed version of Windows. For example, you can get information about required hardware at [Windows 10 Specifications](https://www.microsoft.com/windows/windows-10-specifications).

-   Run a virus detection program. Viruses can infect all types of hard disks formatted for Windows, and resulting disk corruption can generate system bug check codes. Make sure the virus detection program checks the Master Boot Record for infections.

-   Use the System File Checker tool to repair missing or corrupted system files. The System File Checker is a utility in Windows that allows users to scan for corruptions in Windows system files and restore corrupted files. Use the following command to run the System File Checker tool (SFC.exe).

    ```
    SFC /scannow
    ```

    For more information, see [Use the System File Checker tool to repair missing or corrupted system files](https://support.microsoft.com/kb/929833).

-   Look in **Device Manager** to see if any devices are marked with the exclamation point (!). Review the events log displayed in driver properties for any faulting driver. Try updating the related driver.

## <span id="see_also"></span>See also


[Crash dump analysis using the Windows debuggers (WinDbg)](crash-dump-files.md)

[Analyzing a Kernel-Mode Dump File with WinDbg](analyzing-a-kernel-mode-dump-file-with-windbg.md)

 

 




