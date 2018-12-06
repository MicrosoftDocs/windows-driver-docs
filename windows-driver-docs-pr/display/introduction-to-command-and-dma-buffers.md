---
title: Introduction to Command and DMA Buffers
description: Introduction to Command and DMA Buffers
ms.assetid: e9fa38a2-3243-4578-83c3-4559ec3480a7
keywords:
- command buffers WDK display , about command buffers
- DMA buffers WDK display , about DMA buffers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Introduction to Command and DMA Buffers


## <span id="ddk_introduction_to_command_and_dma_buffers_gg"></span><span id="DDK_INTRODUCTION_TO_COMMAND_AND_DMA_BUFFERS_GG"></span>


Command and DMA buffers closely resemble each other. However, a command buffer is used by the user-mode display driver, and a DMA buffer is used by the display miniport driver.

A command buffer has the following characteristics:

-   It is never directly accessed by the GPU.

-   The hardware vendor controls the format.

-   It is allocated for the user-mode display driver from regular pageable memory in the private address space of the rendering application.

A DMA buffer has the following characteristics:

-   It is based on the validated content of a command buffer.

-   It is allocated by the display miniport driver from kernel pageable memory.

-   Before the GPU can read from a DMA buffer, the display miniport driver must page-lock the DMA buffer and map the DMA buffer through an aperture.

 

 





