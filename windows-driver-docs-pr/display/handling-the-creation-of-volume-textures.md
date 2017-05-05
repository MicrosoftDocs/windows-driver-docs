---
title: Handling the Creation of Volume Textures
description: Handling the Creation of Volume Textures
ms.assetid: d5f521df-cd52-4c7e-9ad2-5df343c96e8c
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

# Handling the Creation of Volume Textures


## <span id="ddk_handling_the_creation_of_volume_textures_gg"></span><span id="DDK_HANDLING_THE_CREATION_OF_VOLUME_TEXTURES_GG"></span>


DirectX 8.0 introduces a new surface capability bit DDSCAPS2\_VOLUME. This flag is set in the **ddsCapsEx.dwCaps2** field of the surface's [**DD\_SURFACE\_MORE**](https://msdn.microsoft.com/library/windows/hardware/ff551737) structure. In the [*DdCreateSurface*](https://msdn.microsoft.com/library/windows/hardware/ff549263) and [**D3dCreateSurfaceEx**](https://msdn.microsoft.com/library/windows/hardware/ff542840) callbacks the depth of the volume texture can be found in the low word of the **dwCaps4** field of the extended surface capabilities (**ddsCapsEx**) of the surface's DD\_SURFACE\_MORE structure. The driver should return the "slice pitch" (that is, the number of bytes to add to move from one 2D slice of the volume to the next) of the volume texture in the **dwBlockSizeY** field of the surface global structure.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Handling%20the%20Creation%20of%20Volume%20Textures%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




