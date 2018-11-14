---
title: Activating a Debugging Server
description: There are two ways to activate the debugging server.
ms.assetid: aba75d2d-4077-415f-b847-023e47239e2e
keywords: ["Activating a Debugging Server Windows Debugging"]
ms.author: domars
ms.date: 03/02/2017
topic_type:
- apiref
api_name:
- Activating a Debugging Server
api_type:
- NA
ms.localizationpriority: medium
---

# Activating a Debugging Server


There are two ways to activate the debugging server. It can be activated when the debugger is started by using the **-server** command-line option in a elevated Command Prompt window (Run as Administrator). It can also be activated after the debugger is running. Start the debugger with elevated privileges (Run as Administrator), and enter the [**.server**](-server--create-debugging-server-.md) command.

**Note**  You can activate a debugging server without having elevated privileges, and debugging clients will be able to connect to the server. However, clients will not be able to discover a debugging server unless it was activated with elevated privileges. For information about how to discover debugging servers, see [Searching for Debugging Servers](searching-for-debugging-servers.md).

 

The debuggers support several transport protocols: named pipe (NPIPE), TCP, COM port, secure pipe (SPIPE), and secure sockets layer (SSL).

The general syntax for activating a debugging server depends on the protocol used.

```console
Debugger -server npipe:pipe=PipeName[,hidden][,password=Password][,IcfEnable] [-noio] [Options]

Debugger -server tcp:port=Socket[,hidden][,password=Password][,ipversion=6][,IcfEnable] [-noio] [Options]

Debugger -server tcp:port=Socket,clicon=Client[,password=Password][,ipversion=6] [-noio] [Options]

Debugger -server com:port=COMPort,baud=BaudRate,channel=COMChannel[,hidden][,password=Password] [-noio] [Options]

Debugger -server spipe:proto=Protocol,{certuser=Cert|machuser=Cert},pipe=PipeName[,hidden][,password=Password] [-noio] [Options]

Debugger -server ssl:proto=Protocol,{certuser=Cert|machuser=Cert},port=Socket[,hidden][,password=Password] [-noio] [Options]

Debugger -server ssl:proto=Protocol,{certuser=Cert|machuser=Cert},port=Socket,clicon=Client[,password=Password] [-noio] [Options]
```

Another method of activating a debugging server is to use the [**.server (Create Debugging Server)**](-server--create-debugging-server-.md) command after the debugger has already been started.

```dbgcmd
.server npipe:pipe=PipeName[,hidden][,password=Password][,IcfEnable] 

.server tcp:port=Socket[,hidden][,password=Password][,ipversion=6][,IcfEnable] 

.server tcp:port=Socket,clicon=Client[,password=Password][,ipversion=6] 

.server com:port=COMPort,baud=BaudRate,channel=COMChannel[,hidden][,password=Password] 

.server spipe:proto=Protocol,{certuser=Cert|machuser=Cert},pipe=PipeName[,hidden][,password=Password] 

.server ssl:proto=Protocol,{certuser=Cert|machuser=Cert},port=Socket[,hidden][,password=Password] 

.server ssl:proto=Protocol,{certuser=Cert|machuser=Cert},port=Socket,clicon=Client[,password=Password] 
```

## <span id="ddk_activating_a_debugging_server_dbg"></span><span id="DDK_ACTIVATING_A_DEBUGGING_SERVER_DBG"></span>


The parameters in the previous commands have the following possible values:

<span id="________Debugger"></span><span id="________debugger"></span><span id="________DEBUGGER"></span> *Debugger*  
Can be KD, CDB, NTSD, or WinDbg.

<span id="________pipe_________PipeName"></span><span id="________pipe_________pipename"></span><span id="________PIPE_________PIPENAME"></span> **pipe=** *PipeName*  
When NPIPE or SPIPE protocol is used, *PipeName* is a string that will serve as the name of the pipe. Each pipe name should identify a unique debugging server. If you attempt to reuse a pipe name, you will receive an error message. *PipeName* must not contain spaces or quotation marks. *PipeName* can include a numerical **printf**-style format code, such as **%x** or **%d**. The debugger will replace this with the process ID of the debugger. A second such code will be replaced with the thread ID of the debugger.

**Note**  You might need to enable file and printer sharing on the computer that is running the debugging server. In Control Panel, navigate to **Network and Internet &gt; Network and Sharing Center&gt; Advanced sharing settings**. Select **Turn on file and printer sharing**.

 

<span id="________port_________Socket"></span><span id="________port_________socket"></span><span id="________PORT_________SOCKET"></span> **port=** *Socket*  
When TCP or SSL protocol is used, *Socket* is the socket port number.

It is also possible to specify a range of ports separated by a colon. The debugger will check each port in this range to see if it is free. If it finds a free port and no error occurs, the debugging server will be created. The debugging client will have to specify the actual port being used to connect to the server. To determine the actual port, use any of the methods described in [**Searching for Debugging Servers**](searching-for-debugging-servers.md); when this debugging server is displayed, the port will be followed by two numbers separated by a colon. The first number will be the actual port used; the second can be ignored. For example, if the port was specified as **port=51:60**, and port 53 was actually used, the search results will show "port=53:60". (If you are using the **clicon** parameter to establish a reverse connection, the debugging client can specify a range of ports in this manner, while the server must specify the actual port used.)

