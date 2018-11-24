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
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Memory Configurations


## <span id="ddk_memory_configurations_gg"></span><span id="DDK_MEMORY_CONFIGURATIONS_GG"></span>


The following sections contain three different types of memory configurations: [linear](linear-memory-allocation.md), [rectangular](rectangular-memory-allocation.md), and [mixed](mixed-memory-allocation.md) display memory allocation. Each section includes sample code that can be modified to fit the physical characteristics of the card, and that can be added to the HAL to allocate display memory heaps.

Alignment requirements as described in the [Memory Heap Allocation](memory-heap-allocation.md) topic can apply to any of the three types of memory configuration. Linear memory is generally used more efficiently by the application than rectangular memory because the rows are stored sequentially. Any location can be accessed easily by moving forward or backward along this linear range.

 

 





