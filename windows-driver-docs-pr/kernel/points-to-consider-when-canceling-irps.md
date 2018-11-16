---
title: Points to Consider When Canceling IRPs
description: Points to Consider When Canceling IRPs
ms.assetid: 16a47033-7147-43a2-a9f8-a215f7e90ff1
keywords: ["canceling IRPs, guidelines", "Cancel routines, guidelines", "cancelable IRPs WDK kernel", "current states WDK IRPs"]
ms.date: 05/08/2018
ms.localizationpriority: medium
---

# Points to Consider When Canceling IRPs





This section discusses guidelines for implementing a *Cancel* routine and handling cancelable IRPs. For more information about handling cancelable IRPs, see the [Flow of Control for Cancel-Safe IRP Queuing](http://go.microsoft.com/fwlink/p/?linkid=57844).

### General Guidelines for All Cancel Routines

The I/O manager holds the cancel spin lock any time it calls a driver's *Cancel* routine. Consequently, every *Cancel* routine must:

-   Call [**IoReleaseCancelSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff549550) before it returns control.

-   Not call [**IoAcquireCancelSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff548196) unless it calls **IoReleaseCancelSpinLock** first.

-   Make a reciprocal call to **IoReleaseCancelSpinLock** for each call it makes to **IoAcquireCancelSpinLock**.

Each time the *Cancel* routine calls **IoReleaseCancelSpinLock**, it must pass the IRQL returned by the most recent call to **IoAcquireCancelSpinLock**. When releasing the spin lock acquired by the I/O manager (and held when the *Cancel* routine was called), the *Cancel* routine must pass **Irp-&gt;CancelIrql**.

A driver must not call outside routines (such as **IoCompleteRequest**) while holding a spin lock because a deadlock can result.

### <a href="" id="using-the-queue-defined-by-the-i-o-manager-"></a>Using the Queue Defined by the I/O Manager

Unless a driver manages its own internal queues of IRPs, its *Cancel* routine is called with an incoming IRP that could be either of the following:

-   The **CurrentIrp** in the input target device object

-   An entry in the device queue associated with the target device object

Unless a driver manages its own internal queues of IRPs, its *Cancel* routine should call [**KeRemoveEntryDeviceQueue**](https://msdn.microsoft.com/library/windows/hardware/ff553163) with the input IRP to test whether it is an entry in the device queue associated with the target device object. The driver's *Cancel* routine *cannot* call **KeRemoveDeviceQueue** or **KeRemoveByKeyDeviceQueue** because it cannot assume that the given IRP is at any particular position in the device queue.

### Current State of the Input IRP

If a *Cancel* routine is called with an IRP for which the driver has already started I/O processing and the request will be completed soon, the *Cancel* routine should release the system cancel spin lock and return control.

If the current state of the input IRP is Pending, a *Cancel* routine must do the following:

1.  Set the input IRP's I/O status block with STATUS\_CANCELLED for **Status** and zero for **Information**.

2.  Release any spin locks it is holding, including the system cancel spin lock.

3.  Call [**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343) with the given IRP.

### Holding IRPs in a Cancelable State

Any driver routine that holds an IRP in a cancelable state must call [**IoMarkIrpPending**](https://msdn.microsoft.com/library/windows/hardware/ff549422) and must call [**IoSetCancelRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff549674) to set its entry point for the *Cancel* routine in the IRP. Only then can that driver routine call additional support routines such as **IoStartPacket**, **IoAllocateController**, or an **ExInterlockedInsert..List** routine.

Any driver routine that subsequently processes cancelable IRPs must check whether an IRP has already been canceled before it begins operations to satisfy the request. The routine must call **IoSetCancelRoutine** to reset its entry point for the *Cancel* routine to **NULL** in the IRP. Only then can that routine begin its I/O processing for the input IRP.

A routine might have to reset the entry point for a *Cancel* routine in an IRP if it, too, passes IRPs on for further processing by other driver routines and those IRPs might be held in a cancelable state.

Any higher-level driver that holds an IRP in a cancelable state must reset its *Cancel* entry point to **NULL** before it passes the IRP on to the next-lower driver with **IoCallDriver**.

### Canceling an IRP

Any higher-level driver can call [**IoCancelIrp**](https://msdn.microsoft.com/library/windows/hardware/ff548338) with an IRP that it has allocated and passed on for further processing by lower-level drivers. However, such a driver cannot assume that the given IRP will be completed with STATUS\_CANCELLED by lower drivers.

### Synchronization

A driver can (or must, depending on its design) maintain additional state information in its device extension to track the cancelable status of IRPs. If this state is shared by driver routines running at IRQL &lt;= DISPATCH\_LEVEL, the shared data should be protected with a driver-allocated and initialized spin lock.

The driver should manage its acquisitions and releases of the system cancel spin lock and its own spin locks carefully. It should hold the system cancel spin lock for the shortest possible intervals. Before accessing a cancelable IRP, such a driver should always check the return value of [**IoSetCancelRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff549674) to determine whether the *Cancel* routine is already running (or is about to run); if so, it should let the *Cancel* routine complete the IRP.

If a device driver maintains state information about cancelable IRPs that various driver routines share with its ISR, these other routines must synchronize access to the shared state with the ISR. Only a driver-supplied *SynchCritSection* routine can access state information that is shared with the ISR in a multiprocessor-safe way.

For more information, see [Synchronization Techniques](synchronization-techniques.md).

 

 




