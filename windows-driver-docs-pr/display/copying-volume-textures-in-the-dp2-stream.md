---
title: Copying Volume Textures in the DP2 Stream
description: Copying Volume Textures in the DP2 Stream
ms.assetid: c7f982d8-d35b-4462-a0cf-49dfb82860f8
keywords:
- textures WDK DirectX 8.0
- DirectX 8.0 release notes WDK Windows 2000 display , volume textures
- volume textures WDK DirectX 8.0
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Copying Volume Textures in the DP2 Stream


## <span id="ddk_copying_volume_textures_in_the_dp2_stream_gg"></span><span id="DDK_COPYING_VOLUME_TEXTURES_IN_THE_DP2_STREAM_GG"></span>


A new DP2 token, D3DDP2OP\_VOLUMEBLT, has been added to support optimal copying and updating of volume textures. This token is very similar to the existing D3DDP2OP\_TEXBLT that copies and updates textures but has been extended to support subvolume (box) copying rather than simple rectangles.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Copying%20Volume%20Textures%20in%20the%20DP2%20Stream%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




