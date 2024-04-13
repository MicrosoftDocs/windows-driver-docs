---
title: Points to Consider for StartIo Routines
description: Points to Consider for StartIo Routines
keywords: ["StartIo routines, about StartIo routines"]
ms.date: 06/16/2017
---

# Points to Consider for StartIo Routines





Keep the following points in mind when implementing a [*StartIo*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_startio) routine:

-   A *StartIo* routine must synchronize its access to a physical device and to any shared state information or resources that the driver maintains in the device extension with the driver's other routines that access the same device, memory location, or resources.

    If the *StartIo* routine shares the device or state with the ISR, it must use [**KeSynchronizeExecution**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kesynchronizeexecution) to call a driver-supplied [*SynchCritSection*](/windows-hardware/drivers/ddi/wdm/nc-wdm-ksynchronize_routine) routine to program the device or to access the shared state. For more information, see [Using Critical Sections](using-critical-sections.md).

    If the *StartIo* routine shares state or resources with routines other than the ISR, it must protect the shared state or resources with a driver-initialized executive spin lock for which the driver provides the storage. For more information, see [Spin Locks](./introduction-to-spin-locks.md).

-   If a monolithic non-WDM device driver sets up a controller object, its *StartIo* routine can use the controller object to synchronize operations through a shared physical device with attached (similar) devices.

    See [Controller Objects](./introduction-to-controller-objects.md) for more information.

-   Unless a closely coupled higher-level driver presplits large DMA transfer requests for its underlying device driver, the underlying device driver's *StartIo* routine must split large transfer requests into partial-transfer ranges and the driver must carry out a sequence of partial-transfer device operations. Each partial transfer must be sized to suit the capabilities of the hardware: either the capabilities of the driver's device or, for a subordinate DMA device, the capabilities of the system DMA controller, whichever has stricter constraints.

    See [Adapter Objects and DMA](./introduction-to-adapter-objects.md) for more information about using system or bus-master DMA.

-   The *StartIo* routine of a driver that uses DMA must synchronize transfers using an [adapter object](./introduction-to-adapter-objects.md).

-   A *StartIo* routine is run at IRQL = DISPATCH\_LEVEL, which restricts the set of support routines it can call.

    For example, a *StartIo* routine can neither access nor allocate pageable memory, and it cannot wait for a dispatcher object to be set to the signaled state. On the other hand, a *StartIo* routine can acquire and release a driver-allocated executive spin lock with [**KeAcquireSpinLockAtDpcLevel**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keacquirespinlockatdpclevel) and [**KeReleaseSpinLockFromDpcLevel**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kereleasespinlockfromdpclevel), which run faster than [**KeAcquireSpinLock**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keacquirespinlock) and [**KeReleaseSpinLock**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kereleasespinlock).

    See [Managing Hardware Priorities](managing-hardware-priorities.md) and [Spin Locks](./introduction-to-spin-locks.md) for more information.

-   If the driver holds IRPs in a cancelable state, its *StartIo* routine must check whether the input IRP has already been canceled before it begins any processing for that request on its device. For more information, see [Canceling IRPs](canceling-irps.md).

 

