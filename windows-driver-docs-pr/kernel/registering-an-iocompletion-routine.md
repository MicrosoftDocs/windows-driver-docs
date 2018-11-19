---
title: Registering an IoCompletion Routine
description: Registering an IoCompletion Routine
ms.assetid: 413d8463-b2ce-44b6-846c-f853b5cd580e
keywords: ["IoCompletion routines", "registering IoCompletion routines"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Registering an IoCompletion Routine





To register an [*IoCompletion*](https://msdn.microsoft.com/library/windows/hardware/ff548354) routine, a dispatch routine calls [**IoSetCompletionRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff549679), supplying the *IoCompletion* routine's address and the IRP that it will subsequently pass on to lower drivers using [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336).

When it calls **IoSetCompletionRoutine**, the dispatch routine specifies the circumstances in which the I/O manager should call the specified *IoCompletion* routine. You can choose to have the *IoCompletion* routine called if a lower level driver completes the IRP successfully (*InvokeOnSuccess*), completes the IRP with an error status value (*InvokeOnError*), or cancels the IRP (*InvokeOnCancel*), in any combination.

The purpose of an *IoCompletion* routine is to monitor what lower-level drivers did with the IRP and to do additional completion processing, if necessary. Specifically, the most common uses for a driver's *IoCompletion* routines are the following:

-   To dispose of an IRP that the driver allocated with [**IoAllocateIrp**](https://msdn.microsoft.com/library/windows/hardware/ff548257) or [**IoBuildAsynchronousFsdRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548310)

    Any higher-level driver that allocates an IRP using either of these support routines must supply an *IoCompletion* routine for that IRP. The *IoCompletion* routine must call [**IoFreeIrp**](https://msdn.microsoft.com/library/windows/hardware/ff549113) to dispose of driver-allocated IRPs.

-   To reuse an incoming IRP to request that lower drivers complete some number of operations, such as partial transfers, until the original request can be satisfied and completed by the *IoCompletion* routine

-   To retry a request that a lower driver completed with an error

    Highest-level drivers, such as file systems, are more likely to have *IoCompletion* routines that attempt to retry requests than are intermediate drivers, except possibly class drivers layered above a closely coupled port driver. However, any intermediate driver use *IoCompletion* routines to retry requests.

While a highest-level or intermediate driver's [*DispatchReadWrite*](https://msdn.microsoft.com/library/windows/hardware/ff543381) routine is most likely to process IRPs that require an *IoCompletion* routine, any dispatch routine in any driver that passes IRPs on to lower drivers can register an *IoCompletion* routine.

For driver-allocated IRPs and reused IRPs, the dispatch routine must call **IoSetCompletionRoutine** with the following Boolean parameters:

-   *InvokeOnSuccess* set to **TRUE**

-   *InvokeOnError* set to **TRUE**

-   *InvokeOnCancel* set to **TRUE** if any lower driver in the chain might handle cancelable IRPs

    Usually, *InvokeOnCancel* is set to **TRUE**, regardless of whether an IRP might be returned with STATUS\_CANCELLED, to ensure that the *IoCompletion* routine frees each driver-allocated IRP or checks the completion status of each reuse of an IRP.

A dispatch routine that allocates IRPs for lower drivers using **IoAllocateIrp** or [**IoBuildAsynchronousFsdRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548310)must set an *IoCompletion* routine for each driver-allocated IRP.

-   The dispatch routine must set up state about both the original IRP and its allocated IRP(s) for the *IoCompletion* routine to use. At a minimum, the *IoCompletion* routine needs access to the original IRP and a count of how many additional IRPs were allocated.

-   The dispatch routine should call **IoSetCompletionRoutine** with all *InvokeOnXxx* parameters set to **TRUE** for the IRP(s) it allocates.

A dispatch routine that reuses IRPs for a sequence of operations, or that retries I/O operation, must call **IoSetCompletionRoutine** for each IRP that will be reused or retried.

-   The dispatch routine must save the original IRP's state information, for subsequent use by the *IoCompletion* routine.

    For example, a [*DispatchReadWrite*](https://msdn.microsoft.com/library/windows/hardware/ff543381) routine must save the relevant transfer parameters of an input IRP for the *IoCompletion* routine before setting up a partial transfer for the next-lower driver in that IRP. Saving the parameters is particularly important if the *DispatchReadWrite* routine modifies any parameters that the *IoCompletion* routine needs to determine when the original request has been satisfied.

-   If the *IoCompletion* routine can retry the request, the dispatch routine must set up a driver-determined upper limit for the number of retries its *IoCompletion* routine should attempt before it completes the original IRP with an error.

-   If an IRP is to be reused, the dispatch routine should call **IoSetCompletionRoutine** with all *InvokeOnXxx* parameters set to **TRUE**.

-   For an asynchronous request, the dispatch routine of any intermediate driver must call [**IoMarkIrpPending**](https://msdn.microsoft.com/library/windows/hardware/ff549422) for the original IRP. It must then return STATUS\_PENDING after it has sent the IRP on to lower drivers.

 

 




