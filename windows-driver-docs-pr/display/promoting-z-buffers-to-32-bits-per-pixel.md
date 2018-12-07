---
title: Promoting Z Buffers to 32 Bits Per Pixel
description: Promoting Z Buffers to 32 Bits Per Pixel
ms.assetid: 6b7dddab-e154-44e8-a4e3-45bd706ed638
keywords:
- z buffers WDK DirectX 9.0
- color buffers WDK DirectX 9.0
- D3DFORMAT_OP_ZSTENCIL_WITH_ARBITRARY_COLOR_DEPTH
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Promoting Z Buffers to 32 Bits Per Pixel


## <span id="ddk_promoting_z_buffers_to_32_bits_per_pixel_gg"></span><span id="DDK_PROMOTING_Z_BUFFERS_TO_32_BITS_PER_PIXEL_GG"></span>


**This topic applies to DirectX 8.0 and later.**

A display driver whose display device does not support rendering to z and color buffers with differing pixel depths must transparently promote a 16 bits per pixel (bpp) z buffer to 32 bpp in order to render both the z buffer and a 32 bpp color buffer at the same time. Note, however, that the z buffer cannot also have stencil bits. Therefore, applications are not required to correct this mismatch in buffer pixel depth.

If the driver's display device can render to z and color buffers of differing pixel depth, the driver sets the D3DFORMAT\_OP\_ZSTENCIL\_WITH\_ARBITRARY\_COLOR\_DEPTH flag in the **dwOperations** member of the [**DDPIXELFORMAT**](https://msdn.microsoft.com/library/windows/hardware/ff550274) structure for z-buffer formats. The Direct3D runtime then lets applications render to any mismatch of z- and color-pixel depths.

If the driver does not set D3DFORMAT\_OP\_ZSTENCIL\_WITH\_ARBITRARY\_COLOR\_DEPTH for z-buffer formats, the runtime only lets applications render to a mismatch of 32 bpp color buffer and 16 bpp z buffer with no stencil bits as described in the introductory paragraph. In this case, the driver allocates a 32 bpp z buffer in place of the requested 16 bpp z buffer.

If D3DFORMAT\_OP\_ZSTENCIL\_WITH\_ARBITRARY\_COLOR\_DEPTH is not set, the runtime does not let applications render to the following mismatch scenarios:

-   16 bpp color buffer and 32 bpp z buffer at the same time. For rendering to succeed in this scenario, the driver would have to substitute a 16 bpp z buffer for the 32 bpp z buffer, which would degrade z precision and cause noticeable artifacts.

-   Any z format whose depth stencil does not occupy the same number of bits per pixel as the color buffer (in other words, mismatching z and stencil surfaces). For rendering to succeed in this scenario, the driver would have to change the number of stencil bits, which would also cause noticeable artifacts.

 

 





