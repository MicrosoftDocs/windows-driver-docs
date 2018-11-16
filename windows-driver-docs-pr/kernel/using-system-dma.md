---
title: Using System DMA
description: Using System DMA
ms.assetid: 8d478365-a6c8-4488-9f75-53a822d1daa2
keywords: ["AdapterControl routines, system DMA", "system DMA WDK kernel", "adapter objects WDK kernel , system DMA", "DMA transfers WDK kernel , system DMA", "slave devices WDK DMA", "system DMA WDK kernel , about system DMA"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Using System DMA





Drivers of subordinate DMA devices use one of the following types of system-provided DMA support:

-   Packet-based DMA, if the driver need not use a system DMA controller's auto-initialize mode. See [Using Packet-Based System DMA](using-packet-based-system-dma.md).

-   Common-buffer DMA, if the driver does use the auto-initialize mode. See [Using Common-Buffer System DMA](using-common-buffer-system-dma.md).

In addition, any driver that uses packet-based DMA can use support routines intended to streamline scatter/gather DMA, regardless of whether its device has built-in scatter/gather support. See [Using Scatter/Gather DMA](using-scatter-gather-dma.md) for details.

 

 




