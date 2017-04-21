---
title: Memory Configurations
description: Memory Configurations
ms.assetid: e3341854-13ce-4028-ad75-49e8189ac0f7
keywords:
- stride WDK DirectDraw
- pitch WDK DirectDraw
- offsets WDK DirectDraw
- drawing memory WDK DirectDraw , heaps
- DirectDraw memory WDK Windows 2000 display , heaps
- memory WDK DirectDraw , heaps
- display memory WDK DirectDraw , heaps
- heaps WDK DirectDraw
- allocating memory heaps
- VIDEOMEMORY
- surfaces WDK DirectDraw , memory heap allocation
- drawing memory WDK DirectDraw , configuration options
- DirectDraw memory WDK Windows 2000 display , configuration options
- memory WDK DirectDraw , configuration options
- display memory WDK DirectDraw , configuration options
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Memory Configurations


## <span id="ddk_memory_configurations_gg"></span><span id="DDK_MEMORY_CONFIGURATIONS_GG"></span>


The following sections contain three different types of memory configurations: [linear](linear-memory-allocation.md), [rectangular](rectangular-memory-allocation.md), and [mixed](mixed-memory-allocation.md) display memory allocation. Each section includes sample code that can be modified to fit the physical characteristics of the card, and that can be added to the HAL to allocate display memory heaps.

Alignment requirements as described in the [Memory Heap Allocation](memory-heap-allocation.md) topic can apply to any of the three types of memory configuration. Linear memory is generally used more efficiently by the application than rectangular memory because the rows are stored sequentially. Any location can be accessed easily by moving forward or backward along this linear range.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Memory%20Configurations%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




