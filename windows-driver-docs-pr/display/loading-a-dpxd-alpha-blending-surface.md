---
title: Loading a DPXD Alpha-Blending Surface
description: Loading a DPXD Alpha-Blending Surface
ms.assetid: 6b5f62e9-3211-42c2-8168-505983c7814e
keywords:
- stride WDK DirectX VA
- alpha-blend data loading WDK DirectX VA
- blended pictures WDK DirectX VA , alpha-blend data loading
- DPXD alpha-blending surface WDK DirectX VA
- decoded PXD alpha-blending surface WDK DirectX VA
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Loading a DPXD Alpha-Blending Surface


## <span id="ddk_loading_a_dpxd_alpha_blending_surface_gg"></span><span id="DDK_LOADING_A_DPXD_ALPHA_BLENDING_SURFACE_GG"></span>


A decoded PXD (DPXD) alpha-blending surface is defined as an array of bytes for a frame. Each byte of frame data contains four 2-bit samples. Each 2-bit sample is used as an index into a four-color table determined by highlight and DCCMD (display control command) data. The result of the combination of DPXD, highlight, and DCCMD is equivalent to an IA44 surface, and is used with a 16-entry YUV palette for blending. If the DPXD alpha-blending surface is treated as an array of bytes, the index of the first 2-bit sample is in the most significant bits of the first byte of DPXD data, the next sample is in the next 2 bits, the third sample is in the next 2 bits, the fourth sample is in the least significant bits, the fifth sample is in the most significant bits of the next byte, and so on.

The DPXD alpha-blending surface may be created from the PXD information about a DVD. (The PXD data is recorded on a DVD in a run-length encoded format.) The creation of DPXD from the PXD on a DVD requires the host decoder to perform run-length decoding of the raw PXD data on the DVD.

The stride of the surface must be interpreted as the stride in bytes, not in 2-bit samples. However, the width and height must be in 2-bit sample units.

**Note**   The PXD on a DVD is in a field-structured interlaced format. The DPXD alpha-blending surface defined for DirectX VA is not. The host is therefore responsible for interleaving the data from the two fields if forming DPXD from DVD PXD data.

 

For more clarification of DVD subpicture definition and data field interpretation, see *DVD Specifications for Read-Only Disk: Part 3 - Video Specification (version 1.11, May 1999)*.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Loading%20a%20DPXD%20Alpha-Blending%20Surface%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




