---
title: Event Information
description: Event Information
ms.assetid: e6621b5d-f1af-4021-8832-43f79835a6c1
keywords: ["targets, events"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Event Information


Whenever a debugging session is accessible, there is a *last event*. This is the event that caused the session to become accessible. The *event target* is the target which generated the last event. When the session becomes accessible, the current target is set to the event target. The details of the last event are returned by [**GetLastEventInformation**](https://msdn.microsoft.com/library/windows/hardware/ff546982). The instruction pointer for the last event and the memory at the instruction pointer when the event occurred are returned by the [**Request**](https://msdn.microsoft.com/library/windows/hardware/ff554564) operations [**DEBUG\_REQUEST\_GET\_CAPTURED\_EVENT\_CODE\_OFFSET**](https://msdn.microsoft.com/library/windows/hardware/ff541561) and [**DEBUG\_REQUEST\_READ\_CAPTURED\_EVENT\_CODE\_STREAM**](https://msdn.microsoft.com/library/windows/hardware/ff541572).

If the target is a crash dump file, the *last event* is the last event that occurred before the dump file was created. This event is stored in the dump file and the engine generates it for the event callbacks when the dump file is acquired as a debugging target.

If the target is a kernel-mode target and a [*bug check*](https://msdn.microsoft.com/library/windows/hardware/ff556272#wdkgloss-bug-check) occurred, the bug check code and related parameters can be found using [**ReadBugCheckData**](https://msdn.microsoft.com/library/windows/hardware/ff553517).

If the target is a user-mode Minidump, the dump file generator may store an additional event. Typically, this is the event that provoked the generator to save the dump file. Details of this event are returned by [**GetStoredEventInformation**](https://msdn.microsoft.com/library/windows/hardware/ff548431) and the [**Request**](https://msdn.microsoft.com/library/windows/hardware/ff554564) operations [**DEBUG\_REQUEST\_TARGET\_EXCEPTION\_CONTEXT**](https://msdn.microsoft.com/library/windows/hardware/ff541606), [**DEBUG\_REQUEST\_TARGET\_EXCEPTION\_THREAD**](https://msdn.microsoft.com/library/windows/hardware/ff541623), and [**DEBUG\_REQUEST\_TARGET\_EXCEPTION\_RECORD**](https://msdn.microsoft.com/library/windows/hardware/ff541616).

Dump files may contain a static list of events. Each event represents a snapshot of the target at a particular point in time. The number of events in this list is returned by [**GetNumberEvents**](https://msdn.microsoft.com/library/windows/hardware/ff547906). For a description of each event in the list, use [**GetEventIndexDescription**](https://msdn.microsoft.com/library/windows/hardware/ff546630). To set an event from this list as the current event, use the method [**SetNextEventIndex**](https://msdn.microsoft.com/library/windows/hardware/ff556737); after calling [**WaitForEvent**](https://msdn.microsoft.com/library/windows/hardware/ff561229), the event becomes the current event. To determine which event in the list is the current event, use [**GetCurrentEventIndex**](https://msdn.microsoft.com/library/windows/hardware/ff545755).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Event%20Information%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




