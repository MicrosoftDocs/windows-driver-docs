---
title: Implementing a Cancel Routine
description: Implementing a Cancel Routine
ms.assetid: 243b623b-317c-4084-a753-940c91c4cc50
keywords: ["canceling IRPs, guidelines", "Cancel routines, guidelines"]
ms.date: 05/09/2018
ms.localizationpriority: medium
---

# Implementing a Cancel Routine





The I/O manager calls a driver-supplied [*Cancel*](https://msdn.microsoft.com/library/windows/hardware/ff540742) routine with an input IRP to be canceled and a *DeviceObject* pointer that represents the target device for the I/O request.

The IRP could be one that the driver's [*DispatchReadWrite*](https://msdn.microsoft.com/library/windows/hardware/ff543381) routine has queued just as the current Win32 application is being closed by the user. The IRP also could be one that a higher-level driver explicitly canceled, depending on the nature of the underlying device.

When the *Cancel* routine is called, the input IRP might already be the **CurrentIrp** in the target device object or might already be in the device queue associated with the target device object if the driver has a [*StartIo*](https://msdn.microsoft.com/library/windows/hardware/ff563858) routine. If the driver has no *StartIo* routine, the IRP might be in a driver-managed internal queue of IRPs when its *Cancel* routine is called. In any case, before the I/O manager calls the *Cancel* routine for the incoming IRP, the I/O manager sets the **Cancel** member in this IRP to **TRUE** and sets the **CancelRoutine** member in the IRP to **NULL**.

The *Cancel* routine for a master IRP that has associated IRPs is responsible for calling [**IoCancelIrp**](https://msdn.microsoft.com/library/windows/hardware/ff548338) to cancel those associated IRPs.

All *Cancel* routines must follow these guidelines:

-   Call [**IoReleaseCancelSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff549550) to release the system's cancel spin lock.

-   Set the I/O status block's **Status** member to STATUS\_CANCELLED, and set its **Information** member to zero.

-   Complete the specified IRP by calling [**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343).

-   Because a *Cancel* routine is always called with the system cancel spin lock held, this routine must not call [**IoAcquireCancelSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff548196) unless it calls **IoReleaseCancelSpinLock** first.

-   A *Cancel* routine cannot be holding the system cancel spin lock when it returns control. That is, every *Cancel* routine must call **IoReleaseCancelSpinLock** at least once before it returns control.

-   If it calls **IoAcquireCancelSpinLock**, a *Cancel* routine must make the reciprocal call to **IoReleaseCancelSpinLock** as quickly as possible.

-   Never call [**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343) with an IRP while holding a spin lock. Attempting to complete an IRP while holding a spin lock can cause deadlocks.


 

 




