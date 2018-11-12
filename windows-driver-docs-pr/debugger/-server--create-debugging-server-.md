---
title: .server (Create Debugging Server)
description: The .server command starts a debugging server, allowing a remote connection to the current debugging session.
ms.assetid: 39979a53-d6e7-4660-8884-3044da0b60de
keywords: ["Create Debugging Server (.server) command", "remote debugging through the debugger, Create Debugging Server (.server) command", ".server (Create Debugging Server) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- .server (Create Debugging Server)
api_type:
- NA
ms.localizationpriority: medium
---

# .server (Create Debugging Server)


The **.server** command starts a debugging server, allowing a remote connection to the current debugging session.

```dbgcmd
.server npipe:pipe=PipeName[,hidden][,password=Password][,IcfEnable] 
.server tcp:port=Socket[,hidden][,password=Password][,ipversion=6][,IcfEnable] 
.server tcp:port=Socket,clicon=Client[,password=Password][,ipversion=6] 
.server com:port=COMPort,baud=BaudRate,channel=COMChannel[,hidden][,password=Password] 
.server spipe:proto=Protocol,{certuser=Cert|machuser=Cert},pipe=PipeName[,hidden][,password=Password] 
.server ssl:proto=Protocol,{certuser=Cert|machuser=Cert},port=Socket[,hidden][,password=Password] 
.server ssl:proto=Protocol,{certuser=Cert|machuser=Cert},port=Socket,clicon=Client[,password=Password] 
```

## <span id="ddk_meta_create_debugging_server_dbg"></span><span id="DDK_META_CREATE_DEBUGGING_SERVER_DBG"></span>Parameters


<span id="_______PipeName______"></span><span id="_______pipename______"></span><span id="_______PIPENAME______"></span> *PipeName*   
When NPIPE or SPIPE protocol is used, *PipeName* is a string that will serve as the name of the pipe. Each pipe name should identify a unique debugging server. If you attempt to reuse a pipe name, you will receive an error message. *PipeName* must not contain spaces or quotation marks. *PipeName* can include a numerical **printf**-style format code, such as %x or %d. The debugger will replace this with the process ID of the debugger. A second such code will be replaced with the thread ID of the debugger.

<span id="_______Socket______"></span><span id="_______socket______"></span><span id="_______SOCKET______"></span> *Socket*   
When TCP or SSL protocol is used, *Socket* is the socket port number.

It is also possible to specify a range of ports separated by a colon. The debugger will check each port in this range to see if it is free. If it finds a free port and no error occurs, the debugging server will be created. The debugging client will have to specify the actual port being used to connect to the server. To determine the actual port, use any of the methods described in [**Searching for Debugging Servers**](searching-for-debugging-servers.md); when this debugging server is displayed, the port will be followed by two numbers separated by a colon. The first number will be the actual port used; the second can be ignored. For example, if the port was specified as port=51:60, and port 53 was actually used, the search results will show "port=53:60". (If you are using the **clicon** parameter to establish a reverse connection, the debugging client can specify a range of ports in this manner, while the server must specify the actual port used.)

<span id="clicon_Client"></span><span id="clicon_client"></span><span id="CLICON_CLIENT"></span>**clicon=**<em>Client</em>  
When TCP or SSL protocol is used and the **clicon** parameter is specified, a *reverse connection* will be opened. This means that the debugging server will try to connect to the debugging client, instead of letting the client initiate the contact. This can be useful if you have a firewall that is preventing a connection in the usual direction. *Client* specifies the network name of the machine on which the debugging client exists or will be created. The two initial backslashes (\\\) are optional.

When **clicon** is used, it is best to start the debugging client before the debugging server is created, although the usual order (server before client) is also permitted. A reverse-connection server will not appear when another debugger displays all active servers.

<span id="_______COMPort______"></span><span id="_______comport______"></span><span id="_______COMPORT______"></span> *COMPort*   
When COM protocol is used, *COMPort* specifies the COM port to be used. The prefix COM is optional (for example, both "com2" and "2" are acceptable).

<span id="_______BaudRate______"></span><span id="_______baudrate______"></span><span id="_______BAUDRATE______"></span> *BaudRate*   
When COM protocol is used, *BaudRate* specifies the baud rate at which the connection will run. Any baud rate that is supported by the hardware is permitted.

<span id="_______COMChannel______"></span><span id="_______comchannel______"></span><span id="_______COMCHANNEL______"></span> *COMChannel*   
If COM protocol is used, *COMChannel* specifies the COM channel to be used in communicating with the debugging client. This can be any value between 0 and 254, inclusive.

<span id="_______Protocol______"></span><span id="_______protocol______"></span><span id="_______PROTOCOL______"></span> *Protocol*   
If SSL or SPIPE protocol is used, *Protocol* specifies the Secure Channel (S-Channel) protocol. This can be any one of the strings tls1, pct1, ssl2, or ssl3.

<span id="_______Cert______"></span><span id="_______cert______"></span><span id="_______CERT______"></span> *Cert*   
If SSL or SPIPE protocol is used, *Cert* specifies the certificate. This can either be the certificate name or the certificate's thumbprint (the string of hexadecimal digits given by the certificate's snapin). If the syntax **certuser=**<em>Cert</em> is used, the debugger will look up the certificate in the system store (the default store). If the syntax **machuser=**<em>Cert</em> is used, the debugger will look up the certificate in the machine store. The specified certificate must support server authentication.

<span id="_______hidden______"></span><span id="_______HIDDEN______"></span> **hidden**   
Prevents the server from appearing when another debugger displays all active servers.

<span id="password_Password"></span><span id="password_password"></span><span id="PASSWORD_PASSWORD"></span>**password=**<em>Password</em>  
Requires a debugging client to supply the specified password in order to connect to the debugging session. *Password* can be any alphanumeric string, up to twelve characters in length.

<span id="_______ipversion_6______"></span><span id="_______IPVERSION_6______"></span> **ipversion=6**   
(Debugging Tools for Windows 6.6.07 and earlier only) Forces the debugger to use IP version 6 rather than version 4 when using TCP to connect to the Internet. In Windows Vista and later versions, the debugger attempts to auto-default to IP version 6, making this option unnecessary.

<span id="_______IcfEnable______"></span><span id="_______icfenable______"></span><span id="_______ICFENABLE______"></span> **IcfEnable**   
(Windows XP and later versions only) Causes the debugger to enable the necessary port connections for TCP or named pipe communication when the Internet Connection Firewall is active. By default, the Internet Connection Firewall disables the ports used by these protocols. When **IcfEnable** is used with a TCP connection, the debugger causes Windows to open the port specified by the Socket parameter. When **IcfEnable** is used with a named pipe connection, the debugger causes Windows to open the ports used for named pipes (ports 139 and 445). The debugger does not close these ports after the connection terminates.

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>user mode, kernel mode</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>live, crash dump</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>all</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For full details on how to start a debugging server, see [**Activating a Debugging Server**](activating-a-debugging-server.md). For examples, see [Client and Server Examples](client-and-server-examples.md).

Remarks
-------

This command turns the current debugger into a debugging server. This allows you to start the server after the debugger is already running, whereas the -server [command-line option](command-line-options.md) can only be issued when the debugger is started.

This permits a debugging client to connect to the current debugging session. Note that it is possible to start multiple servers using different options, allowing different kinds of debugging clients to join the session.

 

 





