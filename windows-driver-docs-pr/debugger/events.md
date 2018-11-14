---
title: Events
description: Events
ms.assetid: 2b086e78-ac4d-4f9c-a006-65f6f50b33f1
keywords: ["Debugger Engine, events"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
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

 

 





