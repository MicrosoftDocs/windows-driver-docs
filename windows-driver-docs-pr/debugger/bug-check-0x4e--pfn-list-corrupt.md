---
title: Bug Check 0x4E PFN_LIST_CORRUPT
description: The PFN_LIST_CORRUPT bug check has a value of 0x0000004E. This indicates that the page frame number (PFN) list is corrupted.
keywords: ["Bug Check 0x4E PFN_LIST_CORRUPT", "PFN_LIST_CORRUPT"]
ms.date: 05/22/2023
topic_type:
- apiref
ms.topic: reference
api_name:
- PFN_LIST_CORRUPT
api_type:
- NA
---

# Bug Check 0x4E: PFN\_LIST\_CORRUPT

The PFN\_LIST\_CORRUPT bug check has a value of 0x0000004E. This indicates that the page frame number (PFN) list is corrupted.

> [!IMPORTANT]
> This article is for programmers. If you're a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).

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
<td align="left"><p>0x01</p></td>
<td align="left"><p>The <strong>ListHead</strong> value that was corrupted</p></td>
<td align="left"><p>The number of pages available</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>The list head was corrupted.</p></td>
</tr>
<td align="left"><p>0x02</p></td>
<td align="left"><p>The entry in the list that is being removed</p></td>
<td align="left"><p>The highest physical page number</p></td>
<td align="left"><p>The reference count of the entry being removed</p></td>
<td align="left"><p>A list entry was corrupted.</p></td>
</tr>
<td align="left"><p>0x06</p></td>
<td align="left"><p>The page frame number</p></td>
<td align="left"><p>The prototype PTE</p></td>
<td align="left"><p>The PTE contents</p></td>
<td align="left"><p>The hardware PTE and/or the prototype PTE data structures have been corrupted. This can be caused by hardware single bit errors, broken DMA transfers, etc. </p></td>
</tr>
<td align="left"><p>0x07</p></td>
<td align="left"><p>The page frame number</p></td>
<td align="left"><p>The current share count</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>A driver has unlocked a certain page more times than it locked it.</p></td>
</tr>
<td align="left"><p>0x8D</p></td>
<td align="left"><p>The page frame number whose state is inconsistent</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>The page-free list is corrupted. This error code most likely indicates a hardware issue.</p></td>
</tr>
<td align="left"><p>0x8F</p></td>
<td align="left"><p>New page number</p></td>
<td align="left"><p>Old page number</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>The free or zeroed page listhead is corrupted.</p></td>
</tr>
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

## Cause

This error is typically caused by a driver passing a bad memory descriptor list. For example, the driver might have called **MmUnlockPages** twice with the same list.

If a kernel debugger is available, examine the stack trace: the [**!analyze**](../debuggercmds/-analyze.md) debug extension displays information about the bug check and can be helpful in determining the root cause, then enter one of the [**k (Display Stack Backtrace)**](../debuggercmds/k--kb--kc--kd--kp--kp--kv--display-stack-backtrace-.md) commands to view the call stack.

## See Also

[!analyze](../debuggercmds/-analyze.md)

[Bug Check Code Reference](bug-check-code-reference2.md)
