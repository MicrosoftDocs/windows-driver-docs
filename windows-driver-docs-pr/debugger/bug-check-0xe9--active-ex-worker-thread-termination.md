---
title: Bug Check 0xE9 ACTIVE_EX_WORKER_THREAD_TERMINATION
description: The ACTIVE_EX_WORKER_THREAD_TERMINATION bug check has a value of 0x000000E9. This indicates that an active executive worker thread is being terminated.
keywords: ["Bug Check 0xE9 ACTIVE_EX_WORKER_THREAD_TERMINATION", "ACTIVE_EX_WORKER_THREAD_TERMINATION"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- ACTIVE_EX_WORKER_THREAD_TERMINATION
api_type:
- NA
---

# Bug Check 0xE9: ACTIVE\_EX\_WORKER\_THREAD\_TERMINATION


The ACTIVE\_EX\_WORKER\_THREAD\_TERMINATION bug check has a value of 0x000000E9. This indicates that an active executive worker thread is being terminated.

> [!IMPORTANT]
> This article is for programmers. If you're a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


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

 

## Cause

An executive worker thread is being terminated without having gone through the worker thread rundown code. This is forbidden; work items queued to the **ExWorkerQueue** must not terminate their threads.

A stack trace should indicate the cause.

 

 




