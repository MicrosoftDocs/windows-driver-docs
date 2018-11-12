---
title: Bug Check 0xD1 DRIVER_IRQL_NOT_LESS_OR_EQUAL
description: The DRIVER_IRQL_NOT_LESS_OR_EQUAL bug check has a value of 0x000000D1. This indicates that a kernel-mode driver attempted to access pageable memory at a process IRQL that was too high.
ms.assetid: 26cfd881-cc6e-4cc3-b464-e67d75700b96
keywords: ["Bug Check 0xD1 DRIVER_IRQL_NOT_LESS_OR_EQUAL", "DRIVER_IRQL_NOT_LESS_OR_EQUAL"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- DRIVER_IRQL_NOT_LESS_OR_EQUAL
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0xD1: DRIVER\_IRQL\_NOT\_LESS\_OR\_EQUAL


The DRIVER\_IRQL\_NOT\_LESS\_OR\_EQUAL bug check has a value of 0x000000D1. This indicates that a kernel-mode driver attempted to access pageable memory at a process IRQL that was too high.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## DRIVER\_IRQL\_NOT\_LESS\_OR\_EQUAL Parameters


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
<td align="left"><p>Memory referenced</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>IRQL at time of reference</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p><strong>0:</strong> Read</p>
<p><strong>1:</strong> Write</p>
<p><strong>8:</strong> Execute</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>Address that referenced memory</p></td>
</tr>
</tbody>
</table>

 

Cause
-----

A driver tried to access an address that is pageable (or that is completely invalid) while the IRQL was too high.

This bug check is usually caused by drivers that have used improper addresses.

If the first parameter has the same value as the fourth parameter, and the third parameter indicates an execute operation, this bug check was likely caused by a driver that was trying to execute code when the code itself was paged out. Possible causes for the page fault include the following:

-   The function was marked as pageable and was running at an elevated IRQL (which includes obtaining a lock).

-   The function call was made to a function in another driver, and that driver was unloaded.

-   The function was called by using a function pointer that was an invalid pointer.

Resolution
----------

The [**!analyze**](-analyze.md) debug extension displays information about the bug check and can be very helpful in determining the root cause.

For more information, see [Crash dump analysis using the Windows debuggers (WinDbg)](crash-dump-files.md)

To start, examine the stack trace using the [**k, kb, kc, kd, kp, kP, kv (Display Stack Backtrace)**](k--kb--kc--kd--kp--kp--kv--display-stack-backtrace-.md) command.

If the problem is caused by the driver that you are developing, make sure that the function that was executing at the time of the bug check is not marked as pageable or does not call any other inline functions that could be paged out.

If you are not equipped to use the Windows debugger to work on this problem, you can use some basic troubleshooting techniques.

-   Check the System Log in Event Viewer for additional error messages that might help identify the device or driver that is causing this bug check.

-   If a driver is identified in the bug check message, disable the driver or check with the manufacturer for driver updates.

-   Confirm that any new hardware that is installed is compatible with the installed version of Windows. For example, you can get information about required hardware at [Windows 10 Specifications](https://www.microsoft.com/windows/windows-10-specifications).

-   For additional general troubleshooting information, see [**Blue Screen Data**](blue-screen-data.md).

 

 




