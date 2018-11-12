---
title: .idle_cmd (Set Idle Command)
description: The .idle_cmd command sets the idle command. This is a command that is executed whenever control returns from the target to the debugger. 
ms.assetid: 8cfe7aa8-4e31-4e97-b61d-9e8bb1b7be61
keywords: [".idle_cmd (Set Idle Command) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- .idle_cmd (Set Idle Command)
api_type:
- NA
ms.localizationpriority: medium
---

# .idle\_cmd (Set Idle Command)


The **.idle\_cmd** command sets the *idle command*. This is a command that is executed whenever control returns from the target to the debugger. For example, when the target reaches a breakpoint, this command executes.

```dbgcmd
.idle_cmd
.idle_cmd String 
.idle_cmd /d
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______String______"></span><span id="_______string______"></span><span id="_______STRING______"></span> *String*   
Specifies the string to which the idle command should be set.

<span id="________d______"></span><span id="________D______"></span> **/d**   
Clears the idle command.

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

This command cannot be used in script files.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>user mode, kernel mode</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>live, crash dump</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>all</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

When **.idle\_cmd** is used with no parameters it displays the current idle command.

In WinDbg, idle commands are stored in workspaces.

Here is an example. The idle command is set to [**r eax**](r--registers-.md). Then, because the debugger is already idle, this command immediately executes, displaying the **eax** register:

```dbgcmd
windbg> .idle_cmd r eax 
Execute when idle: r eax
eax=003b0de8
```

 

 





