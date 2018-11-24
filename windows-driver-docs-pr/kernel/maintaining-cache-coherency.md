---
title: Maintaining Cache Coherency
description: Maintaining Cache Coherency
ms.assetid: 70b4b313-ce33-4562-aa0d-127a91706409
keywords: ["I/O WDK kernel , cache coherency", "cache coherency WDK kernel", "integrity WDK I/O", "data transfers WDK kernel , cache coherency", "transferring data WDK kernel , cache coherency", "memory management WDK kernel , cache coherency", "processor cache WDK I/O"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Maintaining Cache Coherency


When a driver is transferring data between system memory and its device, data can be cached in one or more processor caches and/or in the system DMA controller's cache. Drivers that use DMA or PIO to service read/write IRPs or any device I/O control request that requires a DMA or PIO data transfer operation should ensure the integrity of possibly cached data during transfer operations. This section explains how to do so.

This section contains the following topics:

[Flushing Cached Data during DMA Operations](flushing-cached-data-during-dma-operations.md)

[Flushing Cached Data during PIO Operations](flushing-cached-data-during-pio-operations.md)

 

 




