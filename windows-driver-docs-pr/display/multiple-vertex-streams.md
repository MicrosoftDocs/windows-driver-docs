---
title: Multiple Vertex Streams
description: Multiple Vertex Streams
ms.assetid: aaaea27b-79e0-4c48-9102-898b42a1487f
keywords:
- DirectX 8.0 release notes WDK Windows 2000 display , multiple vertex streams
- multiple vertex streams WDK DirectX 8.0
- vertex multiple streams WDK DirectX 8.0
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Multiple Vertex Streams


## <span id="ddk_multiple_vertex_streams_gg"></span><span id="DDK_MULTIPLE_VERTEX_STREAMS_GG"></span>


DirectX 8.0 adds support for multiple vertex streams. Even if the driver and hardware combination does not support more than one stream of vertex data, the driver must still handle the stream binding DP2 tokens (D3DDP2OP\_SETSTREAMSOURCE and D3DDP2OP\_SETSTREAMSOURCEUM) and the new vertex stream based DP2 drawing tokens (see [New DP2 Stream Drawing Tokens](new-dp2-stream-drawing-tokens.md)). These are the mechanisms for passing vertex data to the driver in drawing for DirectX 8.0 level drivers.

 

 





