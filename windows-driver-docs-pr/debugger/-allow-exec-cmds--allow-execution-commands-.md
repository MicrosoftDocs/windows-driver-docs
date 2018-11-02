---
title: .allow_exec_cmds (Allow Execution Commands)
description: The .allow_exec_cmds command controls whether execution commands can be used.
ms.assetid: c6e37cf1-42cc-4f82-9eb8-d252f0b6e196
keywords: [".allow_exec_cmds (Allow Execution Commands) Windows Debugging"]
ms.author: domars
ms.date: 09/17/2018
topic_type:
- apiref
api_name:
- .allow_exec_cmds (Allow Execution Commands)
api_type:
- NA
ms.localizationpriority: medium
---

# .allow\_exec\_cmds (Allow Execution Commands)


The **.allow\_exec\_cmds** command controls whether execution commands can be used.

```dbgcmd
.allow_exec_cmds 0 
.allow_exec_cmds 1 
.allow_exec_cmds 
```

## <span id="ddk_meta_allow_execution_commands_dbg"></span><span id="DDK_META_ALLOW_EXECUTION_COMMANDS_DBG"></span>Parameters


<span id="_______0______"></span> **0**   
Prevents execution commands from being used.

<span id="_______1______"></span> **1**   
Allows execution commands to be used.

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

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

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For a complete list of execution commands, see [Controlling the Target](controlling-the-target.md).

Remarks
-------

With no parameters, **.allow\_exec\_cmds** will display whether execution commands are currently permitted.

Execution commands include [**g (Go)**](g--go-.md), [**t (Trace)**](t--trace-.md), [**p (Step)**](p--step-.md), and any other command or WinDbg graphical interface action that would cause the target to execute.

 

 





