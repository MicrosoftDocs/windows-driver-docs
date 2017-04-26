---
title: Multiple Vertex Streams
description: Multiple Vertex Streams
ms.assetid: aaaea27b-79e0-4c48-9102-898b42a1487f
keywords:
- DirectX 8.0 release notes WDK Windows 2000 display , multiple vertex streams
- multiple vertex streams WDK DirectX 8.0
- vertex multiple streams WDK DirectX 8.0
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Multiple Vertex Streams


## <span id="ddk_multiple_vertex_streams_gg"></span><span id="DDK_MULTIPLE_VERTEX_STREAMS_GG"></span>


DirectX 8.0 adds support for multiple vertex streams. Even if the driver and hardware combination does not support more than one stream of vertex data, the driver must still handle the stream binding DP2 tokens (D3DDP2OP\_SETSTREAMSOURCE and D3DDP2OP\_SETSTREAMSOURCEUM) and the new vertex stream based DP2 drawing tokens (see [New DP2 Stream Drawing Tokens](new-dp2-stream-drawing-tokens.md)). These are the mechanisms for passing vertex data to the driver in drawing for DirectX 8.0 level drivers.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Multiple%20Vertex%20Streams%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




