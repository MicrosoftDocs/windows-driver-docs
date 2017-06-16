---
title: Synchronization and Threaded DPCs
author: windows-driver-content
description: Synchronization and Threaded DPCs
ms.assetid: b4f2c77b-226c-4229-bcbb-5eebabdc28a4
keywords: ["threaded DPCs WDK kernel", "synchronization WDK kernel , interrupts", "queued spin locks WDK kernel"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Synchronization and Threaded DPCs


## <a href="" id="ddk-synchronization-and-threaded-dpcs-kg"></a>


To synchronize access to a memory location that is accessed from both inside and outside a [*CustomThreadedDpc*](https://msdn.microsoft.com/library/windows/hardware/ff542976) routine, a driver can use ordinary spin locks or queued spin locks. When doing so, the driver must obey certain rules to correctly synchronize at IRQL= PASSIVE\_LEVEL and at IRQL = DISPATCH\_LEVEL, because a *CustomThreadedDpc* routine can execute at both IRQLs.

For an ordinary spin lock, the following rules apply:

-   To acquire and release the spin lock, the driver can call [**KeAcquireSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff551917) and [**KeReleaseSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff553145) from both inside and outside the *CustomThreadedDpc* routine.

-   The driver can call [**KeAcquireSpinLockForDpc**](https://msdn.microsoft.com/library/windows/hardware/ff551923) and [**KeReleaseSpinLockForDpc**](https://msdn.microsoft.com/library/windows/hardware/ff553148) from inside the *CustomThreadedDpc* routine. Note that the *CustomThreadedDpc* routine must not call [**KeAcquireSpinLockAtDpcLevel**](https://msdn.microsoft.com/library/windows/hardware/ff551921) or [**KeReleaseSpinLockFromDpcLevel**](https://msdn.microsoft.com/library/windows/hardware/ff553150), because these routines can safely be called only at IRQL = DISPATCH\_LEVEL.

The rules for queued spin locks are similar:

-   To acquire and release the spin lock, the driver can call [**KeAcquireInStackQueuedSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff551899) and [**KeReleaseInStackQueuedSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff553130) from both inside and outside the *CustomThreadedDpc* routine.

-   The driver can call [**KeAcquireInStackQueuedSpinLockForDpc**](https://msdn.microsoft.com/library/windows/hardware/ff551912) and [**KeReleaseInStackQueuedSpinLockForDpc**](https://msdn.microsoft.com/library/windows/hardware/ff553133) from inside the *CustomThreadedDpc* routine. Note that the *CustomThreadedDpc* routine must not call [**KeAcquireInStackQueuedSpinLockAtDpcLevel**](https://msdn.microsoft.com/library/windows/hardware/ff551908) or [**KeReleaseInStackQueuedSpinLockFromDpcLevel**](https://msdn.microsoft.com/library/windows/hardware/ff553137), because these routines can safely be called only at IRQL = DISPATCH\_LEVEL.

Because **KeAcquireSpinLockForDpc** and **KeAcquireInStackQueuedSpinLockForDpc** do not reset the IRQL when called at DISPATCH\_LEVEL, they execute faster than **KeAcquireSpinLock** and **KeAcquireInStackQueuedSpinLock**, respectively.

For more information about spin locks, see [Spin Locks](spin-locks.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Synchronization%20and%20Threaded%20DPCs%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


