---
title: Bug Check 0x76 PROCESS_HAS_LOCKED_PAGES
description: The PROCESS_HAS_LOCKED_PAGES bug check has a value of 0x00000076. This bug check indicates that a driver failed to release locked pages after an I/O operation.
ms.assetid: 25c63e2e-6d2a-401a-b523-ffa70e9f75df
keywords: ["Bug Check 0x76 PROCESS_HAS_LOCKED_PAGES", "PROCESS_HAS_LOCKED_PAGES"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- PROCESS_HAS_LOCKED_PAGES
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x76: PROCESS\_HAS\_LOCKED\_PAGES


The PROCESS\_HAS\_LOCKED\_PAGES bug check has a value of 0x00000076. This bug check indicates that a driver failed to release locked pages after an I/O operation, or that it attempted to unlock pages that were already unlocked.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## PROCESS\_HAS\_LOCKED\_PAGES Parameters


<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Parameter 1</th>
<th align="left">Parameter 2</th>
<th align="left">Parameter 3</th>
<th align="left">Parameter 4</th>
<th align="left">Cause of error</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0x00</p></td>
<td align="left"><p>The pointer to the process object</p></td>
<td align="left"><p>The number of locked pages</p></td>
<td align="left"><p>The pointer to driver stacks (if they are enabled). Otherwise, this parameter is zero.</p></td>
<td align="left"><p>The process being terminated has locked memory pages. The driver must unlock any memory that it might have locked in a process, before the process terminates.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x01</p></td>
<td align="left"><p>MDL specified by the driver</p></td>
<td align="left"><p>Current number of locked memory pages in that process</p></td>
<td align="left"><p>A pointer to driver stacks for that process (if they are enabled). Otherwise, this parameter is zero.</p></td>
<td align="left"><p>The driver is attempting to unlock process memory pages that are not locked.</p></td>
</tr>
</tbody>
</table>

 

Cause
-----

The driver either failed to unlock pages that it locked (parameter 1 value is 0x0), or the driver is attempting to unlock pages that have not been locked or that have already been unlocked (parameter 1 value is 0x1).

Resolution
----------

**If the parameter 1 value is 0x0**

First use the [**!search**](-search.md) extension on the current process pointer throughout all of physical memory. This extension might find at least one memory descriptor list (MDL) that points to the current process. Next, use **!search** on each MDL that you find to obtain the I/O request packet (IRP) that points to the current process. From this IRP, you can identify which driver is leaking the pages.

Otherwise, you can detect which driver caused the error by editing the registry:

1.  In the **\\\\HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management** registry key, create or edit the **TrackLockedPages** value, and then set it equal to DWORD 1.

2.  Restart the computer.

The system then saves stack traces, so you can easily identify the driver that caused the problem. If the driver causes the same error again, [**bug check 0xCB**](bug-check-0xcb--driver-left-locked-pages-in-process.md) (DRIVER\_LEFT\_LOCKED\_PAGES\_IN\_PROCESS) is issued, and the name of the driver that causes this error is displayed on the blue screen and stored in memory at the location (PUNICODE\_STRING) **KiBugCheckDriver**.

**If the parameter 1 value is 0x1**

Examine the driver source code that locks and unlocks memory, and try to locate an instance where memory is unlocked without first being locked.

 

 




