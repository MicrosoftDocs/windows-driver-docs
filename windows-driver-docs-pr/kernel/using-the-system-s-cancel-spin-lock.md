---
title: Using the System's Cancel Spin Lock
author: windows-driver-content
description: Using the System's Cancel Spin Lock
ms.assetid: dd3cf1e7-8ecc-4721-9160-86bf928687e4
keywords: ["cancel spin locks WDK kernel", "spin locks WDK kernel", "system cancel spin locks WDK kernel", "STATUS_CANCELLED"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Using the System's Cancel Spin Lock


## <a href="" id="ddk-using-the-system-s-cancel-spin-lock-kg"></a>


The system provides a single *cancel spin lock*, which is acquired or released when certain system routines are called.

Driver routines that change the state of cancelable IRPs, including all routines that might complete an IRP with STATUS\_CANCELLED, must acquire and release the system cancel spin lock according to the guidelines in this section.

In drivers that use the I/O manager-supplied device queue, any driver routine other than the *Cancel* routine that changes the cancelable state of an IRP must first call [**IoAcquireCancelSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff548196) to acquire the system cancel spin lock.

Acquiring the cancel spin lock ensures that only the caller can change the cancelable state of that IRP. While the caller holds the spin lock, the I/O manager cannot call the driver's *Cancel* routine for that IRP. Likewise, another driver routine, such as a *DispatchCleanup* routine, cannot simultaneously try to change the cancelable state of that IRP.

In drivers that manage their own queues of IRPs and use driver-supplied spin locks to synchronize queue access, the driver routines do not need to acquire the cancel spin lock before calling [**IoSetCancelRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff549674). However, these drivers should check the *Cancel* routine pointer that **IoSetCancelRoutine** returns to determine whether the *Cancel* routine has already started. See [Using a Driver-Supplied Spin Lock](using-a-driver-supplied-spin-lock.md) for details.

Any driver routine that calls **IoAcquireCancelSpinLock** must call **IoReleaseCancelSpinLock** as soon as possible.

A driver must never call [**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343) with an IRP while holding a spin lock. Attempting to complete an IRP while holding a spin lock can cause a deadlock.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Using%20the%20System's%20Cancel%20Spin%20Lock%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


