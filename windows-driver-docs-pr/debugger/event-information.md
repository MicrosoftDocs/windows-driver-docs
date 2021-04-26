---
title: Event Information
description: Event Information
keywords: ["targets, events"]
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Event Information


Whenever a debugging session is accessible, there is a *last event*. This is the event that caused the session to become accessible. The *event target* is the target which generated the last event. When the session becomes accessible, the current target is set to the event target. The details of the last event are returned by [**GetLastEventInformation**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugcontrol3-getlasteventinformation). The instruction pointer for the last event and the memory at the instruction pointer when the event occurred are returned by the [**Request**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugadvanced3-request) operations [**DEBUG\_REQUEST\_GET\_CAPTURED\_EVENT\_CODE\_OFFSET**](./debug-request-get-captured-event-code-offset.md) and [**DEBUG\_REQUEST\_READ\_CAPTURED\_EVENT\_CODE\_STREAM**](./debug-request-read-captured-event-code-stream.md).

If the target is a crash dump file, the *last event* is the last event that occurred before the dump file was created. This event is stored in the dump file and the engine generates it for the event callbacks when the dump file is acquired as a debugging target.

If the target is a kernel-mode target and a *bug check* occurred, the bug check code and related parameters can be found using [**ReadBugCheckData**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugcontrol3-readbugcheckdata).

If the target is a user-mode Minidump, the dump file generator may store an additional event. Typically, this is the event that provoked the generator to save the dump file. Details of this event are returned by [**GetStoredEventInformation**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugcontrol4-getstoredeventinformation) and the [**Request**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugadvanced3-request) operations [**DEBUG\_REQUEST\_TARGET\_EXCEPTION\_CONTEXT**](./debug-request-target-exception-context.md), [**DEBUG\_REQUEST\_TARGET\_EXCEPTION\_THREAD**](./debug-request-target-exception-thread.md), and [**DEBUG\_REQUEST\_TARGET\_EXCEPTION\_RECORD**](./debug-request-target-exception-record.md).

Dump files may contain a static list of events. Each event represents a snapshot of the target at a particular point in time. The number of events in this list is returned by [**GetNumberEvents**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugcontrol3-getnumberevents). For a description of each event in the list, use [**GetEventIndexDescription**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugcontrol3-geteventindexdescription). To set an event from this list as the current event, use the method [**SetNextEventIndex**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugcontrol3-setnexteventindex); after calling [**WaitForEvent**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugcontrol3-waitforevent), the event becomes the current event. To determine which event in the list is the current event, use [**GetCurrentEventIndex**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugcontrol3-getcurrenteventindex).

 

