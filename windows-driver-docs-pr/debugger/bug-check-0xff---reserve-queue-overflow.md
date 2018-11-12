---
title: Bug Check 0xFF RESERVE_QUEUE_OVERFLOW
description: The RESERVE_QUEUE_OVERFLOW bug check has a value of 0x000000FF. This indicates that an attempt was made to insert a new item into a reserve queue, causing the queue to overflow.
ms.assetid: d327ea41-c568-49f6-8b37-183533fd6261
keywords: ["Bug Check 0xFF RESERVE_QUEUE_OVERFLOW", "RESERVE_QUEUE_OVERFLOW"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- RESERVE_QUEUE_OVERFLOW
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0xFF: RESERVE\_QUEUE\_OVERFLOW


The RESERVE\_QUEUE\_OVERFLOW bug check has a value of 0x000000FF. This indicates that an attempt was made to insert a new item into a reserve queue, causing the queue to overflow.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## RESERVE\_QUEUE\_OVERFLOW Parameters


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
<td align="left"><p>The address of the reserve queue</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>The size of the reserve queue</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>0</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>0</p></td>
</tr>
</tbody>
</table>

 

 

 




