---
title: Always Preemptible and Always Interruptible
description: Always Preemptible and Always Interruptible
ms.assetid: 3da667b4-50f3-4536-9049-65719fa003ce
keywords: ["preemptible designs WDK kernel", "interruptible designs WDK kernel", "interrupt request levels WDK kernel", "IRQL levels WDK kernel", "variable priority attributes WDK kernel", "prioritizing criteria WDK kernel", "hardware priorities WDK kernel", "higher IRQL levels WDK kernel", "lower IRQL levels WDK kernel", "PASSIVE_LEVEL WDK", "APC_LEVEL WDK", "DISPATCH_LEVEL WDK", "WAKE_LEVEL WDK", "deferred procedure calls WDK kernel", "DPCs WDK kernel", "arbitrary thread context WDK kernel", "thread preemption WDK kernel", "thread priorities WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Always Preemptible and Always Interruptible





The goal of the preemptible, interruptible design of the operating system is to maximize system performance. Any thread can be preempted by a thread with a higher priority, and any driver's interrupt service routine (ISR) can be interrupted by a routine that runs at a higher interrupt request level (IRQL).

The kernel component determines when a code sequence runs, according to one of these prioritizing criteria:

-   The kernel-defined run-time priority scheme for threads.

    Every thread in the system has an associated priority attribute. In general, most threads have *variable* priority attributes: they are always preemptible and are scheduled to run round-robin with all other threads that are currently at the same priority level. Some threads have *real-time* priority attributes: these time-critical threads run to completion unless they are preempted by a thread that has a higher real-time priority attribute. The Microsoft Windows architecture does not provide an inherently real-time system.

    Whatever its priority attribute, any thread in the system can be preempted when hardware interrupts and certain types of software interrupts occur.

-   The kernel-defined *interrupt request level* (IRQL) to which a particular interrupt vector is assigned on a given platform.

    The kernel prioritizes hardware and software interrupts so that some kernel-mode code, including most drivers, runs at higher IRQLs, thereby making it have a higher scheduling priority than other threads in the system. The particular IRQL at which a piece of kernel-mode driver code executes is determined by the *hardware priority* of its underlying device.

    Kernel-mode code is always interruptible: an interrupt with a higher IRQL value can occur at any time, thereby causing another piece of kernel-mode code that has a higher system-assigned IRQL to be run immediately on that processor. However, when a piece of code runs at a given IRQL, the kernel masks all interrupt vectors with a lesser or equal IRQL value on the processor.

The lowest IRQL level is called PASSIVE\_LEVEL. At this level, no interrupt vectors are masked. Threads generally run at IRQL=PASSIVE\_LEVEL. The next higher IRQL levels are for software interrupts. These levels include APC\_LEVEL, DISPATCH\_LEVEL or, for kernel debugging, WAKE\_LEVEL. Device interrupts have still higher IRQL values. The kernel reserves the highest IRQL values for system-critical interrupts, such as those from the system clock or bus errors.

Some system support routines run at IRQL=PASSIVE\_LEVEL, either because they are implemented as pageable code or access pageable data, or because some kernel-mode components set up their own threads.

Similarly, some [standard driver routines](https://msdn.microsoft.com/library/windows/hardware/ff563842) usually run at IRQL=PASSIVE\_LEVEL. However, several standard driver routines run either at IRQL=DISPATCH\_LEVEL or, for a lowest-level driver, at device IRQL (also called *DIRQL*). For more information about IRQLs, see [Managing Hardware Priorities](managing-hardware-priorities.md).

Every routine in a driver is interruptible. This includes any routine that is running at a higher IRQL than PASSIVE\_LEVEL. Any routine that is running at a particular IRQL retains control of the processor only if no interrupt for a higher IRQL occurs while that routine is running.

Unlike the drivers in some older personal computer operating systems, a Microsoft Windows driver's ISR is never a large, complex routine that does most of the driver's I/O processing. This is because any driver's *interrupt service routine* (ISR) can be interrupted by another routine (for example, by another driver's ISR) that runs at a higher IRQL. Thus, the driver's ISR does not necessarily retain control of a CPU, uninterrupted, from the beginning of its execution path to the end.

In Windows drivers, an ISR typically saves hardware state information, queues a *deferred procedure call* (DPC), and then quickly exits. Later, the system dequeues the driver's DPC so that the driver can complete I/O operations at a lower IRQL (DISPATCH\_LEVEL). For good overall system performance, all routines that run at high IRQLs must relinquish control of the CPU quickly.

In Windows, all threads have a thread context. This context consists of information that identifies the process that owns the thread, plus other characteristics such as the thread's access rights.

In general, only a highest-level driver is called in the context of the thread that is requesting the driver's current I/O operation. An intermediate-level or lowest-level driver can never assume that it is executing in the context of the thread that requested its current I/O operation.

Consequently, driver routines usually execute in an *arbitrary thread context*—the context of whatever thread is current when a standard driver routine is called. For performance reasons (to avoid context switches), very few drivers set up their own threads.

 

 




