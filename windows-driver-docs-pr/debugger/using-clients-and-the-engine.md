---
title: Using Clients and the Engine
description: Using Clients and the Engine
ms.assetid: 899184f5-334b-4fd1-98ce-64475650ace5
keywords: ["DbgEng Extensions, engine client objects"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Using Clients and the Engine


## <span id="ddk_using_clients_and_the_engine_dbx"></span><span id="DDK_USING_CLIENTS_AND_THE_ENGINE_DBX"></span>


A DbgEng extension interacts with the [debugger engine](introduction.md#debugger-engine) through a client object.

When an extension function is called, it is passed a client. The extension function should use this client for all its interaction with the debugger engine, unless it has a specific reason to use another client.

An extension library may create its own client object upon initialization by using [**DebugCreate**](https://msdn.microsoft.com/library/windows/hardware/ff540469). This client can be used to register callback objects from the DLL.

**Note**   Care should be taken when modifying the client passed to an extension function. In particular, registering callbacks with this client could disrupt the input, output, or event handling of the debugger. It is recommended that a new client be created to register callbacks.

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Using%20Clients%20and%20the%20Engine%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




