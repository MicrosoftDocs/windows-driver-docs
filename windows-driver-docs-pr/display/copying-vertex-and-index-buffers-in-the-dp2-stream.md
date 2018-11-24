---
title: Copying Vertex and Index Buffers in the DP2 Stream
description: Copying Vertex and Index Buffers in the DP2 Stream
ms.assetid: 5181e299-4beb-448c-bf11-be9bb5575af1
keywords:
- DirectX 8.0 release notes WDK Windows 2000 display , DP2 drawing tokens
- DP2 drawing tokens WDK DirectX 8.0
- drawing tokens WDK DirectX 8.0
- tokens WDK DirectX 8.0
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Copying Vertex and Index Buffers in the DP2 Stream


## <span id="ddk_copying_vertex_and_index_buffers_in_the_dp2_stream_gg"></span><span id="DDK_COPYING_VERTEX_AND_INDEX_BUFFERS_IN_THE_DP2_STREAM_GG"></span>


A new DP2 token, D3DDP2OP\_BUFFERBLT, has been added to support optimal copying and updating of index and vertex buffers. This token is very similar to the existing D3DDP2OP\_TEXBLT that copies and updates textures but has been modified to support subbuffer copying rather than simple rectangles.

 

 





