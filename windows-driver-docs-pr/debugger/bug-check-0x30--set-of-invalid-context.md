---
title: Bug Check 0x30 SET_OF_INVALID_CONTEXT
description: The SET_OF_INVALID_CONTEXT bug check has a value of 0x00000030. This indicates that the stack pointer in a trap frame had an invalid value.
keywords: ["Bug Check 0x30 SET_OF_INVALID_CONTEXT", "SET_OF_INVALID_CONTEXT"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- SET_OF_INVALID_CONTEXT
api_type:
- NA
---

# Bug Check 0x30: SET\_OF\_INVALID\_CONTEXT


The SET\_OF\_INVALID\_CONTEXT bug check has a value of 0x00000030. This indicates that the stack pointer in a trap frame had an invalid value.

> [!IMPORTANT]
> This article is for programmers. If you're a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


## SET\_OF\_INVALID\_CONTEXT Parameters


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
<td align="left"><p>The new stack pointer</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>The old stack pointer</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>The trap frame address</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>0</p></td>
</tr>
</tbody>
</table>

 

## Cause

This bug check occurs when some routine attempts to set the stack pointer in the trap frame to a lower value than the current stack pointer value.

If this error were not caught, it would cause the kernel to run with a stack pointer pointing to stack which is no longer valid.

 

 




