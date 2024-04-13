---
title: Bug Check 0x51 REGISTRY_ERROR
description: The REGISTRY_ERROR bug check has a value of 0x00000051. This indicates that a severe registry error has occurred.
keywords: ["Bug Check 0x51 REGISTRY_ERROR", "REGISTRY_ERROR"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- REGISTRY_ERROR
api_type:
- NA
---

# Bug Check 0x51: REGISTRY\_ERROR


The REGISTRY\_ERROR bug check has a value of 0x00000051. This indicates that a severe registry error has occurred.

> [!IMPORTANT]
> This article is for programmers. If you're a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


## REGISTRY\_ERROR Parameters


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
<td align="left"><p>Reserved</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>Reserved</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>The pointer to the hive (if available)</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>If the hive is corrupt, the return code of <strong>HvCheckHive</strong> (if available)</p></td>
</tr>
</tbody>
</table>

 

## Cause

Something has gone wrong with the registry. If a kernel debugger is available, get a stack trace: the [**!analyze**](../debuggercmds/-analyze.md) debug extension displays information about the bug check and can be very helpful in determining the root cause, then enter one of the [**k (Display Stack Backtrace)**](../debuggercmds/k--kb--kc--kd--kp--kp--kv--display-stack-backtrace-.md) commands to view the call stack.

This error may indicate that the registry encountered an I/O error while trying to read one of its files. This can be caused by hardware problems or file system corruption.

It may also occur due to a failure in a refresh operation, which is used only in by the security system, and then only when resource limits are encountered.

 

 




