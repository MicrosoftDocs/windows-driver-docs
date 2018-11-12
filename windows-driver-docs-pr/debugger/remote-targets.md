---
title: Remote Targets
description: Remote Targets
ms.assetid: ed7ea3dc-07d1-481c-90e0-7f0b0e77ad42
keywords: ["Debugger Engine API, targets, remote", "Debugger Engine API, debugging servers", "Debugger Engine API, process servers", "Debugger Engine API, kernel connection servers", "Debugger Engine API, smart clients"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Remote Targets


## <span id="ddk_remote_debugging_dbx"></span><span id="DDK_REMOTE_DEBUGGING_DBX"></span>


There are two different forms of remote debugging, depending on which computer (remote client or server) is the host computer. The *host computer* is the computer on which the [debugger engine](introduction.md#debugger-engine) is active. On the other computer, the debugger engine is merely acting as a proxy relaying commands and data to the host engine.

All debugger operations -- such as executing commands and [extensions](introduction.md#extensions), and symbol loading -- are performed by the host engine. A debugger session is also relative to the host engine.

To list the debugging servers and process servers currently running on a computer, use [**OutputServers**](https://msdn.microsoft.com/library/windows/hardware/ff553247).

### <span id="debugging_server_and_debugging_client"></span><span id="DEBUGGING_SERVER_AND_DEBUGGING_CLIENT"></span>Debugging Servers and Debugging Clients

A *debugging server* is an instance of the debugger engine acting as a host and listening for connections from debugging clients. The method [**StartServer**](https://msdn.microsoft.com/library/windows/hardware/ff558813) will tell the debugger engine to start listening for connections from debugging clients.

A *debugging client* is an instance of the debugger engine acting as a proxy, sending debugger commands and I/O to the debugging server. The function [**DebugConnect**](https://msdn.microsoft.com/library/windows/hardware/ff540465) can be used to connect to the debugging server.

The client object returned by **DebugConnect** is not automatically joined to the debugger session on the debugging server. The method [**ConnectSession**](https://msdn.microsoft.com/library/windows/hardware/ff539245) can be used to join the session, synchronizing input and output.

The communication between a debugging server and a debugging client mostly consists of debugger commands and RPC calls sent to the server, and command output sent back to the client.

### <span id="process_server_and_smart_client"></span><span id="PROCESS_SERVER_AND_SMART_CLIENT"></span>Process Servers, Kernel Connection Servers, and Smart Clients

*Process servers* and *kernel connection servers* are both instances of the debugger engine acting as proxies, listening for connections from smart clients, and performing memory, processor, or operating system operations as requested by these remote clients. A *process server* facilitates the debugging of processes that are running on the same computer. A *kernel connection server* facilitates the debugging of a Windows kernel debugging target that is connected to the computer that is running the connection server. A process server can be started using the method [**StartProcessServer**](https://msdn.microsoft.com/library/windows/hardware/ff558810) or the program [DbgSrv](process-servers--user-mode-.md). The method [**WaitForProcessServerEnd**](https://msdn.microsoft.com/library/windows/hardware/ff561230) will wait for a process server started with **StartProcessServer** to end. A kernel connection server can be activated using the program [**KdSrv**](activating-a-kd-connection-server.md).

A *smart client* is an instance of the debugger engine acting as a host engine and connected to a process server. The method [**ConnectProcessServer**](https://msdn.microsoft.com/library/windows/hardware/ff539237) will connect to a process server. Once connected, the methods described in [Live User-Mode Targets](live-user-mode-targets.md) can be used.

When the remote client is finished with the process server, it can disconnect using [**DisconnectProcessServer**](https://msdn.microsoft.com/library/windows/hardware/ff541969), or it can use [**EndProcessServer**](https://msdn.microsoft.com/library/windows/hardware/ff542993) to request that the process server shut down. To shut down the process server from the computer that it is running on, use Task Manager to end the process. If the instance of the debugger engine that used **StartProcessServer** is still running, it can use [**Execute**](https://msdn.microsoft.com/library/windows/hardware/ff543208) to issue the debugger command [**.endsrv 0**](-endsrv--end-debugging-server-.md), which will end the process server (this is an exception to the usual behavior of **.endsrv**, which generally does not affect process servers).

The communication between a process server and a smart client typically consists of low-level memory, processor, and operating system operations and requests that are sent from the remote client to the server. Their results are then sent back to the client.

 

 





