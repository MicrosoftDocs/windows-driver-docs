---
title: Multiprocessor-Safe
description: Multiprocessor-Safe
ms.assetid: 58c51f3e-98c4-4aa0-ad4d-cd9225f78141
keywords: ["multiprocessor safe WDK kernel", "symmetric multiprocessor platforms WDK kernel", "SMP WDK kernel", "spin locks WDK kernel", "synchronization WDK kernel , multiprocessor safe", "symmetric platforms WDK kernel", "locking WDK kernel", "deadlocks WDK kernel", "critical section routines WDK kernel", "shared data protections WDK kernel", "dispatcher objects WDK kernel , multiprocessor safe", "kernel dispatcher objects WDK , multiprocessor safe"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Multiprocessor-Safe





The Microsoft Windows NT-based operating system is designed to run uniformly on uniprocessor and symmetric multiprocessor (SMP) platforms, and kernel-mode drivers should be designed to do likewise.

In any Windows multiprocessor platform, the following conditions exist:

-   All CPUs are identical, and either all or none of the processors must have identical coprocessors.

-   All CPUs share memory and have uniform access to memory.

-   In a *symmetric* platform, every CPU can access memory, take an interrupt, and access I/O control registers. (By contrast, in an *asymmetric* multiprocessor machine, one CPU takes all interrupts for a set of subordinate CPUs.)

To run safely on an SMP platform, an operating system must guarantee that code that executes on one processor does not simultaneously access and modify data that another processor is accessing and modifying. For example, if a lowest-level driver's ISR is handling a device interrupt on one processor, it must have exclusive access to device registers or critical, driver-defined data, in case its device interrupts simultaneously on another processor.

Furthermore, drivers' I/O operations that are serialized in a uniprocessor machine can be overlapped in an SMP machine. That is, a driver's routine that processes incoming I/O requests can be executing on one processor while another routine that communicates with the device executes concurrently on another processor. Whether kernel-mode drivers are executing on a uniprocessor or symmetric multiprocessor machine, they must synchronize access to any driver-defined data or system-provided resources that are shared among driver routines, and synchronize access to the physical device, if any.

The Windows NT kernel component exports a synchronization mechanism, called a [spin lock](spin-locks.md), that drivers can use to protect shared data (or device registers) from simultaneous access by one or more routines that are running concurrently on a symmetric multiprocessor platform. The kernel enforces two policies regarding the use of spin locks:

-   Only one routine can hold a particular spin lock at any given moment. Before accessing shared data, each routine that must reference the data must first attempt to acquire the data's spin lock. To access the same data, another routine must acquire the spin lock, but the spin lock cannot be acquired until the current holder releases it.

-   The kernel assigns an IRQL value to each spin lock in the system. A kernel-mode routine can acquire a particular spin lock only when the routine is run at the spin lock's assigned IRQL.

These policies prevent a driver routine that usually runs at a lower IRQL but currently holds a spin lock from being preempted by a higher-priority driver routine that is trying to acquire the same spin lock. Thus, a deadlock is avoided.

The IRQL that is assigned to a spin lock is generally that of the highest-IRQL routine that can acquire the spin lock.

For example, a lowest-level driver's ISR frequently shares a state area with the driver's DPC routine. The DPC routine calls a driver-supplied [*critical section*](https://msdn.microsoft.com/library/windows/hardware/ff556274#wdkgloss-critical-section) routine to access the shared area. The spin lock that protects the shared area has an IRQL equal to the DIRQL at which the device interrupts. As long as the critical-section routine holds the spin lock and accesses the shared area at DIRQL, the ISR cannot be run in either a uniprocessor or SMP machine.

-   The ISR cannot be run in a uniprocessor machine because the device interrupt is masked, as described in [Always Preemptible and Always Interruptible](always-preemptible-and-always-interruptible.md).

-   In an SMP machine, the ISR cannot acquire the spin lock that protects the shared data while the critical-section routine holds the spin lock and accesses the shared data at DIRQL.

A set of kernel-mode threads can synchronize access to shared data or resources by waiting for one of the kernel's dispatcher objects: an event, mutex, semaphore, timer, or another thread. However, most drivers do not set up their own threads because they have better performance when they avoid thread-context switches. Whenever time-critical kernel-mode support routines and drivers run at IRQL = DISPATCH\_LEVEL or at DIRQL, they must use the kernel's spin locks to synchronize access to shared data or resources.

For more information, see [Spin Locks](spin-locks.md), [Managing Hardware Priorities](managing-hardware-priorities.md), and [Kernel Dispatcher Objects](kernel-dispatcher-objects.md).

 

 




