---
title: Synchronizing Cancellation in Driver Routines that Process IRPs
description: A driver routine that dequeues or is called with an IRP that is held in a cancelable state must synchronize cancellation.
ms.localizationpriority: medium
ms.date: 07/22/2021
---

# Synchronizing Cancellation in Driver Routines that Process IRPs

Any driver routine that dequeues or is called with an IRP that is held in a cancelable state, including a driver's [*StartIo*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_startio) routine, must do the following:

1. Call [**IoAcquireCancelSpinLock**](/previous-versions/windows/hardware/drivers/ff548196(v=vs.85)).

1. Check to make sure that **Irp** equals **DeviceObject-&gt;CurrentIrp**. If not, call [**IoReleaseCancelSpinLock**](/previous-versions/windows/hardware/drivers/ff549550(v=vs.85)) and return control.

    If the two are not the same, the **CurrentIrp** might have been canceled between the time that [**IoStartPacket**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-iostartpacket) released the cancel spin lock and this routine acquired it.

1. Call [**IoSetCancelRoutine**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iosetcancelroutine) with a **NULL** *CancelRoutine* pointer to remove the IRP from the cancelable state.

1. Check the **Irp-&gt;Cancel** field to determine whether to cancel the IRP or to begin processing the I/O request.

    If **Irp-&gt;Cancel** is set to **TRUE**, do the following:

    - Call **IoReleaseCancelSpinLock**.

    - Set **Irp-&gt;IoStatus.Status** to STATUS\_CANCELLED.

    - Set **Irp-&gt;IoStatus.Information** to 0.

    - Call [**IoStartNextPacket**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-iostartnextpacket) (in a *StartIo* routine) to start the next packet.

    - Call [**IoCompleteRequest**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocompleterequest) with a priority boost of IO\_NO\_INCREMENT to complete the IRP.

    If **Irp-&gt;Cancel** is set to **FALSE**, call **IoReleaseCancelSpinLock** and start the requested processing the I/O request or pass the IRP to the next lower driver, as appropriate.

Drivers that manage their own queues of IRPs, rather than using the I/O manager-supplied device queue, do not need to acquire the cancel spin lock when calling **IoSetCancelRoutine**. However, these drivers should check the [*Cancel*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_cancel) routine pointer that **IoSetCancelRoutine** returns to determine whether the cancel routine has already started.

In any driver that handles cancelable IRPs, every driver routine that processes an IRP before the underlying device has been programmed for the requested I/O operation should check the cancelable state of all incoming IRPs. Specifically, a highest-level device driver with both *StartIo* and [*ControllerControl*](writing-controllercontrolroutines.md) routines should process incoming IRPs in both these driver routines as already described.
