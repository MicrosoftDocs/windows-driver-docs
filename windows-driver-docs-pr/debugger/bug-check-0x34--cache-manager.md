---
title: Bug Check 0x34 CACHE_MANAGER
description: The CACHE_MANAGER bug check has a value of 0x00000034. This indicates that a problem occurred in the file system's cache manager.
keywords: ["Bug Check 0x34 CACHE_MANAGER", "CACHE_MANAGER"]
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- CACHE_MANAGER
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x34: CACHE\_MANAGER


The CACHE\_MANAGER bug check has a value of 0x00000034. This indicates that a problem occurred in the file system's cache manager.

> [!IMPORTANT]
> This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


## CACHE\_MANAGER Parameters


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
<td align="left"><p>Specifies source file and line number information. The high 16 bits (the first four hexadecimal digits after the "0x") identify the source file by its identifier number. The low 16 bits identify the source line in the file where the bug check occurred.</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>Reserved</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>Reserved</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>Reserved</p></td>
</tr>
</tbody>
</table>

 

## Cause

One possible cause of this bug check is depletion of nonpaged pool memory. If the nonpaged pool memory is completely depleted, this error can stop the system. However, during the indexing process, if the amount of available nonpaged pool memory is very low, another kernel-mode driver requiring nonpaged pool memory can also trigger this error.

## Resolution

**To resolve a nonpaged pool memory depletion problem:** Add new physical memory to the computer. This will increase the quantity of nonpaged pool memory available to the kernel.

 

 




