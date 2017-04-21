---
title: Command and Vertex Buffers
description: Command and Vertex Buffers
ms.assetid: e23013d2-d545-42e5-9787-e4a90921153b
keywords:
- command buffers WDK Direct3D
- vertex buffers WDK Direct3D
- buffers WDK Direct3D
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Command and Vertex Buffers


## <span id="ddk_command_and_vertex_buffers_gg"></span><span id="DDK_COMMAND_AND_VERTEX_BUFFERS_GG"></span>


The [**D3dDrawPrimitives2**](https://msdn.microsoft.com/library/windows/hardware/ff544704) DDI uses two types of buffers: command buffers and vertex buffers. Command buffers contain instructions followed by data in a structure similar to that of execute buffers. Command buffers might contain indexed and nonindexed primitives and, occasionally, inline vertex data. Command buffers can be either API-level execute buffers or Direct3D internal command buffers. For a description of the main input structure, see [**D3DHAL\_DRAWPRIMITIVES2DATA**](https://msdn.microsoft.com/library/windows/hardware/ff545957).

With internal command buffers, the driver allocates the memory and may do multibuffering. Internal command buffers are write-only. The instruction format can be seen in [**D3DHAL\_DP2COMMAND**](https://msdn.microsoft.com/library/windows/hardware/ff545454).

If the D3DHALDP2\_USERMEMVERTICES flag is set, the vertex buffer is specified by a user-memory pointer. Otherwise, the vertex buffer is a DirectDrawSurface that can be an API-level execute buffer, an internal implicit vertex buffer, or an API-level vertex buffer.

The vertex buffer API can create, destroy, lock and unlock vertex buffers, and can use the **IDirect3DVertexBuffer7::ProcessVertices** method to process vertices from source to destination buffers. The **IDirect3DDevice7::DrawPrimitiveVB** and **IDirect3DDevice7::DrawIndexedPrimitiveVB** methods are the primary API-level calls. Vertex buffers can also be optimized, but optimized vertex buffers cannot be locked. For descriptions of these three methods, see the Direct3D SDK documentation.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Command%20and%20Vertex%20Buffers%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




