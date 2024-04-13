---
title: ".restart (Restart Kernel Connection)"
description: "The .restart command restarts the kernel connection.Do not confuse this command with the .restart (Restart Target Application) command, which works only in user mode."
keywords: [".restart (Restart Kernel Connection) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- .restart (Restart Kernel Connection)
api_type:
- NA
---

# .restart (Restart Kernel Connection)

The **.restart** command restarts the kernel connection.

Do not confuse this command with the [**.restart (Restart Target Application)**](-restart--restart-target-application-.md) command, which works only in user mode.

```dbgcmd
.restart 
```

## Environment

You can use the **.restart** command only in KD.

|  Item       | Description       |
|-----------|------------------|
| Modes     | kernel mode only |
| Targets   | live, crash dump |
| Platforms | all              |

## Additional Information

For more information about reestablishing contact with the target, see [Synchronizing with the Target Computer](../debugger/synchronizing-with-the-target-computer.md).

## Remarks

The **.restart** command is similar to the [**CTRL+R (Re-synchronize)**](../debugger/ctrl-r--re-synchronize-.md) command, except that **.restart** is even more extensive in its effect. This command is equivalent to ending the debugger and then attaching a new debugger to the target computer.

The **.restart** command is most useful when you are performing [remote debugging through remote.exe](../debugger/remote-debugging-through-remote-exe.md) and ending and restarting the debugger might be difficult. However, you cannot use **.restart** from a debugging client if you are performing remote debugging through the debugger.

