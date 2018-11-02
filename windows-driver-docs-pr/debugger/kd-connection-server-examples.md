---
title: KD Connection Server Examples
description: KD Connection Server Examples
ms.assetid: 5e54dda7-4f79-40e3-bcc5-248a3a047e31
keywords: ["KD connection server, examples"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# KD Connection Server Examples


## <span id="ddk_kd_connection_server_examples_dbg"></span><span id="DDK_KD_CONNECTION_SERVER_EXAMPLES_DBG"></span>


Suppose a debugging technician is not present at the site where the computer to be debugged is located. The debugging technician asks someone at this site to connect this target computer to some other computer with a debug cable.

Let this other computer be at IP address 127.0.0.42. The debug cable connects COM1 on this computer to whichever port has been debug-enabled on the target computer. The KD connection server is started with this command:

```console
E:\Debugging Tools for Windows> kdsrv -t tcp:port=1027 
```

Then at the other location, the technician starts WinDbg as a smart client with this command:

```console
G:\Debugging Tools> windbg -k kdsrv:server=@{tcp:server=127.0.0.42,port=1027},trans=@{com:port=com1,baud=57600} -y SymbolPath 
```

The symbol path will be relative to the computer where the smart client is running.

Here is another example. In this case, NPIPE protocol is chosen, and KD is used instead of WinDbg. The first user chooses a pipe name. This can be any alphanumeric string -- in this example, "KernelPipe". The first user opens an elevated Command Prompt window (Run as Administrator) and starts a debugging server by entering these commands:

```console
E:\Debugging Tools for Windows> set _NT_DEBUG_PORT=com1 
E:\Debugging Tools for Windows> kdsrv -t npipe:pipe=KernelPipe 
```

The technician is logged on to the client computer with an account that does not have access to the server computer. But the technician knows the username and password for an account that does have access to the server computer. The username for that account is Contoso. The technician enters the following command:

```console
net use \\BOX17\ipc$ /user:Contoso
```

When prompted, the technician enters the password for the Contoso account.

The technician is not sure what name was used for the named pipe, so she queries 127.0.0.42 for KD connection servers:

```console
G:\Debugging Tools> cdb -QR 127.0.0.42 
Servers on 127.0.0.42:
Debugger Server - npipe:Pipe=MainPipe
Remote Process Server - npipe:Pipe=AnotherPipe
Remote Kernel Debugger Server - npipe:Pipe=KernelPipe
```

Three pipes are shown. However, only one is a KD connection server -- the others are a debugging server and a user-mode process server. The technician enters the following command can to start the smart client:

```console
G:\Debugging Tools> kd -k kdsrv:server=@{npipe:server=127.0.0.42,pipe=KernelPipe},trans=@{com:baud=57600} -y SymbolPath 
```

Notice that although the baud rate is specified, the port is not. This causes the debugger to default to the port specified by \_NT\_DEBUG\_PORT on the computer where KdSrv is running.

 

 





