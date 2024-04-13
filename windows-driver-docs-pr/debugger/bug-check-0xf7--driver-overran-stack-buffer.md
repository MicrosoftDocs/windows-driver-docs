---
title: Bug Check 0xF7 DRIVER_OVERRAN_STACK_BUFFER
description: The DRIVER_OVERRAN_STACK_BUFFER bug check has a value of 0x000000F7. This indicates that a driver has overrun a stack-based buffer.
keywords: ["Bug Check 0xF7 DRIVER_OVERRAN_STACK_BUFFER", "DRIVER_OVERRAN_STACK_BUFFER"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- DRIVER_OVERRAN_STACK_BUFFER
api_type:
- NA
---

# Bug Check 0xF7: DRIVER\_OVERRAN\_STACK\_BUFFER


The DRIVER\_OVERRAN\_STACK\_BUFFER bug check has a value of 0x000000F7. This indicates that a driver has overrun a stack-based buffer.

> [!IMPORTANT]
> This article is for programmers. If you're a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


## DRIVER\_OVERRAN\_STACK\_BUFFER Parameters


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
<td align="left"><p>The actual security check cookie from the stack</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>The expected security check cookie</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>The bit-complement of the expected security check cookie</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>0</p></td>
</tr>
</tbody>
</table>

 

## Cause

A driver overran a stack-based buffer (or local variable) in a way that would have overwritten the function's return address and jumped back to an arbitrary address when the function returned.

This is the classic "buffer overrun" hacking attack. The system has been brought down to prevent a malicious user from gaining complete control of it.

## Resolution

Use the [**kb (Display Stack Backtrace)**](../debuggercmds/k--kb--kc--kd--kp--kp--kv--display-stack-backtrace-.md) command to get a stack trace.

The last routine on the stack before the buffer overrun handlers and bug check call is the one that overran its local variable.

 

 




