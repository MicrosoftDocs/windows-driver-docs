---
title: Deblocking Filter Commands
description: Deblocking Filter Commands
ms.assetid: 9f20c6fa-c515-43b8-a947-f6290d15bd35
keywords:
- macroblocks WDK DirectX VA , deblocking filter commands
- deblocking filter commands WDK DirectX VA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Deblocking Filter Commands


## <span id="ddk_deblocking_filter_commands_gg"></span><span id="DDK_DEBLOCKING_FILTER_COMMANDS_GG"></span>


A deblocking filter command for a macroblock may require the accelerator to read the value of reconstructed samples within, and next to, the current macroblock. The reconstructed values read are the two rows of samples above the current macroblock, the two columns of samples to the left of the current macroblock, and samples within the current macroblock. A deblocking filter command can result in modification of one row of samples above the current macroblock and one column of samples left of the current macroblock, as well as up to three rows and three columns of samples within the current macroblock. The deblocking filtering process for a given macroblock could, therefore, require the prior reconstruction of two other macroblocks.

The two different types of deblocking filter command buffers are:

-   A buffer that requires access and modification of the value of reconstructed samples for macroblocks outside those of the current deblocking filter command buffer (when the **bPicDeblockConfined** member of the [**DXVA\_PictureParameters**](https://msdn.microsoft.com/library/windows/hardware/ff564012) structure is zero).

-   A buffer that does not require access and modification of the value of reconstructed samples for macroblocks outside those of the current deblocking filter command buffer (when **bPicDeblockConfined** is 1).

To process the first type of deblocking command buffer, the accelerator must ensure that the macroblock reconstruction has been completed for all buffers that affect macroblocks to the left or above the macroblocks controlled in the current buffer. This must be done before processing the deblocking commands in the current buffer.

To process the second type of deblocking command buffer, the accelerator uses only prior reconstruction values within the current buffer.

The deblocking filter operations can be performed in the accelerator in one of two ways:

-   Processing the motion prediction and residual difference data for the entire buffer or frame first, followed by reading back in the values of some of the samples and modifying them as a result of the deblocking filter operations.

-   Processing the deblocking command buffer in a coordinated way with the residual difference data buffer. In this case, the deblocking command buffers are processed before writing the reconstructed output values to the destination picture surface.

**Note**   The destination picture surface for the deblocked picture could differ from that of the picture reconstructed prior to deblocking. This would then support "outside the loop" deblocking as a postdecoding process that did not affect the sample values used for prediction of the next picture.

 

 

 





