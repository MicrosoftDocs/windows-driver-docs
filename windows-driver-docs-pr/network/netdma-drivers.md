---
title: NetDMA
description: NetDMA
ms.assetid: 44a76f35-6e7a-4241-b078-ba271cde95c2
keywords:
- network drivers WDK , NetDMA drivers
- Direct Memory Access WDK networking
- memory-to-memory data transfers WDK NetDMA
- data transfers WDK NetDMA
- transferring data WDK NetDMA
- DMA transfers WDK NetDMA
- NetDMA WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# NetDMA


**Note**  The NetDMA interface is not supported in Windows 8 and later.

 




The NetDMA interface provides a generic interface for memory-to-memory direct memory access (DMA) transfers. Although the interface is designed to copy packets that are received from high-performance network interface cards (NICs), you can also use the interface for other applications. There is no direct relationship between NetDMA and NDIS.

**Note**  The Itanium-based versions of the Windows operating systems do not support NetDMA.

 

The Windows Vista operating system was originally released with NetDMA version 1.0 support. Windows Server 2008 includes NetDMA version 2.0.

This section includes:

[Introduction to the NetDMA Interface](introduction-to-the-netdma-interface.md)

[Writing a NetDMA Provider Driver](writing-a-netdma-provider-driver.md)

[Installing a NetDMA Provider Driver](installing-a-netdma-provider-driver.md)

[NetDMA 2.0 Extensions](netdma-2-0-extensions.md)

 

 





