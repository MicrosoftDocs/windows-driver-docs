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
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Field-Structured Pictures


## <span id="ddk_field_structured_pictures_gg"></span><span id="DDK_FIELD_STRUCTURED_PICTURES_GG"></span>


**Field (16x16) MC**: Field (16x16) motion compensation resembles frame motion compensation in that each prediction has a 16x16 shape. However, the reference block data is formed from sequential top field or bottom field lines only (not a mixture of alternating top field and bottom field lines as in progressive motion). As with all motion compensation in field-structured pictures, the reconstructed macroblock is stored in the current frame buffer as only sequential top field or bottom field lines. The top or bottom field destination is determined by the MPEG-2 *picture\_structure* variable.

**16x8 MC**: Although the basic prediction block shapes of this type of motion compensation are the same as for the other 16x8 shapes (field 16x8 MC and dual-prime MC), it does not partition the macroblock in the same manner. The two partitions correspond to the upper and lower halves of a macroblock prediction plane, rather than the top and bottom fields within a macroblock. For more information, see the "Two MPEG-2 Macroblock 16x8 Partitions" illustration in [Macroblock Partitioning](macroblock-partitioning.md). Note that the anchor point for the lower 16x8 half is the upper-left corner of the 16x8 lower portion, not the upper-left corner of the whole macroblock, as is the case with all other types of motion compensation.

**Dual-Prime MC**: At the lowest layer, there is virtually no distinction between dual-prime and the field-structured field motion compensation with bidirectional prediction. The differences are manifested in the frame-buffer selections from which reference blocks are formed. Dual-prime motion compensation in field-structured pictures always consists of two 16x16 prediction blocks (the same and opposite parity predictions).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Field-Structured%20Pictures%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




