---
title: Implementing a Cancel Routine
author: windows-driver-content
description: Implementing a Cancel Routine
MS-HAID:
- 'IRPs\_da2e2f3f-8389-482a-9cbe-9d99491faa45.xml'
- 'kernel.implementing\_a\_cancel\_routine'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 243b623b-317c-4084-a753-940c91c4cc50
keywords: ["canceling IRPs, guidelines", "Cancel routines, guidelines"]
---

# Implementing a Cancel Routine


## <a href="" id="ddk-implementing-a-cancel-routine-kg"></a>


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

For more information about implementing a *Cancel* routine, see the [I/O Completion/Cancellation Guidelines](http://go.microsoft.com/fwlink/p/?linkid=51436) white paper on the Microsoft Windows Hardware Developer Central (WHDC) website.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Implementing%20a%20Cancel%20Routine%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


