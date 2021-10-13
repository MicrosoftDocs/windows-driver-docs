---
title: Cancel Routines in Drivers without StartIo Routines
description: Cancel Routines in Drivers without StartIo Routines
keywords: ["canceling IRPs, StartIo routines", "Cancel routines, StartIo routines", "StartIo routines, Cancel routines"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Cancel Routines in Drivers without StartIo Routines





The I/O manager maintains the **CurrentIrp** field in a device object only if IRPs are queued in the associated device queue object.

Drivers that do not have [*StartIo*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_startio) routines manage their own internal queues of IRPs. In such a driver, a [*Cancel*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_cancel) routine can be called with an input IRP that is neither the **CurrentIrp** for the input target device object, nor an IRP in the driver's internal queue. The driver must maintain its own state about which IRP is currently being processed and should have a *Cancel* routine for each of its queues. The driver's internal queue should be an interlocked queue because its internal queue must be protected by an executive spin lock.

When the driver's *Cancel* routine is called, it typically does the following:

1.  Calls [**IoReleaseCancelSpinLock**](/previous-versions/windows/hardware/drivers/ff549550(v=vs.85)), passing **Irp-&gt;CancelIrql**.

2.  Acquires the spin lock that protects its interlocked queue and walks the queue to find an IRP with **Irp-&gt;Cancel** set to **TRUE**.

    -   If it finds such an IRP in the interlocked queue, dequeues it, releases the spin lock protecting the queue, sets the IRP's I/O status block with w

        STATUS\_CANCELLED for **Status** and zero for **Information**, starts the next queued IRP, calls [**IoCompleteRequest**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocompleterequest) with the canceled IRP, and returns control

    -   If it does not find such an IRP, the *Cancel* routine releases any spin locks it is holding and returns control.

        The driver usually assumes that I/O processing for the input IRP has already begun if the IRP is not queued.

Drivers with *Cancel* routines can handle [**IRP\_MJ\_CLEANUP**](./irp-mj-cleanup.md) requests as well. See [*DispatchCleanup*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch) for more information about **IRP\_MJ\_CLEANUP** requests.

 

