---
title: Using Clients and the Engine
description: Using Clients and the Engine
keywords: ["DbgEng Extensions, engine client objects"]
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Using Clients and the Engine


## <span id="ddk_using_clients_and_the_engine_dbx"></span><span id="DDK_USING_CLIENTS_AND_THE_ENGINE_DBX"></span>


A DbgEng extension interacts with the [debugger engine](introduction.md#debugger-engine) through a client object.

When an extension function is called, it is passed a client. The extension function should use this client for all its interaction with the debugger engine, unless it has a specific reason to use another client.

An extension library may create its own client object upon initialization by using [**DebugCreate**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-debugcreate). This client can be used to register callback objects from the DLL.

**Note**   Care should be taken when modifying the client passed to an extension function. In particular, registering callbacks with this client could disrupt the input, output, or event handling of the debugger. It is recommended that a new client be created to register callbacks.

 

 

