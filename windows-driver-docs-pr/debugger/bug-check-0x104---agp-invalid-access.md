---
title: Bug Check 0x104 AGP_INVALID_ACCESS
description: The AGP_INVALID_ACCESS bug check has a value of 0x00000104. This indicates that the GPU wrote to a range of Accelerated Graphics Port (AGP) memory that had not previously been committed.
ms.assetid: c1f5322e-847a-424f-b117-1714b8572a4f
keywords: ["Bug Check 0x104 AGP_INVALID_ACCESS", "AGP_INVALID_ACCESS"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- AGP_INVALID_ACCESS
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x104: AGP\_INVALID\_ACCESS


The AGP\_INVALID\_ACCESS bug check has a value of 0x00000104. This indicates that the GPU wrote to a range of Accelerated Graphics Port (AGP) memory that had not previously been committed.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## AGP\_INVALID\_ACCESS Parameters


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
<td align="left"><p>Offset (in ULONG) within the AGP verifier page to the first ULONG data that is corrupted</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>0</p></td>
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

 

Cause
-----

Typically, this bug check is caused by an unsigned or improperly tested video driver. It can also be caused by an old BIOS.

Resolution
----------

Check for display driver and computer BIOS updates.

 

 




