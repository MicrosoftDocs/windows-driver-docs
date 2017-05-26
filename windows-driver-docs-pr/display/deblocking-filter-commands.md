---
title: Deblocking Filter Commands
description: Deblocking Filter Commands
ms.assetid: 9f20c6fa-c515-43b8-a947-f6290d15bd35
keywords:
- macroblocks WDK DirectX VA , deblocking filter commands
- deblocking filter commands WDK DirectX VA
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Deblocking%20Filter%20Commands%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




