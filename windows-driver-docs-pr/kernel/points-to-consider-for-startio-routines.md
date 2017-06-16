---
title: Points to Consider for StartIo Routines
author: windows-driver-content
description: Points to Consider for StartIo Routines
ms.assetid: 389240d0-682f-48b3-940f-c107e9f60155
keywords: ["StartIo routines, about StartIo routines"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Points to Consider for StartIo Routines


## <a href="" id="ddk-points-to-consider-for-startio-routines-kg"></a>


Keep the following points in mind when implementing a [*StartIo*](https://msdn.microsoft.com/library/windows/hardware/ff563858) routine:

-   A *StartIo* routine must synchronize its access to a physical device and to any shared state information or resources that the driver maintains in the device extension with the driver's other routines that access the same device, memory location, or resources.

    If the *StartIo* routine shares the device or state with the ISR, it must use [**KeSynchronizeExecution**](https://msdn.microsoft.com/library/windows/hardware/ff553302) to call a driver-supplied [*SynchCritSection*](https://msdn.microsoft.com/library/windows/hardware/ff563928) routine to program the device or to access the shared state. For more information, see [Using Critical Sections](using-critical-sections.md).

    If the *StartIo* routine shares state or resources with routines other than the ISR, it must protect the shared state or resources with a driver-initialized executive spin lock for which the driver provides the storage. For more information, see [Spin Locks](spin-locks.md).

-   If a monolithic non-WDM device driver sets up a controller object, its *StartIo* routine can use the controller object to synchronize operations through a shared physical device with attached (similar) devices.

    See [Controller Objects](using-controller-objects.md) for more information.

-   Unless a closely coupled higher-level driver presplits large DMA transfer requests for its underlying device driver, the underlying device driver's *StartIo* routine must split large transfer requests into partial-transfer ranges and the driver must carry out a sequence of partial-transfer device operations. Each partial transfer must be sized to suit the capabilities of the hardware: either the capabilities of the driver's device or, for a subordinate DMA device, the capabilities of the system DMA controller, whichever has stricter constraints.

    See [Adapter Objects and DMA](adapter-objects-and-dma.md) for more information about using system or bus-master DMA.

-   The *StartIo* routine of a driver that uses DMA must synchronize transfers using an [adapter object](adapter-objects-and-dma.md).

-   A *StartIo* routine is run at IRQL = DISPATCH\_LEVEL, which restricts the set of support routines it can call.

    For example, a *StartIo* routine can neither access nor allocate pageable memory, and it cannot wait for a dispatcher object to be set to the signaled state. On the other hand, a *StartIo* routine can acquire and release a driver-allocated executive spin lock with [**KeAcquireSpinLockAtDpcLevel**](https://msdn.microsoft.com/library/windows/hardware/ff551921) and [**KeReleaseSpinLockFromDpcLevel**](https://msdn.microsoft.com/library/windows/hardware/ff553150), which run faster than [**KeAcquireSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff551917) and [**KeReleaseSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff553145).

    See [Managing Hardware Priorities](managing-hardware-priorities.md) and [Spin Locks](spin-locks.md) for more information.

-   If the driver holds IRPs in a cancelable state, its *StartIo* routine must check whether the input IRP has already been canceled before it begins any processing for that request on its device. For more information, see [Canceling IRPs](canceling-irps.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Points%20to%20Consider%20for%20StartIo%20Routines%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


