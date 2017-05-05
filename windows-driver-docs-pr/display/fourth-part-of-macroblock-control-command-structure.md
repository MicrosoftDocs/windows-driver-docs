---
title: Fourth Part of Macroblock Control Command Structure
description: Fourth Part of Macroblock Control Command Structure
ms.assetid: 26540693-09a2-4664-b0ac-4cc69e909e99
keywords:
- macroblocks WDK DirectX VA , generic command structure
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Fourth Part of Macroblock Control Command Structure


## <span id="ddk_fourth_part_of_macroblock_control_command_structure_gg"></span><span id="DDK_FOURTH_PART_OF_MACROBLOCK_CONTROL_COMMAND_STRUCTURE_GG"></span>


If the **bPicIntra** and the **bMV\_RPS** members of [**DXVA\_PictureParameters**](https://msdn.microsoft.com/library/windows/hardware/ff564012) are zero, the macroblock control command structure ends with the data described in [Third Part of Macroblock Control Command Structure](third-part-of-macroblock-control-command-structure.md). The macroblock control command structure ends with the third part of the structure padded with zero-valued data, if necessary, to align the next macroblock control command to a 16-byte boundary.

If the **bPicIntra** member of DXVA\_PictureParameters is zero and the **bMV\_RPS** member of DXVA\_PictureParameters is 1, the fourth part of the macroblock control command structure is an array of bytes called *bRefPicSelect*. The number of elements in that array is the same as the number of elements in the **MVector** array shown in the preceding table. Each element of the array specifies the index of the uncompressed surface associated with the corresponding motion vector found in the **MVector** array. Then, the macroblock control command structure ends and is padded with zero-valued data, if necessary, to align the next macroblock control command structure to a 16-byte boundary.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Fourth%20Part%20of%20Macroblock%20Control%20Command%20Structure%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




