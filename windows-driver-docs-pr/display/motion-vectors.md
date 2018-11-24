---
title: Motion Vectors
description: Motion Vectors
ms.assetid: 463a2434-7f3e-4960-a595-8ca2ccc21504
keywords:
- macroblocks WDK DirectX VA , motion vectors
- motion vectors WDK DirectX VA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Motion Vectors


## <span id="ddk_motion_vectors_gly"></span><span id="DDK_MOTION_VECTORS_GLY"></span>


If the picture is not an intra picture (the **bPicIntra** member of the [**DXVA\_PictureParameters**](https://msdn.microsoft.com/library/windows/hardware/ff564012) structure is zero), motion vectors are included in the macroblock control command structure. The number of motion vectors that are included in the structure depends upon the type of picture (for example, [*B picture*](https://msdn.microsoft.com/library/windows/hardware/ff556272#wdkgloss-b-picture) or [*P picture*](https://msdn.microsoft.com/library/windows/hardware/ff556325#wdkgloss-predictive-coded-picture--p-picture-)). Additionally, if macroblock-based reference-picture selection (as defined in H.263 Annex U) is in use, then a reference-picture selection index for each motion vector is also included in the macroblock control-command structure.

The space reserved for motion vectors in each macroblock control command structure is generally the amount needed for four motion vectors. Each motion vector is specified using a [**DXVA\_MVvalue**](https://msdn.microsoft.com/library/windows/hardware/ff564004) structure. These usual cases include the two preceding nonintra cases. The remaining cases (not explicitly defined in the *dxva.h* header file) are as follows:

-   If [*OBMC*](https://msdn.microsoft.com/library/windows/hardware/ff556318#wdkgloss-obmc) is in use (the **bPicOBMC** member of the [**DXVA\_PictureParameters**](https://msdn.microsoft.com/library/windows/hardware/ff564012) structure is 1) and the picture is not the B part of a PB picture (the **bPicBinPB** member of this structure is zero), space for 10 motion vectors, plus any additional space needed to align to a 16-byte boundary, is included.

-   If OBMC is in use (the **bPicOBMC** member of the DXVA\_PictureParameters structure is 1) and the picture is the B part of a PB picture (the **bPicBinPB** member of this structure is 1), space for 11 motion vectors, plus any additional space needed to align to a 16-byte boundary, is included.

-   If OBMC is not in use (the **bPicOBMC** member of the DXVA\_PictureParameters structure is zero), the picture is the B part of a PB picture (the **bPicBinPB** member of this structure is 1), and four motion vectors per macroblock are allowed (the **bPic4Mvallowed** member of this structure is 1), the space for five motion vectors, plus any additional space needed to align to a 16-byte boundary, is included.

 

 





