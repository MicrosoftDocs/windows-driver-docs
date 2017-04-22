---
title: Deblocking Filter Control
description: Deblocking Filter Control
ms.assetid: b332421e-da15-4c42-aedb-32f4ba24101e
keywords:
- macroblocks WDK DirectX VA , deblocking filter control
- deblocking filter control WDK DirectX VA
- chrominance prediction blocks WDK DirectX VA
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Deblocking Filter Control


## <span id="ddk_deblocking_filter_control_gg"></span><span id="DDK_DEBLOCKING_FILTER_CONTROL_GG"></span>


Deblocking filter control commands, if present, are sent once for each luminance block in a macroblock and are sent once for each pair of chrominance blocks. The filter control commands are sent in raster-scan order within the macroblock. Filter control commands are sent for all blocks for luminance before any blocks for chrominance. Filter control commands are then sent for one chrominance 4:2:0 block, then for one chrominance 4:2:2 block (if 4:2:2 is in use), then for two chrominance 4:4:4 commands if needed (the same filtering is applied to both chrominance [*components*](https://msdn.microsoft.com/library/windows/hardware/ff556274#wdkgloss-component)).

The filtering for each block is done by specifying deblocking across the top edge of the block, followed by deblocking across the left edge of the block. Deblocking is specified for chrominance only once, and the same deblocking commands are used for both the Cb and Cr components. For example, deblocking of a 16x16 macroblock that contains 4:2:0 data using 8x8 blocks is done by sending four sets of two (top and left) edge-filtering commands for the luminance blocks, followed by one set of two edge-filtering commands for the two chrominance blocks.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Deblocking%20Filter%20Control%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




