---
title: Synchronizing IRP Cancellation
description: Synchronizing IRP Cancellation
ms.assetid: a110c6ad-794d-4b8a-a89d-bceb08ea82b8
keywords: ["canceling IRPs, synchronization", "Cancel routines, synchronization", "synchronization WDK IRPs", "cancelable IRPs WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Synchronizing IRP Cancellation





From a driver's perspective, an IRP can be canceled at any time. IRP cancellation occurs asynchronously; therefore, drivers must be able to handle a number of potential race conditions, created if the IRP is canceled at any of the following points:

-   After a driver routine is called, but before it queues an IRP.

-   After a driver routine is called, but before it tries to process an IRP. For example, an IRP might be canceled after a driver's [*StartIo*](https://msdn.microsoft.com/library/windows/hardware/ff563858) routine is called, but before the *StartIo* routine removes the IRP from the device queue.

-   After the driver routine dequeues the IRP, but before it starts the requested I/O.

Note that after a driver queues an IRP and releases any spin locks that protect the queue, another thread can access and change the IRP. When the original thread resumes—even as soon as the next line of code—the IRP might have already been canceled or otherwise changed.

Driver can use the cancel-safe IRP queue framework to implement IRP queuing. The system then registers a [*Cancel*](https://msdn.microsoft.com/library/windows/hardware/ff540742) routine for the driver that automatically handles synchronization to safely cancel IRPs. See [Cancel-Safe IRP Queues](cancel-safe-irp-queues.md) for more information. Otherwise, drivers must implement their own synchronization.

The following members of an IRP contain information about cancellation:

-   **Irp-&gt;Cancel** indicates whether an IRP is being canceled or should be canceled.

-   **Irp-&gt;CancelRoutine** indicates whether an IRP is cancelable. If this member contains a pointer to a cancel routine, then the IRP is cancelable. If this member is **NULL**, then the IRP is not cancelable. If this member is **NULL**, but **Irp-&gt;Cancel** is set, that indicates that the cancel routine is running and the IRP is in the process of being canceled.

If a driver handles cancelable IRPs, it is responsible for setting the appropriate *Cancel* routine in each IRP that it holds in a cancelable state.

This section includes the following topics on synchronizing IRP cancellation.

[Using the System's Cancel Spin Lock](using-the-system-s-cancel-spin-lock.md)

[Synchronizing Cancellation in Driver Routines that Process IRPs](synchronizing-cancellation-in-driver-routines-that-process-irps.md)

[Synchronizing Cancellation in Higher-Level Drivers without Cancel Routines](synchronizing-cancellation-in-higher-level-drivers-without-cancel-rout.md)

[Using a Driver-Supplied Spin Lock](using-a-driver-supplied-spin-lock.md)

 

 




