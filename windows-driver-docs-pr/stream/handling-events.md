---
title: Handling Events
author: windows-driver-content
description: Handling Events
ms.assetid: 2cd7ccf3-12f5-4ad0-a7c9-a0f437b72445
keywords:
- Stream.sys class driver WDK Windows 2000 Kernel , events
- streaming minidrivers WDK Windows 2000 Kernel , events
- minidrivers WDK Windows 2000 Kernel Streaming , events
- events WDK streaming minidriver
- event sets WDK streaming minidriver
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Handling Events


## <a href="" id="ddk-handling-events-ksg"></a>


Minidrivers may support event sets. Both the device as a whole and individual streams can receive requests to enable or disable events. The class driver handles event enable and disable requests. It queues each enabled event, with a separate queue for each stream, and for the device. If an event is disabled, the class driver deletes it from the queue. Note that the class driver queues each enabled event, whether the minidriver does its own synchronization.

The minidriver supplies the event sets it supports in the **DeviceEventsArray** member of the [**HW\_STREAM\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff559690) structure. Each stream supplies the event sets it supports in the **StreamEventsArray** of the [**HW\_STREAM\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff559692) structure for that stream.

The minidriver defines an event set it handles through the [**KSEVENT\_SET**](https://msdn.microsoft.com/library/windows/hardware/ff561867) data structure, which in turn points to the array of [**KSEVENT\_ITEM**](https://msdn.microsoft.com/library/windows/hardware/ff561862) structures, one for each event in the event set.

The minidriver provides a [*StrMiniEvent*](https://msdn.microsoft.com/library/windows/hardware/ff568457) callback routine for each stream that can receive event requests, as well as a callback for the device itself, if it can receive event requests. If the *StrMiniEvent* routine returns a status code other than SUCCESS, the class driver will not queue the event.

When a client makes an event enable request, it passes a [**KSEVENTDATA**](https://msdn.microsoft.com/library/windows/hardware/ff561750) structure, which describes how the event should be signaled once it occurs, optionally followed by event-specific parameters. When the class driver receives the request, it builds a [**KSEVENT\_ENTRY**](https://msdn.microsoft.com/library/windows/hardware/ff561853) structure to describe how the event should be triggered. It queues the KSEVENT\_ENTRY structures for each event. The minidriver can use the [**StreamClassGetNextEvent**](https://msdn.microsoft.com/library/windows/hardware/ff568244) routine to examine the event queue.

When the event actually occurs, the minidriver signals the class driver by calling either [**StreamClassDeviceNotification**](https://msdn.microsoft.com/library/windows/hardware/ff568239) or [**StreamClassStreamNotification**](https://msdn.microsoft.com/library/windows/hardware/ff568266). The minidriver can signal events in several different ways: it can signal that a specific event has occurred, or it can signal that all events of a specific type has occurred. See **StreamClassDeviceNotification** or **StreamClassStreamNotification** for details.

The class driver can parse a [**KSEVENTDATA**](https://msdn.microsoft.com/library/windows/hardware/ff561750) structure to create its [**KSEVENT\_ENTRY**](https://msdn.microsoft.com/library/windows/hardware/ff561853) structure, but it cannot do the same for any event-specific parameters that follow it in the original request. The minidriver can allocate additional space after the KSEVENT\_ENTRY structure for a specific type of event, by providing a nonzero value for the **ExtraEntryData** member of the KSEVENT\_ITEM it used to declare the event. When *StrMiniEvent* is called for that type of event, it should store any event-specific parameters from KSEVENTDATA in this memory.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Handling%20Events%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


