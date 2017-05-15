---
title: Events
description: Events
ms.assetid: 2b086e78-ac4d-4f9c-a006-65f6f50b33f1
keywords: ["Debugger Engine, events"]
---

# Events


## <span id="events"></span><span id="EVENTS"></span>


The debugger engine provides facilities for monitoring and responding to events in the target. When an event occurs, the engine suspends the target (often only briefly), it then notifies all of the clients of the event, who in turn instruct the engine on how execution should proceed in the target.

To notify a client of an event, the engine calls the event callback object that is registered with the client. The engine provides each event callback with details of the event, and the event callback instructs the engine on how execution should proceed in the target. When different event callbacks provide conflicting instructions, the engine acts on the instruction with the highest precedence (see [**DEBUG\_STATUS\_XXX**](https://msdn.microsoft.com/library/windows/hardware/ff541651)), which typically means choosing the instruction that involves the least execution of the target.

**Note**   While the event callback is handling the event, the target is suspended and the debugging session is accessible; however, because the engine was waiting for an event--either explicitly during a [**WaitForEvent**](https://msdn.microsoft.com/library/windows/hardware/ff561229) call or implicitly by executing a command such as [**g (Go)**](g--go-.md) or [**p (Step)**](p--step-.md)--the event callback cannot call **WaitForEvent**, and if it attempts to execute any commands that would cause the debugger to execute, for example **g (Go)** or **p (Step)**, the engine will interpret these commands as an instruction on how to proceed.

 

### <span id="event_filters"></span><span id="EVENT_FILTERS"></span>Event Filters

The debugger engine also provides *event filters*, which are a simpler alternative for basic event monitoring. The event filters provide a few simple rules that specify whether an event should be printed to the debugger's output stream or break into the debugger. They can also be used to execute debugger commands when an event occurs.

### <span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For details about monitoring events, see [Monitoring Events](monitoring-events.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Events%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




