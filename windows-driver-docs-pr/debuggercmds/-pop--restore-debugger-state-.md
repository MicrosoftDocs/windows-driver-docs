---
title: .pop (Restore Debugger State)
description: The .pop command restores the state of the debugger to a state that has previously been saved by using the .push (Save Debugger State) command.
keywords: ["Restore Debugger State (.pop) command", ".pop (Restore Debugger State) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- .pop (Restore Debugger State)
api_type:
- NA
---

# .pop (Restore Debugger State)


The **.pop** command restores the state of the debugger to a state that has previously been saved by using the [**.push (Save Debugger State)**](-push--save-debugger-state-.md) command.

```dbgcmd
.pop
.pop /r
.pop /r /q
```

## Parameters


<span id="________r______"></span><span id="________R______"></span> **/r**   
Specifies that the saved values of the pseudo-registers $t0 to $t19 should be restored. If **/r** is not included, these values are not affected by the **.pop** command.

<span id="________q______"></span><span id="________Q______"></span> **/q**   
Specifies that the command executes quietly. That is, the command executes without displaying any output.

### Environment

|  Item  | Description          |
|--------|----------------------|
|Modes   |User mode, kernel mode|
|Targets |Live, crash dump      |
|Platforms|All                  |

 

## Remarks

This command is most useful when used with [scripts](using-script-files.md) and [debugger command programs](../debugger/using-debugger-command-programs.md) so that they can work with one fixed state. If the command is successful, no output is displayed.

 

 





