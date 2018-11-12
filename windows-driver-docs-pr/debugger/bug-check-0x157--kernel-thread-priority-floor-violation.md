---
title: Bug Check 0x157 KERNEL_THREAD_PRIORITY_FLOOR_VIOLATION
description: The ATTEMPTED_SWITCH_FROM_DPC bug check has a value of 0x00000157. This indicates that an illegal operation was attempted on the priority floor of a particular thread.
ms.assetid: 93D15A0A-1413-47DB-91E8-DB61A3604BB1
keywords: ["Bug Check 0x157 KERNEL_THREAD_PRIORITY_FLOOR_VIOLATION", "KERNEL_THREAD_PRIORITY_FLOOR_VIOLATION"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- KERNEL_THREAD_PRIORITY_FLOOR_VIOLATION
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x157: KERNEL\_THREAD\_PRIORITY\_FLOOR\_VIOLATION


The ATTEMPTED\_SWITCH\_FROM\_DPC bug check has a value of 0x00000157. This indicates that an illegal operation was attempted on the priority floor of a particular thread.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## KERNEL\_THREAD\_PRIORITY\_FLOOR\_VIOLATION Parameters


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
<td align="left">The target priority value</td>
</tr>
<tr class="odd">
<td align="left">3</td>
<td align="left"><p>A status code indicating the nature of the violation</p>
0x1 : The priority counter for the target priority over-flowed
0x2 : The priority counter for the target priority under-flowed
0x3 : The target priority value was illegal</td>
</tr>
<tr class="even">
<td align="left">4</td>
<td align="left">Reserved</td>
</tr>
</tbody>
</table>

 

 

 




