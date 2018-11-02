---
title: Supporting Kernel-Mode Command Buffers
description: Supporting Kernel-Mode Command Buffers
ms.assetid: c61a39b3-6fd6-461f-a68f-450ccd705f6f
keywords:
- command buffer WDK display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Supporting Kernel-Mode Command Buffers


## <span id="ddk_introduction_to_command_and_dma_buffers_gg"></span><span id="DDK_INTRODUCTION_TO_COMMAND_AND_DMA_BUFFERS_GG"></span>


The display miniport driver should submit a command buffer in response to a call to the [**DxgkDdiRenderKm**](https://msdn.microsoft.com/library/windows/hardware/ff559800) function as described in [Submitting a Command Buffer](submitting-a-command-buffer.md).

The driver can use the **MultipassOffset** member of the [**DXGKARG\_RENDER**](https://msdn.microsoft.com/library/windows/hardware/ff557648) structure to track the progress of input command buffer processing. For example, the display miniport driver can use the high 16 bits as an offset to the last processed command, and the low 16 bits to track the processing of the command.

 

 





