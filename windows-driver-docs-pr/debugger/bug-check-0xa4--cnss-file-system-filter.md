---
title: Bug Check 0xA4 CNSS_FILE_SYSTEM_FILTER
description: The CNSS_FILE_SYSTEM_FILTER bug check has a value of 0x000000A4. This bug check indicates that a problem occurred in the CNSS file system filter.
keywords: ["Bug Check 0xA4 CNSS_FILE_SYSTEM_FILTER", "CNSS_FILE_SYSTEM_FILTER"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- CNSS_FILE_SYSTEM_FILTER
api_type:
- NA
---

# Bug Check 0xA4: CNSS\_FILE\_SYSTEM\_FILTER


The CNSS\_FILE\_SYSTEM\_FILTER bug check has a value of 0x000000A4. This bug check indicates that a problem occurred in the CNSS file system filter.

> [!IMPORTANT]
> This article is for programmers. If you're a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


## CNSS\_FILE\_SYSTEM\_FILTER Parameters


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

The CNSS\_FILE\_SYSTEM\_FILTER bug check might occur because nonpaged pool memory is full. If the nonpaged pool memory is completely full, this error can stop the system. However, during the indexing process, if the amount of available nonpaged pool memory is very low, another kernel-mode driver that requires nonpaged pool memory can also trigger this error.

## Resolution

**To resolve a nonpaged pool memory depletion problem:** Add new physical memory to the computer. This memory sincrease the quantity of nonpaged pool memory available to the kernel.

 ## See Also

[Bug Check Code Reference](bug-check-code-reference2.md) 

 




