---
title: qd (Quit and Detach)
description: The qd command ends the debugging session and leaves any user-mode target application running.
keywords: ["qd (Quit and Detach) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- qd (Quit and Detach)
api_type:
- NA
---

# qd (Quit and Detach)


The **qd** command ends the debugging session and leaves any user-mode target application running. (In CDB and KD, this command also exits the debugger itself. In WinDbg, this command returns the debugger to dormant mode.)

```dbgcmd
qd 
```

## <span id="ddk_cmd_quit_and_detach_dbg"></span><span id="DDK_CMD_QUIT_AND_DETACH_DBG"></span>


### Environment

|  Item  | Description          |
|--------|----------------------|
|Modes | user mode only |
|Targets | live debugging only |
|Platforms | all  |
 

## Remarks

The **qd** command detaches from a target application and ends the debugging session, leaving the target still running. However, this command is supported only on Microsoft Windows XP and later versions of Windows. On Windows 2000, **qd** generates a warning message and has no effect.

When you are performing remote debugging through the debugger, you cannot use the **qd** command from a debugging client.

 

 





