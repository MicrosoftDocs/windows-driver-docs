---
title: Bug Check 0xA4 CNSS_FILE_SYSTEM_FILTER
description: The CNSS_FILE_SYSTEM_FILTER bug check has a value of 0x000000A4. This bug check indicates that a problem occurred in the CNSS file system filter.
ms.assetid: fbf04b17-424c-4b9b-beae-5327d20bf0b9
keywords: ["Bug Check 0xA4 CNSS_FILE_SYSTEM_FILTER", "CNSS_FILE_SYSTEM_FILTER"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- CNSS_FILE_SYSTEM_FILTER
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0xA4: CNSS\_FILE\_SYSTEM\_FILTER


The CNSS\_FILE\_SYSTEM\_FILTER bug check has a value of 0x000000A4. This bug check indicates that a problem occurred in the CNSS file system filter.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

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
<td align="left"><p>Specifies source file and line number information. The high 16 bits (the first four hexadecimal digits after the &quot;0x&quot;) identify the source file by its identifier number. The low 16 bits identify the source line in the file where the bug check occurred.</p></td>
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

 

Cause
-----

The CNSS\_FILE\_SYSTEM\_FILTER bug check might occur because nonpaged pool memory is full. If the nonpaged pool memory is completely full, this error can stop the system. However, during the indexing process, if the amount of available nonpaged pool memory is very low, another kernel-mode driver that requires nonpaged pool memory can also trigger this error.

Resolution
----------

**To resolve a nonpaged pool memory depletion problem:** Add new physical memory to the computer. This memory sincrease the quantity of nonpaged pool memory available to the kernel.

 

 




