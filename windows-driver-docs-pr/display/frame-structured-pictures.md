---
title: Frame-Structured Pictures
description: Frame-Structured Pictures
ms.assetid: 6449492e-06b5-4b8b-9e0d-a2e80272f062
keywords: ["MPEG-2 WDK DirectX VA", "frame motion compensation WDK DirectX VA", "field (16x8) motion compensation WDK DirectX VA", "dual-prime motion compensation WDK DirectX VA", "16x8 motion compensation WDK DirectX VA", "prediction blocks WDK DirectX VA"]
---

# Frame-Structured Pictures


## <span id="ddk_frame_structured_pictures_gg"></span><span id="DDK_FRAME_STRUCTURED_PICTURES_GG"></span>


**Frame MC**: Frame motion compensation has a 16x16 prediction block shape, similar to MPEG-1 predictions. This is the only progressive-style motion compensation within MPEG-2 (as specified by the *motion\_type* variable in MPEG-2). There is either one [*prediction plane*](https://msdn.microsoft.com/library/windows/hardware/ff556325#wdkgloss-prediction-plane) (forward-only or backward-only) or two (bidirectional) as determined by the *macroblock\_type* MPEG-2 variable. Reference blocks are formed from contiguous frame lines from the frame buffer. The frame buffer is selected by the semantics of the decoding process. Half-sample interpolation (MPEG-2 Section 7.6.4) and bidirectional interpolation (MPEG-2 Section 7.6.7.1) have identical averaging operations as in the MPEG-1 case.

**Field (16x8) MC**: Field (16x8) motion compensation has each prediction plane (forward and backward directions) consisting of a top 16x8 prediction block, and a bottom 16x8 prediction block. The reference block corresponding to each prediction block may be extracted from the top field or bottom field of a reference frame, as determined by the MPEG-2 variable *motion\_vertical\_field\_select*\[*r*\]\[*s*\]. There are two possibilities for field (16x8) motion compensation:

-   One set of two prediction blocks for one prediction plane (forward or backward only prediction with two prediction blocks per macroblock).

-   Two sets of two prediction blocks for two prediction planes (bidirectional prediction with four prediction blocks in a macroblock).

**Dual-Prime MC**: Like field (16x8) motion compensation, dual-prime motion compensation has each plane (parity) consisting of a top and bottom 16x8 shape. The same and opposite parity planes are combined together in the averaging operation. This averaging operation is identical to the bidirectional interpolation that is used for other motion types in MPEG-2. Unlike the other motion compensation types, a dual-prime macroblock always consists of two sets of prediction blocks (of the same and opposite parity) for a total of four prediction blocks per macroblock.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Frame-Structured%20Pictures%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




