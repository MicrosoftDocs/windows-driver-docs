---
title: Bug Check 0x96 INVALID_WORK_QUEUE_ITEM
description: The INVALID_WORK_QUEUE_ITEM bug check has a value of 0x00000096. This bug check indicates that a queue entry was removed that contained a NULL pointer.
ms.assetid: 18d7d8b2-814c-4207-aac9-e3affc2ccebd
keywords: ["Bug Check 0x96 INVALID_WORK_QUEUE_ITEM", "INVALID_WORK_QUEUE_ITEM"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- INVALID_WORK_QUEUE_ITEM
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x96: INVALID\_WORK\_QUEUE\_ITEM


The INVALID\_WORK\_QUEUE\_ITEM bug check has a value of 0x00000096. This bug check indicates that a queue entry was removed that contained a **NULL** pointer.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## INVALID\_WORK\_QUEUE\_ITEM Parameters


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
<td align="left"><p>The address of the queue entry whose <strong>flink</strong> or <strong>blink</strong> field is <strong>NULL</strong>.</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>The address of the queue that is being referenced. Typically, this queue is an <strong>ExWorkerQueue</strong>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>The base address of the <strong>ExWorkerQueue</strong> array. (This address helps you determine if the queue in question is indeed an <strong>ExWorkerQueue</strong>. If the queue is an <strong>ExWorkerQueue</strong>, the offset from this parameter will isolate the queue.)</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>Assuming the queue is an <strong>ExWorkerQueue</strong>, this value is the address of the worker routine that would have been called if the work item had been valid. (You can use this address to isolate the driver that is misusing the work queue.)</p></td>
</tr>
</tbody>
</table>

 

Cause
-----

The INVALID\_WORK\_QUEUE\_ITEM bug check occurs when **KeRemoveQueue** removes a queue entry whose **flink** or **blink** field is **NULL**.

Any queue misuse can cause this error. But typically this error occurs because worker thread work items are misused.

An entry on a queue can be inserted on the list only one time. When an item is removed from a queue, its **flink** field is set to **NULL**. Then, when this item is removed the second time, this bug check occurs.

In most situations, the queue that is being referenced is an **ExWorkerQueue** (executive worker queue). To help identify the driver that caused the error, Parameter 4 displays the address of the worker routine that would have been called if this work item had been valid. However, if the queue that is being referenced is not an **ExWorkerQueue**, this parameter is not useful.

 

 




