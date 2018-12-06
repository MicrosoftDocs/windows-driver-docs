---
title: Direct3D Vertex Buffers
description: Direct3D Vertex Buffers
ms.assetid: b93278fc-c05f-40d4-aec1-7a90aed18ff4
keywords:
- vertex buffers WDK Direct3D
- buffers WDK Direct3D
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 





