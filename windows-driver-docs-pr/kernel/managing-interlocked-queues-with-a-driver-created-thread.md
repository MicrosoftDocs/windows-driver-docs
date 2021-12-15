---
title: Managing Interlocked Queues with a Driver-Created Thread
description: Managing Interlocked Queues with a Driver-Created Thread
keywords: ["interlocked IRP queues WDK kernel", "driver-created threads WDK IRPs", "doubly linked IRPs WDK kernel", "driver-dedicated threads WDK IRPs"]
ms.date: 07/22/2021
---

# Managing Interlocked Queues with a Driver-Created Thread

New drivers should use the [cancel-safe IRP queue](cancel-safe-irp-queues.md) framework in preference to the methods outlined in this section.

Like the system floppy controller driver, a driver with a device-dedicated thread, rather than a [*StartIo*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_startio) routine, usually manages its own queuing of IRPs in a doubly linked interlocked queue. The driver's thread pulls IRPs from its interlocked queue when there is work to be done on the device.

In general, the driver must manage synchronization with its thread to any resources shared between the thread and other driver routines. The driver also must have some way to notify its driver-created thread that IRPs are queued. Usually, the thread waits on a dispatcher object, stored in the device extension, until the driver's Dispatch routines set the dispatcher object to the Signaled state after inserting an IRP into the interlocked queue.

When the driver's Dispatch routines are called, each checks the parameters in the I/O stack location of the input IRP and, if they are valid, queues the request for further processing. For each IRP queued to a driver-dedicated thread, the dispatch routine should set up whatever context its thread needs to process that IRP before it calls **ExInterlockedInsert*Xxx*List**. The driver's I/O stack location in each IRP gives the driver's thread access to the device extension of the target device object, where the driver can share context information with its thread, as the thread removes each IRP from the queue.

A driver that queue cancelable IRPs must implement a [*Cancel*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_cancel) routine. Since IRPs are canceled asynchronously, you must ensure that your driver avoids the race conditions that can result. See [Synchronizing IRP Cancellation](synchronizing-irp-cancellation.md) For more information about race conditions associated with canceling IRPs and techniques to avoid them.

Any driver-created thread runs at IRQL = PASSIVE_LEVEL and at a base run-time priority previously set when the driver called [**PsCreateSystemThread**](/windows-hardware/drivers/ddi/wdm/nf-wdm-pscreatesystemthread). The thread's call to [**ExInterlockedRemoveHeadList**](/previous-versions/ff545427(v=vs.85)) temporarily raises the IRQL to DISPATCH_LEVEL on the current processor while the IRP is being removed from the driver's internal queue. The original IRQL is restored to PASSIVE_LEVEL on return from this call.

**Any driver thread (or driver-supplied worker-thread callback) must carefully manage the IRQLs at which it runs. For example, consider the following:**

- Because system threads generally run at IRQL = PASSIVE_LEVEL, it is possible for a driver thread to wait for kernel-defined dispatcher objects to be set to the signaled state.

    For example, a device-dedicated thread might wait for other drivers to satisfy an event and complete some number of partial-transfer IRPs that the thread sets up with [**IoBuildSynchronousFsdRequest**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iobuildsynchronousfsdrequest).

- However, such a device-dedicated thread must raise IRQL on the current processor before it calls certain support routines.

    For example, if a driver uses DMA, its device-dedicated thread must nest its calls to [**AllocateAdapterChannel**](/windows-hardware/drivers/ddi/wdm/nc-wdm-pallocate_adapter_channel) and [**FreeAdapterChannel**](/windows-hardware/drivers/ddi/wdm/nc-wdm-pfree_adapter_channel) between calls to [**KeRaiseIrql**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keraiseirql) and [**KeLowerIrql**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kelowerirql) because these routines and certain other support routines for DMA operations must be called at IRQL = DISPATCH_LEVEL.

    Remember that [*StartIo*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_startio) routines are run at DISPATCH_LEVEL, so drivers that use DMA need not make calls to the **Ke*Xxx*Irql** routines from their *StartIo* routines.

- A driver-created thread can access pageable memory because it runs in a nonarbitrary thread context (its own) at IRQL = PASSIVE_LEVEL, but many other standard driver routines run at IRQL &gt;= DISPATCH_LEVEL. If a driver-created thread allocates memory that can be accessed by such a routine, it must allocate the memory from nonpaged pool. For example, if a device-dedicated thread allocates any buffer that will be accessed later by the driver's ISR or [*SynchCritSection*](/windows-hardware/drivers/ddi/wdm/nc-wdm-ksynchronize_routine), [*AdapterControl*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_control), [*AdapterListControl*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_list_control), [*ControllerControl*](writing-controllercontrolroutines.md), [*DpcForIsr*](/windows-hardware/drivers/ddi/wdm/nc-wdm-io_dpc_routine), [*CustomDpc*](/windows-hardware/drivers/ddi/wdm/nc-wdm-kdeferred_routine), [*IoTimer*](/windows-hardware/drivers/ddi/wdm/nc-wdm-io_timer_routine), [*CustomTimerDpc*](using-a-customtimerdpc-routine.md), or, in a higher-level driver, [*IoCompletion*](/windows-hardware/drivers/ddi/wdm/nc-wdm-io_completion_routine) routine, the thread-allocated memory cannot be pageable.

- If the driver maintains shared state information or resources in a device extension, a driver thread (like a *StartIo* routine) must synchronize its access to a physical device and to the shared data with the driver's other routines that access the same device, memory location, or resources.

    If the thread shares the device or state with the ISR, it must use [**KeSynchronizeExecution**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kesynchronizeexecution) to call a driver-supplied [*SynchCritSection*](/windows-hardware/drivers/ddi/wdm/nc-wdm-ksynchronize_routine) routine to program the device or to access the shared state. See [Using Critical Sections](using-critical-sections.md).

    If the thread shares state or resources with routines other than the ISR, the driver must protect the shared state or resources with a driver-initialized executive spin lock for which the driver provides the storage. For more information, see [Spin Locks](introduction-to-spin-locks.md).

For more information about the design tradeoffs of a using a driver thread for a slow device, see [Polling a Device](avoid-polling-devices.md). See also [Managing Hardware Priorities](managing-hardware-priorities.md). For specific information about IRQLs for particular support routines, see the routine's reference page.
