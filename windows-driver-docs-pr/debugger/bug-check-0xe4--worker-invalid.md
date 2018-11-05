---
title: Bug Check 0xE4 WORKER_INVALID
description: The WORKER_INVALID bug check has a value of 0x000000E4. This typically indicates that memory that should not contain an executive work item does contain such an item.
ms.assetid: 93951b77-bedf-4781-9c2b-e8df2aa8cb1c
keywords: ["Bug Check 0xE4 WORKER_INVALID", "WORKER_INVALID"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- WORKER_INVALID
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0xE4: WORKER\_INVALID


The WORKER\_INVALID bug check has a value of 0x000000E4. This indicates that memory that should not contain an executive work item does contain such an item, or that a currently active work item was queued.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## WORKER\_INVALID Parameters


Parameter 1 indicates the code position.

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
<td align="left"><p>0x0</p></td>
<td align="left"><p>Address of work item</p></td>
<td align="left"><p>Start of pool block</p></td>
<td align="left"><p>End of pool block</p></td>
<td align="left"><p>An active worker item was freed.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x1</p></td>
<td align="left"><p>Address of work item</p></td>
<td align="left"><p>Queue number</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>An active worker item was queued.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x2</p></td>
<td align="left"><p>Address of work item</p></td>
<td align="left"><p>Address of I/O worker routine</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>A queued I/O worker item was freed.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x3</p></td>
<td align="left"><p>Address of work item</p></td>
<td align="left"><p>Address of invalid object</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>An attempt was made to initialize an I/O worker item with an invalid object.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x5</p></td>
<td align="left"><p>Address of work item</p></td>
<td align="left"><p>Queue number</p></td>
<td align="left"><p>NUMA Node targeted or -1 if all NODES were searched for.</p></td>
<td align="left"><p>An attempt was made to queue a work item before Worker Queued was initialized.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x6</p></td>
<td align="left"><p>Address of work item</p></td>
<td align="left"><p>Queue number</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>Invalid queue type was provided.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x7</p></td>
<td align="left"><p>Address of work item</p></td>
<td align="left"><p>Queue number</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>An attempt was made to queue a work item with an invalid worker routine address.</p></td>
</tr>
</tbody>
</table>

 

Cause
-----

This is usually caused by a driver freeing memory which still contains an executive work item.

 

 




