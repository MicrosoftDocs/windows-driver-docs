---
title: Using the System's Cancel Spin Lock
description: Using the System's Cancel Spin Lock
ms.assetid: dd3cf1e7-8ecc-4721-9160-86bf928687e4
keywords: ["cancel spin locks WDK kernel", "spin locks WDK kernel", "system cancel spin locks WDK kernel", "STATUS_CANCELLED"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Using the System's Cancel Spin Lock





The system provides a single *cancel spin lock*, which is acquired or released when certain system routines are called.

Driver routines that change the state of cancelable IRPs, including all routines that might complete an IRP with STATUS\_CANCELLED, must acquire and release the system cancel spin lock according to the guidelines in this section.

In drivers that use the I/O manager-supplied device queue, any driver routine other than the *Cancel* routine that changes the cancelable state of an IRP must first call [**IoAcquireCancelSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff548196) to acquire the system cancel spin lock.

Acquiring the cancel spin lock ensures that only the caller can change the cancelable state of that IRP. While the caller holds the spin lock, the I/O manager cannot call the driver's *Cancel* routine for that IRP. Likewise, another driver routine, such as a *DispatchCleanup* routine, cannot simultaneously try to change the cancelable state of that IRP.

In drivers that manage their own queues of IRPs and use driver-supplied spin locks to synchronize queue access, the driver routines do not need to acquire the cancel spin lock before calling [**IoSetCancelRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff549674). However, these drivers should check the *Cancel* routine pointer that **IoSetCancelRoutine** returns to determine whether the *Cancel* routine has already started. See [Using a Driver-Supplied Spin Lock](using-a-driver-supplied-spin-lock.md) for details.

Any driver routine that calls **IoAcquireCancelSpinLock** must call **IoReleaseCancelSpinLock** as soon as possible.

A driver must never call [**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343) with an IRP while holding a spin lock. Attempting to complete an IRP while holding a spin lock can cause a deadlock.

 

 




