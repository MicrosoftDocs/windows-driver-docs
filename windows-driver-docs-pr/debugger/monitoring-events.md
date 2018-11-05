---
title: Monitoring Events
description: Monitoring Events
ms.assetid: f0381cf9-e568-4789-af08-69d8b2c3ecbf
keywords: ["Debugger Engine, events", "events"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Monitoring Events


## <span id="ddk_monitoring_events_dbx"></span><span id="DDK_MONITORING_EVENTS_DBX"></span>


For an overview of events in the [debugger engine](introduction.md#debugger-engine), see [Events](events.md).

Events occurring in a target or the debugger engine may be monitored using the [IDebugEventCallbacks](https://msdn.microsoft.com/library/windows/hardware/ff550550) interface. An **IDebugEventCallbacks** object may be registered with a client using [*SetEventCallbacks*](https://msdn.microsoft.com/library/windows/hardware/ff556671). Each client can only have at most one **IDebugEventCallbacks** object registered with it.

When an **IDebugEventCallbacks** object is registered with a client, the engine will call the object's [**IDebugEventCallbacks::GetInterestMask**](https://msdn.microsoft.com/library/windows/hardware/ff550737) to determine which events the object is interested in. Only events in which the object is interested will be sent to it.

For each type of event, the engine calls a corresponding callback method on [IDebugEventCallbacks](https://msdn.microsoft.com/library/windows/hardware/ff550550). For events from the target, the [**DEBUG\_STATUS\_XXX**](https://msdn.microsoft.com/library/windows/hardware/ff541651) value returned from these calls specifies how the execution of the target should proceed. The engine collects these return values from each **IDebugEventCallbacks** object it calls and acts on the one with the highest precedence.

### <span id="events_from_the_target_that_break_into_the_debugger_by_default"></span><span id="EVENTS_FROM_THE_TARGET_THAT_BREAK_INTO_THE_DEBUGGER_BY_DEFAULT"></span>Events from the Target That Break into the Debugger by Default

The following events break into the debugger by default:

-   Breakpoint Events

-   Exception Events (not documented here)

-   System Error

### <span id="events_from_the_target_that_do_not_break_into_the_debugger_by_default"></span><span id="EVENTS_FROM_THE_TARGET_THAT_DO_NOT_BREAK_INTO_THE_DEBUGGER_BY_DEFAULT"></span>Events from the Target that Do Not Break into the Debugger by Default

The following events do not break into the debugger by default:

-   Create Process Event

-   Exit Process Event

-   Create Thread Event

-   Exit Thread Event

-   Load Module Event

-   Unload Module Event

### <span id="internal_engine_changes"></span><span id="INTERNAL_ENGINE_CHANGES"></span>Internal Engine Changes

The following are not actual events, but are merely internal engine changes:

-   Target Change

-   Engine Change

-   Engine Symbol Change

-   Session Status Change

 

 





