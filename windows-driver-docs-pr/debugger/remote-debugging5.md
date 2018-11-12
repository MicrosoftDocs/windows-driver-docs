---
title: Remote Debugging (Debugger Engine)
description: Remote debugging occurs when a client's communication with a target is indirect, for example, through a network connection.
ms.assetid: e52cc5fb-9f10-415e-9fe8-6eba71daab6d
keywords: ["Debugger Engine, remote debugging"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Remote Debugging (Debugger Engine)


Remote debugging occurs when a client's communication with a target is indirect, for example, through a network connection. When remote debugging, more than one instance of the debugger engine can be involved in debugging a target. However, exactly one of these instances is responsible for the debugging session; this instance is called the *host engine*.

There are many possible configurations: the client object can be created in the host engine (smart clients), or a different instance of the engine (debugging clients); the host engine can be connected directly to the target (debugging server); or a proxy can be directly connected to the target (process server and kernel connection server).

Multiple clients can simultaneously connect to the host engine. And the host engine can connect to multiple targets in the same debugging session. Optionally, there can be one or more proxies between the clients and the host engine and between the host engine and each target.

Smart clients are client objects that communicate directly with the host engine. A debugging client is created by calling [**DebugConnect**](https://msdn.microsoft.com/library/windows/hardware/ff540465); the client communicates with the host engine using RPC calls that represent method calls in the engine's API (including calls that the host engine makes to the client's [callback objects](client-objects.md#callback-objects)).

A debugging server is an engine instance that communicates directly with the target and is also the host engine. Process servers and kernel connection servers communicate directly with the target but are not the host engine. The host engine communicates with the process server, or kernel connection server, by sending low-level memory, processor, and operating system requests, and the server sends back the results.

**Note**   A typical two-computer setup for kernel debugging--where one computer is the target and the other the host computer--is not considered to be remote debugging as there is only one instance of the engine (on the host computer) and it communicates directly with the target.

 

### <span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For details about performing remote debugging, see [Remote Targets](remote-targets.md).

 

 





