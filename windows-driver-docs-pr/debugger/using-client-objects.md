---
title: Using Client Objects
description: Using Client Objects
keywords: ["Debugger Engine, COM Interfaces"]
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Using Client Objects


For an overview of the role of client objects in interacting with the debugger engine, see [Client Objects](client-objects.md).

In general, a client's methods may be called only from the thread in which the client was created. Typically, methods called from the wrong thread will fail immediately. The notable exception to this rule is the method [**CreateClient**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugclient5-createclient); this method may be called from any thread, and returns a new client that can be used in the thread from which it was called. Other exceptions are documented in the reference section.

A string describing a client object is returned by the method [**GetIdentity**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugclient5-getidentity) or can be written to the engine's output stream using [**OutputIdentity**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugclient5-outputidentity).

### <span id="com_interfaces"></span><span id="COM_INTERFACES"></span>COM Interfaces

The debugger engine API contains several COM like interfaces; they implement the **IUnknown** interface.

The interfaces described in the section [Debug Engine Interfaces](client-com-interfaces.md) is implemented by the client (though not necessarily at the latest version). You may use the COM method **IUnknown::QueryInterface** to obtain each of these interfaces from any of the others.

The clients implement the **IUnknown** COM interface and use it for maintaining reference counts and interface selection. However, the clients are not registered COM objects. The method **IUnknown::AddRef** is used to increment the reference count on the object, and the method **IUnknown::Release** is used to decrement the reference count. When **IUnknown::QueryInterface** is called, the reference count is incremented, so when a client interface pointer is no longer needed **IUnknown::Release** should be called to decrement the reference count.

The reference count will be initialized to one when the client object is created using [**DebugCreate**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-debugcreate) or [**DebugConnect**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-debugconnect).

See the Platform SDK for more information about when reference counts should be incremented and decremented.

**IUnknown::QueryInterface**, **DebugCreate**, and **DebugConnect** each take an interface ID as one of their arguments. This interface ID can be obtained using the **\_\_uuidof** operator. For example:

```cpp
IDebugClient * debugClient;
HRESULT Hr = DebugCreate( __uuidof(IDebugClient), (void **)&debugClient );
```

**Important**  The IDebug\* interfaces such as [**IDebugEventCallbacks**](/windows-hardware/drivers/ddi/dbgeng/nn-dbgeng-idebugeventcallbacks) interface, although COM like, are not proper COM APIs. Calling these interfaces from managed code is an unsupported scenario. Issues such as garbage collection and thread ownership, lead to system instability when the interfaces are called with managed code.

 

 

