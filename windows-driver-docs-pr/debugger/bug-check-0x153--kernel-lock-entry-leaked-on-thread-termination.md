---
title: Bug Check 0x153 KERNEL_LOCK_ENTRY_LEAKED_ON_THREAD_TERMINATION
description: The KERNEL_LOCK_ENTRY_LEAKED_ON_THREAD_TERMINATION bug check has a value of 0x00000153. This indicates that a thread was terminated before it had freed all its AutoBoost lock entries.
ms.assetid: 0837C084-DAB8-4064-903D-10CD5CDE65E5
keywords: ["Bug Check 0x153 KERNEL_LOCK_ENTRY_LEAKED_ON_THREAD_TERMINATION", "KERNEL_LOCK_ENTRY_LEAKED_ON_THREAD_TERMINATION"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- KERNEL_LOCK_ENTRY_LEAKED_ON_THREAD_TERMINATION
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x153: KERNEL\_LOCK\_ENTRY\_LEAKED\_ON\_THREAD\_TERMINATION


The KERNEL\_LOCK\_ENTRY\_LEAKED\_ON\_THREAD\_TERMINATION bug check has a value of 0x00000153. This indicates that a thread was terminated before it had freed all its AutoBoost lock entries.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## KERNEL\_LOCK\_ENTRY\_LEAKED\_ON\_THREAD\_TERMINATION Parameters


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
<td align="left">1</td>
<td align="left">The address of the thread</td>
</tr>
<tr class="even">
<td align="left">2</td>
<td align="left">The address of the entry that was not freed</td>
</tr>
<tr class="odd">
<td align="left">3</td>
<td align="left"><p>A status code indicating the state of the entry</p>
<p>0x1 : Lock pointer was not NULL</p>
<p>0x2 : Thread pointer reserved bits were set</p>
<p>0x3 : Thread pointer was corrupted</p>
<p>0x4 : The entry had residual IO or CPU boosts left</p></td>
</tr>
<tr class="even">
<td align="left">4</td>
<td align="left">Reserved</td>
</tr>
</tbody>
</table>

 

Cause
-----

This is typically caused when a thread never released a lock it previously acquired (e.g. by relying on another thread to release it), or if the thread did not supply a consistent set of flags to lock package APIs.

 

 




