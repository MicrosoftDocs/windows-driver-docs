---
title: Copying Vertex and Index Buffers in the DP2 Stream
description: Copying Vertex and Index Buffers in the DP2 Stream
ms.assetid: 5181e299-4beb-448c-bf11-be9bb5575af1
keywords:
- DirectX 8.0 release notes WDK Windows 2000 display , DP2 drawing tokens
- DP2 drawing tokens WDK DirectX 8.0
- drawing tokens WDK DirectX 8.0
- tokens WDK DirectX 8.0
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Copying Vertex and Index Buffers in the DP2 Stream


## <span id="ddk_copying_vertex_and_index_buffers_in_the_dp2_stream_gg"></span><span id="DDK_COPYING_VERTEX_AND_INDEX_BUFFERS_IN_THE_DP2_STREAM_GG"></span>


A new DP2 token, D3DDP2OP\_BUFFERBLT, has been added to support optimal copying and updating of index and vertex buffers. This token is very similar to the existing D3DDP2OP\_TEXBLT that copies and updates textures but has been modified to support subbuffer copying rather than simple rectangles.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Copying%20Vertex%20and%20Index%20Buffers%20in%20the%20DP2%20Stream%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




