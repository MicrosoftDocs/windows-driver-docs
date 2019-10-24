---
title: Event Information
description: Event Information
ms.assetid: e6621b5d-f1af-4021-8832-43f79835a6c1
keywords: ["targets, events"]
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Event Information


Whenever a debugging session is accessible, there is a *last event*. This is the event that caused the session to become accessible. The *event target* is the target which generated the last event. When the session becomes accessible, the current target is set to the event target. The details of the last event are returned by [**GetLastEventInformation**](https://docs.microsoft.com/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugcontrol3-getlasteventinformation). The instruction pointer for the last event and the memory at the instruction pointer when the event occurred are returned by the [**Request**](https://docs.microsoft.com/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugadvanced3-request) operations [**DEBUG\_REQUEST\_GET\_CAPTURED\_EVENT\_CODE\_OFFSET**](https://docs.microsoft.com/windows-hardware/drivers/debugger/debug-request-get-captured-event-code-offset) and [**DEBUG\_REQUEST\_READ\_CAPTURED\_EVENT\_CODE\_STREAM**](https://docs.microsoft.com/windows-hardware/drivers/debugger/debug-request-read-captured-event-code-stream).

If the target is a crash dump file, the *last event* is the last event that occurred before the dump file was created. This event is stored in the dump file and the engine generates it for the event callbacks when the dump file is acquired as a debugging target.

If the target is a kernel-mode target and a *bug check* occurred, the bug check code and related parameters can be found using [**ReadBugCheckData**](https://docs.microsoft.com/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugcontrol3-readbugcheckdata).

If the target is a user-mode Minidump, the dump file generator may store an additional event. Typically, this is the event that provoked the generator to save the dump file. Details of this event are returned by [**GetStoredEventInformation**](https://docs.microsoft.com/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugcontrol4-getstoredeventinformation) and the [**Request**](https://docs.microsoft.com/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugadvanced3-request) operations [**DEBUG\_REQUEST\_TARGET\_EXCEPTION\_CONTEXT**](https://docs.microsoft.com/windows-hardware/drivers/debugger/debug-request-target-exception-context), [**DEBUG\_REQUEST\_TARGET\_EXCEPTION\_THREAD**](https://docs.microsoft.com/windows-hardware/drivers/debugger/debug-request-target-exception-thread), and [**DEBUG\_REQUEST\_TARGET\_EXCEPTION\_RECORD**](https://docs.microsoft.com/windows-hardware/drivers/debugger/debug-request-target-exception-record).

Dump files may contain a static list of events. Each event represents a snapshot of the target at a particular point in time. The number of events in this list is returned by [**GetNumberEvents**](https://docs.microsoft.com/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugcontrol3-getnumberevents). For a description of each event in the list, use [**GetEventIndexDescription**](https://docs.microsoft.com/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugcontrol3-geteventindexdescription). To set an event from this list as the current event, use the method [**SetNextEventIndex**](https://docs.microsoft.com/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugcontrol3-setnexteventindex); after calling [**WaitForEvent**](https://docs.microsoft.com/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugcontrol3-waitforevent), the event becomes the current event. To determine which event in the list is the current event, use [**GetCurrentEventIndex**](https://docs.microsoft.com/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugcontrol3-getcurrenteventindex).

 

 





