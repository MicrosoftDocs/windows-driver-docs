---
title: Event Information
description: Event Information
ms.assetid: e6621b5d-f1af-4021-8832-43f79835a6c1
keywords: ["targets, events"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Event Information


Whenever a debugging session is accessible, there is a *last event*. This is the event that caused the session to become accessible. The *event target* is the target which generated the last event. When the session becomes accessible, the current target is set to the event target. The details of the last event are returned by [**GetLastEventInformation**](https://msdn.microsoft.com/library/windows/hardware/ff546982). The instruction pointer for the last event and the memory at the instruction pointer when the event occurred are returned by the [**Request**](https://msdn.microsoft.com/library/windows/hardware/ff554564) operations [**DEBUG\_REQUEST\_GET\_CAPTURED\_EVENT\_CODE\_OFFSET**](https://msdn.microsoft.com/library/windows/hardware/ff541561) and [**DEBUG\_REQUEST\_READ\_CAPTURED\_EVENT\_CODE\_STREAM**](https://msdn.microsoft.com/library/windows/hardware/ff541572).

If the target is a crash dump file, the *last event* is the last event that occurred before the dump file was created. This event is stored in the dump file and the engine generates it for the event callbacks when the dump file is acquired as a debugging target.

If the target is a kernel-mode target and a [*bug check*](https://msdn.microsoft.com/library/windows/hardware/ff556272#wdkgloss-bug-check) occurred, the bug check code and related parameters can be found using [**ReadBugCheckData**](https://msdn.microsoft.com/library/windows/hardware/ff553517).

If the target is a user-mode Minidump, the dump file generator may store an additional event. Typically, this is the event that provoked the generator to save the dump file. Details of this event are returned by [**GetStoredEventInformation**](https://msdn.microsoft.com/library/windows/hardware/ff548431) and the [**Request**](https://msdn.microsoft.com/library/windows/hardware/ff554564) operations [**DEBUG\_REQUEST\_TARGET\_EXCEPTION\_CONTEXT**](https://msdn.microsoft.com/library/windows/hardware/ff541606), [**DEBUG\_REQUEST\_TARGET\_EXCEPTION\_THREAD**](https://msdn.microsoft.com/library/windows/hardware/ff541623), and [**DEBUG\_REQUEST\_TARGET\_EXCEPTION\_RECORD**](https://msdn.microsoft.com/library/windows/hardware/ff541616).

Dump files may contain a static list of events. Each event represents a snapshot of the target at a particular point in time. The number of events in this list is returned by [**GetNumberEvents**](https://msdn.microsoft.com/library/windows/hardware/ff547906). For a description of each event in the list, use [**GetEventIndexDescription**](https://msdn.microsoft.com/library/windows/hardware/ff546630). To set an event from this list as the current event, use the method [**SetNextEventIndex**](https://msdn.microsoft.com/library/windows/hardware/ff556737); after calling [**WaitForEvent**](https://msdn.microsoft.com/library/windows/hardware/ff561229), the event becomes the current event. To determine which event in the list is the current event, use [**GetCurrentEventIndex**](https://msdn.microsoft.com/library/windows/hardware/ff545755).

 

 





