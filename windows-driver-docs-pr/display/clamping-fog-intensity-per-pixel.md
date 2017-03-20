---
title: Clamping Fog Intensity Per Pixel
description: Clamping Fog Intensity Per Pixel
ms.assetid: 249d085a-b54c-48b3-bc7a-3fe5f8238b1b
keywords: ["clamping fog intensity per pixel WDK DirectX 9.0", "fog intensity per pixel WDK DirectX 9.0", "pixel fog intensity clamping WDK DirectX 9.0"]
---

# Clamping Fog Intensity Per Pixel


## <span id="ddk_clamping_fog_intensity_per_pixel_gg"></span><span id="DDK_CLAMPING_FOG_INTENSITY_PER_PIXEL_GG"></span>


A DirectX 9.0 version driver for a device that supports either pixel or vertex shader version 2.0 and later must indicate that its device supports clamping the fog intensity value on a per-pixel basis by setting the D3DPMISCCAPS\_FOGINFVF capability bit. This informs users that the device does not save the fog factor in the specular alpha channel when using software vertex shaders. The device can pass the alpha channel of the specular color (computed in the fixed function vertex pipeline) to the pixel processing unit, instead of always overwriting the alpha channel with the per-vertex fog intensity value.

Because the driver clamps the fog intensity value on a per-pixel basis, the runtime for DirectX 9.0 and later no longer clamps the fog intensity value before sending it to the driver.

The driver determines how to obtain the fog value by verifying if the D3DFVF\_FOG bit in the flexible vertex format (FVF) is set. If D3DFVF\_FOG is set, the driver obtains the separate fog value that is passed per vertex. If D3DFVF\_FOG is not set and the driver must use fog, the driver obtains the fog value from the specular color's alpha channel.

When the driver sets D3DPMISCCAPS\_FOGINFVF, the runtime in turn sets the D3DPMISCCAPS\_FOGANDSPECULARALPHA capability bit in the **PrimitiveMiscCaps** member of the D3DCAPS9 structure.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Clamping%20Fog%20Intensity%20Per%20Pixel%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




