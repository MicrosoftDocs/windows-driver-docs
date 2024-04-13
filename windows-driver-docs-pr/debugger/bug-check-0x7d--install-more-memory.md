---
title: Bug Check 0x7D INSTALL_MORE_MEMORY
description: The INSTALL_MORE_MEMORY bug check has a value of 0x0000007D. This bug check indicates that there is not enough memory to start up the Microsoft Windows operating system.
keywords: ["Bug Check 0x7D INSTALL_MORE_MEMORY", "INSTALL_MORE_MEMORY"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- INSTALL_MORE_MEMORY
api_type:
- NA
---

# Bug Check 0x7D: INSTALL\_MORE\_MEMORY


The INSTALL\_MORE\_MEMORY bug check has a value of 0x0000007D. This bug check indicates that there is not enough memory to start up the Microsoft Windows operating system.

> [!IMPORTANT]
> This article is for programmers. If you're a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


## INSTALL\_MORE\_MEMORY Parameters


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
<td align="left"><p>The number of physical pages that are found</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>The lowest physical page</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>The highest physical page</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>0</p></td>
</tr>
</tbody>
</table>

 

## Cause

The Windows operating system does not have sufficient memory to complete the startup process.

## Resolution

Install more memory.

 

 




