---
title: Cancel Routines in Drivers with StartIo Routines
description: Cancel Routines in Drivers with StartIo Routines
keywords: ["canceling IRPs, StartIo routines", "Cancel routines, StartIo routines", "StartIo routines, Cancel routines"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Cancel Routines in Drivers with StartIo Routines





The I/O manager maintains the **CurrentIrp** field in a device object only if IRPs are queued in the associated device queue object. That is, the field is valid only if the driver has a [*StartIo*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_startio) routine.

In a driver that has a *StartIo* routine, a typical [*Cancel*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_cancel) routine must do the following:

1.  Check whether the pointer for the input IRP matches the target device object's **CurrentIrp** address.

    If these pointers are equivalent, the *Cancel* routine calls [**IoReleaseCancelSpinLock**](/previous-versions/windows/hardware/drivers/ff549550(v=vs.85)), passing **Irp-&gt;CancelIrql**, and returns control.

2.  If the canceled IRP is not the current IRP, check whether the input canceled IRP is in the device queue associated with the target device object by calling [**KeRemoveEntryDeviceQueue**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keremoveentrydevicequeue) with the IRP's **Tail.Overlay.DeviceQueueEntry** pointer.
    -   If the IRP is in the device queue, calling **KeRemoveEntryDeviceQueue** removes it from the queue. The *Cancel* routine calls [**IoReleaseCancelSpinLock**](/previous-versions/windows/hardware/drivers/ff549550(v=vs.85)), sets the IRP's I/O status block with STATUS\_CANCELLED for **Status** and zero for **Information**, calls [**IoCompleteRequest**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocompleterequest) with the canceled IRP, and returns control.

    -   If the IRP is not in the device queue, the *Cancel* routine calls **IoReleaseCancelSpinLock** and returns control.

The driver's *Cancel* routine should call **KeRemoveEntryDeviceQueue** to test whether the IRP is in the device queue. This support routine either removes the given IRP from the device queue or does nothing except return **FALSE**, indicating that the given entry was not queued. A *Cancel* routine cannot assume that the input IRP is at any particular position in the device queue, so it cannot call [**KeRemoveDeviceQueue**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keremovedevicequeue) or [**KeRemoveByKeyDeviceQueue**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keremovebykeydevicequeue) to compare the pointers to the returned IRP and input IRP.

Drivers with *Cancel* routines can handle [**IRP\_MJ\_CLEANUP**](./irp-mj-cleanup.md) requests as well. See [*DispatchCleanup*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch) for more information about **IRP\_MJ\_CLEANUP** requests.

 

