---
title: Supporting Operations on Video Substream and Destination Surfaces
description: Supporting Operations on Video Substream and Destination Surfaces
ms.assetid: ad0214b9-5d75-455f-8748-ff7c5a3d89db
keywords:
- DeinterlaceBltEx, destination surfaces
- DeinterlaceBltEx, substream surfaces
- destination surfaces WDK DirectX VA
- substream surfaces WDK DirectX VA
- color filling destination surfaces WDK DirectX VA
- color filling substream surfaces WDK DirectX VA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Supporting Operations on Video Substream and Destination Surfaces


## <span id="ddk_supporting_operations_on_video_substream_and_destination_surfaces_"></span><span id="DDK_SUPPORTING_OPERATIONS_ON_VIDEO_SUBSTREAM_AND_DESTINATION_SURFACES_"></span>


**This section applies only to Windows Server 2003 with SP1 and later, and Windows XP with SP2 and later.**

The VMR on Microsoft Windows Server 2003 SP1 and later and Windows XP SP2 and later must be able to perform certain operations on video substream and destination surfaces.

### <span id="Operations_on_Video_Substream_Surfaces"></span><span id="operations_on_video_substream_surfaces"></span><span id="OPERATIONS_ON_VIDEO_SUBSTREAM_SURFACES"></span>Operations on Video Substream Surfaces

In addition to the operations on video substream surfaces that your driver's [**DeinterlaceBltEx**](https://msdn.microsoft.com/library/windows/hardware/ff563927) and [**DeinterlaceBlt**](https://msdn.microsoft.com/library/windows/hardware/ff563924) functions perform, your driver must support the following operations:

<span id="Color_Filling_Substream_Surfaces"></span><span id="color_filling_substream_surfaces"></span><span id="COLOR_FILLING_SUBSTREAM_SURFACES"></span>**Color Filling Substream Surfaces**  
The VMR and other Microsoft DirectShow components must be able to fill video substream surfaces to a known initial color value, such as transparent black. Therefore, your driver should support calls to its [*DdBlt*](https://msdn.microsoft.com/library/windows/hardware/ff549205) callback function using the DDBLT\_COLORFILL flag where the video substream surface is the target for the bit-block transfer (blt).

For video substream surfaces with the AYUV [*FOURCC*](https://msdn.microsoft.com/library/windows/hardware/ff556280#wdkgloss-fourcc) format, the VMR specifies the AYUV color for transparent black in the **dwFillColor** member of the DDBLTFX structure. The driver receives DDBLTFX in the **bltFX** member of the DD\_BLTDATA structure when its *DdBlt* function is called. For information about the DDBLTFX structure, see the Windows SDK documentation.

The AYUV color for transparent black is set as follows:

```cpp
DXVA_AYUVsample2 clr; 
clr.bCrValue = 0x80;
clr.bCbValue = 0x80;
clr.bY_Value = 0x10;
clr.bSampleAlpha8 = 0x00;
DWORD dwFillColor = *(DWORD*)&clr;
```

For video substream surfaces with the AI44 or IA44 format, the low-order byte of the value in the **dwFillColor** member indicates the color value that the driver should use to fill the surface. Typically, the color value is 0.

<span id="Copying_Contents_to_Substream_Surfaces"></span><span id="copying_contents_to_substream_surfaces"></span><span id="COPYING_CONTENTS_TO_SUBSTREAM_SURFACES"></span>**Copying Contents to Substream Surfaces**  
The Line21 closed caption decoder and the teletext decoder create a source video substream surface that contains a series of cached-character glyphs. Your driver should generate each frame of output by copying the appropriate characters from the glyph cache to the video substream surface. The VMR then sends the video substream surface to your driver's [**DeinterlaceBltEx**](https://msdn.microsoft.com/library/windows/hardware/ff563927) function.

Therefore, your driver's [*DdBlt*](https://msdn.microsoft.com/library/windows/hardware/ff549205) function should support copying any FOURCC surface to a video substream surface of the same FOURCC format.

Your driver should indicate that it supports copying FOURCC formats by setting the DDCAPS2\_COPYFOURCC flag in the **dwCaps2** member of the [**DDCORECAPS**](https://msdn.microsoft.com/library/windows/hardware/ff549248) structure. The driver specifies the DDCORECAPS structure in the **ddCaps** member of a [**DD\_HALINFO**](https://msdn.microsoft.com/library/windows/hardware/ff551627) structure. DD\_HALINFO is returned by the driver's [**DrvGetDirectDrawInfo**](https://msdn.microsoft.com/library/windows/hardware/ff556229) function.

In a FOURCC video substream surface copy operation, the driver should not perform stretching or color-space conversion operations.

### <span id="Operations_on_Destination_Surfaces"></span><span id="operations_on_destination_surfaces"></span><span id="OPERATIONS_ON_DESTINATION_SURFACES"></span>Operations on Destination Surfaces

Your driver must support the following operations on the destination surface that is used in your driver's [**DeinterlaceBltEx**](https://msdn.microsoft.com/library/windows/hardware/ff563927) function:

<span id="Color_Filling_the_Destination_Surface"></span><span id="color_filling_the_destination_surface"></span><span id="COLOR_FILLING_THE_DESTINATION_SURFACE"></span>**Color Filling the Destination Surface**  
Because the VMR must initialize the destination surface to YUV opaque black, your driver must also support calls to its [*DdBlt*](https://msdn.microsoft.com/library/windows/hardware/ff549205) callback function using the DDBLT\_COLORFILL flag where the target for the bit-block transfer is the destination surface. The VMR specifies the color for opaque black in the **dwFillColor** member of the DDBLTFX structure. The driver receives the DDBLTFX structure in the **bltFX** member of the DD\_BLTDATA structure when its *DdBlt* is called.

For YUV packed surface types, the VMR sets the fill color DWORD to the appropriate byte pattern for opaque black. For a YUY2 surface, the fill color DWORD for opaque black is 0x80108010.

For planar surface types, the VMR sets the AYUV color for opaque black as follows:

```cpp
DXVA_AYUVsample2 clr; 
clr.bCrValue = 0x80;
clr.bCbValue = 0x80;
clr.bY_Value = 0x10;
clr.bSampleAlpha8 = 0xFF;
DWORD dwFillColor = *(DWORD*)&clr;
```

Your driver should ensure that the correct pixel values are written to each plane of the YUV surface.

<span id="Stretching_the_Destination_Surface"></span><span id="stretching_the_destination_surface"></span><span id="STRETCHING_THE_DESTINATION_SURFACE"></span>**Stretching the Destination Surface**  
Your driver must also support the destination surface being used as a source surface for a bit-block transfer that combines a stretching operation with a color-space conversion. For more information, see [Supporting Stretch Blit Operations](supporting-stretch-blit-operations.md).

<span id="Copying_Contents_from_the_Destination_Surface"></span><span id="copying_contents_from_the_destination_surface"></span><span id="COPYING_CONTENTS_FROM_THE_DESTINATION_SURFACE"></span>**Copying Contents from the Destination Surface**  
Your driver's *DdBlt* function must support copying the FOURCC destination surface to a surface of the same FOURCC format. The destination surface is used as the source surface in the copy operation. Your driver should indicate that it supports copying FOURCC formats by setting the DDCAPS2\_COPYFOURCC flag.

The destination surface for the bit-block transfer operations can be the primary surface or a Direct3D texture.

 

 





