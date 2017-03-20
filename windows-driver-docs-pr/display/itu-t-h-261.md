---
title: ITU-T H.261
description: ITU-T H.261
ms.assetid: 00fb9001-2896-4ecd-b6ee-5b36bc6e72cd
keywords: ["ITU-T H.261 WDK DirectX VA", "H.261 WDK DirectX VA", "prediction blocks WDK DirectX VA"]
---

# ITU-T H.261


## <span id="ddk_itu_t_h_261_gg"></span><span id="DDK_ITU_T_H_261_GG"></span>


This standard is titled "Video Codec for Audiovisual Services at px64 kbit/s," ITU-T Recommendation H.261. This recommendation contains the same basic design later used in other video codec standards. H.261 uses 8-bit samples with Y, Cb, and Cr components, 4:2:0 sampling, 16x16 macroblock-based motion compensation, 8x8 IDCT, zigzag inverse scanning of coefficients, scalar quantization, and variable-length coding of coefficients based on a combination of zero-valued run-lengths and quantization index values.

All H.261 prediction blocks use forward-only prediction from the previous picture. H.261 does not have half-sample accurate prediction filters, but instead uses a type of low-pass filter called the loop filter (Section 3.2.3 of the H.261 specification) that can be turned off or on during motion compensation prediction for each macroblock.

**Annex D Graphics**

Recommendation H.261 Annex D Graphic Transfer mode can be supported by reading four decoded pictures from the accelerator back onto the host and interleaving them there for display as a higher-resolution graphic picture.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20ITU-T%20H.261%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




