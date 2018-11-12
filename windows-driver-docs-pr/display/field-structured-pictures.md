---
title: Field-Structured Pictures
description: Field-Structured Pictures
ms.assetid: fa058a30-74a2-4e8b-aa65-98ac5aa43e57
keywords:
- MPEG-2 WDK DirectX VA
- field motion compensation WDK DirectX VA
- field (16x8) motion compensation WDK DirectX VA
- dual-prime motion compensation WDK DirectX VA
- 16x8 motion compensation WDK DirectX VA
- prediction blocks WDK DirectX VA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Field-Structured Pictures


## <span id="ddk_field_structured_pictures_gg"></span><span id="DDK_FIELD_STRUCTURED_PICTURES_GG"></span>


**Field (16x16) MC**: Field (16x16) motion compensation resembles frame motion compensation in that each prediction has a 16x16 shape. However, the reference block data is formed from sequential top field or bottom field lines only (not a mixture of alternating top field and bottom field lines as in progressive motion). As with all motion compensation in field-structured pictures, the reconstructed macroblock is stored in the current frame buffer as only sequential top field or bottom field lines. The top or bottom field destination is determined by the MPEG-2 *picture\_structure* variable.

**16x8 MC**: Although the basic prediction block shapes of this type of motion compensation are the same as for the other 16x8 shapes (field 16x8 MC and dual-prime MC), it does not partition the macroblock in the same manner. The two partitions correspond to the upper and lower halves of a macroblock prediction plane, rather than the top and bottom fields within a macroblock. For more information, see the "Two MPEG-2 Macroblock 16x8 Partitions" illustration in [Macroblock Partitioning](macroblock-partitioning.md). Note that the anchor point for the lower 16x8 half is the upper-left corner of the 16x8 lower portion, not the upper-left corner of the whole macroblock, as is the case with all other types of motion compensation.

**Dual-Prime MC**: At the lowest layer, there is virtually no distinction between dual-prime and the field-structured field motion compensation with bidirectional prediction. The differences are manifested in the frame-buffer selections from which reference blocks are formed. Dual-prime motion compensation in field-structured pictures always consists of two 16x16 prediction blocks (the same and opposite parity predictions).

 

 





