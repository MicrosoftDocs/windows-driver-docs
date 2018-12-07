---
title: New DP2 Stream Drawing Tokens
description: New DP2 Stream Drawing Tokens
ms.assetid: 09f3e5a4-60ed-4649-a30b-de4b320a54de
keywords:
- DirectX 8.0 release notes WDK Windows 2000 display , DP2 drawing tokens
- DP2 drawing tokens WDK DirectX 8.0
- drawing tokens WDK DirectX 8.0
- tokens WDK DirectX 8.0
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# New DP2 Stream Drawing Tokens


## <span id="ddk_new_dp2_stream_drawing_tokens_gg"></span><span id="DDK_NEW_DP2_STREAM_DRAWING_TOKENS_GG"></span>


DirectX 8.0's support for multiple streams of vertex data requires that new DP2 drawing tokens be introduced. These new tokens are necessary because existing drawing tokens assumed that there was a single pointer to vertex data for a particular drawing instruction. With multiple streams, this is no longer the case. A drawing command may well access multiple vertex data buffers simultaneously through streams.

Note that these drawing tokens replace the existing primitive type specific tokens (for example, D3DDP2OP\_POINTS, D3DDP2OP\_TRIANGLELIST, D3DDP2OP\_TRIANGLESTRIP) for calls through the new DirectX 8.0 interfaces only. Calls made through DX7 or earlier interfaces are still passed through the DDI as the old style drawing tokens. Therefore, a DX8 driver is required to support both old and new style drawing tokens.

The indexed and nonindexed drawing tokens have two variants. For example, nonindexed drawing is accomplished by the tokens D3DDP2OP\_DRAWPRIMITIVE and D3DDP2OP\_DRAWPRIMITIVE2. Similarly, indexed drawing is accomplished by the tokens D3DDP2OP\_DRAWINDEXEDPRIMITIVE and D3DDP2OP\_DRAWINDEXEDPRIMITIVE2.

The main distinction between the two variants is that D3DDP2OP\_DRAWPRIMITIVE2 and D3DDP2OP\_DRAWINDEXEDPRIMITIVE2 are used when the vertex data has been transformed by the runtime. This is either because the driver/hardware combination does not support hardware vertex processing or the software vertex processing has been explicitly selected. For these tokens, only stream zero is used and it contains transformed and lit vertices.

D3DDP2OP\_DRAWPRIMITIVE and D3DDP2OP\_DRAWINDEXEDPRIMITIVE are used then the runtime has not processed the vertex data. Thus, these tokens can supply untransformed vertex data when the hardware supports hardware vertex processing or transformed vertex data when the application supplies transformed data directly to the runtime. In this case, any number of streams (up to **MaxStreams**) can be active. These variants (along with the other new drawing token, D3DDP2OP\_CLIPPEDTRIANGLEFAN) enable optimal code paths in the runtime and the distinctions beyond those described here are not significant to the driver.

 

 





