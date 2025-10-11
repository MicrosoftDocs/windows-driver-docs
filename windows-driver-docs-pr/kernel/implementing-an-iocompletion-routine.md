---
title: Implementing an IoCompletion Routine
description: Implementing an IoCompletion Routine
keywords: ["IoCompletion routines", "IoCompleteRequest routine", "priority boosts WDK IRPs"]
ms.date: 10/10/2025
ms.topic: concept-article
---

# Implementing an IoCompletion Routine

On entry, an [*IoCompletion*](/windows-hardware/drivers/ddi/wdm/nc-wdm-io_completion_routine) routine receives a *Context* pointer. When a dispatch routine calls [**IoSetCompletionRoutine**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iosetcompletionroutine), it can supply a *Context* pointer. This pointer can reference whatever driver-determined context information the *IoCompletion* routine requires to process an IRP. The context area can't be pageable because the *IoCompletion* routine can be called at IRQL = DISPATCH_LEVEL.

**Consider the following implementation guidelines for IoCompletion routines:**

- An *IoCompletion* routine can check the IRP's [I/O status block](i-o-status-blocks.md) to determine the result of the I/O operation.

- If the dispatch routine allocated the input IRP by using [**IoAllocateIrp**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioallocateirp) or [**IoBuildAsynchronousFsdRequest**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iobuildasynchronousfsdrequest), the *IoCompletion* routine must call [**IoFreeIrp**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iofreeirp) to release that IRP, preferably before it completes the original IRP.

  - The *IoCompletion* routine must release any per-IRP resources the dispatch routine allocated for the driver-allocated IRP, preferably before it frees the corresponding IRP.

    For example, if the dispatch routine allocates an MDL with [**IoAllocateMdl**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioallocatemdl) and calls [**IoBuildPartialMdl**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iobuildpartialmdl) for a partial-transfer IRP it allocates, the *IoCompletion* routine must release the MDL with [**IoFreeMdl**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iofreemdl). If it allocates resources to maintain state about the original IRP, it must free those resources, preferably before it calls [**IoCompleteRequest**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocompleterequest) with the original IRP and definitely before it returns control.

    In general, before freeing or completing an IRP, the *IoCompletion* routine should free any per-IRP resources allocated by the dispatch routine. Otherwise, the driver must maintain state about the resources to be freed before its *IoCompletion* routine returns control from completing the original request.

  - If the *IoCompletion* routine can't complete the original IRP with STATUS_SUCCESS, it must set the I/O status block in the original IRP to the value returned in the driver-allocated IRP that caused the *IoCompletion* routine to fail the original request.

  - If the *IoCompletion* routine completes the original request with STATUS_PENDING, it must call [**IoMarkIrpPending**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iomarkirppending) with the original IRP before it calls **IoCompleteRequest**.

  - If the *IoCompletion* routine must fail the original IRP with an error STATUS_*XXX*, it can [log an error](logging-errors.md). However, it's the responsibility of the underlying device driver to log any device I/O errors that occur, so *IoCompletion* routines usually don't log errors.

  - When the *IoCompletion* routine processes and frees the driver-allocated IRP, it must return control with STATUS_MORE_PROCESSING_REQUIRED.

    Returning STATUS_MORE_PROCESSING_REQUIRED from the *IoCompletion* routine forestalls the I/O manager's completion processing for a driver-allocated and freed IRP. A second call to **IoCompleteRequest** causes the I/O manager to resume calling the IRP's completion routines, starting with the completion routine immediately above the routine that returned STATUS_MORE_PROCESSING_REQUIRED.

