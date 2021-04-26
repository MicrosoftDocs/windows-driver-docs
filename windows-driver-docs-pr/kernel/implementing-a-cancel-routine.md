---
title: Implementing a Cancel Routine
description: Implementing a Cancel Routine
keywords: ["canceling IRPs, guidelines", "Cancel routines, guidelines"]
ms.date: 05/09/2018
ms.localizationpriority: medium
---

# Implementing a Cancel Routine





The I/O manager calls a driver-supplied [*Cancel*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_cancel) routine with an input IRP to be canceled and a *DeviceObject* pointer that represents the target device for the I/O request.

The IRP could be one that the driver's [*DispatchReadWrite*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch) routine has queued just as the current Win32 application is being closed by the user. The IRP also could be one that a higher-level driver explicitly canceled, depending on the nature of the underlying device.

When the *Cancel* routine is called, the input IRP might already be the **CurrentIrp** in the target device object or might already be in the device queue associated with the target device object if the driver has a [*StartIo*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_startio) routine. If the driver has no *StartIo* routine, the IRP might be in a driver-managed internal queue of IRPs when its *Cancel* routine is called. In any case, before the I/O manager calls the *Cancel* routine for the incoming IRP, the I/O manager sets the **Cancel** member in this IRP to **TRUE** and sets the **CancelRoutine** member in the IRP to **NULL**.

The *Cancel* routine for a master IRP that has associated IRPs is responsible for calling [**IoCancelIrp**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocancelirp) to cancel those associated IRPs.

All *Cancel* routines must follow these guidelines:

-   Call [**IoReleaseCancelSpinLock**](/previous-versions/windows/hardware/drivers/ff549550(v=vs.85)) to release the system's cancel spin lock.

-   Set the I/O status block's **Status** member to STATUS\_CANCELLED, and set its **Information** member to zero.

-   Complete the specified IRP by calling [**IoCompleteRequest**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocompleterequest).

-   Because a *Cancel* routine is always called with the system cancel spin lock held, this routine must not call [**IoAcquireCancelSpinLock**](/previous-versions/windows/hardware/drivers/ff548196(v=vs.85)) unless it calls **IoReleaseCancelSpinLock** first.

-   A *Cancel* routine cannot be holding the system cancel spin lock when it returns control. That is, every *Cancel* routine must call **IoReleaseCancelSpinLock** at least once before it returns control.

-   If it calls **IoAcquireCancelSpinLock**, a *Cancel* routine must make the reciprocal call to **IoReleaseCancelSpinLock** as quickly as possible.

-   Never call [**IoCompleteRequest**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocompleterequest) with an IRP while holding a spin lock. Attempting to complete an IRP while holding a spin lock can cause deadlocks.


 

