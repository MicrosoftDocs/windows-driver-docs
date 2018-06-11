---
title: Note to discourage NDIS DMA use on ARM/ARM64 processors
---
> [!CAUTION]
> For ARM and ARM64 processors, we strongly recommend that NDIS driver writers use WDF DMA or HAL DMA instead of NDIS Scatter/Gather DMA. 
>
> For more information about WDF DMA, see [Handling DMA Operations in KMDF Drivers](../wdf/handling-dma-operations-in-kmdf-drivers.md).