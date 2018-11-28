---
title: Managing Interlocked Queues with a Driver-Created Thread
description: Managing Interlocked Queues with a Driver-Created Thread
ms.assetid: e2712d52-e98a-4450-b010-9278db3a7a1e
keywords: ["interlocked IRP queues WDK kernel", "driver-created threads WDK IRPs", "doubly linked IRPs WDK kernel", "driver-dedicated threads WDK IRPs"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Managing Interlocked Queues with a Driver-Created Thread





New drivers should use the [cancel-safe IRP queue](cancel-safe-irp-queues.md) framework in preference to the methods outlined in this section.

Like the system floppy controller driver, a driver with a device-dedicated thread, rather than a [*StartIo*](https://msdn.microsoft.com/library/windows/hardware/ff563858) routine, usually manages its own queuing of IRPs in a doubly linked interlocked queue. The driver's thread pulls IRPs from its interlocked queue when there is work to be done on the device.

In general, the driver must manage synchronization with its thread to any resources shared between the thread and other driver routines. The driver also must have some way to notify its driver-created thread that IRPs are queued. Usually, the thread waits on a dispatcher object, stored in the device extension, until the driver's Dispatch routines set the dispatcher object to the Signaled state after inserting an IRP into the interlocked queue.

When the driver's Dispatch routines are called, each checks the parameters in the I/O stack location of the input IRP and, if they are valid, queues the request for further processing. For each IRP queued to a driver-dedicated thread, the dispatch routine should set up whatever context its thread needs to process that IRP before it calls **ExInterlockedInsert*Xxx*List**. The driver's I/O stack location in each IRP gives the driver's thread access to the device extension of the target device object, where the driver can share context information with its thread, as the thread removes each IRP from the queue.

A driver that queue cancelable IRPs must implement a [*Cancel*](https://msdn.microsoft.com/library/windows/hardware/ff540742) routine. Since IRPs are canceled asynchronously, you must ensure that your driver avoids the race conditions that can result. See [Synchronizing IRP Cancellation](synchronizing-irp-cancellation.md) For more information about race conditions associated with canceling IRPs and techniques to avoid them.

Any driver-created thread runs at IRQL = PASSIVE\_LEVEL and at a base run-time priority previously set when the driver called [**PsCreateSystemThread**](https://msdn.microsoft.com/library/windows/hardware/ff559932). The thread's call to [**ExInterlockedRemoveHeadList**](https://msdn.microsoft.com/library/windows/hardware/ff545427) temporarily raises the IRQL to DISPATCH\_LEVEL on the current processor while the IRP is being removed from the driver's internal queue. The original IRQL is restored to PASSIVE\_LEVEL on return from this call.

**Any driver thread (or driver-supplied worker-thread callback) must carefully manage the IRQLs at which it runs. For example, consider the following:**

-   Because system threads generally run at IRQL = PASSIVE\_LEVEL, it is possible for a driver thread to wait for kernel-defined dispatcher objects to be set to the signaled state.

    For example, a device-dedicated thread might wait for other drivers to satisfy an event and complete some number of partial-transfer IRPs that the thread sets up with [**IoBuildSynchronousFsdRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548330).

-   However, such a device-dedicated thread must raise IRQL on the current processor before it calls certain support routines.

    For example, if a driver uses DMA, its device-dedicated thread must nest its calls to [**AllocateAdapterChannel**](https://msdn.microsoft.com/library/windows/hardware/ff540573) and [**FreeAdapterChannel**](https://msdn.microsoft.com/library/windows/hardware/ff546507) between calls to [**KeRaiseIrql**](https://msdn.microsoft.com/library/windows/hardware/ff553079) and [**KeLowerIrql**](https://msdn.microsoft.com/library/windows/hardware/ff552968) because these routines and certain other support routines for DMA operations must be called at IRQL = DISPATCH\_LEVEL.

    Remember that [*StartIo*](https://msdn.microsoft.com/library/windows/hardware/ff563858) routines are run at DISPATCH\_LEVEL, so drivers that use DMA need not make calls to the **Ke*Xxx*Irql** routines from their *StartIo* routines.

-   A driver-created thread can access pageable memory because it runs in a nonarbitrary thread context (its own) at IRQL = PASSIVE\_LEVEL, but many other standard driver routines run at IRQL &gt;= DISPATCH\_LEVEL. If a driver-created thread allocates memory that can be accessed by such a routine, it must allocate the memory from nonpaged pool. For example, if a device-dedicated thread allocates any buffer that will be accessed later by the driver's ISR or [*SynchCritSection*](https://msdn.microsoft.com/library/windows/hardware/ff563928), [*AdapterControl*](https://msdn.microsoft.com/library/windows/hardware/ff540504), [*AdapterListControl*](https://msdn.microsoft.com/library/windows/hardware/ff540513), [*ControllerControl*](https://msdn.microsoft.com/library/windows/hardware/ff542049), [*DpcForIsr*](https://msdn.microsoft.com/library/windows/hardware/ff544079), [*CustomDpc*](https://msdn.microsoft.com/library/windows/hardware/ff542972), [*IoTimer*](https://msdn.microsoft.com/library/windows/hardware/ff550381), [*CustomTimerDpc*](https://msdn.microsoft.com/library/windows/hardware/ff542983), or, in a higher-level driver, [*IoCompletion*](https://msdn.microsoft.com/library/windows/hardware/ff548354) routine, the thread-allocated memory cannot be pageable.

-   If the driver maintains shared state information or resources in a device extension, a driver thread (like a *StartIo* routine) must synchronize its access to a physical device and to the shared data with the driver's other routines that access the same device, memory location, or resources.

    If the thread shares the device or state with the ISR, it must use [**KeSynchronizeExecution**](https://msdn.microsoft.com/library/windows/hardware/ff553302) to call a driver-supplied [*SynchCritSection*](https://msdn.microsoft.com/library/windows/hardware/ff563928) routine to program the device or to access the shared state. See [Using Critical Sections](using-critical-sections.md).

    If the thread shares state or resources with routines other than the ISR, the driver must protect the shared state or resources with a driver-initialized executive spin lock for which the driver provides the storage. For more information, see [Spin Locks](spin-locks.md).

For more information about the design tradeoffs of a using a driver thread for a slow device, see [Polling a Device](avoid-polling-devices.md). See also [Managing Hardware Priorities](managing-hardware-priorities.md). For specific information about IRQLs for particular support routines, see the routine's reference page.

 

 




