---
title: ".restart (Restart Target Application)"
description: "The .restart command restarts the target application.Do not confuse this command with the .restart (Restart Kernel Connection) command, which works only in kernel mode."
keywords: [".restart (Restart Target Application) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- .restart (Restart Target Application)
api_type:
- NA
---

# .restart (Restart Target Application)

The **.restart** command restarts the target application.

Do not confuse this command with the [**.restart (Restart Kernel Connection)**](-restart--restart-kernel-connection-.md) command, which works only in kernel mode.

```dbgcmd
.restart [/f]
```

## Parameters

**/f** 
Forces the restart of a process which wasn't launched by the debugger (e.g. a process which was attached to). This will use the command line of the PEB to restart the process. However, this may not be 100% identical to how the process was started and then attached to.

## Environment

|  Item  | Description          |
|--------|----------------------|
|Modes | user mode only |
|Targets | live debugging only |
|Platforms | all  |
 
## Additional Information

For more information about how to issue this command and an overview of related commands, see [Controlling the Target](../debugger/controlling-the-target.md).

## Remarks

CDB and WinDbg can restart a target application if the debugger originally created the application. You can use the **.restart** command even if the target application has already closed.

However, if the application is running and the debugger is later attached to the process, the **.restart** command displays the following message and has no other effect:
```dbgcmd
0:000> .restart
Process attaches cannot be restarted.  If you want to
restart the process, use !peb to get what command line
to use and other initialization information.
```
Use the **/f** option to mimic a restart.

After the process is restarted, it immediately breaks into the debugger.

In WinDbg, use the **View | WinDbg Command Line** command if you started your target from the WinDbg command prompt and you want to review this command line before you decide whether to use **.restart**.

