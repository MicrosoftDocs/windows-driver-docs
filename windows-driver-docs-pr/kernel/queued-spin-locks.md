---
title: Queued Spin Locks
description: Queued Spin Locks
ms.assetid: 7ccec366-5436-4e69-9fb7-f0090cf2adcb
keywords: ["queued spin locks WDK kernel", "first-come first-served spin locks WDK kernel", "KeAcquireInStackQueuedSpinLock"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Queued Spin Locks





*Queued spin locks* are a variant of spin locks that are more efficient for high contention locks on multiprocessor machines. On multiprocessor machines, using queued spin locks guarantees that processors acquire the spin lock on a first-come first-served basis. Drivers for Windows XP and later versions of Windows should use queued spin locks instead of ordinary spin locks.

The driver supplies storage for the spin lock, and initializes it with [**KeInitializeSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff552160). The driver uses [**KeAcquireInStackQueuedSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff551899) to acquire the queued spin lock, and [**KeReleaseInStackQueuedSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff553130) to release it.

The driver allocates a [**KLOCK\_QUEUE\_HANDLE**](https://msdn.microsoft.com/library/windows/hardware/ff554247) structure that it passes by pointer to **KeAcquireInStackQueuedSpinLock**. The driver passes the same structure by pointer to **KeReleaseInStackQueuedSpinLock** when it releases the spin lock. Drivers should normally allocate the structure on the stack each time they acquire the lock.

Drivers must not mix calls to the queued spin lock routines and the ordinary **Ke*Xxx*SpinLock** routines on the same spin lock.

If the driver is already at IRQL = DISPATCH\_LEVEL, it can call [**KeAcquireInStackQueuedSpinLockAtDpcLevel**](https://msdn.microsoft.com/library/windows/hardware/ff551908) and [**KeReleaseInStackQueuedSpinLockFromDpcLevel**](https://msdn.microsoft.com/library/windows/hardware/ff553137) instead.

 

 




