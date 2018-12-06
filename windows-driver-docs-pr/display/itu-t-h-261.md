---
title: ITU-T H.261
description: ITU-T H.261
ms.assetid: 00fb9001-2896-4ecd-b6ee-5b36bc6e72cd
keywords:
- ITU-T H.261 WDK DirectX VA
- H.261 WDK DirectX VA
- prediction blocks WDK DirectX VA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# ITU-T H.261


## <span id="ddk_itu_t_h_261_gg"></span><span id="DDK_ITU_T_H_261_GG"></span>


This standard is titled "Video Codec for Audiovisual Services at px64 kbit/s," ITU-T Recommendation H.261. This recommendation contains the same basic design later used in other video codec standards. H.261 uses 8-bit samples with Y, Cb, and Cr components, 4:2:0 sampling, 16x16 macroblock-based motion compensation, 8x8 IDCT, zigzag inverse scanning of coefficients, scalar quantization, and variable-length coding of coefficients based on a combination of zero-valued run-lengths and quantization index values.

All H.261 prediction blocks use forward-only prediction from the previous picture. H.261 does not have half-sample accurate prediction filters, but instead uses a type of low-pass filter called the loop filter (Section 3.2.3 of the H.261 specification) that can be turned off or on during motion compensation prediction for each macroblock.

**Annex D Graphics**

Recommendation H.261 Annex D Graphic Transfer mode can be supported by reading four decoded pictures from the accelerator back onto the host and interleaving them there for display as a higher-resolution graphic picture.

 

 





