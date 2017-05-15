---
title: Client Objects
description: Client Objects
ms.assetid: 173a67f1-093e-4462-8e2c-41d0f10106d0
keywords: ["Debugger Engine, client objects", "client objects"]
---

# Client Objects


## <span id="client_objects"></span><span id="CLIENT_OBJECTS"></span>


Almost all interaction with the [debugger engine](introduction.md#debugger-engine) is through *client objects*, often simply referred to as *clients*. Each client provides an implementation of the top-level engine interfaces. Each interface provides a different set of methods, which can be used to interact with the engine and, through the engine, the targets. An instance of the engine can have many clients, each with its own state.

### <span id="primary_clients"></span><span id="PRIMARY_CLIENTS"></span>Primary Clients

A *primary client* is a client that has joined the current debugging session. Initially, when a new client object is created, it is not a primary client. A client becomes a primary client when it is used to acquire a target (for example, by calling [**CreateProcess2**](https://msdn.microsoft.com/library/windows/hardware/ff539323)) or is connected to the debugging session using [**ConnectSession**](https://msdn.microsoft.com/library/windows/hardware/ff539245). The debugger command [**.clients**](-clients--list-debugging-clients-.md) lists only the primary clients.

### <span id="callback_objects"></span><span id="CALLBACK_OBJECTS"></span>Callback Objects

Callback objects can be registered with each client. There are three types of callback objects:

1.  **Input Callback Objects** (or *input callbacks*): the engine calls input callbacks to request input. For example, a debugger with a console window could register an input callback to provide the engine with input from the user, or a debugger might register an input callback to provide the engine with input from a file.

2.  **Output Callback Objects** (or *output callbacks*): the engine calls output callbacks to display output. For example, a debugger with a console window could register an output callback to present the debugger's output to the user, or a debugger might register an output callback to send the output to a log file.

3.  **Event Callback Objects** (or *event callbacks*): the engine calls event callbacks whenever an event occurs in a target (or there is a change in the engine's state). For example, a debugger extension library could register an event callback to monitor certain events or perform automated actions when an particular event occurs.

### <span id="remote_debugging"></span><span id="REMOTE_DEBUGGING"></span>Remote Debugging

Client objects facilitate communication to remote instances of the host engine. The [**DebugConnect**](https://msdn.microsoft.com/library/windows/hardware/ff540465) function creates a client object that is connected to a remote engine instance; methods called on this client are executed by the remote engine and callback objects registered locally with the client will be called when the remote engine makes callback calls.

### <span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For details about creating and using client objects, see [Using Callback Objects](using-callback-objects.md). For details about registering callback objects, see Using Callback Objects.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Client%20Objects%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




