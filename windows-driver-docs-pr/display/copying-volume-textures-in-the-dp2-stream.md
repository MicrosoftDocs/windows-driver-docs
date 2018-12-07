---
title: Copying Volume Textures in the DP2 Stream
description: Copying Volume Textures in the DP2 Stream
ms.assetid: c7f982d8-d35b-4462-a0cf-49dfb82860f8
keywords:
- textures WDK DirectX 8.0
- DirectX 8.0 release notes WDK Windows 2000 display , volume textures
- volume textures WDK DirectX 8.0
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Copying Volume Textures in the DP2 Stream


## <span id="ddk_copying_volume_textures_in_the_dp2_stream_gg"></span><span id="DDK_COPYING_VOLUME_TEXTURES_IN_THE_DP2_STREAM_GG"></span>


A new DP2 token, D3DDP2OP\_VOLUMEBLT, has been added to support optimal copying and updating of volume textures. This token is very similar to the existing D3DDP2OP\_TEXBLT that copies and updates textures but has been extended to support subvolume (box) copying rather than simple rectangles.

 

 





