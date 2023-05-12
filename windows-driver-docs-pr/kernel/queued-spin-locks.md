---
title: Queued Spin Locks
description: Queued Spin Locks
keywords: ["queued spin locks WDK kernel", "first-come first-served spin locks WDK kernel", "KeAcquireInStackQueuedSpinLock"]
ms.date: 05/12/2023
---

# Queued Spin Locks





*Queued spin locks* are a variant of spin locks that are a better choice for highly contended locks.  Unqueued spinlocks are a better choice for lightly contended locks.

The driver supplies storage for the spin lock, and initializes it with [**KeInitializeSpinLock**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keinitializespinlock). The driver uses [**KeAcquireInStackQueuedSpinLock**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keacquireinstackqueuedspinlock) to acquire the queued spin lock, and [**KeReleaseInStackQueuedSpinLock**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kereleaseinstackqueuedspinlock) to release it.

The driver allocates a [**KLOCK\_QUEUE\_HANDLE**](./eprocess.md) structure that it passes by pointer to **KeAcquireInStackQueuedSpinLock**. The driver passes the same structure by pointer to **KeReleaseInStackQueuedSpinLock** when it releases the spin lock.

Drivers should normally allocate the structure on the stack each time they acquire the lock. A driver should not allocate the structure as part of its device context and then share the same structure from multiple threads.

Drivers must not mix calls to the queued spin lock routines and the ordinary **Ke*Xxx*SpinLock** routines on the same spin lock.

If the driver is already at IRQL = DISPATCH\_LEVEL, it can call [**KeAcquireInStackQueuedSpinLockAtDpcLevel**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keacquireinstackqueuedspinlockatdpclevel) and [**KeReleaseInStackQueuedSpinLockFromDpcLevel**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kereleaseinstackqueuedspinlockfromdpclevel) instead.

 

