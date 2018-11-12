---
title: Bug Check 0xAC HAL_MEMORY_ALLOCATION
description: The HAL_MEMORY_ALLOCATION bug check has a value of 0x000000AC. This bug check indicates that the hardware abstraction layer (HAL) could not obtain sufficient memory.
ms.assetid: 816e6ab5-ccec-47fb-8618-865cb5bb6cb2
keywords: ["Bug Check 0xAC HAL_MEMORY_ALLOCATION", "HAL_MEMORY_ALLOCATION"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- HAL_MEMORY_ALLOCATION
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0xAC: HAL\_MEMORY\_ALLOCATION


The HAL\_MEMORY\_ALLOCATION bug check has a value of 0x000000AC. This bug check indicates that the hardware abstraction layer (HAL) could not obtain sufficient memory.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## HAL\_MEMORY\_ALLOCATION Parameters


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
<td align="left"><p>The allocation size</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>0</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>A pointer to a string that contains the file name</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>Reserved</p></td>
</tr>
</tbody>
</table>

 

Cause
-----

The HAL could not obtain non-paged memory pool for a system critical requirement.

These critical memory allocations are made early in system initialization, and the HAL\_MEMORY\_ALLOCATION bug check is not expected. This bug check probably indicates some other critical error such as pool corruption or massive consumption.

 

 




