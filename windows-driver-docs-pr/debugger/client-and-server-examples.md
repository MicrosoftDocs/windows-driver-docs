---
title: Client and Server Examples
description: Client and Server Examples
ms.assetid: 78dea1c0-6e94-4980-8042-375f11386d53
keywords: ["remote debugging through the debugger, examples"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Client and Server Examples


## <span id="ddk_client_and_server_examples_dbg"></span><span id="DDK_CLIENT_AND_SERVER_EXAMPLES_DBG"></span>


Suppose one person is running an application on a computer named *\\\\BOX17*. This application has problems, but the debugging technician is at a different site.

The first person sets up a debugging server using CDB on *\\\\BOX17*. The target application has a process ID of 122. TCP protocol is chosen, with a socket port number of 1025. The server is started by entering the following command in an elevated Command Prompt window (Run as Administrator):

```console
E:\Debugging Tools for Windows> cdb -server tcp:port=1025 -p 122
```

On the other computer, the technician decides to use WinDbg as the debugging client. It can be started with this command:

```console
G:\Debugging Tools> windbg -remote tcp:server=BOX17,port=1025
```

Here is another example. In this case, NPIPE protocol is chosen, and CDB is used instead of WinDbg. The first user chooses a pipe name. This can be any alphanumeric string -- in this example, "MainPipe". The first user opens an elevated Command Prompt window (Run as Administrator) and starts a debugging server by entering this command:

```console
E:\Debugging Tools for Windows> cdb -server npipe:pipe=MainPipe -v winmine.exe 
```

The technician is logged on to the client computer with an account that does not have access to the server computer. But the technician knows the username and password for an account that does have access to the server computer. The username for that account is Contoso. The technician enters the following command:

```console
net use \\BOX17\ipc$ /user:Contoso
```

When prompted, the technician enters the password for the Contoso account.

The technician is not sure what name was used for the named pipe, so she queries BOX17 for available debugging servers.

```console
G:\Debugging Tools> cdb -QR \\BOX17 
Servers on \\BOX17:
Debugger Server - npipe:Pipe=MainPipe
Remote Process Server - npipe:Pipe=AnotherPipe
```

Two pipes are shown. However, only one is a debugging server -- the other is a process server, and we are not interested in that. So **MainPipe** must be the correct name. The technician uses the following command to start the debugging client:

```console
G:\Debugging Tools> cdb -remote npipe:server=BOX17,pipe=MyPipe 
```

### <span id="using_a_secure_server"></span><span id="USING_A_SECURE_SERVER"></span>Using a Secure Server

Here is an example of a secure server. This server uses secure sockets layer with an S-Channel protocol of TLS1. The debugger will look for the certificate in the machine store. The certificate is specified by its hexadecimal thumbprint.

```console
D:\> cdb -server "ssl:proto=tls1,machuser=ab 38 f7 ae 13 20 ac da 05 14 65 60 30 83 7b 83 09 2c d2 34,port=1234" notepad.exe
```

 

 





