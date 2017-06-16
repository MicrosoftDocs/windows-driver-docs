---
title: Cancel Routines in Drivers without StartIo Routines
author: windows-driver-content
description: Cancel Routines in Drivers without StartIo Routines
ms.assetid: c6e1a05e-28ed-4f42-8678-55f01303b312
keywords: ["canceling IRPs, StartIo routines", "Cancel routines, StartIo routines", "StartIo routines, Cancel routines"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Cancel Routines in Drivers without StartIo Routines


## <a href="" id="ddk-cancel-routines-in-drivers-without-startio-routines-kg"></a>


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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Cancel%20Routines%20in%20Drivers%20without%20StartIo%20Routines%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


