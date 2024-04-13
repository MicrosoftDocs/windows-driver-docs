---
title: ".push (Save Debugger State)"
description: "The .push command saves the current state of the debugger."
keywords: [".push (Save Debugger State) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- .push (Save Debugger State)
api_type:
- NA
---

# .push (Save Debugger State)

The **.push** command saves the current state of the debugger.

```dbgcmd
.push
.push /r
.push /r /q
```

## Parameters

<span id="________r______"></span><span id="________R______"></span> **/r**   
Specifies that the current values in the pseudo-registers **$t0** to **$t19** should be saved. If the **/r** parameter is not used, these values are not saved by the **.push** command.

<span id="________q______"></span><span id="________Q______"></span> **/q**   
Specifies that the command executes quietly. That is, the command executes without displaying any output.

## Environment

|  Item  | Description          |
|--------|----------------------|
|Modes   |User mode, kernel mode|
|Targets |Live, crash dump      |
|Platforms|All                  |

## Remarks

This command is most useful when used with [scripts](using-script-files.md) and [debugger command programs](../debugger/using-debugger-command-programs.md) so that they can work with one fixed state. To restore the debugger to a state that was previously saved using this command, use the [**.pop (Restore Debugger State)**](-pop--restore-debugger-state-.md) command. If the command is successful, no output is displayed.
