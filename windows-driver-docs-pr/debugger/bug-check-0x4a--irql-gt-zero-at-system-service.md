---
title: Bug Check 0x4A IRQL_GT_ZERO_AT_SYSTEM_SERVICE
description: The IRQL_GT_ZERO_AT_SYSTEM_SERVICE bug check has a value of 0x0000004A. This indicates that a thread is returning to user mode from a system call when its IRQL is still above PASSIVE_LEVEL.
ms.assetid: 0da64630-d446-426a-a51f-34117fe9daa7
keywords: ["Bug Check 0x4A IRQL_GT_ZERO_AT_SYSTEM_SERVICE", "IRQL_GT_ZERO_AT_SYSTEM_SERVICE"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- IRQL_GT_ZERO_AT_SYSTEM_SERVICE
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x4A: IRQL\_GT\_ZERO\_AT\_SYSTEM\_SERVICE


The IRQL\_GT\_ZERO\_AT\_SYSTEM\_SERVICE bug check has a value of 0x0000004A. This indicates that a thread is returning to user mode from a system call when its IRQL is still above PASSIVE\_LEVEL.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## IRQL\_GT\_ZERO\_AT\_SYSTEM\_SERVICE Parameters


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
<td align="left"><p>The address of the system function (system call routine)</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>The current IRQL</p></td>
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

 

 

 




