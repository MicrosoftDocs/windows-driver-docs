---
title: Reusing Framework Request Objects
description: Reusing Framework Request Objects
keywords:
- request processing WDK KMDF , reusing request objects
- request objects WDK KMDF , reusing
- reusing request objects WDK KMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Reusing Framework Request Objects





To improve performance, framework-based drivers that create and send lots of nearly identical asynchronous requests to an I/O target can reuse request objects instead of creating a new request object for each request. A driver can reuse a request object after the request has been completed.

If a driver has created a request object by calling [**WdfRequestCreate**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestcreate) or [**WdfRequestCreateFromIrp**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestcreatefromirp), it can reuse the request by calling [**WdfRequestReuse**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestreuse). A driver can also reuse request objects that it has received from the framework in its I/O queues, but it cannot change the IRP that the received request object contains.

If you are careful to avoid situations that cause the unsuccessful return values described in [**WdfRequestReuse**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestreuse), your driver can call **WdfRequestReuse** from within a [*CompletionRoutine*](/windows-hardware/drivers/ddi/wdfrequest/nc-wdfrequest-evt_wdf_request_completion_routine) callback function. (The *CompletionRoutine* callback function has a VOID return value and therefore cannot report errors.)

If your driver provides a [*CompletionRoutine*](/windows-hardware/drivers/ddi/wdfrequest/nc-wdfrequest-evt_wdf_request_completion_routine) callback function for a request object that it reuses, the driver must call [**WdfRequestSetCompletionRoutine**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestsetcompletionroutine) after calling [**WdfRequestReuse**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestreuse).

 

