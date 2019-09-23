---
title: Handling Events
description: Handling Events
ms.assetid: 2cd7ccf3-12f5-4ad0-a7c9-a0f437b72445
keywords:
- Stream.sys class driver WDK Windows 2000 Kernel , events
- streaming minidrivers WDK Windows 2000 Kernel , events
- minidrivers WDK Windows 2000 Kernel Streaming , events
- events WDK streaming minidriver
- event sets WDK streaming minidriver
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Handling Events





Minidrivers may support event sets. Both the device as a whole and individual streams can receive requests to enable or disable events. The class driver handles event enable and disable requests. It queues each enabled event, with a separate queue for each stream, and for the device. If an event is disabled, the class driver deletes it from the queue. Note that the class driver queues each enabled event, whether the minidriver does its own synchronization.

The minidriver supplies the event sets it supports in the **DeviceEventsArray** member of the [**HW\_STREAM\_HEADER**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/strmini/ns-strmini-_hw_stream_header) structure. Each stream supplies the event sets it supports in the **StreamEventsArray** of the [**HW\_STREAM\_INFORMATION**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/strmini/ns-strmini-_hw_stream_information) structure for that stream.

The minidriver defines an event set it handles through the [**KSEVENT\_SET**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/ns-ks-ksevent_set) data structure, which in turn points to the array of [**KSEVENT\_ITEM**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/ns-ks-ksevent_item) structures, one for each event in the event set.

The minidriver provides a [*StrMiniEvent*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/strmini/nc-strmini-phw_event_routine) callback routine for each stream that can receive event requests, as well as a callback for the device itself, if it can receive event requests. If the *StrMiniEvent* routine returns a status code other than SUCCESS, the class driver will not queue the event.

When a client makes an event enable request, it passes a [**KSEVENTDATA**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/ns-ks-kseventdata) structure, which describes how the event should be signaled once it occurs, optionally followed by event-specific parameters. When the class driver receives the request, it builds a [**KSEVENT\_ENTRY**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/ns-ks-_ksevent_entry) structure to describe how the event should be triggered. It queues the KSEVENT\_ENTRY structures for each event. The minidriver can use the [**StreamClassGetNextEvent**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/strmini/nf-strmini-streamclassgetnextevent) routine to examine the event queue.

When the event actually occurs, the minidriver signals the class driver by calling either [**StreamClassDeviceNotification**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/strmini/nf-strmini-streamclassdevicenotification) or [**StreamClassStreamNotification**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/strmini/nf-strmini-streamclassstreamnotification). The minidriver can signal events in several different ways: it can signal that a specific event has occurred, or it can signal that all events of a specific type has occurred. See **StreamClassDeviceNotification** or **StreamClassStreamNotification** for details.

The class driver can parse a [**KSEVENTDATA**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/ns-ks-kseventdata) structure to create its [**KSEVENT\_ENTRY**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/ns-ks-_ksevent_entry) structure, but it cannot do the same for any event-specific parameters that follow it in the original request. The minidriver can allocate additional space after the KSEVENT\_ENTRY structure for a specific type of event, by providing a nonzero value for the **ExtraEntryData** member of the KSEVENT\_ITEM it used to declare the event. When *StrMiniEvent* is called for that type of event, it should store any event-specific parameters from KSEVENTDATA in this memory.

 

 




