---
title: Bug Check 0x3B SYSTEM_SERVICE_EXCEPTION
description: The SYSTEM_SERVICE_EXCEPTION bug check has a value of 0x0000003B. This indicates that an exception happened while executing a routine that transitions from non-privileged code to privileged code.
ms.assetid: 0e2c230e-d942-4f32-ae8e-7a54aceb4c19
keywords: ["Bug Check 0x3B SYSTEM_SERVICE_EXCEPTION", "SYSTEM_SERVICE_EXCEPTION"]
ms.author: domars
ms.date: 09/12/2018
topic_type:
- apiref
api_name:
- SYSTEM_SERVICE_EXCEPTION
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x3B: SYSTEM\_SERVICE\_EXCEPTION


The SYSTEM\_SERVICE\_EXCEPTION bug check has a value of 0x0000003B. This indicates that an exception happened while executing a routine that transitions from non-privileged code to privileged code.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## SYSTEM\_SERVICE\_EXCEPTION Parameters


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
<td align="left"><p>The exception that caused the bug check. </p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>The address of the instruction that caused the bug check</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>The address of the context record for the exception that caused the bug check</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>0</p></td>
</tr>
</tbody>
</table>

 

Cause
-----

The stop code indicates that executing code had an exception and the thread that was below it, is a system thread.

The exception information returned in paramter one is listed in [NTSTATUS Values](https://msdn.microsoft.com/library/cc704588.aspx) and is also available in the ntstatus.h file located in the inc directory of the Windows Driver Kit. 

One possible exception value is 0xC0000005: STATUS\_ACCESS\_VIOLATION 

This means that a memory access violation occurred. 

The [**!analyze**](-analyze.md) debug extension displays information about the bug check and can be very helpful in determining the root cause.

For more information see the following topics:

[Crash dump analysis using the Windows debuggers (WinDbg)](crash-dump-files.md)

[Analyzing a Kernel-Mode Dump File with WinDbg](analyzing-a-kernel-mode-dump-file-with-windbg.md)

[Using the !analyze Extension](using-the--analyze-extension.md) and [!analyze](-analyze.md)


In the past, this error has been linked to excessive paged pool usage and may occur due to user-mode graphics drivers crossing over and passing bad data to the kernel code. If you suspect this is the case, use the pool options in driver verifier to gather additional information.

Resolution
----------

**To debug this problem:** Use the [**.cxr (Display Context Record)**](-cxr--display-context-record-.md) command with Parameter 3, and then use [**kb (Display Stack Backtrace)**](k--kb--kc--kd--kp--kp--kv--display-stack-backtrace-.md). You can also set a breakpoint in the code leading up to this stop code and attempt to single step forward into the faulting code.

For general troubleshooting of Windows bug check codes, follow these suggestions:

-   If you recently added hardware to the system, try removing or replacing it. Or check with the manufacturer to see if any patches are available.

-   If new device drivers or system services have been added recently, try removing or updating them. Try to determine what changed in the system that caused the new bug check code to appear.

-   Look in **Device Manager** to see if any devices are marked with the exclamation point (!). Review the events log displayed in driver properties for any faulting driver. Try updating the related driver.

-   Check the System Log in Event Viewer for additional error messages that might help pinpoint the device or driver that is causing the error. For more information, see [Open Event Viewer](https://windows.microsoft.com/windows/what-information-event-logs-event-viewer#1TC=windows-7). Look for critical errors in the system log that occurred in the same time window as the blue screen.

-   For additional general troubleshooting information, see [**Blue Screen Data**](blue-screen-data.md).

 

 




