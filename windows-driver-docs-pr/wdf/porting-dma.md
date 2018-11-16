---
title: Porting DMA
description: Porting DMA
ms.assetid: 457B6459-EE02-4A2C-8D25-81CE1D9265DC
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Porting DMA


\[Applies to KMDF only\]

Performing DMA (Direct Memory Access) in a KMDF driver is simpler than in a WDM driver because the framework handles many of the details on behalf of the driver.

Basically, the framework-based driver creates a DMA enabler object, specifies the DMA capabilities of the device, and supplies a callback function that manipulates the hardware to perform the transfer.

The framework determines the number of map registers that are required for the transfer, allocates the map registers, builds a scatter/gather list (if the device supports scatter/gather DMA), and flushes the processor cache and the buffers whenever necessary.

For implementation details, see [Handling DMA Operations in KMDF Drivers](handling-dma-operations-in-kmdf-drivers.md).

 

 





