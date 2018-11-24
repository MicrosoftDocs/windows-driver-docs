---
title: Patching a DMA Buffer
description: Patching a DMA Buffer
ms.assetid: 4d8a8a89-0617-4ab8-8609-37bbdb8999f0
keywords:
- DMA buffers WDK display , patching
- patching DMA buffers WDK display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Patching a DMA Buffer


## <span id="ddk_patching_a_dma_buffer_gg"></span><span id="DDK_PATCHING_A_DMA_BUFFER_GG"></span>


After the video memory manager is informed where every memory resource for the DMA buffer is located, the GPU scheduler calls the display miniport driver's [**DxgkDdiPatch**](https://msdn.microsoft.com/library/windows/hardware/ff559737) function to patch the resource with a physical address (that is, assign a physical address to the resource).

 

 





