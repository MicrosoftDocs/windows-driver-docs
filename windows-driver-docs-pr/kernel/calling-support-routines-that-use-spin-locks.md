---
title: Calling Support Routines That Use Spin Locks
description: Calling Support Routines That Use Spin Locks
keywords: ["KeAcquireSpinLock", "KeAcquireInStackQueuedSpinLock", "spin locks WDK kernel", "calling spin lock support routines WDK kernel", "executive spin locks WDK kernel", "interrupt spin locks WDK kernel", "queued spin locks WDK kernel"]
ms.date: 06/16/2017
---

# Calling Support Routines That Use Spin Locks





Calling [**KeAcquireSpinLock**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keacquirespinlock) or [**KeAcquireInStackQueuedSpinLock**](/previous-versions/windows/hardware/drivers/ff551899(v=vs.85)) sets the IRQL on the current processor to DISPATCH\_LEVEL until a corresponding call to [**KeReleaseSpinLock**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kereleasespinlock) or [**KeReleaseInStackQueuedSpinLock**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kereleaseinstackqueuedspinlock) restores the previous IRQL. Consequently, drivers must be executing at IRQL &lt;= DISPATCH\_LEVEL when they call **KeAcquireSpinLock** or **KeAcquireInStackQueuedSpinLock**.

Callers of [**KeAcquireSpinLockAtDpcLevel**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keacquirespinlockatdpclevel), [**KeAcquireInStackQueuedSpinLockAtDpcLevel**](/previous-versions/windows/hardware/drivers/ff551908(v=vs.85)), [**KeReleaseInStackQueuedSpinLockFromDpcLevel**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kereleaseinstackqueuedspinlockfromdpclevel), and [**KeReleaseSpinLockFromDpcLevel**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kereleasespinlockfromdpclevel) run faster because they are already running at IRQL = DISPATCH\_LEVEL so these support routines need not reset IRQL on the current processor. Consequently, it is a fatal error on most Windows platforms to call **KeAcquireSpinLockAtDpcLevel** or **KeAcquireInStackQueuedSpinLockAtDpcLevel** while running at IRQL less than DISPATCH\_LEVEL. It is also an error to release a spin lock that was acquired with **KeAcquireSpinLock** by calling **KeReleaseSpinLockFromDpcLevel** because the caller's original IRQL is not restored.

Routines that hold an executive spin lock, such as the <strong>ExInterlocked*Xxx</strong><em>, usually execute at IRQL = DISPATCH\_LEVEL until they release the spin lock and return control to the caller. However, it is possible for a driver's [</em>InterruptService<em>](/windows-hardware/drivers/ddi/wdm/nc-wdm-kservice_routine) routine and [</em>SynchCritSection<em>](/windows-hardware/drivers/ddi/wdm/nc-wdm-ksynchronize_routine) routines (which run at DIRQL) to call certain **ExInterlocked</em>Xxx*** routines, such as the **ExInterlocked*Xxx*List** routines, as long as the spin lock passed to the routine is used exclusively by the ISR and *SynchCritSection* routines.

Each routine that holds an interrupt spin lock executes at the DIRQL of an associated set of interrupt objects. Therefore, a driver must not call **KeAcquireSpinLock** and **KeReleaseSpinLock** nor any other routine that uses an executive spin lock from its ISR or *SynchCritSection* routines. Such a call is an error that can cause a system deadlock, requiring the user to reboot his or her machine. Note that if a driver's ISR or *SynchCritSection* routine calls an **ExInterlocked*Xxx*List** routine, the driver cannot reuse the spin lock it passes to the **ExInterlocked*Xxx*List** routines in calls to the **Ke*Xxx*SpinLock** or **Ke*Xxx*SpinLock*Xxx*DpcLevel** support routines.

If a driver has a multivector ISR or more than one ISR, its routines can call [**KeSynchronizeExecution**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kesynchronizeexecution) while executing at any IRQL up to the *SynchronizeIrql* value specified for the associated interrupt objects when they were connected.

