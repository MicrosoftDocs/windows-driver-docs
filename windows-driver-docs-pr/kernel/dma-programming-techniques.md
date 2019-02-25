---
title: DMA Programming Techniques
description: DMA Programming Techniques
ms.assetid: bdd8ffa4-8f09-41ed-b0f8-8edabbe65393
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DMA Programming Techniques


Direct Memory Access (DMA) is one of the most basic hardware techniques for transferring memory-based data between the central processor (CPU) and a particular device. Computer systems use a DMA controller which is an intermediate device that handles the memory transfer, allowing the CPU to do other things.

Drivers can use the DMA controller to transfer memory-based data directly. The following topics discuss DMA issues related to I/O programming.

Drivers can use adapter objects to control DMA. For more information about adapter objects, see [Adapter Objects and DMA](adapter-objects-and-dma.md).

When a driver is transferring data between system memory and its device, data can be cached in one or more processor caches and/or in the system DMA controller's cache. For more information about DMA and caches, see [Flushing Cached Data during DMA Operations](flushing-cached-data-during-dma-operations.md).

If you need to split up your DMA operations into smaller chunks, see [Splitting DMA Transfer Requests](splitting-dma-transfer-requests.md).

Version 3 of the DMA operations interface is available starting with Windows 8. For more information about this interface, see [Version 3 of the DMA Operations Interface](version-3-of-the-dma-operations-interface.md).

 

 




