---
title: Process Servers (User Mode)
description: Process Servers (User Mode)
ms.assetid: 9391fcd4-c64f-4c2b-89c2-da09be7646d1
keywords: ["remote debugging through a process server", "process server", "process server, overview", "smart client (user mode)", "DbgSrv", "DbgSrv, overview"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Process Servers (User Mode)


## <span id="ddk_process_servers_user_mode__dbg"></span><span id="DDK_PROCESS_SERVERS_USER_MODE__DBG"></span>


Remote debugging through a process server involves running a small application called a *process server* on the server computer. Then a user-mode debugger is started on the client computer. Since this debugger will be doing all of the actual processing, it is called the *smart client*.

The Debugging Tools for Windows package includes a process server called DbgSrv (dbgsrv.exe) for use in user mode.

The two computers do not have to be running the same version of Windows; they can be running any version of Windows. However, the debugger binaries used on the client and the DbgSrv binary used on the server must be from the same release of the Debugging Tools for Windows package. This method cannot be used for dump-file debugging.

To set up this remote session, the process server is set up first, and then the smart client is activated. Any number of smart clients can operate through a single process server -- these debugging sessions will remain separate and will not interfere with each other. If a debugging session is ended, the process server will continue to run and can be used for new debugging sessions.

## <span id="in_this_section"></span>In this section


-   [**Activating a Process Server**](activating-a-process-server.md)
-   [**Searching for Process Servers**](searching-for-process-servers.md)
-   [**Activating a Smart Client**](activating-a-smart-client.md)
-   [Process Server Examples](process-server-examples.md)
-   [Controlling a Process Server Session](controlling-a-process-server-session.md)

 

 





