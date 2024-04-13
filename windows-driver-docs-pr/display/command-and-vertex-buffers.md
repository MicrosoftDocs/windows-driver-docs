---
title: Command and Vertex Buffers
description: Command and Vertex Buffers
keywords:
- command buffers WDK Direct3D
- vertex buffers WDK Direct3D
- buffers WDK Direct3D
ms.date: 04/20/2017
---

# Command and Vertex Buffers


## <span id="ddk_command_and_vertex_buffers_gg"></span><span id="DDK_COMMAND_AND_VERTEX_BUFFERS_GG"></span>


The [**D3dDrawPrimitives2**](/windows-hardware/drivers/ddi/d3dhal/nc-d3dhal-lpd3dhal_drawprimitives2cb) DDI uses two types of buffers: command buffers and vertex buffers. Command buffers contain instructions followed by data in a structure similar to that of execute buffers. Command buffers might contain indexed and nonindexed primitives and, occasionally, inline vertex data. Command buffers can be either API-level execute buffers or Direct3D internal command buffers. For a description of the main input structure, see [**D3DHAL\_DRAWPRIMITIVES2DATA**](/windows-hardware/drivers/ddi/d3dhal/ns-d3dhal-_d3dhal_drawprimitives2data).

With internal command buffers, the driver allocates the memory and may do multibuffering. Internal command buffers are write-only. The instruction format can be seen in [**D3DHAL\_DP2COMMAND**](/windows-hardware/drivers/ddi/d3dhal/ns-d3dhal-_d3dhal_dp2command).

If the D3DHALDP2\_USERMEMVERTICES flag is set, the vertex buffer is specified by a user-memory pointer. Otherwise, the vertex buffer is a DirectDrawSurface that can be an API-level execute buffer, an internal implicit vertex buffer, or an API-level vertex buffer.

The vertex buffer API can create, destroy, lock and unlock vertex buffers, and can use the **IDirect3DVertexBuffer7::ProcessVertices** method to process vertices from source to destination buffers. The **IDirect3DDevice7::DrawPrimitiveVB** and **IDirect3DDevice7::DrawIndexedPrimitiveVB** methods are the primary API-level calls. Vertex buffers can also be optimized, but optimized vertex buffers cannot be locked. For descriptions of these three methods, see the Direct3D SDK documentation.

 

