---
title: .restart (Restart Target Application)
description: The .restart command restarts the target application.Do not confuse this command with the .restart (Restart Kernel Connection) command, which works only in kernel mode.
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
.restart 
```

## <span id="ddk_meta_restart_target_application_dbg"></span><span id="DDK_META_RESTART_TARGET_APPLICATION_DBG"></span>


### Environment

|  Item  | Description          |
|--------|----------------------|
|Modes | user mode only |
|Targets | live debugging only |
|Platforms | all  |
 

### Additional Information

For more information about how to issue this command and an overview of related commands, see [Controlling the Target](controlling-the-target.md).

## Remarks

CDB and WinDbg can restart a target application if the debugger originally created the application. You can use the **.restart** command even if the target application has already closed.

However, if the application is running and the debugger is later attached to the process, the **.restart** command has no effect.

After the process is restarted, it immediately breaks into the debugger.

In WinDbg, use the **View | WinDbg Command Line** command if you started your target from the WinDbg command prompt and you want to review this command line before you decide whether to use **.restart**.

 

 





