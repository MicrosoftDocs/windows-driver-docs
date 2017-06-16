---
title: DMA Programming Techniques
author: windows-driver-content
description: DMA Programming Techniques
ms.assetid: bdd8ffa4-8f09-41ed-b0f8-8edabbe65393
---

# DMA Programming Techniques


Direct Memory Access (DMA) is one of the most basic hardware techniques for transferring memory-based data between the central processor (CPU) and a particular device. Computer systems use a DMA controller which is an intermediate device that handles the memory transfer, allowing the CPU to do other things.

Drivers can use the DMA controller to transfer memory-based data directly. The following topics discuss DMA issues related to I/O programming.

Drivers can use adapter objects to control DMA. For more information about adapter objects, see [Adapter Objects and DMA](adapter-objects-and-dma.md).

When a driver is transferring data between system memory and its device, data can be cached in one or more processor caches and/or in the system DMA controller's cache. For more information about DMA and caches, see [Flushing Cached Data during DMA Operations](flushing-cached-data-during-dma-operations.md).

If you need to split up your DMA operations into smaller chunks, see [Splitting DMA Transfer Requests](splitting-dma-transfer-requests.md).

Version 3 of the DMA operations interface is available starting with Windows 8. For more information about this interface, see [Version 3 of the DMA Operations Interface](version-3-of-the-dma-operations-interface.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20DMA%20Programming%20Techniques%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


