---
title: Adapter Objects and DMA
author: windows-driver-content
description: Adapter Objects and DMA
ms.assetid: 8bc672b4-0f4d-4e0c-9904-c8d0a3f3639c
keywords: ["adapter objects WDK kernel", "I/O WDK kernel , adapter objects", "I/O WDK kernel , DMA", "DMA transfers WDK kernel", "AdapterControl routines", "Direct Memory Access WDK kernel", "data transfers WDK kernel , adapter objects", "transferring data WDK kernel , ad"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Adapter Objects and DMA


## <a href="" id="ddk-adapter-objects-and-dma-kg"></a>


This section describes adapter objects and [*AdapterControl*](https://msdn.microsoft.com/library/windows/hardware/ff540504) routines, and how they are used to control DMA operations. The section contains the following topics:

[Introduction to Adapter Objects](introduction-to-adapter-objects.md)

[Getting an Adapter Object](getting-an-adapter-object.md)

[Using System DMA](using-system-dma.md)

[Using Bus-Master DMA](using-bus-master-dma.md)

[Using Scatter/Gather DMA](using-scatter-gather-dma.md)

[Writing AdapterControl Routines](writing-adaptercontrol-routines.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Adapter%20Objects%20and%20DMA%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


