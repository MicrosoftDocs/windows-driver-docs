---
title: Bug Check 0x126 NETIO_INVALID_POOL_CALLER
description: The NETIO_INVALID_POOL_CALLER bug check has a value of 0x00000126. This indicates that an invalid pool request has been made to netio managed memory pool, e.g. FSB and MDL.
ms.assetid: D155D39D-0E8B-4BA5-91B4-AF8F291F7F1F
keywords: ["Bug Check 0x126 NETIO_INVALID_POOL_CALLER", "NETIO_INVALID_POOL_CALLER"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- NETIO_INVALID_POOL_CALLER
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x126: NETIO\_INVALID\_POOL\_CALLER


The NETIO\_INVALID\_POOL\_CALLER bug check has a value of 0x00000126. This indicates that an invalid pool request has been made to netio managed memory pool, e.g. FSB and MDL.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## NETIO\_INVALID\_POOL\_CALLER Parameters


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
<td align="left"><p>The subtype of the bugcheck.</p>
<p>0x1 : Invalid pool. Pool is at an invalid state.</p>
Parameter 2 - Pointer to memory block or MDL.
Parameter 3 - Pointer to page.
Parameter 4 - Pointer to CPU pool.
<p>0x2 : Invalid MDL. MDL is at an invalid state.</p>
Parameter 2 - Pointer to MDL.
Parameter 3 - Pointer to CPU pool.
Parameter 4 - Pointer to pool header.</td>
</tr>
<tr class="even">
<td align="left">2</td>
<td align="left">See parameter 1</td>
</tr>
<tr class="odd">
<td align="left">3</td>
<td align="left">See parameter 1</td>
</tr>
<tr class="even">
<td align="left">4</td>
<td align="left">See parameter 1</td>
</tr>
</tbody>
</table>

 

 

 




