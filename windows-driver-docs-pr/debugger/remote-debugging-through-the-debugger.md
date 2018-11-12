---
title: Remote Debugging Through the Debugger
description: Remote Debugging Through the Debugger
ms.assetid: a9f6f355-e684-471f-a45c-b2235a5372b1
keywords: ["remote debugging through the debugger", "remote debugging through the debugger, overview", "debugging client", "debugging server", "TCP (remote debugging protocol)", "COM port (remote debugging protocol)", "modem (remote debugging protocol)", "named pipe (remote debuggi"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Remote Debugging Through the Debugger


## <span id="ddk_remote_debugging_through_the_debugger_dbg"></span><span id="DDK_REMOTE_DEBUGGING_THROUGH_THE_DEBUGGER_DBG"></span>


Remote debugging directly through the debugger is usually the best and easiest method of performing remote debugging.

This technique involves running two debuggers at different locations. The debugger that is actually doing the debugging is called the *debugging server*. The debugger that is controlling the session from a distance is called the *debugging client*.

The two computers do not have to be running the same version of Windows; they can be running any version of Windows. The actual debuggers used need not be the same; a WinDbg debugging client can connect to a CDB debugging server, and so on.

However, it is best that the debugger binaries on the two computers both be from the same release of the Debugging Tools for Windows package, or at least both from recent releases.

To set up this remote session, the debugging server is set up first, and then the debugging client is activated. Any number of debugging clients can connect to a debugging server. A single debugger can turn itself into several debugging servers at the same time, to facilitate different kinds of connections.

However, no single debugger can be a debugging client and a debugging server simultaneously.

This section includes:

[Activating a Debugging Server](activating-a-debugging-server.md)

[Searching for Debugging Servers](searching-for-debugging-servers.md)

[Activating a Debugging Client](activating-a-debugging-client.md)

[Client and Server Examples](client-and-server-examples.md)

[Controlling a Remote Debugging Session](controlling-a-remote-debugging-session.md)

 

 





