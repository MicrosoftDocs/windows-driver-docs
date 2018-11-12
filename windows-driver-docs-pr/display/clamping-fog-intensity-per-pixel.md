---
title: Clamping Fog Intensity Per Pixel
description: Clamping Fog Intensity Per Pixel
ms.assetid: 249d085a-b54c-48b3-bc7a-3fe5f8238b1b
keywords:
- clamping fog intensity per pixel WDK DirectX 9.0
- fog intensity per pixel WDK DirectX 9.0
- pixel fog intensity clamping WDK DirectX 9.0
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Clamping Fog Intensity Per Pixel


## <span id="ddk_clamping_fog_intensity_per_pixel_gg"></span><span id="DDK_CLAMPING_FOG_INTENSITY_PER_PIXEL_GG"></span>


A DirectX 9.0 version driver for a device that supports either pixel or vertex shader version 2.0 and later must indicate that its device supports clamping the fog intensity value on a per-pixel basis by setting the D3DPMISCCAPS\_FOGINFVF capability bit. This informs users that the device does not save the fog factor in the specular alpha channel when using software vertex shaders. The device can pass the alpha channel of the specular color (computed in the fixed function vertex pipeline) to the pixel processing unit, instead of always overwriting the alpha channel with the per-vertex fog intensity value.

Because the driver clamps the fog intensity value on a per-pixel basis, the runtime for DirectX 9.0 and later no longer clamps the fog intensity value before sending it to the driver.

The driver determines how to obtain the fog value by verifying if the D3DFVF\_FOG bit in the flexible vertex format (FVF) is set. If D3DFVF\_FOG is set, the driver obtains the separate fog value that is passed per vertex. If D3DFVF\_FOG is not set and the driver must use fog, the driver obtains the fog value from the specular color's alpha channel.

When the driver sets D3DPMISCCAPS\_FOGINFVF, the runtime in turn sets the D3DPMISCCAPS\_FOGANDSPECULARALPHA capability bit in the **PrimitiveMiscCaps** member of the D3DCAPS9 structure.

 

 





