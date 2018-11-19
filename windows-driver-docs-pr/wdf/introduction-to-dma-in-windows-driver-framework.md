---
title: Introduction to DMA in Windows Driver Framework
description: Introduction to DMA in Windows Driver Framework
ms.assetid: 9bcd8ac1-f3dd-4bb3-a671-51c9465f8efa
keywords:
- DMA operations WDK KMDF , about DMA operations
- bus-master DMA WDK KMDF , about DMA operations
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Introduction to DMA in Windows Driver Framework


\[Applies to KMDF only\]




On Windows 7 and earlier, Kernel-Mode Driver Framework (KMDF) supports only bus-master direct memory access (DMA) devices. Such devices contain their own DMA controllers.

On System on a Chip (SoC)–based platforms running Windows 8 and later, the framework also supports system-mode DMA, in which multiple devices share a single multichannel DMA controller.

The framework's DMA support consists of:

-   A set of framework DMA objects and methods that drivers use to convert I/O requests into DMA operations.

-   A set of driver-supplied event callback functions that configure the device's DMA behavior as different events occur.

The framework supports both single packet and scatter/gather DMA transfers. It also supports the use of common buffers.

On SoC-based platforms running Windows 8 and later, the framework supports single-packet system-mode DMA transfers. For more information, see [Supporting System-Mode DMA](supporting-system-mode-dma.md).

The framework does not support system-mode DMA transfers on PC-based platforms.

 

 





