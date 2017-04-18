---
title: Direct3D Vertex Buffers
description: Direct3D Vertex Buffers
ms.assetid: b93278fc-c05f-40d4-aec1-7a90aed18ff4
keywords: ["vertex buffers WDK Direct3D", "buffers WDK Direct3D"]
---

# Direct3D Vertex Buffers


## <span id="ddk_direct3d_vertex_buffers_gg"></span><span id="DDK_DIRECT3D_VERTEX_BUFFERS_GG"></span>


A vertex buffer contains the vertex data associated with a command buffer's primitives in a call to [**D3dDrawPrimitives2**](https://msdn.microsoft.com/library/windows/hardware/ff544704). Vertices are represented using the flexible vertex format ([FVF](fvf--flexible-vertex-format-.md)), where each vertex can have the following data associated with it:

-   Position (*x,y,z, and optional w*) (required)

-   Diffuse color (optional)

-   Specular color (optional)

-   Texture coordinates (optional). Direct3D can send up to a maximum of eight sets of (*u,v*) values.

Drivers must provide FVF support.

The actual vertices and the order in which they should be processed depends on the D3DDP2OP\_*Xxx* primitive command just parsed from the command buffer. For details, see the individual D3DHAL\_DP2*Xxx* structure reference pages.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Direct3D%20Vertex%20Buffers%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




