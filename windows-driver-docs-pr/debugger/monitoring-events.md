---
title: Monitoring Events
description: Monitoring Events
ms.assetid: f0381cf9-e568-4789-af08-69d8b2c3ecbf
keywords: ["Debugger Engine, events", "events"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Monitoring%20Events%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




