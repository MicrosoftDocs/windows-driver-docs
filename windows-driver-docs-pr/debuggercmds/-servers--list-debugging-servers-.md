---
title: ".servers (List Debugging Servers)"
description: "The .servers command lists all debugging servers that have been established by this debugger."
keywords: ["List Debugging Servers (.servers) command", "remote debugging through the debugger, List Debugging Servers (.servers) command", ".servers (List Debugging Servers) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- .servers (List Debugging Servers)
api_type:
- NA
---

# .servers (List Debugging Servers)

The **.servers** command lists all debugging servers that have been established by this debugger.

```dbgcmd
.servers 
```

## Environment

|  Item  | Description          |
|--------|----------------------|
|Modes   |User mode, kernel mode|
|Targets |Live, crash dump      |
|Platforms|All                  |

## Additional Information

For full details on debugging servers, see [Remote Debugging Through the Debugger](../debugger/remote-debugging-through-the-debugger.md).

## Remarks

The output of the **.servers** command lists all the debugging servers started by the debugger on which this command is issued. The output is formatted so that it can be used literally as the argument for the -remote command-line option or pasted into the WinDbg dialog box.

Each debugging server is identified by a unique ID. This ID can be used as the argument for the [**.endsrv (End Debugging Server)**](-endsrv--end-debugging-server-.md) command, if you wish to terminate the debugging server.

The **.servers** command does not list debugging servers started on this computer by different instances of the debugger, nor does it list process servers or KD connection servers.
