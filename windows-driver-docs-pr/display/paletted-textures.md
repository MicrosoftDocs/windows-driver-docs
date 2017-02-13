---
title: Paletted Textures
description: Paletted Textures
ms.assetid: eac46256-db08-4a9b-aaaf-2bc8a9f30e98
keywords: ["texture management WDK Direct3D , paletted textures", "paletted textures WDK Direct3D"]
---

# Paletted Textures


## <span id="ddk_paletted_textures_gg"></span><span id="DDK_PALETTED_TEXTURES_GG"></span>


Direct3D allows palettes to be used with textures. A palette can be attached to a texture, just as it can to any other DirectDrawSurface object. To support paletted textures, drivers must respond to the D3DDP2OP\_SETPALETTE and D3DDP2OP\_UPDATEPALETTE operation codes in their implementation of [**D3dDrawPrimitives2**](https://msdn.microsoft.com/library/windows/hardware/ff544704). These operation codes are followed by [**D3DHAL\_DP2SETPALETTE**](https://msdn.microsoft.com/library/windows/hardware/ff545744) and [**D3DHAL\_DP2UPDATEPALETTE**](https://msdn.microsoft.com/library/windows/hardware/ff545923) structures, respectively, in the command stream. D3DDP2OP\_SETPALETTE creates an association between a palette handle and a surface handle (already created by [**D3dCreateSurfaceEx**](https://msdn.microsoft.com/library/windows/hardware/ff542840)). Later, D3DDP2OP\_UPDATEPALETTE can be sent multiple times to set the values of the palette entries for this texture.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Paletted%20Textures%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




