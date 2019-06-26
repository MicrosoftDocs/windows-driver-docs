---
title: Guidelines for Writing DPC Routines
description: Guidelines for Writing DPC Routines
ms.assetid: 570219be-d152-4826-855a-737bbed67ffd
keywords: ["deferred procedure calls WDK kernel", "DPCs WDK kernel", "DpcForIsr", "CustomDpc"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Guidelines for Writing DPC Routines





Keep the following points in mind when writing a [*DpcForIsr*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nc-wdm-io_dpc_routine) or [*CustomDpc*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nc-wdm-kdeferred_routine) routine:

-   A *DpcForIsr* or *CustomDpc* routine must synchronize its access to a physical device, and to any shared state information or resources that the driver maintains, with the driver's other routines that access the same device or memory locations.

    If a *DpcForIsr* or *CustomDpc* routine shares the device or state with an ISR, it must call [**KeSynchronizeExecution**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-kesynchronizeexecution), supplying the address of a driver-supplied [*SynchCritSection*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nc-wdm-ksynchronize_routine) routine that programs the device or accesses the shared state. For more information, see [Using Critical Sections](using-critical-sections.md).

    If a *DpcForIsr* or *CustomDpc* routine shares state or resources, such as an interlocked queue or a timer object, with routines other than an ISR, it must protect the shared state or resources with a driver-initialized executive spin lock. For more information, see [Spin Locks](spin-locks.md).

-   *DpcForIsr* and *CustomDpc* routines run at IRQL = DISPATCH\_LEVEL, which restricts the set of support routines they can call.

    For example, *DpcForIsr* and *CustomDpc* routines can neither access nor allocate pageable memory, and they cannot wait for [kernel dispatcher objects](kernel-dispatcher-objects.md) to be set to the signaled state. On the other hand, they can acquire and release a driver's executive spin lock with [**KeAcquireSpinLockAtDpcLevel**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-keacquirespinlockatdpclevel) and [**KeReleaseSpinLockFromDpcLevel**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-kereleasespinlockfromdpclevel), which run faster than **KeAcquireSpinLock** and **KeReleaseSpinLock**.

    Although a DPC routine cannot make blocking calls, it can queue a work item to run in a [system worker thread](system-worker-threads.md) that runs at IRQL = PASSIVE\_LEVEL. The work item can make blocking calls that wait on dispatcher objects. To queue a work item, a *DpcForIsr* routine typically calls a routine such as [**IoQueueWorkItem**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-ioqueueworkitem), and a *CustomDpc* routine typically calls the [**ExQueueWorkItem**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-exqueueworkitem) routine.

-   *DpcForIsr* and *CustomDpc* routines are typically responsible for starting the next I/O operation on the device.

    For lowest-level physical device drivers that use direct I/O, this responsibility can include using a [*SynchCritSection*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nc-wdm-ksynchronize_routine) routine to program the device to transfer more data in order to satisfy the current IRP before the driver calls [**IoStartNextPacket**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntifs/nf-ntifs-iostartnextpacket).

-   *DpcForIsr* and *CustomDpc* routines should run only for brief periods, and should delegate as much processing as possible to worker threads.

    While a DPC routine runs on a processor, all threads are prevented from running on the same processor. Other DPC routines that are queued and ready to run can be blocked from executing until the current DPC routine is finished. To avoid degrading system responsiveness, a typical DPC routine should run for no more than 100 microseconds each time it is called. If a task requires longer than 100 microseconds and must execute at IRQL = DISPATCH\_LEVEL, the DPC routine should end after 100 microseconds and schedule one or more [*CustomTimerDpc*](https://msdn.microsoft.com/library/windows/hardware/ff542983) routines to complete the task at a later time. For more information about *CustomTimerDpc* routines, see [Timer Objects and DPCs](timer-objects-and-dpcs.md).

    A DPC routine should perform only tasks that must run at DISPATCH\_LEVEL, and then delegate any remaining interrupt-related work to threads that run at IRQL = PASSIVE\_LEVEL. For example, a DPC routine can queue a work item to run in a [system worker thread](system-worker-threads.md).

    DPC routines that call the [**KeStallExecutionProcessor**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntifs/nf-ntifs-kestallexecutionprocessor) routine to delay execution must not specify delays of more than 100 microseconds.

    Use the performance analysis tools in the WDK to evaluate the execution times of DPC routines. For an example that uses the [Tracelog](https://docs.microsoft.com/windows-hardware/drivers/devtest/tracelog) tool to monitor DPC execution times, see [Example 15: Measuring DPC/ISR Time](https://docs.microsoft.com/windows-hardware/drivers/devtest/example-15--measuring-dpc-isr-time).

-   If the driver uses DMA and its [*AdapterControl*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nc-wdm-driver_control) routine returns **KeepObject** or **DeallocateObjectKeepRegisters** (thereby retaining the system DMA controller channel or bus-master adapter for additional transfer operations), the *DpcForIsr* or *CustomDpc* routine is responsible for releasing the adapter object or map registers with [**FreeAdapterChannel**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nc-wdm-pfree_adapter_channel) or [**FreeMapRegisters**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nc-wdm-pfree_map_registers) before it completes the current IRP and returns control.

-   If a lowest-level physical device driver sets up a [controller object](using-controller-objects.md) to synchronize I/O operations through the controller to attached devices, its *DpcForIsr* or *CustomDpc* routine is responsible for releasing the controller object using [**IoFreeController**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddk/nf-ntddk-iofreecontroller) before it completes the current IRP and returns control.

-   *DpcForIsr* and *CustomDpc* routines are generally responsible for logging any device errors that occurred during the processing of a given request, retrying the current request if necessary and possible, and for setting the I/O status block and calling [**IoCompleteRequest**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-iocompleterequest) for the current IRP.

-   If the driver and device support overlapped I/O operations, the driver must follow the rules for [handling overlapped I/O operations](handling-overlapped-i-o-operations.md).

-   The *DpcForIsr* or *CustomDpc* routine of any driver usually completes the I/O processing only for a subset of the public I/O control codes that the driver must support. In particular, the DPC routine completes operations for device control requests with the following characteristics:
    -   Requests that change the state of the physical device
    -   Requests that require the return of inherently volatile information about the physical device

 

 




