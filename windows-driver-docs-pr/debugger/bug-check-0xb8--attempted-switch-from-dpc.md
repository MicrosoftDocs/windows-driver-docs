---
title: Bug Check 0xB8 ATTEMPTED_SWITCH_FROM_DPC
description: The ATTEMPTED_SWITCH_FROM_DPC bug check has a value of 0x000000B8. This indicates that an illegal operation was attempted by a delayed procedure call (DPC) routine.
ms.assetid: 614b7be8-cec9-4dd9-b183-66db1790c31f
keywords: ["Bug Check 0xB8 ATTEMPTED_SWITCH_FROM_DPC", "ATTEMPTED_SWITCH_FROM_DPC"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- ATTEMPTED_SWITCH_FROM_DPC
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0xB8: ATTEMPTED\_SWITCH\_FROM\_DPC


The ATTEMPTED\_SWITCH\_FROM\_DPC bug check has a value of 0x000000B8. This indicates that an illegal operation was attempted by a delayed procedure call (DPC) routine.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## ATTEMPTED\_SWITCH\_FROM\_DPC Parameters


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
<td align="left"><p>The original thread causing the failure</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>The new thread</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>The stack address of the original thread</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>Reserved</p></td>
</tr>
</tbody>
</table>

 

Cause
-----

A wait operation, attach process, or yield was attempted from a DPC routine. This is an illegal operation.

Resolution
----------

The stack trace will lead to the code in the original DPC routine that caused the error.

 

 




