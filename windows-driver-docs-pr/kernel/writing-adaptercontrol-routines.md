---
title: Writing AdapterControl Routines
author: windows-driver-content
description: Writing AdapterControl Routines
ms.assetid: a5a7501f-ba4f-441e-be07-6a1b7fac9938
keywords: ["AdapterControl routines, writing", "adapter objects WDK kernel , writing AdapterControl routines", "DMA transfers WDK kernel , writing AdapterControl routines"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Writing AdapterControl Routines


## <a href="" id="ddk-writing-adaptercontrol-routines-kg"></a>


Most drivers of DMA devices have an [*AdapterControl*](https://msdn.microsoft.com/library/windows/hardware/ff540504) routine, which is responsible for initiating DMA operations. (Drivers that do not require *AdapterControl* routines include those that [use scatter/gather DMA](using-scatter-gather-dma.md) and those that [use common-buffer, bus-master DMA](using-common-buffer-bus-master-dma.md).)

When a driver calls [**AllocateAdapterChannel**](https://msdn.microsoft.com/library/windows/hardware/ff540573), its *AdapterControl* routine is run immediately if the system DMA controller or bus-master adapter is available for a DMA operation, and if enough map registers are available. Otherwise, the *AdapterControl* routine is queued until these resources are available.

If the driver's *AdapterControl* routine returns **KeepObject** or **DeallocateObjectKeepRegisters** (thereby retaining the system DMA controller channel or bus-master adapter for additional transfer operations), the driver's [*DpcForIsr*](https://msdn.microsoft.com/library/windows/hardware/ff544079) or [*CustomDpc*](https://msdn.microsoft.com/library/windows/hardware/ff542972) routine is responsible for releasing the adapter object or map registers by calling [**FreeAdapterChannel**](https://msdn.microsoft.com/library/windows/hardware/ff546507) or [**FreeMapRegisters**](https://msdn.microsoft.com/library/windows/hardware/ff546513) before the DPC routine completes the current IRP and returns control.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Writing%20AdapterControl%20Routines%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


