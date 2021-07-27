---
title: Guidelines for Writing DPC Routines
description: Guidelines for Writing DPC Routines
keywords: ["deferred procedure calls WDK kernel", "DPCs WDK kernel", "DpcForIsr", "CustomDpc"]
ms.date: 07/21/2021
ms.localizationpriority: medium
---

# Guidelines for Writing DPC Routines

Keep the following points in mind when writing a [*DpcForIsr*](/windows-hardware/drivers/ddi/wdm/nc-wdm-io_dpc_routine) or [*CustomDpc*](/windows-hardware/drivers/ddi/wdm/nc-wdm-kdeferred_routine) routine:

- A *DpcForIsr* or *CustomDpc* routine must synchronize its access to a physical device, and to any shared state information or resources that the driver maintains, with the driver's other routines that access the same device or memory locations.

    If a *DpcForIsr* or *CustomDpc* routine shares the device or state with an ISR, it must call [**KeSynchronizeExecution**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kesynchronizeexecution), supplying the address of a driver-supplied [*SynchCritSection*](/windows-hardware/drivers/ddi/wdm/nc-wdm-ksynchronize_routine) routine that programs the device or accesses the shared state. For more information, see [Using Critical Sections](using-critical-sections.md).

    If a *DpcForIsr* or *CustomDpc* routine shares state or resources, such as an interlocked queue or a timer object, with routines other than an ISR, it must protect the shared state or resources with a driver-initialized executive spin lock. For more information, see [Spin Locks](./introduction-to-spin-locks.md).

- *DpcForIsr* and *CustomDpc* routines run at IRQL = DISPATCH_LEVEL, which restricts the set of support routines they can call.

    For example, *DpcForIsr* and *CustomDpc* routines can neither access nor allocate pageable memory, and they cannot wait for [kernel dispatcher objects](./introduction-to-kernel-dispatcher-objects.md) to be set to the signaled state. On the other hand, they can acquire and release a driver's executive spin lock with [**KeAcquireSpinLockAtDpcLevel**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keacquirespinlockatdpclevel) and [**KeReleaseSpinLockFromDpcLevel**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kereleasespinlockfromdpclevel), which run faster than **KeAcquireSpinLock** and **KeReleaseSpinLock**.

    Although a DPC routine cannot make blocking calls, it can queue a work item to run in a [system worker thread](system-worker-threads.md) that runs at IRQL equal to PASSIVE_LEVEL. The work item can make blocking calls that wait on dispatcher objects. To queue a work item, a *DpcForIsr* routine typically calls a routine such as [**IoQueueWorkItem**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioqueueworkitem), and a *CustomDpc* routine typically calls the [**ExQueueWorkItem**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exqueueworkitem) routine.

- *DpcForIsr* and *CustomDpc* routines are typically responsible for starting the next I/O operation on the device.

    For lowest-level physical device drivers that use direct I/O, this responsibility can include using a [*SynchCritSection*](/windows-hardware/drivers/ddi/wdm/nc-wdm-ksynchronize_routine) routine to program the device to transfer more data in order to satisfy the current IRP before the driver calls [**IoStartNextPacket**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-iostartnextpacket).

- *DpcForIsr* and *CustomDpc* routines should run only for brief periods, and should delegate as much processing as possible to worker threads.

    While a DPC routine runs on a processor, all threads are prevented from running on the same processor. Other DPC routines that are queued and ready to run can be blocked from executing until the current DPC routine is finished. To avoid degrading system responsiveness, a typical DPC routine should run for no more than 100 microseconds each time it is called. If a task requires longer than 100 microseconds and must execute at IRQL equal to DISPATCH_LEVEL, the DPC routine should end after 100 microseconds and schedule one or more [*CustomTimerDpc*](using-a-customtimerdpc-routine.md) routines to complete the task at a later time. For more information about *CustomTimerDpc* routines, see [Timer Objects and DPCs](timer-objects-and-dpcs.md).

    A DPC routine should perform only tasks that must run at DISPATCH_LEVEL, and then delegate any remaining interrupt-related work to threads that run at IRQL = PASSIVE_LEVEL. For example, a DPC routine can queue a work item to run in a [system worker thread](system-worker-threads.md).

    DPC routines that call the [**KeStallExecutionProcessor**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-kestallexecutionprocessor) routine to delay execution must not specify delays of more than 100 microseconds.

    Use the performance analysis tools in the WDK to evaluate the execution times of DPC routines. For an example that uses the [Tracelog](../devtest/tracelog.md) tool to monitor DPC execution times, see [Example 15: Measuring DPC/ISR Time](../devtest/example-15--measuring-dpc-isr-time.md).

- If the driver uses DMA and its [*AdapterControl*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_control) routine returns **KeepObject** or **DeallocateObjectKeepRegisters** (thereby retaining the system DMA controller channel or bus-master adapter for additional transfer operations), the *DpcForIsr* or *CustomDpc* routine is responsible for releasing the adapter object or map registers with [**FreeAdapterChannel**](/windows-hardware/drivers/ddi/wdm/nc-wdm-pfree_adapter_channel) or [**FreeMapRegisters**](/windows-hardware/drivers/ddi/wdm/nc-wdm-pfree_map_registers) before it completes the current IRP and returns control.

- If a lowest-level physical device driver sets up a [controller object](./introduction-to-controller-objects.md) to synchronize I/O operations through the controller to attached devices, its *DpcForIsr* or *CustomDpc* routine is responsible for releasing the controller object using [**IoFreeController**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-iofreecontroller) before it completes the current IRP and returns control.

- *DpcForIsr* and *CustomDpc* routines are generally responsible for logging any device errors that occurred during the processing of a given request, retrying the current request if necessary and possible, and for setting the I/O status block and calling [**IoCompleteRequest**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocompleterequest) for the current IRP.

- If the driver and device support overlapped I/O operations, the driver must follow the rules for [handling overlapped I/O operations](handling-overlapped-i-o-operations.md).

- The *DpcForIsr* or *CustomDpc* routine of any driver usually completes the I/O processing only for a subset of the public I/O control codes that the driver must support. In particular, the DPC routine completes operations for device control requests with the following characteristics:

  - Requests that change the state of the physical device

  - Requests that require the return of inherently volatile information about the physical device
