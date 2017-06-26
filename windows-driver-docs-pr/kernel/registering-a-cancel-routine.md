---
title: Registering a Cancel Routine
author: windows-driver-content
description: Registering a Cancel Routine
ms.assetid: ebc63fb6-bf4d-4de3-9232-08d810c2f730
keywords: ["canceling IRPs, registering Cancel routines", "Cancel routines, registering", "registering Cancel routines"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Registering a Cancel Routine


## <a href="" id="ddk-registering-a-cancel-routine-kg"></a>


If a device driver has a [*StartIo*](https://msdn.microsoft.com/library/windows/hardware/ff563858) routine, its dispatch routines can register a [*Cancel*](https://msdn.microsoft.com/library/windows/hardware/ff540742) routine by supplying its address as input to [**IoStartPacket**](https://msdn.microsoft.com/library/windows/hardware/ff550370).

If a driver does not have a *StartIo* routine, its dispatch routines must do the following before queuing an IRP for further processing by other driver routines:

1.  Call [**IoAcquireCancelSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff548196).

2.  Call [**IoSetCancelRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff549674) with the input IRP and the entry point for a driver-supplied *Cancel* routine.

3.  Call [**IoReleaseCancelSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff549550).

For information about the cancel spin lock, see [Using the System's Cancel Spin Lock](using-the-system-s-cancel-spin-lock.md).

Drivers that manage their own queues of IRPs, rather than using the I/O manager-supplied device queue, do not need to acquire the cancel spin lock when calling **IoSetCancelRoutine**. However, these drivers should check the *Cancel* routine pointer that **IoSetCancelRoutine** returns to determine whether the *Cancel* routine has already started.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Registering%20a%20Cancel%20Routine%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


