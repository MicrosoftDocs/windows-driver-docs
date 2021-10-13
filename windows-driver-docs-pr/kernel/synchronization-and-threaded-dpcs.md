---
title: Synchronization and Threaded DPCs
description: To synchronize access to a memory location that is accessed from both inside and outside a CustomThreadedDpc routine, a driver can use ordinary spin locks or queued spin locks.
keywords: ["threaded DPCs WDK kernel", "synchronization WDK kernel , interrupts", "queued spin locks WDK kernel"]
ms.date: 07/22/2021
ms.localizationpriority: medium
---

# Synchronization and Threaded DPCs

To synchronize access to a memory location that is accessed from both inside and outside a [*CustomThreadedDpc*](using-a-customtimerdpc-routine.md) routine, a driver can use ordinary spin locks or queued spin locks. When doing so, the driver must obey certain rules to correctly synchronize at IRQL = PASSIVE_LEVEL and at IRQL = DISPATCH_LEVEL, because a *CustomThreadedDpc* routine can execute at both IRQLs.

For an ordinary spin lock, the following rules apply:

- To acquire and release the spin lock, the driver can call [**KeAcquireSpinLock**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keacquirespinlock) and [**KeReleaseSpinLock**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kereleasespinlock) from both inside and outside the *CustomThreadedDpc* routine.

- The driver can call [**KeAcquireSpinLockForDpc**](/previous-versions/windows/hardware/drivers/ff551923(v=vs.85)) and [**KeReleaseSpinLockForDpc**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kereleasespinlockfordpc) from inside the *CustomThreadedDpc* routine. Note that the *CustomThreadedDpc* routine must not call [**KeAcquireSpinLockAtDpcLevel**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keacquirespinlockatdpclevel) or [**KeReleaseSpinLockFromDpcLevel**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kereleasespinlockfromdpclevel), because these routines can safely be called only at IRQL = DISPATCH_LEVEL.

The rules for queued spin locks are similar:

- To acquire and release the spin lock, the driver can call [**KeAcquireInStackQueuedSpinLock**](/previous-versions/windows/hardware/drivers/ff551899(v=vs.85)) and [**KeReleaseInStackQueuedSpinLock**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kereleaseinstackqueuedspinlock) from both inside and outside the *CustomThreadedDpc* routine.

- The driver can call [**KeAcquireInStackQueuedSpinLockForDpc**](/previous-versions/windows/hardware/drivers/ff551912(v=vs.85)) and [**KeReleaseInStackQueuedSpinLockForDpc**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kereleaseinstackqueuedspinlockfordpc) from inside the *CustomThreadedDpc* routine. Note that the *CustomThreadedDpc* routine must not call [**KeAcquireInStackQueuedSpinLockAtDpcLevel**](/previous-versions/windows/hardware/drivers/ff551908(v=vs.85)) or [**KeReleaseInStackQueuedSpinLockFromDpcLevel**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kereleaseinstackqueuedspinlockfromdpclevel), because these routines can safely be called only at IRQL = DISPATCH_LEVEL.

Because **KeAcquireSpinLockForDpc** and **KeAcquireInStackQueuedSpinLockForDpc** do not reset the IRQL when called at DISPATCH_LEVEL, they execute faster than **KeAcquireSpinLock** and **KeAcquireInStackQueuedSpinLock**, respectively.

For more information about spin locks, see [Spin Locks](introduction-to-spin-locks.md).
