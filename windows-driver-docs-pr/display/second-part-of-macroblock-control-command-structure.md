---
title: Second Part of Macroblock Control Command Structure
description: Second Part of Macroblock Control Command Structure
ms.assetid: 94ef61d1-cd7d-4e73-8be8-01f7d23bb91d
keywords:
- macroblocks WDK DirectX VA , generic command structure
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Second Part of Macroblock Control Command Structure


## <span id="ddk_second_part_of_macroblock_control_command_structure_gg"></span><span id="DDK_SECOND_PART_OF_MACROBLOCK_CONTROL_COMMAND_STRUCTURE_GG"></span>


The second part of a generic macroblock control command structure contains three variations, depending on the configuration of the picture decoding process:

1.  If *HostResidDiff* (bit 11 in the **wMBtype** member) is equal to 1, the next element of the macroblock control command is **wPC\_Overflow**. The **wPC\_Overflow** member, if used, specifies which blocks of the macroblock use overflow residual difference data. **wPC\_Overflow** is followed by a DWORD equal to zero.

2.  If *HostResidDiff* (bit 11 in the **wMBtype** member) is equal to zero and the **bChromaFormat** member of [**DXVA\_PictureParameters**](https://msdn.microsoft.com/library/windows/hardware/ff564012) is equal to 1, the next element of the macroblock control command is **bNumCoef,** a six-element array of bytes. The **bNumCoef** member indicates the number of coefficients in the residual difference data buffer for each block of the macroblock.

3.  If *HostResidDiff* (bit 11 in the **wMBtype** element) is equal to zero and the **bChromaFormat** member of DXVA\_PictureParameters is not equal to 1, the next element of the macroblock control command is **wTotalNumCoef**. This is followed by a DWORD equal to zero.

### <span id="wPC_Overflow"></span><span id="wpc_overflow"></span><span id="WPC_OVERFLOW"></span>wPC\_Overflow

The **wPC\_Overflow** structure member specifies which blocks of the macroblock use overflow residual difference data.

When using host-based residual difference decoding (when *HostResidDiff* is equal to 1) with the **bPicOverflowBlocks** member of [**DXVA\_PictureParameters**](https://msdn.microsoft.com/library/windows/hardware/ff564012) equal to 1 and *IntraMacroblock* equal to zero (the 8-8 overflow method), **wPC\_Overflow** contains the pattern code of the overflow blocks specified in the same manner as **wPatternCode**. The data for the coded overflow blocks (those blocks having bit 11 minus *i* equal to 1) is found in the residual coding buffer in the same indexing order (increasing *i*).

### <span id="bNumCoef"></span><span id="bnumcoef"></span><span id="BNUMCOEF"></span>bNumCoef

The **bNumCoef** structure member is an array of six elements. The *i*th element of the **bNumCoef** array contains the number of coefficients in the residual difference data buffer for each block *i* of the macroblock, where *i* is the index of the block within the macroblock as specified in MPEG-2 video Figures 6-10, 6-11, and 6-12 (raster-scan order for Y, followed by Cb, followed by Cr). **bNumCoef** is used only when *HostResidDiff* is zero and the **bChromaFormat** member of [**DXVA\_PictureParameters**](https://msdn.microsoft.com/library/windows/hardware/ff564012) is 1 (4:2:0). If used in 4:2:2 or 4:4:4 formats, it will increase the size of typical macroblock control commands past a critical memory alignment boundary, so only an EOB within the transform coefficient structure is used for determining the number of coefficients in each block in non-4:2:0 cases. The purpose of **bNumCoef** is to indicate the quantity of data present for each block in the residual difference data buffer, expressed as the number of coefficients present. When the **bConfig4GroupedCoefs** member of [**DXVA\_ConfigPictureDecode**](https://msdn.microsoft.com/library/windows/hardware/ff563133) is 1, **bNumCoef** may contain either the actual number of coefficients sent for the block or that value rounded up to be a multiple of four. The data for these coefficients is found in the residual difference buffer in the same order.

### <span id="wTotalNumCoef"></span><span id="wtotalnumcoef"></span><span id="WTOTALNUMCOEF"></span>wTotalNumCoef

The **wTotalNumCoef** structure member indicates the total number of coefficients in the residual difference data buffer for the entire macroblock. This member is used only when *HostResidDiff* is zero and the **bChromaFormat** member of [**DXVA\_PictureParameters**](https://msdn.microsoft.com/library/windows/hardware/ff564012) is not equal to 1 (4:2:0).

 

 





