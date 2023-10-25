---
title: .endpsrv (End Process Server)
description: The .endpsrv command causes the current process server or KD connection server to close.
keywords: [".endpsrv (End Process Server) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- .endpsrv (End Process Server)
api_type:
- NA
---

# .endpsrv (End Process Server)


The **.endpsrv** command causes the current process server or KD connection server to close.

```dbgcmd
.endpsrv 
```

## <span id="ddk_meta_end_process_server_dbg"></span><span id="DDK_META_END_PROCESS_SERVER_DBG"></span>


### Environment

You can use this command only when you are performing remote debugging through a process server or KD connection server.

|  Item  | Description          |
|--------|----------------------|
|Modes   |User mode, kernel mode|
|Targets |Live, crash dump      |
|Platforms|All                  |

 

### Additional Information

For more information about these servers, see [Process Servers (User Mode)](../debugger/process-servers--user-mode-.md) or [KD Connection Servers (Kernel Mode)](../debugger/kd-connection-servers--kernel-mode-.md)

## Remarks

The **.endpsrv** command terminates the process server or KD connection server currently connected to your smart client.

If you wish to terminate a process server or KD connection server from the computer on which it is running, use Task Manager to end the process (dbgsrv.exe or kdsrv.exe).

The **.endpsrv** command can terminate a process server or KD connection server, but it cannot terminate a debugging server. For information on how to do that, see [Controlling a Remote Debugging Session](../debugger/controlling-a-remote-debugging-session.md).

 

 





