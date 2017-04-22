---
title: Reporting Support for Volume Textures
description: Reporting Support for Volume Textures
ms.assetid: da0c1c88-504e-4293-96ca-65cac2e0fe97
keywords:
- textures WDK DirectX 8.0
- DirectX 8.0 release notes WDK Windows 2000 display , volume textures
- volume textures WDK DirectX 8.0
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Reporting Support for Volume Textures


## <span id="ddk_reporting_support_for_volume_textures_gg"></span><span id="DDK_REPORTING_SUPPORT_FOR_VOLUME_TEXTURES_GG"></span>


DirectX 8.0 introduces two new primitive texture capabilities flags that the driver sets to indicate support for volume textures. These flags are D3DPTEXTURECAPS\_VOLUMEMAP and D3DPTEXTURECAPS\_MIPVOLUMEMAP. D3DPTEXTURECAPS\_VOLUMEMAP should be set in the **dwTextureCaps** field of the D3DPRIMCAPS8 structure (part of D3DCAPS8) if the hardware has support for volume textures. D3DPTEXTURECAPS\_MIPVOLUMEMAP indicates that the driver supports MIP mapped volume textures.

Hardware that supports volume textures must also support the use of volume textures in multitexturing scenarios (in combination with other volume textures or 2D textures). If this scenario is not supported by the hardware, the driver cannot set D3DPTEXTURECAPS\_VOLUMEMAP.

The driver can indicate that it requires the dimensions of the volume texture to be a power of 2 by setting the primitive texture capability D3DPTEXTURECAPS\_VOLUMEMAP\_POW2.

A driver that supports volume textures is also required to specify the minimum and maximum volume texture dimensions that it supports. The field **MaxVolumeExtent** should be set to the maximum supported dimensions of the volume texture. The same constraint must apply to all three dimensions of the volume texture (width, height and depth).

A driver notifies the runtime of the volume texture filtering and texture addressing modes supported by the hardware by setting the **VolumeTextureFilterCaps** and **VolumeTextureAddressCaps** to the appropriate combinations of flags.

Finally, the driver notifies the runtime about what surface formats can be used with volume textures by setting the D3DFORMAT\_OP\_VOLUMETEXTURE in the **dwOperations** field of the surface format's [**DDPIXELFORMAT**](https://msdn.microsoft.com/library/windows/hardware/ff550274).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Reporting%20Support%20for%20Volume%20Textures%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




