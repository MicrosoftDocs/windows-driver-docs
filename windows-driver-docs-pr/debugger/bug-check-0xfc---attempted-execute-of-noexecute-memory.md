---
title: Bug Check 0xFC ATTEMPTED_EXECUTE_OF_NOEXECUTE_MEMORY
description: The ATTEMPTED_EXECUTE_OF_NOEXECUTE_MEMORY bug check has a value of 0x000000FC. This indicates that an attempt was made to execute non-executable memory.
keywords: ["Bug Check 0xFC ATTEMPTED_EXECUTE_OF_NOEXECUTE_MEMORY", "ATTEMPTED_EXECUTE_OF_NOEXECUTE_MEMORY"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- ATTEMPTED_EXECUTE_OF_NOEXECUTE_MEMORY
api_type:
- NA
---

# Bug Check 0xFC: ATTEMPTED\_EXECUTE\_OF\_NOEXECUTE\_MEMORY


The ATTEMPTED\_EXECUTE\_OF\_NOEXECUTE\_MEMORY bug check has a value of 0x000000FC. This indicates that an attempt was made to execute non-executable memory.

> [!IMPORTANT]
> This article is for programmers. If you're a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


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

 

## Resolution

The [**!analyze**](../debuggercmds/-analyze.md) debug extension displays information about the bug check and can be helpful in determining the root cause.
When possible, the Unicode string of the driver name that attempted to execute non-executable memory is printed on the bug check screen and is also saved in **KiBugCheckDriver**. Otherwise, the driver in question can often be found by running a stack trace and then reviewing the current instruction pointer.

 

 




