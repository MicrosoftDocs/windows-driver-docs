---
title: Bug Check 0xE9 ACTIVE_EX_WORKER_THREAD_TERMINATION
description: The ACTIVE_EX_WORKER_THREAD_TERMINATION bug check has a value of 0x000000E9. This indicates that an active executive worker thread is being terminated.
ms.assetid: dd68f07f-fab1-402c-9a81-f43722f91b69
keywords: ["Bug Check 0xE9 ACTIVE_EX_WORKER_THREAD_TERMINATION", "ACTIVE_EX_WORKER_THREAD_TERMINATION"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- ACTIVE_EX_WORKER_THREAD_TERMINATION
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0xE9: ACTIVE\_EX\_WORKER\_THREAD\_TERMINATION


The ACTIVE\_EX\_WORKER\_THREAD\_TERMINATION bug check has a value of 0x000000E9. This indicates that an active executive worker thread is being terminated.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## ACTIVE\_EX\_WORKER\_THREAD\_TERMINATION Parameters


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
<td align="left"><p>The exiting ETHREAD</p></td>
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

 

Cause
-----

An executive worker thread is being terminated without having gone through the worker thread rundown code. This is forbidden; work items queued to the **ExWorkerQueue** must not terminate their threads.

A stack trace should indicate the cause.

 

 




