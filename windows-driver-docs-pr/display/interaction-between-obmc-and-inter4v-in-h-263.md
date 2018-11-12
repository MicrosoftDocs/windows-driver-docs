---
title: Interaction Between OBMC and INTER4V in H.263
description: Interaction Between OBMC and INTER4V in H.263
ms.assetid: 096c723d-ec16-49f7-acaa-62ed228338c3
keywords:
- macroblocks WDK DirectX VA , generic command structure
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Interaction Between OBMC and INTER4V in H.263


## <span id="ddk_interaction_between_obmc_and_inter4v_in_h_263_gg"></span><span id="DDK_INTERACTION_BETWEEN_OBMC_AND_INTER4V_IN_H_263_GG"></span>


Some details about the interactions between H.263's [*OBMC*](https://msdn.microsoft.com/library/windows/hardware/ff556318#wdkgloss-obmc), *INTER4V*, *B*, *EP*, and B in PB frames may be helpful:

-   No current configuration of the H.263 standard will exercise the case in which **bPicOBMC** is equal to 1, *Motion4MV* is equal to 1, and *MotionBackward* is equal to 1.

-   OBMC cannot be used in a H.263 B or EP picture.

-   OBMC cannot be used in the B part of a H.263 PB picture.

-   INTER4V cannot be used in a H.263 B or EP picture.

-   If INTER4V is used in the macroblock of a H.263 P picture and this macroblock is later used as the reference macroblock for "direct" prediction in a H.263 B picture, OBMC is not used in the direct prediction. This is because four motion vectors are used according to H.263 Annex M, which uses them like H.263 Annex G, which does not apply the OBMC. H.263 never requires both OBMC and backward prediction at the same time, and never uses INTER4V in a backward direction.

### <span id="dwMB_SNL"></span><span id="dwmb_snl"></span><span id="DWMB_SNL"></span>dwMB\_SNL

The **dwMB\_SNL** structure member specifies the number of skipped macroblocks to be generated following the current macroblock, and indicates the location of the residual difference data for the blocks of the current macroblock. This member contains two variables: *MBskipsFollowing* in the most significant 8 bits and *MBdataLocation* in the least significant 24 bits. *MBskipsFollowing* indicates the number of skipped macroblocks to be generated following the current macroblock. *MBdataLocation* is an index into the residual difference block data buffer. This index indicates the location of the residual difference data for the blocks of the current macroblock, expressed as a multiple of 32 bits.

Each skipped macroblock indicated by *MBskipsFollowing* must be generated in a manner mathematically equivalent to incrementing the value of **wMBaddress** and then repeating the same macroblock control command.

Any macroblock control command with a nonzero value for *MBskipsFollowing* specifies how motion-compensated prediction is performed for each macroblock to be skipped, and is equivalent (except for the value of *MBskipsFollowing*) to an explicit nonskip specification of the generation of the first of the series of skipped macroblocks. Thus, whenever *MBskipsFollowing* is not zero, the following structure members and variables must all be equal to zero: *Motion4MV IntraMacroblock* **wPatternCode** *and* **wPCOverflow**.

The *MBdataLocation* variable must be zero for the first macroblock in the macroblock control command buffer. *MBdataLocation* may contain any value if **wPatternCode** is zero. When **wPatternCode** is zero, decoders are recommended but not required to set this value either to zero or to the same value as in the next macroblock control command.

For more information about generating skipped macroblocks, see [Generating Skipped Macroblocks](generating-skipped-macroblocks.md).

### <span id="wPatternCode"></span><span id="wpatterncode"></span><span id="WPATTERNCODE"></span>wPatternCode

The **wPatternCode** structure member indicates whether residual difference data is sent for each block in the macroblock.

Bit (11- *i*) of **wPatternCode** (where bit zero is the least significant bit) indicates whether residual difference data is sent for block *i*, where *i* is the index of the block within the macroblock as specified in MPEG-2 video figures 6-10, 6-11, and 6-12 (raster-scan order for Y, followed by 4:2:0 blocks of Cb in raster-scan order, followed by 4:2:0 blocks of Cr, followed by 4:2:2 blocks of Cb, followed by 4:2:2 blocks of Cr, followed by 4:4:4 blocks of Cb, followed by 4:4:4 blocks of Cr). The data for the coded blocks (those blocks having bit 11-*i* equal to 1) is found in the residual coding buffer in the same indexing order (increasing *i*). For 4:2:0 MPEG-2 data, the value of **wPatternCode** corresponds to shifting the decoded value of CBP (Coded Block Pattern) to the left by six bit positions (those lower bit positions being used for 4:2:2 and 4:4:4 chroma formats).

If the **bConfigSpatialResidInterleaved** member of [**DXVA\_ConfigPictureDecode**](https://msdn.microsoft.com/library/windows/hardware/ff563133) is 1, host-based residual differences are sent in a chroma-interleaved form matching that of the YUV pixel format in use. In this case, each Cb and spatially corresponding Cr pair of blocks is treated as a single residual difference structure unit. This does not alter the value or meaning of **wPatternCode**, but it implies that both members of each pair of Cb and Cr data blocks are sent whenever either of these data blocks has the corresponding bit (bit 7 or bit 6) set in **wPatternCode**. If the bit in **wPatternCode** for a particular data block is zero, the corresponding residual difference data values must be sent as zero whenever the pairing of the Cb and Cr blocks necessitates sending a residual difference data block for a block with a **wPatternCode** bit equal to zero.

 

 





