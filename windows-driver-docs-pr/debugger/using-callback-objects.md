---
title: Using Callback Objects
description: Using Callback Objects
keywords: ["Debugger Engine API, callback objects", "callback objects", "callback objects, event callbacks", "event callbacks", "callback objects, input callbacks", "input callbacks", "callback objects, output callbacks", "output callbacks"]
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Using Callback Objects


There are three callback COM like interfaces that are used by the engine: [IDebugEventCallbacks](/windows-hardware/drivers/ddi/dbgeng/nn-dbgeng-idebugeventcallbacks) for notifying [debugger extensions](debugger-extensions.md) and applications of changes to the engine or target, [IDebugInputCallbacks](/windows-hardware/drivers/ddi/dbgeng/nn-dbgeng-idebuginputcallbacks) for requesting input, and [IDebugOutputCallbacks](/windows-hardware/drivers/ddi/dbgeng/nn-dbgeng-idebugoutputcallbacks) for sending output.

Callback objects are registered with clients. At most, one instance of each of the three callback interfaces can be registered with each client (the Unicode and ASCII versions of a interface count as the same interface).

When a client is created, the engine remembers the thread in which it was created. The engine uses this same thread whenever it makes a call to a callback instance registered with the client. If the thread is in use, the engine will queue the calls it needs to make. To allow the engine to make these calls, the method [*DispatchCallbacks*](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugclient5-dispatchcallbacks) should be called whenever a client's thread is idle. The method [**ExitDispatch**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugclient5-exitdispatch) will cause *DispatchCallbacks* to return. If the thread is the same thread that was used to start the debugger session, then the engine can make the callback calls during the [**WaitForEvent**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugcontrol3-waitforevent) method, and *DispatchCallbacks* does not need to be called.

The method [**FlushCallbacks**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugclient5-flushcallbacks) tells the engine to send all buffered output to the output callbacks.

### <span id="event_callbacks"></span><span id="EVENT_CALLBACKS"></span>Event Callback Objects

The [IDebugEventCallbacks](/windows-hardware/drivers/ddi/dbgeng/nn-dbgeng-idebugeventcallbacks) interface is used by the engine to notify the debugger extensions and applications of [events](events.md#events) and changes to the engine and target. An implementation of **IDebugEventCallbacks** can be registered with a client using [*SetEventCallbacks*](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugclient5-seteventcallbacks). The current implementation registered with a client can be found using [*GetEventCallbacks*](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugclient5-geteventcallbacks). The number of event callbacks registered across all clients can be found using [*GetNumberEventCallbacks*](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugclient5-getnumbereventcallbacks).

For details on how the engine manages events, see [Monitoring Events](monitoring-events.md).

### <span id="input_callbacks"></span><span id="INPUT_CALLBACKS"></span>Input Callback Objects

The [IDebugInputCallbacks](/windows-hardware/drivers/ddi/dbgeng/nn-dbgeng-idebuginputcallbacks) interface is used by the engine to request input from debugger extensions and applications. An implementation of **IDebugInputCallbacks** can be registered with a client using [*SetInputCallbacks*](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugclient5-setinputcallbacks). The current implementation registered with a client can be found using [*GetInputCallbacks*](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugclient5-getinputcallbacks). The number of input callbacks registered across all clients can be found using [*GetNumberInputCallbacks*](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugclient5-getnumberinputcallbacks).

For details on how the engine manages input, see [Input and Output](using-input-and-output.md).

### <span id="output_callbacks"></span><span id="OUTPUT_CALLBACKS"></span>Output Callback Objects

The **IDebugOutputCallbacks** interface is used by the engine to send output to the debugger extensions and applications. An implementation of **IDebugOutputCallbacks** can be registered with a client using [*SetOutputCallbacks*](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugclient5-setoutputcallbacks). The current implementation registered with a client can be found using [*GetOutputCallbacks*](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugclient5-getoutputcallbacks). The number of output callbacks registered across all clients can be found using [*GetNumberOutputCallbacks*](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugclient5-getnumberoutputcallbacks).

For details on how the engine manages output, see [Input and Output](using-input-and-output.md).

**Note**   As is typical for COM objects, the engine will call **IUnknown::AddRef** on a callback COM object when it is registered with a client, and **IUnknown::Release** when the object is replaced or the client is deleted.

 

 

