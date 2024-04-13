---
title: Bug Check 0xD3 DRIVER_PORTION_MUST_BE_NONPAGED
description: The DRIVER_PORTION_MUST_BE_NONPAGED bug check has a value of 0x000000D3. This indicates that the system attempted to access pageable memory at a process IRQL that was too high.
keywords: ["Bug Check 0xD3 DRIVER_PORTION_MUST_BE_NONPAGED", "DRIVER_PORTION_MUST_BE_NONPAGED"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- DRIVER_PORTION_MUST_BE_NONPAGED
api_type:
- NA
---

# Bug Check 0xD3: DRIVER\_PORTION\_MUST\_BE\_NONPAGED


The DRIVER\_PORTION\_MUST\_BE\_NONPAGED bug check has a value of 0x000000D3. This indicates that the system attempted to access pageable memory at a process IRQL that was too high.

> [!IMPORTANT]
> This article is for programmers. If you're a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


## DRIVER\_PORTION\_MUST\_BE\_NONPAGED Parameters


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
<td align="left"><p>Memory referenced</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>IRQL at time of reference</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p><strong>0:</strong> Read</p>
<p><strong>1:</strong> Write</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>Address that referenced memory</p></td>
</tr>
</tbody>
</table>

 

If the driver responsible for the error can be identified, its name is printed on the blue screen and stored in memory at the location (PUNICODE\_STRING) **KiBugCheckDriver**.

## Cause

This bug check is usually caused by drivers that have incorrectly marked their own code or data as pageable.

## Resolution

To begin debugging, use a kernel debugger to get a stack trace: the [**!analyze**](../debuggercmds/-analyze.md) debug extension displays information about the bug check and can be helpful in determining the root cause, then use the [**kb (Display Stack Backtrace)**](../debuggercmds/k--kb--kc--kd--kp--kp--kv--display-stack-backtrace-.md)  command to get a stack trace.

 

 




