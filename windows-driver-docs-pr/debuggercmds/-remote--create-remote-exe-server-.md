---
title: .remote (Create Remote.exe Server)
description: The .remote command starts a Remote.exe Server, enabling a remote connection to the current debugging session.
keywords: ["Create Remote.exe Server (.remote) command", "remote debugging through remote.exe, Create Remote.exe Server (.remote) command", ".remote (Create Remote.exe Server) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- .remote (Create Remote.exe Server)
api_type:
- NA
---

# .remote (Create Remote.exe Server)


The **.remote** command starts a [Remote.exe Server](../debugger/starting-a-remote-exe-session.md), enabling a remote connection to the current debugging session.

```dbgcmd
.remote session
```

## <span id="ddk_meta_create_remote_exe_server_dbg"></span><span id="DDK_META_CREATE_REMOTE_EXE_SERVER_DBG"></span>Parameters


<span id="_______session______"></span><span id="_______SESSION______"></span> *session*   
Specifies a name that you give to the debugging session.

### Environment

You can use the **.remote** command in KD and CDB, but you cannot use it in WinDbg.

|  Item  | Description          |
|--------|----------------------|
|Modes   |User mode, kernel mode|
|Targets |Live, crash dump      |
|Platforms|All                  |

 

### Additional Information

For more information about how to use Remote.exe Servers and Remote.exe Clients, see [Remote Debugging Through Remote.exe](../debugger/remote-debugging-through-remote-exe.md).

## Remarks

The **.remote** command creates a Remote.exe process and turns the current debugger into a Remote.exe Server. This server enables a Remote.exe Client to connect to the current debugging session.

 

 





