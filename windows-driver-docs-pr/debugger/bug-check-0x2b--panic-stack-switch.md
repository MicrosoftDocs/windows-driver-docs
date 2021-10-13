---
title: Bug Check 0x2B PANIC_STACK_SWITCH
description: The PANIC_STACK_SWITCH bug check has a value of 0x0000002B. This indicates that the kernel mode stack was overrun.
keywords: ["Bug Check 0x2B PANIC_STACK_SWITCH", "PANIC_STACK_SWITCH"]
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- PANIC_STACK_SWITCH
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x2B: PANIC\_STACK\_SWITCH


The PANIC\_STACK\_SWITCH bug check has a value of 0x0000002B. This indicates that the kernel mode stack was overrun.

> [!IMPORTANT]
> This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


## PANIC\_STACK\_SWITCH Parameters


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
<td align="left"><p>The trap frame</p></td>
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

This error normally appears when a kernel-mode driver uses too much stack space. It can also appear when serious data corruption occurs in the kernel.


## Resolution
The [**!analyze**](-analyze.md) debug extension displays information about the bug check and can be helpful in determining the root cause.
 

 




