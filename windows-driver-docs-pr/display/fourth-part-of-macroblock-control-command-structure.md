---
title: Fourth Part of Macroblock Control Command Structure
description: Fourth Part of Macroblock Control Command Structure
ms.assetid: 26540693-09a2-4664-b0ac-4cc69e909e99
keywords:
- macroblocks WDK DirectX VA , generic command structure
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Fourth Part of Macroblock Control Command Structure


## <span id="ddk_fourth_part_of_macroblock_control_command_structure_gg"></span><span id="DDK_FOURTH_PART_OF_MACROBLOCK_CONTROL_COMMAND_STRUCTURE_GG"></span>


If the **bPicIntra** and the **bMV\_RPS** members of [**DXVA\_PictureParameters**](https://msdn.microsoft.com/library/windows/hardware/ff564012) are zero, the macroblock control command structure ends with the data described in [Third Part of Macroblock Control Command Structure](third-part-of-macroblock-control-command-structure.md). The macroblock control command structure ends with the third part of the structure padded with zero-valued data, if necessary, to align the next macroblock control command to a 16-byte boundary.

If the **bPicIntra** member of DXVA\_PictureParameters is zero and the **bMV\_RPS** member of DXVA\_PictureParameters is 1, the fourth part of the macroblock control command structure is an array of bytes called *bRefPicSelect*. The number of elements in that array is the same as the number of elements in the **MVector** array shown in the preceding table. Each element of the array specifies the index of the uncompressed surface associated with the corresponding motion vector found in the **MVector** array. Then, the macroblock control command structure ends and is padded with zero-valued data, if necessary, to align the next macroblock control command structure to a 16-byte boundary.

 

 





