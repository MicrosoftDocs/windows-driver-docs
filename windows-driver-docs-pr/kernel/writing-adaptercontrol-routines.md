---
title: Writing AdapterControl Routines
description: Writing AdapterControl Routines
ms.assetid: a5a7501f-ba4f-441e-be07-6a1b7fac9938
keywords: ["AdapterControl routines, writing", "adapter objects WDK kernel , writing AdapterControl routines", "DMA transfers WDK kernel , writing AdapterControl routines"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Writing AdapterControl Routines





Most drivers of DMA devices have an [*AdapterControl*](https://msdn.microsoft.com/library/windows/hardware/ff540504) routine, which is responsible for initiating DMA operations. (Drivers that do not require *AdapterControl* routines include those that [use scatter/gather DMA](using-scatter-gather-dma.md) and those that [use common-buffer, bus-master DMA](using-common-buffer-bus-master-dma.md).)

When a driver calls [**AllocateAdapterChannel**](https://msdn.microsoft.com/library/windows/hardware/ff540573), its *AdapterControl* routine is run immediately if the system DMA controller or bus-master adapter is available for a DMA operation, and if enough map registers are available. Otherwise, the *AdapterControl* routine is queued until these resources are available.

If the driver's *AdapterControl* routine returns **KeepObject** or **DeallocateObjectKeepRegisters** (thereby retaining the system DMA controller channel or bus-master adapter for additional transfer operations), the driver's [*DpcForIsr*](https://msdn.microsoft.com/library/windows/hardware/ff544079) or [*CustomDpc*](https://msdn.microsoft.com/library/windows/hardware/ff542972) routine is responsible for releasing the adapter object or map registers by calling [**FreeAdapterChannel**](https://msdn.microsoft.com/library/windows/hardware/ff546507) or [**FreeMapRegisters**](https://msdn.microsoft.com/library/windows/hardware/ff546513) before the DPC routine completes the current IRP and returns control.

 

 




