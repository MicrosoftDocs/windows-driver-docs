---
title: Bug Check 0xBE ATTEMPTED_WRITE_TO_READONLY_MEMORY
description: The ATTEMPTED_WRITE_TO_READONLY_MEMORY bug check has a value of 0x000000BE. This is issued if a driver attempts to write to a read-only memory segment.
ms.assetid: d6247828-09ae-4071-9b4f-917af29265bc
keywords: ["Bug Check 0xBE ATTEMPTED_WRITE_TO_READONLY_MEMORY", "ATTEMPTED_WRITE_TO_READONLY_MEMORY"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- ATTEMPTED_WRITE_TO_READONLY_MEMORY
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0xBE: ATTEMPTED\_WRITE\_TO\_READONLY\_MEMORY


The ATTEMPTED\_WRITE\_TO\_READONLY\_MEMORY bug check has a value of 0x000000BE. This is issued if a driver attempts to write to a read-only memory segment.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## ATTEMPTED\_WRITE\_TO\_READONLY\_MEMORY Parameters


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
<td align="left"><p>Virtual address of attempted write</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>PTE contents</p></td>
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

 

If the driver responsible for the error can be identified, its name is printed on the blue screen and stored in memory at the location (PUNICODE\_STRING) **KiBugCheckDriver**.


Remarks
-------

The [**!analyze**](https://docs.microsoft.com/windows-hardware/drivers/debugger/-analyze) debug extension displays information about the bug check and can be very helpful in determining the root cause.
 




