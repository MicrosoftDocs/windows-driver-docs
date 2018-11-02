---
title: Bug Check 0xFC ATTEMPTED_EXECUTE_OF_NOEXECUTE_MEMORY
description: The ATTEMPTED_EXECUTE_OF_NOEXECUTE_MEMORY bug check has a value of 0x000000FC. This indicates that an attempt was made to execute non-executable memory.
ms.assetid: bece76bd-03ca-40fd-a69b-f6cc05d09806
keywords: ["Bug Check 0xFC ATTEMPTED_EXECUTE_OF_NOEXECUTE_MEMORY", "ATTEMPTED_EXECUTE_OF_NOEXECUTE_MEMORY"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- ATTEMPTED_EXECUTE_OF_NOEXECUTE_MEMORY
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0xFC: ATTEMPTED\_EXECUTE\_OF\_NOEXECUTE\_MEMORY


The ATTEMPTED\_EXECUTE\_OF\_NOEXECUTE\_MEMORY bug check has a value of 0x000000FC. This indicates that an attempt was made to execute non-executable memory.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## ATTEMPTED\_EXECUTE\_OF\_NOEXECUTE\_MEMORY Parameters


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
<td align="left"><p>The virtual address whose execution was attempted</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>The contents of the page table entry (PTE)</p></td>
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

 

Resolution
----------

When possible, the Unicode string of the driver name that attempted to execute non-executable memory is printed on the bug check screen and is also saved in **KiBugCheckDriver**. Otherwise, the driver in question can often be found by running a stack trace and then reviewing the current instruction pointer.

 

 




