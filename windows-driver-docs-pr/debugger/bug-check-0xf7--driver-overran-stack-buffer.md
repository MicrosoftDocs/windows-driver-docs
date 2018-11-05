---
title: Bug Check 0xF7 DRIVER_OVERRAN_STACK_BUFFER
description: The DRIVER_OVERRAN_STACK_BUFFER bug check has a value of 0x000000F7. This indicates that a driver has overrun a stack-based buffer.
ms.assetid: 5981b5e0-90c1-486e-8bbf-2778f2595f6b
keywords: ["Bug Check 0xF7 DRIVER_OVERRAN_STACK_BUFFER", "DRIVER_OVERRAN_STACK_BUFFER"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- DRIVER_OVERRAN_STACK_BUFFER
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0xF7: DRIVER\_OVERRAN\_STACK\_BUFFER


The DRIVER\_OVERRAN\_STACK\_BUFFER bug check has a value of 0x000000F7. This indicates that a driver has overrun a stack-based buffer.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

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

 

Cause
-----

A driver overran a stack-based buffer (or local variable) in a way that would have overwritten the function's return address and jumped back to an arbitrary address when the function returned.

This is the classic "buffer overrun" hacking attack. The system has been brought down to prevent a malicious user from gaining complete control of it.

Resolution
----------

Use the [**kb (Display Stack Backtrace)**](k--kb--kc--kd--kp--kp--kv--display-stack-backtrace-.md) command to get a stack trace.

The last routine on the stack before the buffer overrun handlers and bug check call is the one that overran its local variable.

 

 




