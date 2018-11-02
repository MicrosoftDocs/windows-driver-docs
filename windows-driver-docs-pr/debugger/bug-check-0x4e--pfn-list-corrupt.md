---
title: Bug Check 0x4E PFN_LIST_CORRUPT
description: The PFN_LIST_CORRUPT bug check has a value of 0x0000004E. This indicates that the page frame number (PFN) list is corrupted.
ms.assetid: cf78aecb-80d3-4637-a2b5-a2511999c5e3
keywords: ["Bug Check 0x4E PFN_LIST_CORRUPT", "PFN_LIST_CORRUPT"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- PFN_LIST_CORRUPT
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x4E: PFN\_LIST\_CORRUPT


The PFN\_LIST\_CORRUPT bug check has a value of 0x0000004E. This indicates that the page frame number (PFN) list is corrupted.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## PFN\_LIST\_CORRUPT Parameters


*Parameter 1* indicates the type of violation. The meaning of the other parameters depends on the value of *Parameter 1*.

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
<th align="left">Cause of Error</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0x01</p></td>
<td align="left"><p>The <strong>ListHead</strong> value that was corrupted</p></td>
<td align="left"><p>The number of pages available</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>The list head was corrupted.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x02</p></td>
<td align="left"><p>The entry in the list that is being removed</p></td>
<td align="left"><p>The highest physical page number</p></td>
<td align="left"><p>The reference count of the entry being removed</p></td>
<td align="left"><p>A list entry was corrupted.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x07</p></td>
<td align="left"><p>The page frame number</p></td>
<td align="left"><p>The current share count</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>A driver has unlocked a certain page more times than it locked it.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x8D</p></td>
<td align="left"><p>The page frame number whose state is inconsistent</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>The page-free list is corrupted. This error code most likely indicates a hardware issue.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x8F</p></td>
<td align="left"><p>New page number</p></td>
<td align="left"><p>Old page number</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>The free or zeroed page listhead is corrupted.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x99</p></td>
<td align="left"><p>Page frame number</p></td>
<td align="left"><p>Current page state</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>A page table entry (PTE) or PFN is corrupted.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x9A</p></td>
<td align="left"><p>Page frame number</p></td>
<td align="left"><p>Current page state</p></td>
<td align="left"><p>The reference count of the entry that is being removed</p></td>
<td align="left"><p>A driver attempted to free a page that is still locked for IO.</p></td>
</tr>
</tbody>
</table>

 

Cause
-----

This error is typically caused by a driver passing a bad memory descriptor list. For example, the driver might have called **MmUnlockPages** twice with the same list.

If a kernel debugger is available, examine the stack trace: the [**!analyze**](https://docs.microsoft.com/windows-hardware/drivers/debugger/-analyze) debug extension displays information about the bug check and can be very helpful in determining the root cause, then enter one of the [**k (Display Stack Backtrace)**](https://docs.microsoft.com/windows-hardware/drivers/debugger/k--kb--kc--kd--kp--kp--kv--display-stack-backtrace-) commands to view the call stack.

 

 




