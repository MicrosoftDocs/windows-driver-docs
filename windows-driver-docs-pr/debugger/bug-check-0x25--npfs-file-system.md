---
title: Bug Check 0x25 NPFS_FILE_SYSTEM
description: The NPFS_FILE_SYSTEM bug check has a value of 0x00000025. This indicates that a problem occurred in the NPFS file system.
keywords: ["Bug Check 0x25 NPFS_FILE_SYSTEM", "NPFS_FILE_SYSTEM"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- NPFS_FILE_SYSTEM
api_type:
- NA
---

# Bug Check 0x25: NPFS\_FILE\_SYSTEM


The NPFS\_FILE\_SYSTEM bug check has a value of 0x00000025. This indicates that a problem occurred in the NPFS file system.

> [!IMPORTANT]
> This article is for programmers. If you're a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


## NPFS\_FILE\_SYSTEM Parameters


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

 

 




