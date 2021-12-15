---
description: "Note to discourage NDIS DMA use on ARM/ARM64 processors"
title: Note to discourage NDIS DMA use on ARM/ARM64 processors
ms.date: 10/17/2018
ms.topic: include
---

> [!CAUTION]
> For ARM and ARM64 processors, we strongly recommend that NDIS driver writers use WDF DMA or WDM DMA instead of NDIS Scatter/Gather DMA.
>
> For more information about WDF DMA, see [Handling DMA Operations in KMDF Drivers](../wdf/introduction-to-dma-in-windows-driver-framework.md).
>
> For more information about WDM DMA, see the DMA-related child topics of [Managing Input/Output for Drivers](../kernel/handling-irps.md).
