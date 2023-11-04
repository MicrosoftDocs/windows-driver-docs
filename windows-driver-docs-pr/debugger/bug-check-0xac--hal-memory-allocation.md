---
title: Bug Check 0xAC HAL_MEMORY_ALLOCATION
description: The HAL_MEMORY_ALLOCATION bug check has a value of 0x000000AC. This bug check indicates that the hardware abstraction layer (HAL) could not obtain sufficient memory.
keywords: ["Bug Check 0xAC HAL_MEMORY_ALLOCATION", "HAL_MEMORY_ALLOCATION"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- HAL_MEMORY_ALLOCATION
api_type:
- NA
---

# Bug Check 0xAC: HAL\_MEMORY\_ALLOCATION


The HAL\_MEMORY\_ALLOCATION bug check has a value of 0x000000AC. This bug check indicates that the hardware abstraction layer (HAL) could not obtain sufficient memory.

> [!IMPORTANT]
> This article is for programmers. If you're a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


## HAL\_MEMORY\_ALLOCATION Parameters


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
<td align="left"><p>The allocation size</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>0</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>A pointer to a string that contains the file name</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>Reserved</p></td>
</tr>
</tbody>
</table>

 

## Cause

The HAL could not obtain non-paged memory pool for a system critical requirement.

These critical memory allocations are made early in system initialization, and the HAL\_MEMORY\_ALLOCATION bug check is not expected. This bug check probably indicates some other critical error such as pool corruption or massive consumption.



## Resolution
The [!analyze](https://docs.microsoft.com/windows-hardware/drivers/debugger/-analyze) debug extension displays information about the bug check and can be helpful in determining the root cause.



## See Also

[Bug Check Code Reference](bug-check-code-reference2.md)




