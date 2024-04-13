---
title: Bug Check 0xE3 RESOURCE_NOT_OWNED
description: The RESOURCE_NOT_OWNED bug check has a value of 0x000000E3. This indicates that a thread tried to release a resource it did not own.
keywords: ["Bug Check 0xE3 RESOURCE_NOT_OWNED", "RESOURCE_NOT_OWNED"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- RESOURCE_NOT_OWNED
api_type:
- NA
---

# Bug Check 0xE3: RESOURCE\_NOT\_OWNED


The RESOURCE\_NOT\_OWNED bug check has a value of 0x000000E3. This indicates that a thread tried to release a resource it did not own.

> [!IMPORTANT]
> This article is for programmers. If you're a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


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

 

 

 




