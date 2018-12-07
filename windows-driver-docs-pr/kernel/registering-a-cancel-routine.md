---
title: Registering a Cancel Routine
description: Registering a Cancel Routine
ms.assetid: ebc63fb6-bf4d-4de3-9232-08d810c2f730
keywords: ["canceling IRPs, registering Cancel routines", "Cancel routines, registering", "registering Cancel routines"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Registering a Cancel Routine





If a device driver has a [*StartIo*](https://msdn.microsoft.com/library/windows/hardware/ff563858) routine, its dispatch routines can register a [*Cancel*](https://msdn.microsoft.com/library/windows/hardware/ff540742) routine by supplying its address as input to [**IoStartPacket**](https://msdn.microsoft.com/library/windows/hardware/ff550370).

If a driver does not have a *StartIo* routine, its dispatch routines must do the following before queuing an IRP for further processing by other driver routines:

1.  Call [**IoAcquireCancelSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff548196).

2.  Call [**IoSetCancelRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff549674) with the input IRP and the entry point for a driver-supplied *Cancel* routine.

3.  Call [**IoReleaseCancelSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff549550).

For information about the cancel spin lock, see [Using the System's Cancel Spin Lock](using-the-system-s-cancel-spin-lock.md).

Drivers that manage their own queues of IRPs, rather than using the I/O manager-supplied device queue, do not need to acquire the cancel spin lock when calling **IoSetCancelRoutine**. However, these drivers should check the *Cancel* routine pointer that **IoSetCancelRoutine** returns to determine whether the *Cancel* routine has already started.

 

 




