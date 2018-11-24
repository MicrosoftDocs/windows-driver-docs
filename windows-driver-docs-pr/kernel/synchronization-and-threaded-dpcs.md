---
title: Synchronization and Threaded DPCs
description: Synchronization and Threaded DPCs
ms.assetid: b4f2c77b-226c-4229-bcbb-5eebabdc28a4
keywords: ["threaded DPCs WDK kernel", "synchronization WDK kernel , interrupts", "queued spin locks WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Synchronization and Threaded DPCs





To synchronize access to a memory location that is accessed from both inside and outside a [*CustomThreadedDpc*](https://msdn.microsoft.com/library/windows/hardware/ff542976) routine, a driver can use ordinary spin locks or queued spin locks. When doing so, the driver must obey certain rules to correctly synchronize at IRQL= PASSIVE\_LEVEL and at IRQL = DISPATCH\_LEVEL, because a *CustomThreadedDpc* routine can execute at both IRQLs.

For an ordinary spin lock, the following rules apply:

-   To acquire and release the spin lock, the driver can call [**KeAcquireSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff551917) and [**KeReleaseSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff553145) from both inside and outside the *CustomThreadedDpc* routine.

-   The driver can call [**KeAcquireSpinLockForDpc**](https://msdn.microsoft.com/library/windows/hardware/ff551923) and [**KeReleaseSpinLockForDpc**](https://msdn.microsoft.com/library/windows/hardware/ff553148) from inside the *CustomThreadedDpc* routine. Note that the *CustomThreadedDpc* routine must not call [**KeAcquireSpinLockAtDpcLevel**](https://msdn.microsoft.com/library/windows/hardware/ff551921) or [**KeReleaseSpinLockFromDpcLevel**](https://msdn.microsoft.com/library/windows/hardware/ff553150), because these routines can safely be called only at IRQL = DISPATCH\_LEVEL.

The rules for queued spin locks are similar:

-   To acquire and release the spin lock, the driver can call [**KeAcquireInStackQueuedSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff551899) and [**KeReleaseInStackQueuedSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff553130) from both inside and outside the *CustomThreadedDpc* routine.

-   The driver can call [**KeAcquireInStackQueuedSpinLockForDpc**](https://msdn.microsoft.com/library/windows/hardware/ff551912) and [**KeReleaseInStackQueuedSpinLockForDpc**](https://msdn.microsoft.com/library/windows/hardware/ff553133) from inside the *CustomThreadedDpc* routine. Note that the *CustomThreadedDpc* routine must not call [**KeAcquireInStackQueuedSpinLockAtDpcLevel**](https://msdn.microsoft.com/library/windows/hardware/ff551908) or [**KeReleaseInStackQueuedSpinLockFromDpcLevel**](https://msdn.microsoft.com/library/windows/hardware/ff553137), because these routines can safely be called only at IRQL = DISPATCH\_LEVEL.

Because **KeAcquireSpinLockForDpc** and **KeAcquireInStackQueuedSpinLockForDpc** do not reset the IRQL when called at DISPATCH\_LEVEL, they execute faster than **KeAcquireSpinLock** and **KeAcquireInStackQueuedSpinLock**, respectively.

For more information about spin locks, see [Spin Locks](spin-locks.md).

 

 




