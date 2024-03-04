---
title: .idle_cmd (Set Idle Command)
description: The .idle_cmd command sets the idle command. This is a command that is executed whenever control returns from the target to the debugger. 
keywords: [".idle_cmd (Set Idle Command) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- .idle_cmd (Set Idle Command)
api_type:
- NA
---

# .idle\_cmd (Set Idle Command)


The **.idle\_cmd** command sets the *idle command*. This is a command that is executed whenever control returns from the target to the debugger. For example, when the target reaches a breakpoint, this command executes.

```dbgcmd
.idle_cmd
.idle_cmd String 
.idle_cmd /d
```

## Parameters


<span id="_______String______"></span><span id="_______string______"></span><span id="_______STRING______"></span> *String*   
Specifies the string to which the idle command should be set.

<span id="________d______"></span><span id="________D______"></span> **/d**   
Clears the idle command.

### Environment

This command cannot be used in script files.

|  Item  | Description          |
|--------|----------------------|
|Modes   |User mode, kernel mode|
|Targets |Live, crash dump      |
|Platforms|All                  |

 

## Remarks

When **.idle\_cmd** is used with no parameters it displays the current idle command.

In WinDbg, idle commands are stored in workspaces.

Here is an example. The idle command is set to [**r eax**](r--registers-.md). Then, because the debugger is already idle, this command immediately executes, displaying the **eax** register:

```dbgcmd
windbg> .idle_cmd r eax 
Execute when idle: r eax
eax=003b0de8
```

 

 





