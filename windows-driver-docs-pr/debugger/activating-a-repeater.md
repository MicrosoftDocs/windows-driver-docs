---
title: Activating a Repeater
description: To activate the repeater connection, you will usually first start the server, then start the repeater, then start the client.It is also possible to start the repeater first and then the server.
ms.assetid: a2409b3d-48eb-46eb-8a53-7c4d505bb6ea
keywords: ["Activating a Repeater Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- Activating a Repeater
api_type:
- NA
ms.localizationpriority: medium
---

# Activating a Repeater


To activate the repeater connection, you will usually first start the server, then start the repeater, then start the client.

It is also possible to start the repeater first and then the server. But unless you are using the **clicon** parameter to establish a reverse connection, the client must always be started last.

## <span id="step_one__starting_the_server"></span><span id="STEP_ONE__STARTING_THE_SERVER"></span>Step One: Starting the Server


The server can be a debugging server, a process server, or a KD connection server. You start this as you normally would, except that the transport protocol settings will be used to connect to the repeater, not the client. For details, see [**Activating a Debugging Server**](activating-a-debugging-server.md), [**Activating a Process Server**](activating-a-process-server.md), or [**Activating a KD Connection Server**](activating-a-kd-connection-server.md).

If you use a password when creating the server, this password will be required when the client attaches, but not when the repeater is created.

If you use the **hidden** parameter, the server will be hidden as usual. The repeater itself is always hidden.

## <span id="step_two__starting_the_repeater"></span><span id="STEP_TWO__STARTING_THE_REPEATER"></span>Step Two: Starting the Repeater


The repeater that is included in Debugging Tools for Windows is called DbEngPrx (dbengprx.exe).

DbEngPrx understands the following transport protocols: named pipe (NPIPE), TCP, and COM port.

If your client and server are using secure sockets layer (SSL) protocol, you should use TCP protocol for the repeater. If your client and server are using secure pipe (SPIPE) protocol, you should use NPIPE protocol for the repeater. The repeater will pass on whatever data it receives -- it does not interpret, encrypt, or decrypt any information. All encryption and decryption will be done by the client and the server.

The syntax for the DbEnPrx command line is as follows:

## <span id="ddk_activating_a_repeater_dbg"></span><span id="DDK_ACTIVATING_A_REPEATER_DBG"></span>


**dbengprx \[-p\] -c** *ClientTransport* **-s** *ServerTransport*

The parameters in the previous commands have the following possible values:

<span id="________-p"></span><span id="________-P"></span> **-p**  
Causes DbEngPrx to continue existing even after all connections to it are dropped.

<span id="ClientTransport"></span><span id="clienttransport"></span><span id="CLIENTTRANSPORT"></span>*ClientTransport*  
Specifies the protocol settings to be used in connecting to the server. The protocol should match that used when the server was created. The protocol syntaxes are as follows:

```dbgcmd
npipe:server=Server,pipe=PipeName[,password=Password] 
tcp:server=Server,port=Socket[,password=Password][,ipversion=6] 
tcp:clicon=Server,port=Socket[,password=Password][,ipversion=6] 
com:port=COMPort,baud=BaudRate,channel=COMChannel[,password=Password] 
```

The protocol parameters have the following meanings:

<span id="Server"></span><span id="server"></span><span id="SERVER"></span>*Server*  
This is the network name or IP address of the computer on which the server was created. The two initial backslashes (\\\) are optional.

<span id="________pipe_________PipeName"></span><span id="________pipe_________pipename"></span><span id="________PIPE_________PIPENAME"></span> **pipe=** *PipeName*  
If NPIPE or SPIPE protocol is used, *PipeName* is the name that was given to the pipe when the server was created.

<span id="________port_________Socket"></span><span id="________port_________socket"></span><span id="________PORT_________SOCKET"></span> **port=** *Socket*  
If TCP or SSL protocol is used, *Socket* is the same socket port number that was used when the server was created.

<span id="clicon"></span><span id="CLICON"></span>**clicon**  
Specifies that the server will try to connect to the repeater through a reverse connection. *ClientTransport* must use **clicon** if and only if the server is using **clicon**. In most cases, the repeater is started before the server when a reverse connection is used.

<span id="port_________COMPort"></span><span id="port_________comport"></span><span id="PORT_________COMPORT"></span>**port=** *COMPort*  
If COM protocol is used, *COMPort* specifies the COM port to be used. The prefix "COM" is optional -- for example, both "com2" and "2" are acceptable.

<span id="baud_________BaudRate"></span><span id="baud_________baudrate"></span><span id="BAUD_________BAUDRATE"></span>**baud=** *BaudRate*  
If COM protocol is used, *BaudRate* should match the baud rate chosen when the server was created.

<span id="channel_________COMChannel"></span><span id="channel_________comchannel"></span><span id="CHANNEL_________COMCHANNEL"></span>**channel=** *COMChannel*  
If COM protocol is used, *COMChannel* should match the channel number chosen when the server was created.

<span id="________password_________Password"></span><span id="________password_________password"></span><span id="________PASSWORD_________PASSWORD"></span> **password=** *Password*  
If a password was used when the server was created, *Password* must be supplied in order to create the debugging client. It must match the original password. Passwords are case-sensitive. If the wrong password is supplied, the error message will specify "Error 0x80004005."

<span id="________ipversion_6"></span><span id="________IPVERSION_6"></span> **ipversion=6**  
(Debugging Tools for Windows 6.6.07 and earlier only) Forces the debugger to use IP version 6 rather than version 4 when using TCP to connect to the Internet. In Windows Vista and later versions, the debugger attempts to auto-default to IP version 6, making this option unnecessary.

<span id="ServerTransport"></span><span id="servertransport"></span><span id="SERVERTRANSPORT"></span>ServerTransport  
Specifies the protocol settings that will be used when the client connects to the repeater. The possible protocol syntaxes are:

```dbgcmd
npipe:pipe=PipeName[,hidden][,password=Password][,IcfEnable] 
tcp:port=Socket[,hidden][,password=Password][,IcfEnable] 
tcp:port=Socket,clicon=Client[,password=Password] 
com:port=COMPort,baud=BaudRate,channel=COMChannel[,hidden][,password=Password] 
```

The protocol parameters have the following meanings:

<span id="________pipe_________PipeName"></span><span id="________pipe_________pipename"></span><span id="________PIPE_________PIPENAME"></span> **pipe=** *PipeName*  
When NPIPE or SPIPE protocol is used, *PipeName* is a string that will serve as the name of the pipe. Each pipe name should identify a unique repeater. If you attempt to reuse a pipe name, you will receive an error message. *PipeName* must not contain spaces or quotation marks. *PipeName* can include a numerical **printf**-style format code, such as **%x** or **%d**. The repeater will replace this with the process ID of DbEngPrx. A second such code will be replaced with the thread ID of DbEngPrx.

<span id="________port_________Socket"></span><span id="________port_________socket"></span><span id="________PORT_________SOCKET"></span> **port=** *Socket*  
When TCP or SSL protocol is used, *Socket* is the socket port number.

It is also possible to specify a range of ports separated by a colon. DbEngPrx will check each port in this range to see if it is free. If it finds a free port and no error occurs, the repeater will be created. The client will have to specify the actual port being used to connect to the repeater. To determine the actual port, search for the repeater; when this repeater is displayed, the port will be followed by two numbers separated by a colon. The first number will be the actual port used; the second can be ignored. For example, if the port was specified as **port=51:60**, and port 53 was actually used, the search results will show "port=53:60". (If you are using the **clicon** parameter to establish a reverse connection, the client can specify a range of ports in this manner, while the repeater must specify the actual port used.)

<span id="clicon_Client"></span><span id="clicon_client"></span><span id="CLICON_CLIENT"></span>**clicon=**<em>Client</em>  
When TCP or SSL protocol is used and the **clicon** parameter is specified, a *reverse connection* will be opened. This means that the repeater will try to connect to the client, instead of letting the client initiate the contact. This can be useful if you have a firewall that is preventing a connection in the usual direction. *Client* specifies the network name or IP address of the computer on which the client exists or will be created. The two initial backslashes (\\\) are optional.

Since the repeater is looking for one specific client, you cannot connect multiple clients to the repeater if you use this method. If the connection is refused or is broken you will have to restart the repeater.

When **clicon** is used, it is best to start the client before the repeater is created, although the usual order (repeater before client) is also permitted.

<span id="port_________COMPort"></span><span id="port_________comport"></span><span id="PORT_________COMPORT"></span>**port=** *COMPort*  
When COM protocol is used, *COMPort* specifies the COM port to be used. The prefix "COM" is optional -- for example, both "com2" and "2" are acceptable. You cannot use the same COM port in the *ClientTransport* and the *ServerTransport*.

<span id="baud_________BaudRate"></span><span id="baud_________baudrate"></span><span id="BAUD_________BAUDRATE"></span>**baud=** *BaudRate*  
When COM protocol is used, *BaudRate* specifies the baud rate at which the connection will run. Any baud rate that is supported by the hardware is permitted. If you are using COM protocol in both the *ClientTransport* and the *ServerTransport* you may specify different baud rates, but naturally the slower rate will be the limit on how fast the client and server can communicate with each other.

<span id="channel_________COMChannel"></span><span id="channel_________comchannel"></span><span id="CHANNEL_________COMCHANNEL"></span>**channel=** *COMChannel*  
If COM protocol is used, *COMChannel* specifies the COM channel to be used in communicating with the client. This can be any value between 0 and 254, inclusive. You can use a single COM port for multiple connections using different channel numbers. (This is different from the use of a COM ports for a debug cable -- in that situation you cannot use channels within a COM port.)

<span id="hidden"></span><span id="HIDDEN"></span>**hidden**  
Prevents the server from appearing when another debugger displays all active servers.

<span id="________password_________Password"></span><span id="________password_________password"></span><span id="________PASSWORD_________PASSWORD"></span> **password=** *Password*  
Requires a client to supply the specified password in order to connect to the debugging session. *Password* can be any alphanumeric string.

<span id="IcfEnable"></span><span id="icfenable"></span><span id="ICFENABLE"></span>**IcfEnable**  
(Windows XP and later versions only) Causes the debugger to enable the necessary port connections for TCP or named pipe communication when the Internet Connection Firewall is active. By default, the Internet Connection Firewall disables the ports used by these protocols. When **IcfEnable** is used with a TCP connection, the debugger causes Windows to open the port specified by the *Socket* parameter. When **IcfEnable** is used with a named pipe connection, the debugger causes Windows to open the ports used for named pipes (ports 139 and 445). The debugger does not close these ports after the connection terminates.

### <span id="step_three__starting_the_client"></span><span id="STEP_THREE__STARTING_THE_CLIENT"></span>Step Three: Starting the Client

The client should be a debugging client or a smart client -- whichever corresponds to your server type. For details, see [**Activating a Debugging Client**](activating-a-debugging-client.md), [**Activating a Smart Client**](activating-a-smart-client.md), or [**Activating a Smart Client (Kernel Mode)**](activating-a-smart-client--kernel-mode-.md).

If the server rejects the connection (for example, if you supply an incorrect password), both the repeater and the client will be shut down. You will have to restart both of them to reestablish contact with the server.

 

 





