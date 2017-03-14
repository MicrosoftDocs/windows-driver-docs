---
title: Promoting Z Buffers to 32 Bits Per Pixel
description: Promoting Z Buffers to 32 Bits Per Pixel
ms.assetid: 6b7dddab-e154-44e8-a4e3-45bd706ed638
keywords: ["z buffers WDK DirectX 9.0", "color buffers WDK DirectX 9.0", "D3DFORMAT_OP_ZSTENCIL_WITH_ARBITRARY_COLOR_DEPTH"]
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Promoting%20Z%20Buffers%20to%2032%20Bits%20Per%20Pixel%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




