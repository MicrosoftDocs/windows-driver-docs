---
title: Remote Debugging Through the Debugger
description: Remote Debugging Through the Debugger
ms.assetid: a9f6f355-e684-471f-a45c-b2235a5372b1
keywords: ["remote debugging through the debugger", "remote debugging through the debugger, overview", "debugging client", "debugging server", "TCP (remote debugging protocol)", "COM port (remote debugging protocol)", "modem (remote debugging protocol)", "named pipe (remote debuggi"]
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Remote%20Debugging%20Through%20the%20Debugger%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




