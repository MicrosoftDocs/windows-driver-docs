---
title: Maintaining Cache Coherency
author: windows-driver-content
description: Maintaining Cache Coherency
ms.assetid: 70b4b313-ce33-4562-aa0d-127a91706409
keywords: ["I/O WDK kernel , cache coherency", "cache coherency WDK kernel", "integrity WDK I/O", "data transfers WDK kernel , cache coherency", "transferring data WDK kernel , cache coherency", "memory management WDK kernel , cache coherency", "processor cache WDK I/O"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Maintaining Cache Coherency


When a driver is transferring data between system memory and its device, data can be cached in one or more processor caches and/or in the system DMA controller's cache. Drivers that use DMA or PIO to service read/write IRPs or any device I/O control request that requires a DMA or PIO data transfer operation should ensure the integrity of possibly cached data during transfer operations. This section explains how to do so.

This section contains the following topics:

[Flushing Cached Data during DMA Operations](flushing-cached-data-during-dma-operations.md)

[Flushing Cached Data during PIO Operations](flushing-cached-data-during-pio-operations.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Maintaining%20Cache%20Coherency%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


