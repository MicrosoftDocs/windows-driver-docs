---
title: Cancel Routines in Drivers with StartIo Routines
description: Cancel Routines in Drivers with StartIo Routines
ms.assetid: 5098e4b9-d4db-44c2-acb3-a46878d6f1c4
keywords: ["canceling IRPs, StartIo routines", "Cancel routines, StartIo routines", "StartIo routines, Cancel routines"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Cancel Routines in Drivers with StartIo Routines





The I/O manager maintains the **CurrentIrp** field in a device object only if IRPs are queued in the associated device queue object. That is, the field is valid only if the driver has a [*StartIo*](https://msdn.microsoft.com/library/windows/hardware/ff563858) routine.

In a driver that has a *StartIo* routine, a typical [*Cancel*](https://msdn.microsoft.com/library/windows/hardware/ff540742) routine must do the following:

1.  Check whether the pointer for the input IRP matches the target device object's **CurrentIrp** address.

    If these pointers are equivalent, the *Cancel* routine calls [**IoReleaseCancelSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff549550), passing **Irp-&gt;CancelIrql**, and returns control.

2.  If the canceled IRP is not the current IRP, check whether the input canceled IRP is in the device queue associated with the target device object by calling [**KeRemoveEntryDeviceQueue**](https://msdn.microsoft.com/library/windows/hardware/ff553163) with the IRP's **Tail.Overlay.DeviceQueueEntry** pointer.
    -   If the IRP is in the device queue, calling **KeRemoveEntryDeviceQueue** removes it from the queue. The *Cancel* routine calls [**IoReleaseCancelSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff549550), sets the IRP's I/O status block with STATUS\_CANCELLED for **Status** and zero for **Information**, calls [**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343) with the canceled IRP, and returns control.

    -   If the IRP is not in the device queue, the *Cancel* routine calls **IoReleaseCancelSpinLock** and returns control.

The driver's *Cancel* routine should call **KeRemoveEntryDeviceQueue** to test whether the IRP is in the device queue. This support routine either removes the given IRP from the device queue or does nothing except return **FALSE**, indicating that the given entry was not queued. A *Cancel* routine cannot assume that the input IRP is at any particular position in the device queue, so it cannot call [**KeRemoveDeviceQueue**](https://msdn.microsoft.com/library/windows/hardware/ff553156) or [**KeRemoveByKeyDeviceQueue**](https://msdn.microsoft.com/library/windows/hardware/ff553152) to compare the pointers to the returned IRP and input IRP.

Drivers with *Cancel* routines can handle [**IRP\_MJ\_CLEANUP**](https://msdn.microsoft.com/library/windows/hardware/ff550718) requests as well. See [*DispatchCleanup*](https://msdn.microsoft.com/library/windows/hardware/ff543233) for more information about **IRP\_MJ\_CLEANUP** requests.

 

 




