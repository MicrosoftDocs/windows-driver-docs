---
title: Rasterizer Update
description: Rasterizer Update
ms.assetid: 0b7db462-2b04-42e1-baa0-ec9070741c1d
keywords: ["rasterizers WDK Direct3D", "production rasterizers WDK Direct3D", "reference rasterizers WDK Direct3D"]
---

# Rasterizer Update


## <span id="ddk_rasterizer_update_gg"></span><span id="DDK_RASTERIZER_UPDATE_GG"></span>


The reference rasterizer has been extracted into a separate DLL to enable additional WHQL tests to be added asynchronously of normal DirectX ship cycles (quarterly is typical). It has been updated to support any of the rasterizer-level operations added to the API either in the core or as extensions that require guaranteed consistency of implementation.

The production rasterizer may not be updated to support these techniques, because environment mapping at the vertex level is likely to be faster than at the pixel level when running in software.

This rasterizer is likely to be upgraded in terms of performance on key cases that are identified.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Rasterizer%20Update%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




