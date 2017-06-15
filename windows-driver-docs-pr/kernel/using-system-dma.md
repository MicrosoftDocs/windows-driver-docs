---
title: Using System DMA
author: windows-driver-content
description: Using System DMA
MS-HAID:
- 'ioprogdma\_fc0ff4f7-c3eb-43da-9321-b4df64a9fef7.xml'
- 'kernel.using\_system\_dma'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 8d478365-a6c8-4488-9f75-53a822d1daa2
keywords: ["AdapterControl routines, system DMA", "system DMA WDK kernel", "adapter objects WDK kernel , system DMA", "DMA transfers WDK kernel , system DMA", "slave devices WDK DMA", "system DMA WDK kernel , about system DMA"]
---

# Using System DMA


## <a href="" id="ddk-using-system-dma-kg"></a>


Drivers of subordinate DMA devices use one of the following types of system-provided DMA support:

-   Packet-based DMA, if the driver need not use a system DMA controller's auto-initialize mode. See [Using Packet-Based System DMA](using-packet-based-system-dma.md).

-   Common-buffer DMA, if the driver does use the auto-initialize mode. See [Using Common-Buffer System DMA](using-common-buffer-system-dma.md).

In addition, any driver that uses packet-based DMA can use support routines intended to streamline scatter/gather DMA, regardless of whether its device has built-in scatter/gather support. See [Using Scatter/Gather DMA](using-scatter-gather-dma.md) for details.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Using%20System%20DMA%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


