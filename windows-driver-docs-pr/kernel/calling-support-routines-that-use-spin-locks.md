---
title: Calling Support Routines That Use Spin Locks
author: windows-driver-content
description: Calling Support Routines That Use Spin Locks
ms.assetid: 89cf1fd4-4f4b-4b82-9e50-e5766918c421
keywords: ["KeAcquireSpinLock", "KeAcquireInStackQueuedSpinLock", "spin locks WDK kernel", "calling spin lock support routines WDK kernel", "executive spin locks WDK kernel", "interrupt spin locks WDK kernel", "queued spin locks WDK kernel"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Calling Support Routines That Use Spin Locks


## <a href="" id="ddk-calling-support-routines-that-use-spin-locks-kg"></a>


Calling [**KeAcquireSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff551917) or [**KeAcquireInStackQueuedSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff551899) sets the IRQL on the current processor to DISPATCH\_LEVEL until a corresponding call to [**KeReleaseSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff553145) or [**KeReleaseInStackQueuedSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff553130) restores the previous IRQL. Consequently, drivers must be executing at IRQL &lt;= DISPATCH\_LEVEL when they call **KeAcquireSpinLock** or **KeAcquireInStackQueuedSpinLock**.

Callers of [**KeAcquireSpinLockAtDpcLevel**](https://msdn.microsoft.com/library/windows/hardware/ff551921), [**KeAcquireInStackQueuedSpinLockAtDpcLevel**](https://msdn.microsoft.com/library/windows/hardware/ff551908), [**KeReleaseInStackQueuedSpinLockFromDpcLevel**](https://msdn.microsoft.com/library/windows/hardware/ff553137), and [**KeReleaseSpinLockFromDpcLevel**](https://msdn.microsoft.com/library/windows/hardware/ff553150) run faster because they are already running at IRQL = DISPATCH\_LEVEL so these support routines need not reset IRQL on the current processor. Consequently, it is a fatal error on most Windows platforms to call **KeAcquireSpinLockAtDpcLevel** or **KeAcquireInStackQueuedSpinLockAtDpcLevel** while running at IRQL less than DISPATCH\_LEVEL. It is also an error to release a spin lock that was acquired with **KeAcquireSpinLock** by calling **KeReleaseSpinLockFromDpcLevel** because the caller's original IRQL is not restored.

Routines that hold an executive spin lock, such as the **ExInterlocked*Xxx***, usually execute at IRQL = DISPATCH\_LEVEL until they release the spin lock and return control to the caller. However, it is possible for a driver's [*InterruptService*](https://msdn.microsoft.com/library/windows/hardware/ff547958) routine and [*SynchCritSection*](https://msdn.microsoft.com/library/windows/hardware/ff563928) routines (which run at DIRQL) to call certain **ExInterlocked*Xxx*** routines, such as the **ExInterlocked*Xxx*List** routines, as long as the spin lock passed to the routine is used exclusively by the ISR and *SynchCritSection* routines.

Each routine that holds an interrupt spin lock executes at the DIRQL of an associated set of interrupt objects. Therefore, a driver must not call **KeAcquireSpinLock** and **KeReleaseSpinLock** nor any other routine that uses an executive spin lock from its ISR or *SynchCritSection* routines. Such a call is an error that can cause a system deadlock, requiring the user to reboot his or her machine. Note that if a driver's ISR or *SynchCritSection* routine calls an **ExInterlocked*Xxx*List** routine, the driver cannot reuse the spin lock it passes to the **ExInterlocked*Xxx*List** routines in calls to the **Ke*Xxx*SpinLock** or **Ke*Xxx*SpinLock*Xxx*DpcLevel** support routines.

If a driver has a multivector ISR or more than one ISR, its routines can call [**KeSynchronizeExecution**](https://msdn.microsoft.com/library/windows/hardware/ff553302) while executing at any IRQL up to the *SynchronizeIrql* value specified for the associated interrupt objects when they were connected.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Calling%20Support%20Routines%20That%20Use%20Spin%20Locks%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


