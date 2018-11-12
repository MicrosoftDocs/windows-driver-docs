---
title: Bug Check 0xC7 TIMER_OR_DPC_INVALID
description: The TIMER_OR_DPC_INVALID bug check has a value of 0x000000C7. This is issued if a kernel timer or delayed procedure call (DPC) is found somewhere in memory where it is not permitted.
ms.assetid: 25a85b38-c299-4bf8-a7ed-f516adb5fcb1
keywords: ["Bug Check 0xC7 TIMER_OR_DPC_INVALID", "TIMER_OR_DPC_INVALID"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- TIMER_OR_DPC_INVALID
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0xC7: TIMER\_OR\_DPC\_INVALID


The TIMER\_OR\_DPC\_INVALID bug check has a value of 0x000000C7. This is issued if a kernel timer or delayed procedure call (DPC) is found somewhere in memory where it is not permitted.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## TIMER\_OR\_DPC\_INVALID Parameters


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
<td align="left"><p>0x0</p></td>
<td align="left"><p>Address of the timer object</p></td>
<td align="left"><p>Start of memory range being checked</p></td>
<td align="left"><p>End of memory range being checked</p></td>
<td align="left"><p>The timer object was found in a block of memory where a timer object is not permitted. .</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x1</p></td>
<td align="left"><p>Address of the DPC object</p></td>
<td align="left"><p>Start of memory range being checked</p></td>
<td align="left"><p>End of memory range being checked</p></td>
<td align="left"><p>The DPC object was found in a block of memory where a DPC object is not permitted.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x2</p></td>
<td align="left"><p>Address of the DPC routine</p></td>
<td align="left"><p>Start of memory range being checked</p></td>
<td align="left"><p>End of memory range being checked</p></td>
<td align="left"><p>The DPC routine was found in a block of memory where a DPC object is not permitted.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x3</p></td>
<td align="left"><p>Address of the DPC object</p></td>
<td align="left"><p>Processor number</p></td>
<td align="left"><p>Number of processors in the system</p></td>
<td align="left"><p>The processor number for the DPC object is not correct.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x4</p></td>
<td align="left"><p>Address of the DPC routine</p></td>
<td align="left"><p>The thread&#39;s APC disable count before the kernel calls the DPC routine</p></td>
<td align="left"><p>The thread&#39;s APC disable count after the DPC routine is called</p></td>
<td align="left"><p>The thread&#39;s APC disable count was changed during DPC routine execution.</p>
<p>The APC disable count is decremented each time a driver calls <strong>KeEnterCriticalRegion</strong>, <strong>FsRtlEnterFileSystem</strong>, or acquires a mutex.</p>
<p>The APC disable count is incremented each time a driver calls <strong>KeLeaveCriticalRegion</strong>, <strong>KeReleaseMutex</strong>, or <strong>FsRtlExitFileSystem</strong>.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x5</p></td>
<td align="left"><p>Address of the DPC routine</p></td>
<td align="left"><p>The thread&#39;s APC disable count before the kernel calls the DPC routine</p></td>
<td align="left"><p>The thread&#39;s APC disable count after the DPC routine is called</p></td>
<td align="left"><p>The thread&#39;s APC disable count was changed during the execution of timer DPC routine.</p>
<p>The APC disable count is decremented each time a driver calls <strong>KeEnterCriticalRegion</strong>, <strong>FsRtlEnterFileSystem</strong>, or acquires a mutex.</p>
<p>The APC disable count is incremented each time a driver calls <strong>KeLeaveCriticalRegion</strong>, <strong>KeReleaseMutex</strong>, or <strong>FsRtlExitFileSystem</strong>.</p></td>
</tr>
</tbody>
</table>

 

Cause
-----

This condition is usually caused by a driver failing to cancel a timer or DPC before freeing the memory where it resides.

Resolution
----------

If you are the driver writer, use the information obtained through this bug check to fix the bugs in your code.

If you are a system administrator, you should unload the driver if the problem persists.

 

 




