---
title: Synchronizing Cancellation in Driver Routines that Process IRPs
author: windows-driver-content
description: Synchronizing Cancellation in Driver Routines that Process IRPs
MS-HAID:
- 'IRPs\_a71d8710-1708-4c68-bd57-56335867457c.xml'
- 'kernel.synchronizing\_cancellation\_in\_driver\_routines\_that\_process\_irps'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 0b252ebd-b9d5-4747-9a27-c1ecffdbae18
---

# Synchronizing Cancellation in Driver Routines that Process IRPs


## <a href="" id="ddk-synchronizing-cancellation-in-driver-routines-that-process-irps-kg"></a>


Any driver routine that dequeues or is called with an IRP that is held in a cancelable state, including a driver's [*StartIo*](https://msdn.microsoft.com/library/windows/hardware/ff563858) routine, must do the following:

1.  Call [**IoAcquireCancelSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff548196).

2.  Check to make sure that **Irp** equals **DeviceObject-&gt;CurrentIrp**. If not, call [**IoReleaseCancelSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff549550) and return control.

    If the two are not the same, the **CurrentIrp** might have been canceled between the time that [**IoStartPacket**](https://msdn.microsoft.com/library/windows/hardware/ff550370) released the cancel spin lock and this routine acquired it.

3.  Call [**IoSetCancelRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff549674) with a **NULL** *CancelRoutine* pointer to remove the IRP from the cancelable state.

4.  Check the **Irp-&gt;Cancel** field to determine whether to cancel the IRP or to begin processing the I/O request.

    If **Irp-&gt;Cancel** is set to **TRUE**, do the following:

    -   Call **IoReleaseCancelSpinLock**.
    -   Set **Irp-&gt;IoStatus.Status** to STATUS\_CANCELLED.
    -   Set **Irp-&gt;IoStatus.Information** to 0.
    -   Call [**IoStartNextPacket**](https://msdn.microsoft.com/library/windows/hardware/ff550358) (in a *StartIo* routine) to start the next packet.
    -   Call [**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343) with a priority boost of IO\_NO\_INCREMENT to complete the IRP.

    If **Irp-&gt;Cancel** is set to **FALSE**, call **IoReleaseCancelSpinLock** and start the requested processing the I/O request or pass the IRP to the next lower driver, as appropriate.

Drivers that manage their own queues of IRPs, rather than using the I/O manager-supplied device queue, do not need to acquire the cancel spin lock when calling **IoSetCancelRoutine**. However, these drivers should check the [*Cancel*](https://msdn.microsoft.com/library/windows/hardware/ff540742) routine pointer that **IoSetCancelRoutine** returns to determine whether the cancel routine has already started.

In any driver that handles cancelable IRPs, every driver routine that processes an IRP before the underlying device has been programmed for the requested I/O operation should check the cancelable state of all incoming IRPs. Specifically, a highest-level device driver with both *StartIo* and [*ControllerControl*](https://msdn.microsoft.com/library/windows/hardware/ff542049) routines should process incoming IRPs in both these driver routines as already described.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Synchronizing%20Cancellation%20in%20Driver%20Routines%20that%20Process%20IRPs%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


