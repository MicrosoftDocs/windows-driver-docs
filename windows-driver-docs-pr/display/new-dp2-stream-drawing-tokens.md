---
title: New DP2 Stream Drawing Tokens
description: New DP2 Stream Drawing Tokens
ms.assetid: 09f3e5a4-60ed-4649-a30b-de4b320a54de
keywords: ["DirectX 8.0 release notes WDK Windows 2000 display , DP2 drawing tokens", "DP2 drawing tokens WDK DirectX 8.0", "drawing tokens WDK DirectX 8.0", "tokens WDK DirectX 8.0"]
---

# New DP2 Stream Drawing Tokens


## <span id="ddk_new_dp2_stream_drawing_tokens_gg"></span><span id="DDK_NEW_DP2_STREAM_DRAWING_TOKENS_GG"></span>


DirectX 8.0's support for multiple streams of vertex data requires that new DP2 drawing tokens be introduced. These new tokens are necessary because existing drawing tokens assumed that there was a single pointer to vertex data for a particular drawing instruction. With multiple streams, this is no longer the case. A drawing command may well access multiple vertex data buffers simultaneously through streams.

Note that these drawing tokens replace the existing primitive type specific tokens (for example, D3DDP2OP\_POINTS, D3DDP2OP\_TRIANGLELIST, D3DDP2OP\_TRIANGLESTRIP) for calls through the new DirectX 8.0 interfaces only. Calls made through DX7 or earlier interfaces are still passed through the DDI as the old style drawing tokens. Therefore, a DX8 driver is required to support both old and new style drawing tokens.

The indexed and nonindexed drawing tokens have two variants. For example, nonindexed drawing is accomplished by the tokens D3DDP2OP\_DRAWPRIMITIVE and D3DDP2OP\_DRAWPRIMITIVE2. Similarly, indexed drawing is accomplished by the tokens D3DDP2OP\_DRAWINDEXEDPRIMITIVE and D3DDP2OP\_DRAWINDEXEDPRIMITIVE2.

The main distinction between the two variants is that D3DDP2OP\_DRAWPRIMITIVE2 and D3DDP2OP\_DRAWINDEXEDPRIMITIVE2 are used when the vertex data has been transformed by the runtime. This is either because the driver/hardware combination does not support hardware vertex processing or the software vertex processing has been explicitly selected. For these tokens, only stream zero is used and it contains transformed and lit vertices.

D3DDP2OP\_DRAWPRIMITIVE and D3DDP2OP\_DRAWINDEXEDPRIMITIVE are used then the runtime has not processed the vertex data. Thus, these tokens can supply untransformed vertex data when the hardware supports hardware vertex processing or transformed vertex data when the application supplies transformed data directly to the runtime. In this case, any number of streams (up to **MaxStreams**) can be active. These variants (along with the other new drawing token, D3DDP2OP\_CLIPPEDTRIANGLEFAN) enable optimal code paths in the runtime and the distinctions beyond those described here are not significant to the driver.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20New%20DP2%20Stream%20Drawing%20Tokens%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




