---
title: Using Client Objects
description: Using Client Objects
ms.assetid: 07311a2e-86a7-4985-9dfa-55a876cd7899
keywords: ["Debugger Engine, COM Interfaces"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Using Client Objects


For an overview of the role of client objects in interacting with the debugger engine, see [Client Objects](client-objects.md).

In general, a client's methods may be called only from the thread in which the client was created. Typically, methods called from the wrong thread will fail immediately. The notable exception to this rule is the method [**CreateClient**](https://msdn.microsoft.com/library/windows/hardware/ff539320); this method may be called from any thread, and returns a new client that can be used in the thread from which it was called. Other exceptions are documented in the reference section.

A string describing a client object is returned by the method [**GetIdentity**](https://msdn.microsoft.com/library/windows/hardware/ff546831) or can be written to the engine's output stream using [**OutputIdentity**](https://msdn.microsoft.com/library/windows/hardware/ff553219).

### <span id="com_interfaces"></span><span id="COM_INTERFACES"></span>COM Interfaces

The debugger engine API contains several COM like interfaces; they implement the **IUnknown** interface.

The interfaces described in the section [Debug Engine Interfaces](https://msdn.microsoft.com/library/windows/hardware/ff539131) is implemented by the client (though not necessarily at the latest version). You may use the COM method **IUnknown::QueryInterface** to obtain each of these interfaces from any of the others.

The clients implement the **IUnknown** COM interface and use it for maintaining reference counts and interface selection. However, the clients are not registered COM objects. The method **IUnknown::AddRef** is used to increment the reference count on the object, and the method **IUnknown::Release** is used to decrement the reference count. When **IUnknown::QueryInterface** is called, the reference count is incremented, so when a client interface pointer is no longer needed **IUnknown::Release** should be called to decrement the reference count.

The reference count will be initialized to one when the client object is created using [**DebugCreate**](https://msdn.microsoft.com/library/windows/hardware/ff540469) or [**DebugConnect**](https://msdn.microsoft.com/library/windows/hardware/ff540465).

See the Platform SDK for more information about when reference counts should be incremented and decremented.

**IUnknown::QueryInterface**, **DebugCreate**, and **DebugConnect** each take an interface ID as one of their arguments. This interface ID can be obtained using the **\_\_uuidof** operator. For example:

```
IDebugClient * debugClient;
HRESULT Hr = DebugCreate( __uuidof(IDebugClient), (void **)&debugClient );
```

**Important**  The IDebug\* interfaces such as [**IDebugEventCallbacks**](https://msdn.microsoft.com/library/windows/hardware/ff550550) interface, although COM like, are not proper COM APIs. Calling these interfaces from managed code is an unsupported scenario. Issues such as garbage collection and thread ownership, lead to system instability when the interfaces are called with managed code.

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Using%20Client%20Objects%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




