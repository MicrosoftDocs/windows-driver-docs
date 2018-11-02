---
title: Activating a Smart Client (Kernel Mode)
description: Once the KD connection server has been activated, you can create a smart client on another computer and begin a debugging session.
ms.assetid: bf0f1dd5-e6dc-4168-8476-cf21e77bd335
keywords: ["Activating a Smart Client (Kernel Mode) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- Activating a Smart Client (Kernel Mode)
api_type:
- NA
ms.localizationpriority: medium
---

# Activating a Smart Client (Kernel Mode)


Once the KD connection server has been activated, you can create a smart client on another computer and begin a debugging session.

There are two ways to start a smart client: by starting KD or WinDbg with the kernel protocol **kdsrv**, or by using the WinDbg graphical interface.

You need to specify the remote transfer protocol used by the KD connection server. You can also specify the protocol for the actual kernel connection between the KD connection server and the target computer, or you can use the default.

The general syntax for starting a smart client depends on the protocol used. The following options exist:

```console
Debugger -k kdsrv:server=@{npipe:server=Server,pipe=PipeName[,password=Password]},trans=@{ConnectType} [Options]

Debugger -k kdsrv:server=@{tcp:server=Server,port=Socket[,password=Password][,ipversion=6]},trans=@{ConnectType} [Options]

Debugger -k kdsrv:server=@{tcp:clicon=Server,port=Socket[,password=Password][,ipversion=6]},trans=@{ConnectType} [Options]

Debugger -k kdsrv:server=@{com:port=COMPort,baud=BaudRate,channel=COMChannel[,password=Password]},trans=@{ConnectType} [Options]

Debugger -k kdsrv:server=@{spipe:proto=Protocol,{certuser=Cert|machuser=Cert},server=Server,pipe=PipeName[,password=Password]},trans=@{ConnectType} [Options]

Debugger -k kdsrv:server=@{ssl:proto=Protocol,{certuser=Cert|machuser=Cert},server=Server,port=Socket[,password=Password]},trans=@{ConnectType} [Options]

Debugger -k kdsrv:server=@{ssl:proto=Protocol,{certuser=Cert|machuser=Cert},clicon=Server,port=Socket[,password=Password]},trans=@{ConnectType} [Options]
```

To use the graphical interface to connect to a KD connection server, WinDbg must be in dormant mode -- it must either have been started with no command-line parameters, or it must have ended the previous debugging session. Select the **File | Connect to Remote Stub** menu command. When the **Connect to Remote Stub Server** dialog box appears, enter one of the following strings into the **Connection string** text box:

```dbgcmd
npipe:server=Server,pipe=PipeName[,password=Password] 

tcp:server=Server,port=Socket[,password=Password][,ipversion=6] 

tcp:clicon=Server,port=Socket[,password=Password][,ipversion=6] 

com:port=COMPort,baud=BaudRate,channel=COMChannel[,password=Password] 

spipe:proto=Protocol,{certuser=Cert|machuser=Cert},server=Server,pipe=PipeName[,password=Password] 

ssl:proto=Protocol,{certuser=Cert|machuser=Cert},server=Server,port=Socket[,password=Password] 

ssl:proto=Protocol,{certuser=Cert|machuser=Cert},clicon=Server,port=Socket[,password=Password] 
```

Alternatively, you can use the **Browse** button to locate active KD connection servers. See [File | Connect to Remote Stub](file---connect-to-remote-stub.md) for details.

## <span id="ddk_activating_a_smart_client_kernel_mode__dbg"></span><span id="DDK_ACTIVATING_A_SMART_CLIENT_KERNEL_MODE__DBG"></span>


The parameters in the preceding commands have the following possible values:

<span id="________Debugger"></span><span id="________debugger"></span><span id="________DEBUGGER"></span> *Debugger*  
This can be KD or WinDbg.

<span id="Server"></span><span id="server"></span><span id="SERVER"></span>*Server*  
This is the network name or IP address of the computer on which the KD connection server was created.The two initial backslashes (\\\) are optional on the command line, but are not permitted in the WinDbg dialog box.

<span id="________pipe_________PipeName"></span><span id="________pipe_________pipename"></span><span id="________PIPE_________PIPENAME"></span> **pipe=** *PipeName*  
If NPIPE or SPIPE protocol is used, *PipeName* is the name that was given to the pipe when the KD connection server was created.

If you are not logged on to the client computer with an account that has access to the server computer, you must provide a user name and password. On the client computer, in a Command Prompt window, enter the following command.

**net use \\\\**<em>Server</em>**\\ipc$ /user:**<em>UserName</em>

where *Server* is the name of the server computer, and *UserName* is the name of an account that has access to the server computer.

When you are prompted, enter the password for *UserName*.

After this command succeeds, you can activate a smart client by using **-k kdsrv** or by using the WinDbg graphical interface.

<span id="________port_________Socket"></span><span id="________port_________socket"></span><span id="________PORT_________SOCKET"></span> **port=** *Socket*  
If TCP or SSL protocol is used, *Socket* is the same socket port number that was used when the KD connection server was created.

<span id="clicon"></span><span id="CLICON"></span>**clicon**  
Specifies that the KD connection server will try to connect to the smart client through a reverse connection. The client must use **clicon** if and only if the server is using **clicon**. In most cases, the smart client is started before the KD connection server when a reverse connection is used.

<span id="port_________COMPort"></span><span id="port_________comport"></span><span id="PORT_________COMPORT"></span>**port=** *COMPort*  
If COM protocol is used, *COMPort* specifies the COM port to be used. The prefix "COM" is optional -- for example, both "com2" and "2" are acceptable.

<span id="baud_________BaudRate"></span><span id="baud_________baudrate"></span><span id="BAUD_________BAUDRATE"></span>**baud=** *BaudRate*  
If COM protocol is used, *BaudRate* should match the baud rate chosen when the KD connection server was created.

<span id="channel_________COMChannel"></span><span id="channel_________comchannel"></span><span id="CHANNEL_________COMCHANNEL"></span>**channel=** *COMChannel*  
If COM protocol is used, *COMChannel* should match the channel number chosen when the KD connection server was created.

<span id="________proto_________Protocol"></span><span id="________proto_________protocol"></span><span id="________PROTO_________PROTOCOL"></span> **proto=** *Protocol*  
If SSL or SPIPE protocol is used, *Protocol* should match the secure protocol used when the KD connection server was created.

<span id="________Cert"></span><span id="________cert"></span><span id="________CERT"></span> *Cert*  
If SSL or SPIPE protocol is used, you should use the identical **certuser=**<em>Cert</em> or **machuser=**<em>Cert</em> parameter that was used when the KD connection server was created.

<span id="________password_________Password"></span><span id="________password_________password"></span><span id="________PASSWORD_________PASSWORD"></span> **password=** *Password*  
If a password was used when the KD connection server was created, *Password* must be supplied in order to create the smart client. It must match the original password. Passwords are case-sensitive. If the wrong password is supplied, the error message will specify "Error 0x80004005."

<span id="________ipversion_6"></span><span id="________IPVERSION_6"></span> **ipversion=6**  
(Debugging Tools for Windows 6.6.07 and earlier only) Forces the debugger to use IP version 6 rather than version 4 when using TCP to connect to the Internet. In Windows Vista and later versions, the debugger attempts to auto-default to IP version 6, making this option unnecessary.

<span id="________trans___________ConnectType_________"></span><span id="________trans___________connecttype_________"></span><span id="________TRANS___________CONNECTTYPE_________"></span> **trans=@{** *ConnectType* **}**  
Tells the debugger how to connect to the target. The following kernel connection protocols are permitted:

```dbgcmd
com:port=ComPort,baud=BaudRate 
1394:channel=1394Channel[,symlink=1394Protocol] 
usb2:targetname=String 
com:pipe,port=\\VMHost\pipe\PipeName[,resets=0][,reconnect]
com:modem 
```

For information about these protocols, see [Getting Set Up for Debugging](getting-set-up-for-debugging.md). You can omit any of the parameters for these protocols -- for example, you can say **trans=@{com:}** -- and the debugger will default to the values specified by the environment variables on the computer where KdSrv is running.

<span id="Options"></span><span id="options"></span><span id="OPTIONS"></span>*Options*  
Any additional command-line parameters can be placed here. See [Command-Line Options](command-line-options.md) for a full list.

Since the KD connection server simply acts as a gateway for the smart client, the additional *Options* will be the same as those you would use if you were starting a kernel debugger on computer where KdSrv is running. The exception to this is any option that specifies a path or filename will be taken as a path on the computer where the smart client is running.

 

 





