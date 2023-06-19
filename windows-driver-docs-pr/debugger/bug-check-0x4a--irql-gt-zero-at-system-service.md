---
title: Bug Check 0x4A IRQL_GT_ZERO_AT_SYSTEM_SERVICE
description: The IRQL_GT_ZERO_AT_SYSTEM_SERVICE bug check has a value of 0x0000004A. This indicates that a thread is returning to user mode from a system call when its IRQL is still above PASSIVE_LEVEL.
keywords: ["Bug Check 0x4A IRQL_GT_ZERO_AT_SYSTEM_SERVICE", "IRQL_GT_ZERO_AT_SYSTEM_SERVICE"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- IRQL_GT_ZERO_AT_SYSTEM_SERVICE
api_type:
- NA
---

# Bug Check 0x4A: IRQL\_GT\_ZERO\_AT\_SYSTEM\_SERVICE


The IRQL\_GT\_ZERO\_AT\_SYSTEM\_SERVICE bug check has a value of 0x0000004A. This indicates that a thread is returning to user mode from a system call when its IRQL is still above PASSIVE\_LEVEL.

> [!IMPORTANT]
> This article is for programmers. If you're a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


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


## Resolution 
The [**!analyze**](-analyze.md) debug extension displays information about the bug check and can be helpful in determining the root cause.
 

 




