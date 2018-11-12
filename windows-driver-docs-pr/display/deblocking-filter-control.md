---
title: Deblocking Filter Control
description: Deblocking Filter Control
ms.assetid: b332421e-da15-4c42-aedb-32f4ba24101e
keywords:
- macroblocks WDK DirectX VA , deblocking filter control
- deblocking filter control WDK DirectX VA
- chrominance prediction blocks WDK DirectX VA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Deblocking Filter Control


## <span id="ddk_deblocking_filter_control_gg"></span><span id="DDK_DEBLOCKING_FILTER_CONTROL_GG"></span>


Deblocking filter control commands, if present, are sent once for each luminance block in a macroblock and are sent once for each pair of chrominance blocks. The filter control commands are sent in raster-scan order within the macroblock. Filter control commands are sent for all blocks for luminance before any blocks for chrominance. Filter control commands are then sent for one chrominance 4:2:0 block, then for one chrominance 4:2:2 block (if 4:2:2 is in use), then for two chrominance 4:4:4 commands if needed (the same filtering is applied to both chrominance [*components*](https://msdn.microsoft.com/library/windows/hardware/ff556274#wdkgloss-component)).

The filtering for each block is done by specifying deblocking across the top edge of the block, followed by deblocking across the left edge of the block. Deblocking is specified for chrominance only once, and the same deblocking commands are used for both the Cb and Cr components. For example, deblocking of a 16x16 macroblock that contains 4:2:0 data using 8x8 blocks is done by sending four sets of two (top and left) edge-filtering commands for the luminance blocks, followed by one set of two edge-filtering commands for the two chrominance blocks.

 

 





