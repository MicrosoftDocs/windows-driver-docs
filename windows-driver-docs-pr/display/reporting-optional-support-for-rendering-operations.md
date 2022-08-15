---
title: Reporting Optional Support for Rendering Operations
description: Reporting Optional Support for Rendering Operations
ms.date: 04/20/2017
---

# Reporting Optional Support for Rendering Operations


## <span id="ddk_introduction_to_command_and_dma_buffers_gg"></span><span id="DDK_INTRODUCTION_TO_COMMAND_AND_DMA_BUFFERS_GG"></span>


Beginning with Windows 7, a display miniport driver can set additional members in the [**DXGK\_PRESENTATIONCAPS**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_presentationcaps) structure to indicate certain rendering operations that the driver can or cannot support.

For further information about available rendering capability settings, see [**DXGK\_PRESENTATIONCAPS**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_presentationcaps).

 

