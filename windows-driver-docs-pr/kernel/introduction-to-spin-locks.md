---
title: Introduction to Spin Locks
description: Introduction to Spin Locks
ms.assetid: a37c0db4-ff9c-4958-a9f4-62b671458d03
keywords: ["KSPIN_LOCK", "executive spin locks WDK kernel", "interrupt spin locks WDK kernel", "queued spin locks WDK kernel", "spin locks WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Introduction to Spin Locks





Spin locks are kernel-defined, kernel-mode-only synchronization mechanisms, exported as an opaque type: KSPIN\_LOCK. A spin lock can be used to protect shared data or resources from simultaneous access by routines that can execute concurrently and at IRQL &gt;= DISPATCH\_LEVEL in SMP machines.

Many components use spin locks, including drivers. Any kind of driver might use one or more *executive spin locks*. For example, most file systems use an interlocked work queue in the file system driver's (FSD's) device extension to store IRPs that are processed both by the file system's worker-thread callback routines and by the FSD. An interlocked work queue is protected by an executive spin lock, which resolves contention among the FSD trying to insert IRPs into the queue and any threads simultaneously trying to remove IRPs. As another example, the system floppy controller driver uses two executive spin locks. One executive spin lock protects an interlocked work queue shared with this driver's device-dedicated thread; the other protects a timer object shared by three driver routines.

Drivers for Microsoft Windows XP and later versions of Windows can use [**KeAcquireInStackQueuedSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff551899) and [**KeReleaseInStackQueuedSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff553130) to acquire and release the spin lock as a *queued spin lock*. Queued spin locks provide better performance than ordinary spin locks for high contention locks on multiprocessor machines. For more information, see [Queued Spin Locks](queued-spin-locks.md). Drivers for Windows 2000 can use [**KeAcquireSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff551917) and [**KeReleaseSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff553145) to acquire and release a spin lock as an ordinary spin lock.

To synchronize access to simple data structures, drivers can use any of the **ExInterlocked*Xxx*** routines to ensure atomic access to the data structure. Drivers that use these routines do not need to acquire or release the spin lock explicitly.

Every driver that has an ISR uses an *interrupt spin lock* to protect any data or hardware shared between its ISR and its [*SynchCritSection*](https://msdn.microsoft.com/library/windows/hardware/ff563928) routines that are usually called from its [*StartIo*](https://msdn.microsoft.com/library/windows/hardware/ff563858) and [*DpcForIsr*](https://msdn.microsoft.com/library/windows/hardware/ff544079) routines. An interrupt spin lock is associated with the set of interrupt objects created when the driver calls [**IoConnectInterrupt**](https://msdn.microsoft.com/library/windows/hardware/ff548371), as described in Registering an ISR.

**Follow these guidelines for using spin locks in drivers:**

-   Provide the storage for any data or resource protected by a spin lock and for the corresponding spin lock in resident system-space memory (nonpaged pool, as shown in the [Virtual Memory Spaces and Physical Memory](overview-of-windows-memory-space.md) figure). A driver must provide the storage for any executive spin locks it uses. However, a device driver need not provide the storage for an interrupt spin lock unless it has a multivector ISR or has more than one ISR, as described in Registering an ISR.

-   Call [**KeInitializeSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff552160) to initialize each spin lock for which the driver provides storage before using it to synchronize access to the shared data or resource it protects.

-   Call every support routine that uses a spin lock at an appropriate IRQL, generally at &lt;= DISPATCH\_LEVEL for executive spin locks or at &lt;= DIRQL for an interrupt spin lock associated with the driver's interrupt objects.

-   Implement routines to execute as quickly as possible while they hold a spin lock. No routine should hold a spin lock for longer than 25 microseconds.

-   Never implement routines that do any of the following while holding a spin lock:

    -   Cause hardware exceptions or raise software exceptions.

    -   Attempt to access pageable memory.

    -   Make a recursive call that would cause a deadlock or could cause a spin lock to be held for longer than 25 microseconds.

    -   Attempt to acquire another spin lock if doing so might cause a deadlock.

    -   Call an external routine that violates any of the preceding rules.

 

 




