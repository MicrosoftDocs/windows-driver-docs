---
title: Implementing an IoCompletion Routine
description: Implementing an IoCompletion Routine
ms.assetid: 669860b1-5e85-4b28-a9b1-1ccf8c689b7a
keywords: ["IoCompletion routines", "IoCompleteRequest routine", "priority boosts WDK IRPs"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Implementing an IoCompletion Routine





On entry, an [*IoCompletion*](https://msdn.microsoft.com/library/windows/hardware/ff548354) routine receives a *Context* pointer. When a dispatch routine calls [**IoSetCompletionRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff549679), it can supply a *Context* pointer. This pointer can reference whatever driver-determined context information the *IoCompletion* routine requires to process an IRP. Note that the context area cannot be pageable because the *IoCompletion* routine can be called at IRQL = DISPATCH\_LEVEL.

**Consider the following implementation guidelines for IoCompletion routines:**

-   An *IoCompletion* routine can check the IRP's [I/O status block](i-o-status-blocks.md) to determine the result of the I/O operation.

-   If the input IRP was allocated by the dispatch routine using [**IoAllocateIrp**](https://msdn.microsoft.com/library/windows/hardware/ff548257) or [**IoBuildAsynchronousFsdRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548310), the *IoCompletion* routine must call [**IoFreeIrp**](https://msdn.microsoft.com/library/windows/hardware/ff549113) to release that IRP, preferably before it completes the original IRP.

    -   The *IoCompletion* routine must release any per-IRP resources the dispatch routine allocated for the driver-allocated IRP, preferably before it frees the corresponding IRP.

        For example, if the dispatch routine allocates an MDL with [**IoAllocateMdl**](https://msdn.microsoft.com/library/windows/hardware/ff548263) and calls [**IoBuildPartialMdl**](https://msdn.microsoft.com/library/windows/hardware/ff548324) for a partial-transfer IRP it allocates, the *IoCompletion* routine must release the MDL with [**IoFreeMdl**](https://msdn.microsoft.com/library/windows/hardware/ff549126). If it allocates resources to maintain state about the original IRP, it must free those resources, preferably before it calls [**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343) with the original IRP and definitely before it returns control.

        In general, before freeing or completing an IRP, the *IoCompletion* routine should free any per-IRP resources allocated by the Dispatch routine. Otherwise, the driver must maintain state about the resources to be freed before its *IoCompletion* routine returns control from completing the original request.

    -   If the *IoCompletion* routine cannot complete the original IRP with STATUS\_SUCCESS, it must set the I/O status block in the original IRP to the value returned in the driver-allocated IRP that caused the *IoCompletion* routine to fail the original request.

    -   If the *IoCompletion* routine will complete the original request with STATUS\_PENDING, it must call [**IoMarkIrpPending**](https://msdn.microsoft.com/library/windows/hardware/ff549422) with the original IRP before it calls **IoCompleteRequest**.

    -   If the *IoCompletion* routine must fail the original IRP with an error STATUS\_*XXX*, it can [log an error](logging-errors.md). However, it is the responsibility of the underlying device driver to log any device I/O errors that occur, so *IoCompletion* routines usually do not log errors.

    -   When the *IoCompletion* routine has processed and freed the driver-allocated IRP, the routine must return control with STATUS\_MORE\_PROCESSING\_REQUIRED.

        Returning STATUS\_MORE\_PROCESSING\_REQUIRED from the *IoCompletion* routine forestalls the I/O manager's completion processing for a driver-allocated and freed IRP. A second call to **IoCompleteRequest** causes the I/O manager to resume calling the IRP's completion routines, starting with the completion routine immediately above the routine that returned STATUS\_MORE\_PROCESSING\_REQUIRED.

-   If the *IoCompletion* routine reuses an incoming IRP to send one or more requests to lower drivers, or if the routine retries failed operations, it should update whatever context the *IoCompletion* routine maintains about each reuse or retry of the IRP. Then it can set up the next-lower driver's I/O stack location again, call [**IoSetCompletionRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff549679) with its own entry point, and call [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336) for the IRP.

    -   The *IoCompletion* routine should not call [**IoMarkIrpPending**](https://msdn.microsoft.com/library/windows/hardware/ff549422) at each reuse or retry of the IRP.

        The dispatch routine already marked the original IRP as pending. Until all drivers in the chain complete the original IRP with **IoCompleteRequest**, it remains pending.

    -   Before retrying a request, the *IoCompletion* routine should reset the I/O status block with STATUS\_SUCCESS for **Status** and zero for **Information**, possibly after saving the returned error information.

        For each retry, the *IoCompletion* routine usually decrements a retry count set up by the Dispatch routine. Typically, the *IoCompletion* routine must call **IoCompleteRequest** to fail the IRP when some limited number of retries have failed.

    -   The *IoCompletion* routine must return STATUS\_MORE\_PROCESSING\_REQUIRED after it calls [**IoSetCompletionRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff549679) and [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336) with an IRP that is being reused or retried.

        Returning STATUS\_MORE\_PROCESSING\_REQUIRED from the *IoCompletion* routine forestalls the I/O manager's completion processing of a reused or retried IRP.

    -   If the *IoCompletion* routine cannot complete the original IRP with STATUS\_SUCCESS, it must leave the I/O status block as returned by lower drivers for the reuse or retry operation that causes the *IoCompletion* routine to fail the IRP.

    -   If the *IoCompletion* routine will complete the original request with STATUS\_PENDING, it must call **IoMarkIrpPending** with the original IRP before it calls **IoCompleteRequest**.
    -   If the *IoCompletion* routine must fail the original IRP with an error STATUS\_*XXX*, it can [log an error](logging-errors.md). However, it is the responsibility of the underlying device driver to log any device I/O errors that occur, so *IoCompletion* routines usually do not log errors.

-   Any driver that sets an *IoCompletion* routine in an IRP and then passes the IRP down to a lower driver should check the **IRP-&gt;PendingReturned** flag in the *IoCompletion* routine. If the flag is set, the *IoCompletion* routine must call **IoMarkIrpPending** with the IRP. Note, however, that a driver that passes down the IRP and then waits on an event should not mark the IRP pending. Instead, its *IoCompletion* routine should signal the event and return STATUS\_MORE\_PROCESSING\_REQUIRED.

-   The *IoCompletion* routine must release any resources the dispatch routine allocated for processing the original IRP, preferably before the *IoCompletion* routine calls **IoCompleteRequest** with the original IRP and definitely before the *IoCompletion* routine returns control from completing the original IRP.

If any higher-level driver has set its *IoCompletion* routine in the original IRP, that driver's *IoCompletion* routine is not called until the *IoCompletion* routines of all lower-level drivers have been called.

### Supplying a Priority Boost in Calls to IoCompleteRequest

If a lowest-level device driver can complete an IRP in its dispatch routine, it calls [**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343) with a *PriorityBoost* of IO\_NO\_INCREMENT. No run-time priority increase is needed because the driver can assume that the original requester did not wait for its I/O operation to be completed.

Otherwise, the lowest-level driver supplies a system-defined and device-type-specific value that boosts the requester's run-time priority to compensate for the time the requester waited on its device I/O request. See Wdm.h or Ntddk.h for the boost values.

Higher-level drivers apply the same *PriorityBoost* as their respective underlying device drivers when they call **IoCompleteRequest**.

### Effect of Calling IoCompleteRequest

When a driver calls **IoCompleteRequest**, the I/O manager fills that driver's I/O stack location with zeros before calling the next higher-level driver, if any, that has set up an *IoCompletion* routine to be called for the IRP.

A higher-level driver's *IoCompletion* routine can check only the IRP's I/O status block to determine how all lower drivers handled the request.

The caller of **IoCompleteRequest** must not attempt to access the just-completed IRP. Such an attempt is a programming error that causes a system crash.

 

 




