---
title: .endsrv (End Debugging Server)
description: The .endsrv command causes the debugger to cancel an active debugging server.
ms.assetid: 6be6c774-fe6b-4bd4-8174-55ef207db3e6
keywords: [".endsrv (End Debugging Server) Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- .endsrv (End Debugging Server)
api_type:
- NA
---

# .endsrv (End Debugging Server)


The **.endsrv** command causes the debugger to cancel an active debugging server.

``` syntax
    .endsrv ServerID 
```

## <span id="ddk_meta_end_debugging_server_dbg"></span><span id="DDK_META_END_DEBUGGING_SERVER_DBG"></span>Parameters


<span id="_______ServerID______"></span><span id="_______serverid______"></span><span id="_______SERVERID______"></span> *ServerID*   
Specifies the ID of the debugging server.

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

You can use this command only when you are performing remote debugging through the debugger.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>User mode only</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>Live, crash dump</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>All</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information about remote debugging, see [Remote Debugging Through the Debugger](remote-debugging-through-the-debugger.md).

Remarks
-------

You must issue the **.endsrv** command from the debugging server or from one of the debugging clients that are connected to the debugging server.

To determine the ID of a debugging server, use the [**.servers (List Debugging Servers)**](-servers--list-debugging-servers-.md) command.

The **.endsrv** command can terminate a debugging server, but it cannot terminate a process server or KD connection server. For information on how to end these servers, see [Controlling a Process Server Session](controlling-a-process-server-session.md) and [Controlling a KD Connection Server Session](controlling-a-kd-connection-server-session.md). (There is, however, one exceptional case when **.endsrv** can end a process server that has been launched programmatically; for details, see [**IDebugClient::StartProcessServer**](https://msdn.microsoft.com/library/windows/hardware/ff558810).)

If you cancel a debugging server, you prevent any future debugging clients from attaching to the server. However, if you cancel a debugging server, you do not detach any clients that are currently attached through the server.

Consider the following situation. Suppose that you start some debugging servers, as the following example shows.

```
0:000> .server npipe:pipe=rabbit
Server started with &#39;npipe:pipe=rabbit&#39;
0:000> .server tcp:port=7
Server started with &#39;tcp:port=7&#39;
```

Then, you decide to use a password, as the following example shows.

```
0:000> .server npipe:pipe=tiger,password=hardtoguess
Server started with &#39;npipe:pipe=tiger,password=hardtoguess&#39;
```

But the earlier servers are still running, so you should cancel them, as the following example shows.

```
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

```
0:000> .clients
HotMachine\HostUser, last active Mon Mar 04 16:05:21 2002
```

**Caution**   Using a password with TCP, NPIPE, or COM protocol offers only a small amount of protection, because the password is not encrypted. When you use a password together with a SSL or SPIPE protocol, the password is encrypted. If you want to establish a secure remote session, you must use the SSL or SPIPE protocol.

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20.endsrv%20%28End%20Debugging%20Server%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




