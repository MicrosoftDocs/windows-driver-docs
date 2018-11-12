---
title: E (Windows Debugger Glossary)
description: Glossary page - E
Robots: noindex, nofollow
ms.assetid: 1e32bd40-8c77-4c6b-913c-6ec26707ed36
ms.author: domars
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# E


<span id="effective_processor_type"></span><span id="EFFECTIVE_PROCESSOR_TYPE"></span>**effective processor type**  
The processor type the debugger uses when dealing with the target computer. The effective processor type affects how the debugger sets breakpoints, accesses registers, gets stack traces, and performs other processor-specific actions.

<span id="engine"></span><span id="ENGINE"></span>**engine**  
See debugger engine.

<span id="event"></span><span id="EVENT"></span>**event**  
The debugger engine monitors some of the events that occur in its targets. These include a breakpoint being triggered, an exception, thread and process creation, module loading, and internal debugger engine changes.

<span id="event_filter"></span><span id="EVENT_FILTER"></span>**event filter**  
A collection of rules that influence how the debugger engine proceeds after an event has occurred in a target. There are three types of event filters: specific event filters, specific exception filters, and arbitrary exception filters.

<span id="event_callback_objects"></span><span id="EVENT_CALLBACK_OBJECTS"></span>**event callback objects**  
Instances of the [IDebugEventCallbacks](https://msdn.microsoft.com/library/windows/hardware/ff550550) interface which have been registered with a client. The engine notifies the event callbacks whenever an event occurs.

<span id="event_callbacks"></span><span id="EVENT_CALLBACKS"></span>**event callbacks**  
See event callback objects.

<span id="event_process"></span><span id="EVENT_PROCESS"></span>**event process**  
The process for which the last event occurred.

<span id="event_target"></span><span id="EVENT_TARGET"></span>**event target**  
The target for which the last event occurred.

<span id="event_thread"></span><span id="EVENT_THREAD"></span>**event thread**  
The thread for which the last event occurred.

<span id="executing_processor_type"></span><span id="EXECUTING_PROCESSOR_TYPE"></span>**executing processor type**  
The type of the processor in the current processor context.

<span id="exception"></span><span id="EXCEPTION"></span>**exception**  
An error condition resulting from the execution of a particular machine instruction or from the target indicating that it has encountered an error. Exceptions can be hardware or software-related errors.

An exception is an and is identified by its .

<span id="exception_code"></span><span id="EXCEPTION_CODE"></span>**exception code**  
An identifier which determines the type of an exception event.

<span id="exception_filter"></span><span id="EXCEPTION_FILTER"></span>**exception filter**  
An event filter for an exception event specified by exception code.

<span id="extension"></span><span id="EXTENSION"></span>**extension**  
See debugger extension.

<span id="extension_command"></span><span id="EXTENSION_COMMAND"></span>**extension command**  
See debugger extension.

 

 





