---
title: Cancel Routines in Drivers without StartIo Routines
description: Cancel Routines in Drivers without StartIo Routines
ms.assetid: c6e1a05e-28ed-4f42-8678-55f01303b312
keywords: ["canceling IRPs, StartIo routines", "Cancel routines, StartIo routines", "StartIo routines, Cancel routines"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Cancel Routines in Drivers without StartIo Routines





The I/O manager maintains the **CurrentIrp** field in a device object only if IRPs are queued in the associated device queue object.

Drivers that do not have [*StartIo*](https://msdn.microsoft.com/library/windows/hardware/ff563858) routines manage their own internal queues of IRPs. In such a driver, a [*Cancel*](https://msdn.microsoft.com/library/windows/hardware/ff540742) routine can be called with an input IRP that is neither the **CurrentIrp** for the input target device object, nor an IRP in the driver's internal queue. The driver must maintain its own state about which IRP is currently being processed and should have a *Cancel* routine for each of its queues. The driver's internal queue should be an interlocked queue because its internal queue must be protected by an executive spin lock.

When the driver's *Cancel* routine is called, it typically does the following:

1.  Calls [**IoReleaseCancelSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff549550), passing **Irp-&gt;CancelIrql**.

2.  Acquires the spin lock that protects its interlocked queue and walks the queue to find an IRP with **Irp-&gt;Cancel** set to **TRUE**.

    -   If it finds such an IRP in the interlocked queue, dequeues it, releases the spin lock protecting the queue, sets the IRP's I/O status block with w

        STATUS\_CANCELLED for **Status** and zero for **Information**, starts the next queued IRP, calls [**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343) with the canceled IRP, and returns control

    -   If it does not find such an IRP, the *Cancel* routine releases any spin locks it is holding and returns control.

        The driver usually assumes that I/O processing for the input IRP has already begun if the IRP is not queued.

Drivers with *Cancel* routines can handle [**IRP\_MJ\_CLEANUP**](https://msdn.microsoft.com/library/windows/hardware/ff550718) requests as well. See [*DispatchCleanup*](https://msdn.microsoft.com/library/windows/hardware/ff543233) for more information about **IRP\_MJ\_CLEANUP** requests.

 

 




