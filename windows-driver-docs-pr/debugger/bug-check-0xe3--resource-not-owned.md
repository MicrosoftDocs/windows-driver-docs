---
title: Bug Check 0xE3 RESOURCE_NOT_OWNED
description: The RESOURCE_NOT_OWNED bug check has a value of 0x000000E3. This indicates that a thread tried to release a resource it did not own.
ms.assetid: f0f47af6-cba0-42a0-912b-562f069d5b3e
keywords: ["Bug Check 0xE3 RESOURCE_NOT_OWNED", "RESOURCE_NOT_OWNED"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- RESOURCE_NOT_OWNED
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0xE3: RESOURCE\_NOT\_OWNED


The RESOURCE\_NOT\_OWNED bug check has a value of 0x000000E3. This indicates that a thread tried to release a resource it did not own.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## RESOURCE\_NOT\_OWNED Parameters


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
<td align="left"><p>Address of resource</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>Address of thread</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>Address of owner table (if it exists)</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>Reserved</p></td>
</tr>
</tbody>
</table>

 

 

 




