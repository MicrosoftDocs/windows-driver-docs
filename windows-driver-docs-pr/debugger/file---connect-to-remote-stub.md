---
title: File Connect to Remote Stub
description: File Connect to Remote Stub
ms.assetid: 7357db85-babe-4729-9a20-76ba284f5bf3
keywords: ["File Connect to Remote Stub"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# File | Connect to Remote Stub


Click **Connect to Remote Stub** on the **File** menu to make WinDbg a smart client and connect to a process server or a KD connection server.

This command is equivalent to using the -premote command line option in user mode, or the -k kdsrv transport protocol command-line option in kernel mode. You can use this command only when WinDbg is in dormant mode.

You cannot use this command to connect to a debugging server; for that purpose, use [File | Connect to Remote Session](file---connect-to-remote-session.md) instead.

### <span id="connect_to_remote_stub_server_dialog_box"></span><span id="CONNECT_TO_REMOTE_STUB_SERVER_DIALOG_BOX"></span>Connect to Remote Stub Server Dialog Box

When you click **Connect to Remote Stub**, the **Connect to Remote Stub Server** dialog box appears. You can use this dialog box to enter the remote connection parameters or to browse a list of process servers and KD connection servers.

To manually specify the remote connection parameters, enter one of the following strings in the **Connection string** box:

```text
npipe:server=Server,pipe=PipeName[,password=Password] 

tcp:server=Server,port=Socket[,password=Password][,ipversion=6]

tcp:clicon=Server,port=Socket[,password=Password][,ipversion=6]

com:port=COMPort,baud=BaudRate,channel=COMChannel[,password=Password] 

spipe:proto=Protocol,{certuser=Cert|machuser=Cert},server=Server,pipe=PipeName[,password=Password] 

ssl:proto=Protocol,{certuser=Cert|machuser=Cert},server=Server,port=Socket[,password=Password]

ssl:proto=Protocol,{certuser=Cert|machuser=Cert},clicon=Server,port=Socket[,password=Password]
```

The various parameters in the preceding options have the following possible values:

<span id="Server"></span><span id="server"></span><span id="SERVER"></span>*Server*  
The network name of the computer on which the process server or KD connection server was created. Do not precede this name with backslashes (**\\\\**).

<span id="PipeName"></span><span id="pipename"></span><span id="PIPENAME"></span>*PipeName*  
If you use the NPIPE or SPIPE protocol, *PipeName* is the name that was given to the pipe when the server was created.

<span id="Socket"></span><span id="socket"></span><span id="SOCKET"></span>*Socket*  
If you use the TCP or SSL protocol, *Socket* is the same socket port number that was used when the server was created.

<span id="COMPort"></span><span id="comport"></span><span id="COMPORT"></span>*COMPort*  
If you use the COM protocol, *COMPort* specifies the COM port to use. The "COM" prefix is optional (for example, both "com2" and "2" are correct).

<span id="BaudRate"></span><span id="baudrate"></span><span id="BAUDRATE"></span>*BaudRate*  
If you use the COM protocol, *BaudRate* should match the baud rate that you chose when the server was created.

<span id="COMChannel"></span><span id="comchannel"></span><span id="COMCHANNEL"></span>*COMChannel*  
If you use the COM protocol, *COMChannel* should match the channel number that you chose when the server was created.

<span id="Protocol"></span><span id="protocol"></span><span id="PROTOCOL"></span>*Protocol*  
(Windows 2000 and later) If you use the SSL or SPIPE protocol, *Protocol* should match the secure protocol that you used when the server was created.

<span id="Cert"></span><span id="cert"></span><span id="CERT"></span>*Cert*  
(Windows 2000 and later) If you use the SSL or SPIPE protocol, you should use the identical **certuser=**<em>Cert</em> or **machuser=**<em>Cert</em> parameter that was used when the server was created.

<span id="clicon"></span><span id="CLICON"></span>**clicon**  
Specifies that the process server or KD connection server will try to connect to the client through a reverse connection. The client must use **clicon** if and only if the server is using **clicon**. In most cases, the smart client is started before the server when a reverse connection is used.

<span id="Password"></span><span id="password"></span><span id="PASSWORD"></span>*Password*  
If you used a password when the server was created, you must supply *Password* to create the smart client. This value must match the original password. Passwords are case-sensitive. If the wrong password is supplied, the error message will specify "Error 0x80004005".

<span id="ipversion_6"></span><span id="IPVERSION_6"></span>**ipversion=6**  
(Debugging Tools for Windows 6.6.07 and earlier only) Forces the debugger to use IP version 6 rather than version 4 when you are using TCP to connect to the Internet. In Windows Vista and later versions, the debugger attempts to auto-default to IP version 6, making this option unnecessary.

Instead of manually specifying the remote connection parameters, you can press the **Browse** button in the **Connect to Remote Stub Server** dialog box and use the **Browse Remote Servers** dialog box.

### <span id="browse_remote_servers_dialog_box"></span><span id="BROWSE_REMOTE_SERVERS_DIALOG_BOX"></span>Browse Remote Servers Dialog Box

In the **Browse Remote Servers** dialog box, in the **Machine** text box, enter the name of the computer that the process server or KD connection server is running on. (The two initial backslashes are optional: "MyBox" and "\\\\MyBox" are both correct.) Then, press the **Refresh** button.

The **Servers** area lists all of the process servers and KD connection servers that are running on that computer. Select any of the listed servers and then press ENTER or click **OK**. (You can also double-click one of the listed servers.) The proper connection string for the process server that you selected will now appear in the **Connection string** box in the **Connect to Remote Stub Server** dialog box.

If the server is password-protected, the connection string includes **Password=\\**<em>. You must replace the asterisk (</em>*\***) with the actual password.

After you specify the server and password, click **OK** to open the connection.

The list of servers in the **Browse Remote Servers** dialog box can also include servers that no longer exist but were shut down improperly. If you connect to one of these nonexistent servers, you will receive an error message.

The list of servers does not include debugging servers. To view those servers, use the [File | Connect to Remote Session](file---connect-to-remote-session.md) command.

### <span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information and for other methods of joining a remote stub session, see [**Activating a Smart Client**](activating-a-smart-client.md) and [**Activating a Smart Client (Kernel Mode)**](activating-a-smart-client--kernel-mode-.md).

 

 





