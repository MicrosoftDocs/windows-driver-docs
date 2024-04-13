---
title: ".endsrv (End Debugging Server)"
description: "The .endsrv command causes the debugger to cancel an active debugging server."
keywords: [".endsrv (End Debugging Server) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- .endsrv (End Debugging Server)
api_type:
- NA
---

# .endsrv (End Debugging Server)


The **.endsrv** command causes the debugger to cancel an active debugging server.

```dbgcmd
.endsrv ServerID 
```

## <span id="ddk_meta_end_debugging_server_dbg"></span><span id="DDK_META_END_DEBUGGING_SERVER_DBG"></span>Parameters


<span id="_______ServerID______"></span><span id="_______serverid______"></span><span id="_______SERVERID______"></span> *ServerID*   
Specifies the ID of the debugging server.

## Environment

You can use this command only when you are performing remote debugging through the debugger.

|  Item  | Description          |
|--------|----------------------|
|Modes|User mode only|
|Targets|Live, crash dump|
|Platforms|All|

 

## Additional Information

For more information about remote debugging, see [Remote Debugging Through the Debugger](../debugger/remote-debugging-through-the-debugger.md).

## Remarks

You must issue the **.endsrv** command from the debugging server or from one of the debugging clients that are connected to the debugging server.

To determine the ID of a debugging server, use the [**.servers (List Debugging Servers)**](-servers--list-debugging-servers-.md) command.

The **.endsrv** command can terminate a debugging server, but it cannot terminate a process server or KD connection server. For information on how to end these servers, see [Controlling a Process Server Session](../debugger/controlling-a-process-server-session.md) and [Controlling a KD Connection Server Session](../debugger/controlling-a-kd-connection-server-session.md). (There is, however, one exceptional case when **.endsrv** can end a process server that has been launched programmatically; for details, see [**IDebugClient::StartProcessServer**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugclient5-startprocessserver).)

If you cancel a debugging server, you prevent any future debugging clients from attaching to the server. However, if you cancel a debugging server, you do not detach any clients that are currently attached through the server.

Consider the following situation. Suppose that you start some debugging servers, as the following example shows.

```dbgcmd
0:000> .server npipe:pipe=rabbit
Server started with 'npipe:pipe=rabbit'
0:000> .server tcp:port=7
Server started with 'tcp:port=7'
```

Then, you decide to use a password, as the following example shows.

```dbgcmd
0:000> .server npipe:pipe=tiger,password=hardtoguess
Server started with 'npipe:pipe=tiger,password=hardtoguess'
```

But the earlier servers are still running, so you should cancel them, as the following example shows.

```dbgcmd
0:000> .servers
0 - Debugger Server - npipe:Pipe=rabbit
1 - Debugger Server - tcp:Port=7
2 - Debugger Server - npipe:Pipe=tiger,Password=*
0:000> .endsrv 0
Server told to exit.  Actual exit may be delayed until
the next connection attempt.
0:000> .endsrv 1
Server told to exit.  Actual exit may be delayed until
the next connection attempt.
0:000> .servers
0 - <Disabled, exit pending>
1 - <Disabled, exit pending>
2 - Debugger Server - npipe:Pipe=tiger,Password=*
```

Finally, to make sure that nothing attached to your computer while the earlier servers were active, use the [**.clients (List Debugging Clients)**](-clients--list-debugging-clients-.md) command.

```dbgcmd
0:000> .clients
HotMachine\HostUser, last active Mon Mar 04 16:05:21 2002
```

**Caution**   Using a password with TCP, NPIPE, or COM protocol offers only a small amount of protection, because the password is not encrypted. When you use a password together with a SSL or SPIPE protocol, the password is encrypted. If you want to establish a secure remote session, you must use the SSL or SPIPE protocol.

 

 


