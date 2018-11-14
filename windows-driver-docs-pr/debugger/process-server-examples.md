---
title: Process Server Examples
description: Process Server Examples
ms.assetid: f87e6ff5-05a4-4dae-8151-913ea469b4ec
keywords: ["process server, examples"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Process Server Examples


## <span id="ddk_process_server_examples_dbg"></span><span id="DDK_PROCESS_SERVER_EXAMPLES_DBG"></span>


Suppose one person is running an application on a computer named \\\\BOX17. This application has problems, but the debugging technician is at a different site.

The first person sets up a process server using DbgSrv on \\\\BOX17. The target application has a process ID of 122. TCP protocol is chosen, with a socket port number of 1025. The server is started with the following command:

```console
E:\Debugging Tools for Windows> dbgsrv -t tcp:port=1025 
```

On the other computer, the technician starts WinDbg as a smart client with this command:

```console
G:\Debugging Tools> windbg -premote tcp:server=BOX17,port=1025 -p 122 
```

Here is another example. In this case, NPIPE protocol is chosen, and CDB is used instead of WinDbg. The first user chooses a pipe name. This can be any alphanumeric string -- in this example, "AnotherPipe". The first user opens an elevated Command Prompt window (Run as Administrator) and starts a debugging server by entering this command:

```console
E:\Debugging Tools for Windows> dbgsrv -t npipe:pipe=AnotherPipe
```

The technician is logged on to the client computer with an account that does not have access to the server computer. But the technician knows the username and password for an account that does have access to the server computer. The username for that account is Contoso. The technician enters the following command:

```console
net use \\BOX17\ipc$ /user:Contoso
```

When prompted, the technician enters the password for the Contoso account.

The technician is not sure what name was used for the named pipe, so she queries BOX17 for process servers:

```console
G:\Debugging Tools> cdb -QR \\BOX17 
Servers on \\BOX17:
Debugger Server - npipe:Pipe=MainPipe
Remote Process Server - npipe:Pipe=AnotherPipe
```

Two pipes are shown. However, only one is a process server -- the other is a debugging server, and we are not interested in that. So **AnotherPipe** must be the correct name. The technician enters the following command to start the smart client:

```console
G:\Debugging Tools> cdb -premote npipe:server=BOX17,pipe=AnotherPipe -v sol.exe 
```

For a more complicated example using a process server, see [Symbols in the Middle](symbols-in-the-middle.md).

 

 





