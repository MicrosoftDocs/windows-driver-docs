---
title: Client Objects
description: Client Objects
ms.assetid: 173a67f1-093e-4462-8e2c-41d0f10106d0
keywords: ["Debugger Engine, client objects", "client objects"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Client Objects


## <span id="client-objects"></span><span id="CLIENT_OBJECTS"></span>


Almost all interaction with the [debugger engine](introduction.md#debugger-engine) is through *client objects*, often simply referred to as *clients*. Each client provides an implementation of the top-level engine interfaces. Each interface provides a different set of methods, which can be used to interact with the engine and, through the engine, the targets. An instance of the engine can have many clients, each with its own state.

### <span id="primary-clients"></span><span id="PRIMARY_CLIENTS"></span>Primary Clients

A *primary client* is a client that has joined the current debugging session. Initially, when a new client object is created, it is not a primary client. A client becomes a primary client when it is used to acquire a target (for example, by calling [**CreateProcess2**](https://msdn.microsoft.com/library/windows/hardware/ff539323)) or is connected to the debugging session using [**ConnectSession**](https://msdn.microsoft.com/library/windows/hardware/ff539245). The debugger command [**.clients**](-clients--list-debugging-clients-.md) lists only the primary clients.

### <span id="callback-objects"></span><span id="CALLBACK_OBJECTS"></span>Callback Objects

Callback objects can be registered with each client. There are three types of callback objects:

1.  **Input Callback Objects** (or *input callbacks*): the engine calls input callbacks to request input. For example, a debugger with a console window could register an input callback to provide the engine with input from the user, or a debugger might register an input callback to provide the engine with input from a file.

2.  **Output Callback Objects** (or *output callbacks*): the engine calls output callbacks to display output. For example, a debugger with a console window could register an output callback to present the debugger's output to the user, or a debugger might register an output callback to send the output to a log file.

3.  **Event Callback Objects** (or *event callbacks*): the engine calls event callbacks whenever an event occurs in a target (or there is a change in the engine's state). For example, a debugger extension library could register an event callback to monitor certain events or perform automated actions when an particular event occurs.

### <span id="remote-debugging"></span><span id="REMOTE_DEBUGGING"></span>Remote Debugging

Client objects facilitate communication to remote instances of the host engine. The [**DebugConnect**](https://msdn.microsoft.com/library/windows/hardware/ff540465) function creates a client object that is connected to a remote engine instance; methods called on this client are executed by the remote engine and callback objects registered locally with the client will be called when the remote engine makes callback calls.

### <span id="additional-information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For details about creating and using client objects, see [Using Callback Objects](using-callback-objects.md). For details about registering callback objects, see Using Callback Objects.

 

 





