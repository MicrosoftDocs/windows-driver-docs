---
title: Supporting Kernel-Mode Command Buffers
description: Supporting Kernel-Mode Command Buffers
keywords:
- command buffer WDK display
ms.date: 04/20/2017
---

# Supporting Kernel-Mode Command Buffers


## <span id="ddk_introduction_to_command_and_dma_buffers_gg"></span><span id="DDK_INTRODUCTION_TO_COMMAND_AND_DMA_BUFFERS_GG"></span>


The display miniport driver should submit a command buffer in response to a call to the [**DxgkDdiRenderKm**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_renderkm) function as described in [Submitting a Command Buffer](submitting-a-command-buffer.md).

The driver can use the **MultipassOffset** member of the [**DXGKARG\_RENDER**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgkarg_render) structure to track the progress of input command buffer processing. For example, the display miniport driver can use the high 16 bits as an offset to the last processed command, and the low 16 bits to track the processing of the command.

 

