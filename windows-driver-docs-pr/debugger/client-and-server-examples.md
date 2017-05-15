---
title: Client and Server Examples
description: Client and Server Examples
ms.assetid: 78dea1c0-6e94-4980-8042-375f11386d53
keywords: ["remote debugging through the debugger, examples"]
---

# Client and Server Examples


## <span id="ddk_client_and_server_examples_dbg"></span><span id="DDK_CLIENT_AND_SERVER_EXAMPLES_DBG"></span>


Suppose one person is running an application on a computer named *\\\\BOX17*. This application has problems, but the debugging technician is at a different site.

The first person sets up a debugging server using CDB on *\\\\BOX17*. The target application has a process ID of 122. TCP protocol is chosen, with a socket port number of 1025. The server is started by entering the following command in an elevated Command Prompt window (Run as Administrator):

```
E:\Debugging Tools for Windows> cdb -server tcp:port=1025 -p 122
```

On the other computer, the technician decides to use WinDbg as the debugging client. It can be started with this command:

```
G:\Debugging Tools> windbg -remote tcp:server=BOX17,port=1025
```

Here is another example. In this case, NPIPE protocol is chosen, and CDB is used instead of WinDbg. The first user chooses a pipe name. This can be any alphanumeric string -- in this example, "MainPipe". The first user opens an elevated Command Prompt window (Run as Administrator) and starts a debugging server by entering this command:

```
E:\Debugging Tools for Windows> cdb -server npipe:pipe=MainPipe -v winmine.exe 
```

The technician is logged on to the client computer with an account that does not have access to the server computer. But the technician knows the username and password for an account that does have access to the server computer. The username for that account is Contoso. The technician enters the following command:

```
net use \\BOX17\ipc$ /user:Contoso
```

When prompted, the technician enters the password for the Contoso account.

The technician is not sure what name was used for the named pipe, so she queries BOX17 for available debugging servers.

```
G:\Debugging Tools> cdb -QR \\BOX17 
Servers on \\BOX17:
Debugger Server - npipe:Pipe=MainPipe
Remote Process Server - npipe:Pipe=AnotherPipe
```

Two pipes are shown. However, only one is a debugging server -- the other is a process server, and we are not interested in that. So **MainPipe** must be the correct name. The technician uses the following command to start the debugging client:

```
G:\Debugging Tools> cdb -remote npipe:server=BOX17,pipe=MyPipe 
```

### <span id="using_a_secure_server"></span><span id="USING_A_SECURE_SERVER"></span>Using a Secure Server

Here is an example of a secure server. This server uses secure sockets layer with an S-Channel protocol of TLS1. The debugger will look for the certificate in the machine store. The certificate is specified by its hexadecimal thumbprint.

```
D:\> cdb -server "ssl:proto=tls1,machuser=ab 38 f7 ae 13 20 ac da 05 14 65 60 30 83 7b 83 09 2c d2 34,port=1234" notepad.exe
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Client%20and%20Server%20Examples%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




