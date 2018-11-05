---
title: Activating a Smart Client
description: Once the DbgSrv process server has been activated, you can create a smart client on another computer and begin a debugging session.
ms.assetid: 7199dc95-e8fc-4f58-ab6e-c0141681113e
keywords: ["Activating a Smart Client Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- Activating a Smart Client
api_type:
- NA
ms.localizationpriority: medium
---

# Activating a Smart Client


Once the DbgSrv process server has been activated, you can create a smart client on another computer and begin a debugging session.

There are two ways to start a smart client: by starting CDB or WinDbg with the -premote [command-line option](command-line-options.md), or by using the WinDbg graphical interface.

The protocol of the smart client must match the protocol of the process server. The general syntax for starting a smart client depends on the protocol used. The following options exist:

```console
Debugger -premote npipe:server=Server,pipe=PipeName[,password=Password] [Options]

Debugger -premote tcp:server=Server,port=Socket[,password=Password][,ipversion=6] [Options]

Debugger -premote tcp:clicon=Server,port=Socket[,password=Password][,ipversion=6] [Options]

Debugger -premote com:port=COMPort,baud=BaudRate,channel=COMChannel[,password=Password] [Options]

Debugger -premote spipe:proto=Protocol,{certuser=Cert|machuser=Cert},server=Server,pipe=PipeName[,password=Password] [Options]

Debugger -premote ssl:proto=Protocol,{certuser=Cert|machuser=Cert},server=Server,port=Socket[,password=Password] [Options]

Debugger -premote ssl:proto=Protocol,{certuser=Cert|machuser=Cert},clicon=Server,port=Socket[,password=Password] [Options]
```

To use the graphical interface to connect to a process server, WinDbg must be in dormant mode -- it must either have been started with no command-line parameters, or it must have ended the previous debugging session. Select the **File | Connect to Remote Stub** menu command. When the **Connect to Remote Stub Server** dialog box appears, enter one of the following strings into the **Connection string** text box:

```dbgcmd
npipe:server=Server,pipe=PipeName[,password=Password] 

tcp:server=Server,port=Socket[,password=Password][,ipversion=6] 

tcp:clicon=Server,port=Socket[,password=Password][,ipversion=6] 

com:port=COMPort,baud=BaudRate,channel=COMChannel[,password=Password] 

spipe:proto=Protocol,{certuser=Cert|machuser=Cert},server=Server,pipe=PipeName[,password=Password] 

ssl:proto=Protocol,{certuser=Cert|machuser=Cert},server=Server,port=Socket[,password=Password] 

ssl:proto=Protocol,{certuser=Cert|machuser=Cert},clicon=Server,port=Socket[,password=Password] 
```

Alternatively, you can use the **Browse** button to locate active process servers. See [File | Connect to Remote Stub](file---connect-to-remote-stub.md) for details.

## <span id="ddk_activating_a_smart_client_dbg"></span><span id="DDK_ACTIVATING_A_SMART_CLIENT_DBG"></span>


The parameters in the preceding commands have the following possible values:

<span id="________Debugger"></span><span id="________debugger"></span><span id="________DEBUGGER"></span> *Debugger*  
This can be CDB or WinDbg.

<span id="________Server"></span><span id="________server"></span><span id="________SERVER"></span> *Server*  
This is the network name or IP address of the computer on which the process server was created. The two initial backslashes (\\\) are optional on the command line, but are not permitted in the WinDbg dialog box.

<span id="________pipe_________PipeName"></span><span id="________pipe_________pipename"></span><span id="________PIPE_________PIPENAME"></span> **pipe=** *PipeName*  
If NPIPE or SPIPE protocol is used, *PipeName* is the name that was given to the pipe when the process server was created.

If you are not logged on to the client computer with an account that has access to the server computer, you must provide a user name and password. On the client computer, in a Command Prompt window, enter the following command.

**net use \\\\**<em>Server</em>**\\ipc$ /user:**<em>UserName</em>

where *Server* is the name of the server computer, and *UserName* is the name of an account that has access to the server computer.

When you are prompted, enter the password for *UserName*.

After this command succeeds, you can activate a smart client by using the **-premote** command-line option or by using the WinDbg graphical interface.

**Note**  You might need to enable file and printer sharing on the server computer. In Control Panel, navigate to **Network and Internet &gt; Network and Sharing Center&gt; Advanced sharing settings**. Select **Turn on file and printer sharing**.

 

<span id="________port_________Socket"></span><span id="________port_________socket"></span><span id="________PORT_________SOCKET"></span> **port=** *Socket*  
If TCP or SSL protocol is used, *Socket* is the same socket port number that was used when the process server was created.

<span id="________clicon"></span><span id="________CLICON"></span> **clicon**  
Specifies that the process server will try to connect to the smart client through a reverse connection. The client must use **clicon** if and only if the server is using **clicon**. In most cases, the smart client is started before the process server when a reverse connection is used.

<span id="port_________COMPort"></span><span id="port_________comport"></span><span id="PORT_________COMPORT"></span>**port=** *COMPort*  
If COM protocol is used, *COMPort* specifies the COM port to be used. The prefix "COM" is optional -- for example, both "com2" and "2" are acceptable.

<span id="baud_________BaudRate"></span><span id="baud_________baudrate"></span><span id="BAUD_________BAUDRATE"></span>**baud=** *BaudRate*  
If COM protocol is used, *BaudRate* should match the baud rate chosen when the process server was created.

<span id="channel_________COMChannel"></span><span id="channel_________comchannel"></span><span id="CHANNEL_________COMCHANNEL"></span>**channel=** *COMChannel*  
If COM protocol is used, *COMChannel* should match the channel number chosen when the process server was created.

<span id="________proto_________Protocol"></span><span id="________proto_________protocol"></span><span id="________PROTO_________PROTOCOL"></span> **proto=** *Protocol*  
If SSL or SPIPE protocol is used, *Protocol* should match the secure protocol used when the process server was created.

<span id="Cert"></span><span id="cert"></span><span id="CERT"></span>*Cert*  
If SSL or SPIPE protocol is used, you should use the identical **certuser=**<em>Cert</em> or **machuser=**<em>Cert</em> parameter that was used when the process server was created.

<span id="________password_________Password"></span><span id="________password_________password"></span><span id="________PASSWORD_________PASSWORD"></span> **password=** *Password*  
If a password was used when the process server was created, *Password* must be supplied in order to create the smart client. It must match the original password. Passwords are case-sensitive. If the wrong password is supplied, the error message will specify "Error 0x80004005."

<span id="________________ipversion_6"></span><span id="________________IPVERSION_6"></span> **ipversion=6**  
(Debugging Tools for Windows 6.6.07 and earlier only) Forces the debugger to use IP version 6 rather than version 4 when using TCP to connect to the Internet. In Windows Vista and later versions, the debugger attempts to auto-default to IP version 6, making this option unnecessary.

<span id="Options"></span><span id="options"></span><span id="OPTIONS"></span>*Options*  
Any additional command-line parameters can be placed here. See [Command-Line Options](command-line-options.md) for a full list. If you are using CDB, this must specify the process you wish to debug. If you are using WinDbg, you can specify the process on the command line or through the graphical interface.

Since the process server simply acts as a gateway for the smart client, the additional *Options* will be the same as those you would use if you were starting a user-mode debugger on the same machine as the target application.

If you are using the **-premote** option with [**.attach (Attach to Process)**](-attach--attach-to-process-.md) or [**.create (Create Process)**](-create--create-process-.md), the parameters are the same as those listed above.

 

 





