---
title: Activating a Debugging Client
description: Once the debugging server has been activated, you can start a debugging client on another computer and connect to the debugging session.
ms.assetid: 45a7baa7-08dc-47ae-a137-874aaa4ec8aa
keywords: ["Activating a Debugging Client Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- Activating a Debugging Client
api_type:
- NA
ms.localizationpriority: medium
---

# Activating a Debugging Client


Once the debugging server has been activated, you can start a debugging client on another computer and connect to the debugging session.

There are two ways to start a debugging client: by using the -remote [command-line option](command-line-options.md), or by using the WinDbg graphical interface.

The protocol of the client must match the protocol of the server. The general syntax for starting a debugging client depends on the protocol used. The following options exist:

```dbgcmd
Debugger -remote npipe:server=Server,pipe=PipeName[,password=Password] 

Debugger -remote tcp:server=Server,port=Socket[,password=Password][,ipversion=6] 

Debugger -remote tcp:clicon=Server,port=Socket[,password=Password][,ipversion=6] 

Debugger -remote com:port=COMPort,baud=BaudRate,channel=COMChannel[,password=Password] 

Debugger -remote spipe:proto=Protocol,{certuser=Cert|machuser=Cert},server=Server,pipe=PipeName[,password=Password] 

Debugger -remote ssl:proto=Protocol,{certuser=Cert|machuser=Cert},server=Server,port=Socket[,password=Password] 

Debugger -remote ssl:proto=Protocol,{certuser=Cert|machuser=Cert},clicon=Server,port=Socket[,password=Password] 
```

To use the graphical interface to connect to a remote debugging session, WinDbg must be in dormant mode -- it must either have been started with no command-line parameters, or it must have ended the previous debugging session. Select the **File | Connect to Remote Session** menu command, or press the CTRL+R shortcut key. When the **Connect to Remote Debugger Session** dialog box appears, enter one of the following strings into the **Connection string** text box:

```dbgcmd
npipe:server=Server,pipe=PipeName[,password=Password] 

tcp:server=Server,port=Socket[,password=Password][,ipversion=6] 

tcp:clicon=Server,port=Socket[,password=Password][,ipversion=6] 

com:port=COMPort,baud=BaudRate,channel=COMChannel[,password=Password] 

spipe:proto=Protocol,{certuser=Cert|machuser=Cert},server=Server,pipe=PipeName[,password=Password] 

ssl:proto=Protocol,{certuser=Cert|machuser=Cert},server=Server,port=Socket[,password=Password] 

ssl:proto=Protocol,{certuser=Cert|machuser=Cert},clicon=Server,port=Socket[,password=Password] 
```

Alternatively, you can use the **Browse** button to locate active debugging servers. See [File | Connect to Remote Session](file---connect-to-remote-session.md) for details.

## <span id="ddk_activating_a_debugging_client_dbg"></span><span id="DDK_ACTIVATING_A_DEBUGGING_CLIENT_DBG"></span>


The parameters in the preceding commands have the following possible values:

<span id="________Debugger"></span><span id="________debugger"></span><span id="________DEBUGGER"></span> *Debugger*  
This does not have to be the same debugger as the one used by the debugging client -- WinDbg, KD, and CDB are all interchangeable for purposes of remote debugging through the debugger.

<span id="________Server"></span><span id="________server"></span><span id="________SERVER"></span> *Server*  
This is the network name or IP address of the computer on which the debugging server was created. The two initial backslashes (\\\) are optional on the command line, but are not permitted in the WinDbg dialog box.

<span id="________pipe_________PipeName"></span><span id="________pipe_________pipename"></span><span id="________PIPE_________PIPENAME"></span> **pipe=** *PipeName*  
If NPIPE or SPIPE protocol is used, *PipeName* is the name that was given to the pipe when the server was created.

If you are not logged on to the client computer with an account that has access to the server computer, you must provide a user name and password. On the client computer, in a Command Prompt window, enter the following command.

**net use \\\\**<em>Server</em>**\\ipc$ /user:**<em>UserName</em>

where *Server* is the name of the server computer, and *UserName* is the name of an account that has access to the server computer.

When you are prompted, enter the password for *UserName*.

After this command succeeds, you can activate a debugging client by using the **-remote** command-line option or by using the WinDbg graphical interface.

**Note**  You might need to enable file and printer sharing on the server computer. In Control Panel, navigate to **Network and Internet &gt; Network and Sharing Center&gt; Advanced sharing settings**. Select **Turn on file and printer sharing**.

 

<span id="________port_________Socket"></span><span id="________port_________socket"></span><span id="________PORT_________SOCKET"></span> **port=** *Socket*  
If TCP or SSL protocol is used, *Socket* is the same socket port number that was used when the server was created.

<span id="clicon"></span><span id="CLICON"></span>**clicon**  
Specifies that the debugging server will try to connect to the client through a reverse connection. The client must use **clicon** if and only if the server is using **clicon**. In most cases, the debugging client is started before the debugging server when a reverse connection is used.

<span id="________port_________COMPort"></span><span id="________port_________comport"></span><span id="________PORT_________COMPORT"></span> **port=** *COMPort*  
If COM protocol is used, *COMPort* specifies the COM port to be used. The prefix "COM" is optional -- for example, both "com2" and "2" are acceptable.

<span id="baud_________BaudRate"></span><span id="baud_________baudrate"></span><span id="BAUD_________BAUDRATE"></span>**baud=** *BaudRate*  
If COM protocol is used, *BaudRate* should match the baud rate chosen when the server was created.

<span id="channel_________COMChannel"></span><span id="channel_________comchannel"></span><span id="CHANNEL_________COMCHANNEL"></span>**channel=** *COMChannel*  
If COM protocol is used, *COMChannel* should match the channel number chosen when the server was created.

<span id="________proto_________Protocol"></span><span id="________proto_________protocol"></span><span id="________PROTO_________PROTOCOL"></span> **proto=** *Protocol*  
If SSL or SPIPE protocol is used, *Protocol* should match the secure protocol used when the server was created.

<span id="________Cert"></span><span id="________cert"></span><span id="________CERT"></span> *Cert*  
If SSL or SPIPE protocol is used, you should use the identical **certuser=**<em>Cert</em> or **machuser=** *Cert* parameter that was used when the server was created.

<span id="________password_________Password"></span><span id="________password_________password"></span><span id="________PASSWORD_________PASSWORD"></span> **password=** *Password*  
If a password was used when the server was created, *Password* must be supplied in order to create the debugging client. It must match the original password. Passwords are case-sensitive. If the wrong password is supplied, the error message will specify "Error 0x80004005." Passwords must be twelve characters or less in length.

<span id="________ipversion_6"></span><span id="________IPVERSION_6"></span> **ipversion=6**  
(Debugging Tools for Windows 6.6.07 and earlier only) Forces the debugger to use IP version 6 rather than version 4 when using TCP to connect to the Internet. In Windows Vista and later versions, the debugger attempts to auto-default to IP version 6, making this option unnecessary.

Command-line options used to start new debugging sessions (like **-p**) cannot be used by the debugging client, but only by the server. Configuration options (like **-n**) will work from either the client or the server.

 

 





