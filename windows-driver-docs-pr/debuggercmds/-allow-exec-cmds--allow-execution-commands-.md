---
title: ".allow_exec_cmds (Allow Execution Commands)"
description: "The .allow_exec_cmds command controls whether execution commands can be used."
keywords: [".allow_exec_cmds (Allow Execution Commands) Windows Debugging"]
ms.date: 09/17/2018
topic_type:
- apiref
ms.topic: reference
api_name:
- .allow_exec_cmds (Allow Execution Commands)
api_type:
- NA
---

# .allow_exec_cmds (Allow Execution Commands)

The **.allow\_exec\_cmds** command controls whether execution commands can be used.

```dbgcmd
.allow_exec_cmds 0 
.allow_exec_cmds 1 
.allow_exec_cmds 
```

## Parameters

<span id="_______0______"></span> **0**   
Prevents execution commands from being used.

<span id="_______1______"></span> **1**   
Allows execution commands to be used.

## Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>user mode and kernel mode</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>live debugging only</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>all</p></td>
</tr>
</tbody>
</table>

## Additional Information

For a complete list of execution commands, see [Controlling the Target](../debugger/controlling-the-target.md).

## Remarks

With no parameters, **.allow\_exec\_cmds** will display whether execution commands are currently permitted.

Execution commands include [**g (Go)**](g--go-.md), [**t (Trace)**](t--trace-.md), [**p (Step)**](p--step-.md), and any other command or WinDbg graphical interface action that would cause the target to execute.