<span id="________clicon_________Client"></span><span id="________clicon_________client"></span><span id="________CLICON_________CLIENT"></span> **clicon=** *Client*  
When TCP or SSL protocol is used and the **clicon** parameter is specified, a *reverse connection* will be opened. This means that the debugging server will try to connect to the debugging client, instead of letting the client initiate the contact. This can be useful if you have a firewall that is preventing a connection in the usual direction. *Client* specifies the network name or IP address of the computer on which the debugging client exists or will be created. The two initial backslashes (\\\) are optional.

Since the server is looking for one specific client, you cannot connect multiple clients to the server if you use this method. If the connection is refused or is broken you will have to restart the server connection. A reverse-connection server will not appear when another debugger displays all active servers.

**Note**   When **clicon** is used, it is best to start the debugging client before the debugging server is created, although the usual order (server before client) is also permitted.

 

<span id="port_________COMPort"></span><span id="port_________comport"></span><span id="PORT_________COMPORT"></span>**port=** *COMPort*  
When COM protocol is used, *COMPort* specifies the COM port to be used. The prefix "COM" is optional -- for example, both "com2" and "2" are acceptable.

<span id="baud_________BaudRate"></span><span id="baud_________baudrate"></span><span id="BAUD_________BAUDRATE"></span>**baud=** *BaudRate*  
When COM protocol is used, *BaudRate* specifies the baud rate at which the connection will run. Any baud rate that is supported by the hardware is permitted.

<span id="channel_________COMChannel"></span><span id="channel_________comchannel"></span><span id="CHANNEL_________COMCHANNEL"></span>**channel=** *COMChannel*  
If COM protocol is used, *COMChannel* specifies the COM channel to be used in communicating with the debugging client. This can be any value between 0 and 254, inclusive. You can use a single COM port for multiple connections using different channel numbers. (This is different from the use of a COM ports for a debug cable -- in that situation you cannot use channels within a COM port.)

<span id="________proto_________Protocol"></span><span id="________proto_________protocol"></span><span id="________PROTO_________PROTOCOL"></span> **proto=** *Protocol*  
If SSL or SPIPE protocol is used, *Protocol* specifies the Secure Channel (S-Channel) protocol. This can be any one of the strings tls1, pct1, ssl2, or ssl3.

<span id="Cert"></span><span id="cert"></span><span id="CERT"></span>*Cert*  
If SSL or SPIPE protocol is used, *Cert* specifies the certificate. This can either be the certificate name or the certificate's thumbprint (the string of hexadecimal digits given by the certificate's snapin). If the syntax **certuser=**<em>Cert</em> is used, the debugger will look up the certificate in the system store (the default store). If the syntax **machuser=**<em>Cert</em> is used, the debugger will look up the certificate in the machine store. The specified certificate must support server authentication.

<span id="________hidden"></span><span id="________HIDDEN"></span> **hidden**  
Prevents the server from appearing when another debugger displays all active servers.

<span id="________password_________Password"></span><span id="________password_________password"></span><span id="________PASSWORD_________PASSWORD"></span> **password=** *Password*  
Requires a client to supply the specified password in order to connect to the debugging session. *Password* can be any alphanumeric string, up to twelve characters in length.

**Warning**   Using a password with TCP, NPIPE, or COM protocol only offers a small amount of protection, because the password is not encrypted. When a password is used with SSL or SPIPE protocol, it is encrypted. If you want to establish a secure remote session, you must use SSL or SPIPE protocol.

 

<span id="________ipversion_6"></span><span id="________IPVERSION_6"></span> **ipversion=6**  
(Debugging Tools for Windows 6.6.07 and earlier only) Forces the debugger to use IP version 6 rather than version 4 when using TCP to connect to the Internet. In Windows Vista and later versions, the debugger attempts to auto-default to IP version 6, making this option unnecessary.

<span id="-noio"></span><span id="-NOIO"></span>**-noio**  
If the debugging server is created with the **-noio** option, no input or output can be done through the server itself. The debugger will only accept input from the debugging client (plus any initial command or command script specified by the **-c** command-line option). All output will be directed to the debugging client. The **-noio** option is only available with KD, CDB, and NTSD. If NTSD is used for the server, no console window will be created at all.

<span id="________IcfEnable"></span><span id="________icfenable"></span><span id="________ICFENABLE"></span> **IcfEnable**  
(Windows XP and later versions only) Causes the debugger to enable the necessary port connections for TCP or named pipe communication when the Internet Connection Firewall is active. By default, the Internet Connection Firewall disables the ports used by these protocols. When **IcfEnable** is used with a TCP connection, the debugger causes Windows to open the port specified by the *Socket* parameter. When **IcfEnable** is used with a named pipe connection, the debugger causes Windows to open the ports used for named pipes (ports 139 and 445). The debugger does not close these ports after the connection terminates.

<span id="Options_______"></span><span id="options_______"></span><span id="OPTIONS_______"></span>*Options*   
Any additional command-line parameters can be placed here. See [Command-Line Options](command-line-options.md) for a full list.

You can use the [**.server**](-server--create-debugging-server-.md) command to start multiple servers using different protocol options. This allows different kinds of debugging clients to join the session.


## See Also

[Controlling a Remote Debugging Session](controlling-a-remote-debugging-session.md)

[.endsrv (End Debugging Server)](-endsrv--end-debugging-server-.md)
 

------





