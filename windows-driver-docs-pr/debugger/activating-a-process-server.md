---
title: Activating a Process Server
description: To activate a process server, open an elevated Command Prompt window (Run as Administrator), and enter the dbgsrv command.
ms.assetid: 566a4f64-8a14-469b-b50c-20e3c00aa2f8
keywords: ["Activating a Process Server Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- Activating a Process Server
api_type:
- NA
ms.localizationpriority: medium
---

# Activating a Process Server


The process server that is included in Debugging Tools for Windows is called DbgSrv (dbgsrv.exe). To activate a process server, open an elevated Command Prompt window (Run as Administrator), and enter the **dbgsrv** command.

**Note**  You can activate a process server without having elevated privileges, and debugging clients will be able to connect to the server. However, clients will not be able to discover a process server unless it was activated with elevated privileges. For information about how to discover debugging servers, see [Searching for Process Servers](searching-for-process-servers.md).

 

DbgSrv supports several transport protocols: named pipe (NPIPE), TCP, COM port, secure pipe (SPIPE), and secure sockets layer (SSL).

```console
dbgsrv -t npipe:pipe=PipeName[,hidden][,password=Password][,IcfEnable] [[-sifeo Executable] -c[s] AppCmdLine] [-x | -pc] 

dbgsrv -t tcp:port=Socket[,hidden][,password=Password][,ipversion=6][,IcfEnable] [[-sifeo Executable] -c[s] AppCmdLine] [-x | -pc] 

dbgsrv -t tcp:port=Socket,clicon=Client[,password=Password][,ipversion=6] [[-sifeo Executable] -c[s] AppCmdLine] [-x | -pc] 

dbgsrv -t com:port=COMPort,baud=BaudRate,channel=COMChannel[,hidden][,password=Password] [[-sifeo Executable] -c[s] AppCmdLine] [-x | -pc] 

dbgsrv -t spipe:proto=Protocol,{certuser=Cert|machuser=Cert},pipe=PipeName[,hidden][,password=Password] [[-sifeo Executable] -c[s] AppCmdLine] [-x | -pc] 

dbgsrv -t ssl:proto=Protocol,{certuser=Cert|machuser=Cert},port=Socket[,hidden][,password=Password] [[-sifeo Executable] -c[s] AppCmdLine] [-x | -pc] 

dbgsrv -t ssl:proto=Protocol,{certuser=Cert|machuser=Cert},port=Socket,clicon=Client[,password=Password] [[-sifeo Executable] -c[s] AppCmdLine] [-x | -pc] 
```

## <span id="ddk_activating_a_process_server_dbg"></span><span id="DDK_ACTIVATING_A_PROCESS_SERVER_DBG"></span>


The parameters in the previous commands have the following possible values:

<span id="________pipe_________PipeName"></span><span id="________pipe_________pipename"></span><span id="________PIPE_________PIPENAME"></span> **pipe=** *PipeName*  
When NPIPE or SPIPE protocol is used, *PipeName* is a string that will serve as the name of the pipe. Each pipe name should identify a unique process server. If you attempt to reuse a pipe name, you will receive an error message. *PipeName* must not contain spaces or quotation marks. *PipeName* can include a numerical **printf**-style format code, such as **%x** or **%d**. The process server will replace this with the process ID of DbgSrv. A second such code will be replaced with the thread ID of DbgSrv.

**Note**  You might need to enable file and printer sharing on the computer that is running the process server. In Control Panel, navigate to **Network and Internet &gt; Network and Sharing Center&gt; Advanced sharing settings**. Select **Turn on file and printer sharing**.

 

<span id="________port_________Socket"></span><span id="________port_________socket"></span><span id="________PORT_________SOCKET"></span> **port=** *Socket*  
When TCP or SSL protocol is used, *Socket* is the socket port number.

It is also possible to specify a range of ports separated by a colon. DbgSrv will check each port in this range to see if it is free. If it finds a free port and no error occurs, the process server will be created. The smart client will have to specify the actual port being used to connect to the server. To determine the actual port, use any of the methods described in [**Searching for Process Servers**](searching-for-process-servers.md); when this process server is displayed, the port will be followed by two numbers separated by a colon. The first number will be the actual port used; the second can be ignored. For example, if the port was specified as **port=51:60**, and port 53 was actually used, the search results will show "port=53:60". (If you are using the **clicon** parameter to establish a reverse connection, the smart client can specify a range of ports in this manner, while the process server must specify the actual port used.)

<span id="________clicon_________Client"></span><span id="________clicon_________client"></span><span id="________CLICON_________CLIENT"></span> **clicon=** *Client*  
When TCP or SSL protocol is used and the **clicon** parameter is specified, a *reverse connection* will be opened. This means that the process server will try to connect to the smart client, instead of letting the client initiate the contact. This can be useful if you have a firewall that is preventing a connection in the usual direction. *Client* specifies the network name or IP address of the computer on which the smart client exists or will be created. The two initial backslashes (\\\) are optional.

Since the process server is looking for one specific client, you cannot connect multiple clients to the server if you use this method. If the connection is refused or is broken you will have to restart the process server. A reverse-connection process server will not appear when someone uses the **-QR** command-line option to display all active servers.

**Note**   When **clicon** is used, it is best to start the smart client before the process server is created, although the usual order (server before client) is also permitted.

 

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
Prevents the process server from appearing when someone uses the **-QR** command-line option to display all active servers.

<span id="________password_________Password"></span><span id="________password_________password"></span><span id="________PASSWORD_________PASSWORD"></span> **password=** *Password*  
Requires a smart client to supply the specified password in order to connect to the process server. *Password* can be any alphanumeric string, up to twelve characters in length.

**Warning**   Using a password with TCP, NPIPE, or COM protocol only offers a small amount of protection, because the password is not encrypted. When a password is used with SSL or SPIPE protocol, it is encrypted. If you want to establish a secure remote session, you must use SSL or SPIPE protocol.

 

<span id="________ipversion_6"></span><span id="________IPVERSION_6"></span> **ipversion=6**  
(Debugging Tools for Windows 6.6.07 and earlier only) Forces the debugger to use IP version 6 rather than version 4 when using TCP to connect to the Internet. In Windows Vista and later versions, the debugger attempts to auto-default to IP version 6, making this option unnecessary.

<span id="________IcfEnable"></span><span id="________icfenable"></span><span id="________ICFENABLE"></span> **IcfEnable**  
(Windows XP and later versions only) Causes the debugger to enable the necessary port connections for TCP or named pipe communication when the Internet Connection Firewall is active. By default, the Internet Connection Firewall disables the ports used by these protocols. When **IcfEnable** is used with a TCP connection, the debugger causes Windows to open the port specified by the *Socket* parameter. When **IcfEnable** is used with a named pipe connection, the debugger causes Windows to open the ports used for named pipes (ports 139 and 445). The debugger does not close these ports after the connection terminates.

<span id="-sifeo__________Executable"></span><span id="-sifeo__________executable"></span><span id="-SIFEO__________EXECUTABLE"></span>**-sifeo** *Executable*  
Suspends the Image File Execution Option (IFEO) value for the given image. *Executable* should include the file name of the executable image, including the file name extensions. The **-sifeo** option allows DbgSrv to be set as the IFEO debugger for an image created by the **-c** option, without causing recursive invocation due to the IFEO setting. This option can be used only if **-c** is used.

<span id="________-c"></span><span id="________-C"></span> **-c**  
Causes DbgSrv to create a new process. You can use this to create a process that you intend to debug. This is similar to spawning a new process from the debugger, except that this process will not be debugged when it is created. To debug this process, determine its PID and use the **-p** option when starting the smart client to debug this process.

<span id="s"></span><span id="S"></span>**s**  
Causes the newly-created process to be immediately suspended. If you are using this option, it is recommended that you use CDB as your smart client, and that you start the smart client with the **-pb** command-line option, in conjunction with **-p PID**. If you include the **-pb** option on the command line, the process will resume when the debugger attaches to it; otherwise you can resume the process with the [**~\*m**](-m--resume-thread-.md) command.

<span id="AppCmdLine"></span><span id="appcmdline"></span><span id="APPCMDLINE"></span>*AppCmdLine*  
Specifies the full command line of the process to be created. *AppCmdLine* can be either a Unicode or ASCII string, and can include any printable character. All text that appears after the **-c\[s\]** parameter will be taken to form the string *AppCmdLine*.

<span id="-x"></span><span id="-X"></span>**-x**  
Causes the remainder of the command line to be ignored. This option is useful if you are launching DbgSrv from an application that may append unwanted text to its command line.

<span id="________-pc"></span><span id="________-PC"></span> **-pc**  
Causes the remainder of the command line to be ignored. This option is useful if you are launching DbgSrv from an application that may append unwanted text to its command line. A syntax error results if **-pc** is the final element on the DbgSrv command line. Aside from this restriction, **-pc** is identical to **-x**.

You can start any number of process servers on one computer. However, this is generally unnecessary, since one process server can be used by any number of smart clients (each engaged in a different debugging session).

 

 





