---
title: Preparing DMA Buffers
description: Preparing DMA Buffers
ms.assetid: 9231badb-7b42-46d1-95f6-34c0ec7ab3cb
keywords:
- DMA buffers WDK display , preparing
- GPU starvation WDK display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Preparing DMA Buffers


## <span id="ddk_preparing_dma_buffers_gg"></span><span id="DDK_PREPARING_DMA_BUFFERS_GG"></span>


The display miniport driver must prepare DMA buffers in a timely manner. While the GPU processes a DMA buffer, the display miniport driver is typically called upon to prepare the next DMA buffer for submission to the GPU. To prevent GPU starvation, the display miniport driver must spend less time preparing and submitting subsequent DMA buffers than the GPU takes to process the current DMA buffer.

 

 





