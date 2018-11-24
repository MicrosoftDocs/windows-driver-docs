---
title: Loading an AYUV Alpha-Blending Surface
description: Loading an AYUV Alpha-Blending Surface
ms.assetid: 93b60622-47af-485c-a1db-9a05783ff698
keywords:
- alpha-blend data loading WDK DirectX VA
- blended pictures WDK DirectX VA , alpha-blend data loading
- AYUV alpha-blending surface WDK DirectX VA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Loading an AYUV Alpha-Blending Surface


## <span id="ddk_loading_an_ayuv_alpha_blending_surface_gg"></span><span id="DDK_LOADING_AN_AYUV_ALPHA_BLENDING_SURFACE_GG"></span>


An AYUV alpha-blending surface is defined as an array of samples of 32 bits each in the [**DXVA\_AYUVsample2**](https://msdn.microsoft.com/library/windows/hardware/ff563116) structure. This surface can be used as the source for blending a graphic with decoded video pictures.

The width and height of the AYUV alpha-blending surface are specified in the associated [buffer description list](buffer-description-list.md).

### <span id="Loading_a_16-Entry_YUV_Palette"></span><span id="loading_a_16-entry_yuv_palette"></span><span id="LOADING_A_16-ENTRY_YUV_PALETTE"></span>Loading a 16-Entry YUV Palette

A 16-entry YUV palette is defined as an array of 16 [**DXVA\_AYUVsample2**](https://msdn.microsoft.com/library/windows/hardware/ff563116) structures. This palette is used along with an IA44 or AI44 alpha-blending surface. The palette array is sent to the accelerator in an AYUV alpha-blending sample buffer (buffer type 8). In this case, the **bSampleAlpha8** member of the DXVA\_AYUVsample2 structure for each sample has no meaning and must be zero.

The YUV palette can be used to create the source for blending a graphic with decoded video pictures. This palette can be used to create the graphic source along with either

-   An IA44/AI44 alpha-blending surface, *or*

-   A DPXD alpha-blending surface, a highlight buffer, and DCCMD data

### <span id="Loading_an_AYUV_Surface"></span><span id="loading_an_ayuv_surface"></span><span id="LOADING_AN_AYUV_SURFACE"></span>Loading an AYUV Surface

Rather than loading just a 16-entry palette, an entire image graphic can simply be loaded directly as an AYUV image to specify the graphic content. In this case, the AYUV graphic is sent to the accelerator in an AYUV alpha-blending sample buffer (buffer type 8) as specified in the [**DXVA\_BufferDescription**](https://msdn.microsoft.com/library/windows/hardware/ff563122) structure.

### <span id="Loading_an_IA44_AI44_Alpha-Blending_Surface"></span><span id="loading_an_ia44_ai44_alpha-blending_surface"></span><span id="LOADING_AN_IA44_AI44_ALPHA-BLENDING_SURFACE"></span>Loading an IA44/AI44 Alpha-Blending Surface

An index-alpha 4-4 (IA44) alpha-blending surface is defined as an array of 8-bit samples, each of which is structured as a byte. This byte is referred to as *DXVA\_IA44sample* and is defined in *dxva.h*. The 4 most significant bits of this byte contain an index referred to as *SampleIndex4*, and the 4 least significant bits of this byte contain an alpha value referred to as *SampleAlpha4*.

An alpha-index 4-4 (AI44) alpha-blending surface is defined as an array of 8-bit samples, each of which is structured as a byte. This byte is referred to as *DXVA\_AI44sample* and is defined in *dxva.h*. The 4 most significant bits of this byte contain an alpha value referred to as *SampleAlpha4* and the 4 least significant bits of this byte contain an index referred to as *SampleIndex4*.

The *SampleIndex4* field for both *DXVA\_IA44sample* and *DXVA\_AI44sample* contains the index into the 16-entry palette for the sample.

The *SampleAlpha4* field for both *DXVA\_IA44sample* and *DXVA\_AI44sample* contains the following values to specify the opacity of the sample:

-   Zero indicates that the sample is transparent (so that the palette entry for *SampleIndex4* has no effect on the resulting blended picture). For a zero value of *SampleAlpha4*, the blend specified is to use the picture value without alteration.

-   A value of 15 indicates that the sample is opaque (so that the palette entry for *SampleIndex4* completely determines the resulting blended picture).

-   Nonzero values indicate that the blend specified is found by the following expression:

((*SampleAlpha4*+1) X graphic\_value + (15-*SampleAlpha4*) X picture\_value + 8) &gt;&gt; 4

The width and height of the IA44 alpha-blending surface are specified in the associated [buffer description list](buffer-description-list.md).

 

 





