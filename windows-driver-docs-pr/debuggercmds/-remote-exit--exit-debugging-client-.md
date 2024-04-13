---
title: ".remote_exit (Exit Debugging Client)"
description: "The .remote_exit command exits the debugging client but does not end the debugging session."
keywords: ["Exit Debugging Client (.remote_exit) command", "remote debugging through the debugger, Exit Debugging Client (.remote_exit) command", ".remote_exit (Exit Debugging Client) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- .remote_exit (Exit Debugging Client)
api_type:
- NA
---

# .remote\_exit (Exit Debugging Client)

The **.remote\_exit** command exits the debugging client but does not end the debugging session.

```dbgcmd
.remote_exit [FinalCommands]
```

## Parameters

<span id="_______FinalCommands______"></span><span id="_______finalcommands______"></span><span id="_______FINALCOMMANDS______"></span> *FinalCommands*   
Specifies a command string to pass to the debugging server. You should separate multiple commands by using semicolons. These commands are passed to the debugging server and the connection is then broken.

## Environment

You can use the **.remote\_exit** command only in a script file. You can use it in KD and CDB, but you cannot use it in WinDbg.

|  Item  | Description          |
|--------|----------------------|
|Modes   |User mode, kernel mode|
|Targets |Live, crash dump      |
|Platforms|All                  |

## Additional Information

For more information about script files, see [Using Script Files](using-script-files.md). For more information about debugging clients and debugging servers, see [Remote Debugging Through the Debugger](../debugger/remote-debugging-through-the-debugger.md).

## Remarks

If you are using KD or CDB directly, instead of using a script, you can exit from the debugging client by using the [**CTRL+B**](../debugger/ctrl-b--quit-local-debugger-.md) key.

You cannot exit from a debugging client through a script that is executed in WinDbg.