- If the *IoCompletion* routine reuses an incoming IRP to send one or more requests to lower drivers, or if the routine retries failed operations, it should update whatever context the *IoCompletion* routine maintains about each reuse or retry of the IRP. Then it can set up the next-lower driver's I/O stack location again, call [**IoSetCompletionRoutine**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iosetcompletionroutine) with its own entry point, and call [**IoCallDriver**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocalldriver) for the IRP.

  - The *IoCompletion* routine shouldn't call [**IoMarkIrpPending**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iomarkirppending) at each reuse or retry of the IRP.

    The dispatch routine already marked the original IRP as pending. Until all drivers in the chain complete the original IRP with **IoCompleteRequest**, it remains pending.

  - Before retrying a request, the *IoCompletion* routine should reset the I/O status block with STATUS_SUCCESS for **Status** and zero for **Information**, possibly after saving the returned error information.

    For each retry, the *IoCompletion* routine usually decrements a retry count set up by the dispatch routine. Typically, the *IoCompletion* routine must call **IoCompleteRequest** to fail the IRP when some limited number of retries have failed.

  - The *IoCompletion* routine must return STATUS_MORE_PROCESSING_REQUIRED after it calls [**IoSetCompletionRoutine**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iosetcompletionroutine) and [**IoCallDriver**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocalldriver) with an IRP that it's reusing or retrying.

    Returning STATUS_MORE_PROCESSING_REQUIRED from the *IoCompletion* routine forestalls the I/O manager's completion processing of a reused or retried IRP.

  - If the *IoCompletion* routine can't complete the original IRP with STATUS_SUCCESS, it must leave the I/O status block as returned by lower drivers for the reuse or retry operation that causes the *IoCompletion* routine to fail the IRP.

  - If the *IoCompletion* routine will complete the original request with STATUS_PENDING, it must call **IoMarkIrpPending** with the original IRP before it calls **IoCompleteRequest**.
  - If the *IoCompletion* routine must fail the original IRP with an error STATUS_*XXX*, it can [log an error](logging-errors.md). However, it's the responsibility of the underlying device driver to log any device I/O errors that occur, so *IoCompletion* routines usually don't log errors.

- Any driver that sets an *IoCompletion* routine in an IRP and then passes the IRP down to a lower driver should check the **IRP-&gt;PendingReturned** flag in the *IoCompletion* routine. If the flag is set, the *IoCompletion* routine must call **IoMarkIrpPending** with the IRP. However, a driver that passes down the IRP and then waits on an event shouldn't mark the IRP pending. Instead, its *IoCompletion* routine should signal the event and return STATUS_MORE_PROCESSING_REQUIRED.

- The *IoCompletion* routine must release any resources the dispatch routine allocated for processing the original IRP, preferably before the *IoCompletion* routine calls **IoCompleteRequest** with the original IRP and definitely before the *IoCompletion* routine returns control from completing the original IRP.

If any higher-level driver set its *IoCompletion* routine in the original IRP, that driver's *IoCompletion* routine isn't called until the *IoCompletion* routines of all lower-level drivers have been called.

## Supplying a Priority Boost in Calls to IoCompleteRequest

If a lowest-level device driver can complete an IRP in its dispatch routine, it calls [**IoCompleteRequest**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocompleterequest) with a *PriorityBoost* of IO_NO_INCREMENT. No run-time priority increase is needed because the driver can assume that the original requester didn't wait for its I/O operation to be completed.

Otherwise, the lowest-level driver supplies a system-defined and device-type-specific value that boosts the requester's run-time priority to compensate for the time the requester waited on its device I/O request. See Wdm.h or Ntddk.h for the boost values.

Higher-level drivers apply the same *PriorityBoost* as their respective underlying device drivers when they call **IoCompleteRequest**.

## Effect of Calling IoCompleteRequest

When a driver calls **IoCompleteRequest**, the I/O manager fills that driver's I/O stack location with zeros before calling the next higher-level driver, if any, that set up an *IoCompletion* routine to be called for the IRP.

A higher-level driver's *IoCompletion* routine can check only the IRP's I/O status block to determine how all lower drivers handled the request.

The caller of **IoCompleteRequest** must not attempt to access the just-completed IRP. Such an attempt is a programming error that causes a system crash.
