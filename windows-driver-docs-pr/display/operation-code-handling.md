---
title: Operation Code Handling
description: Operation Code Handling
ms.assetid: 97de8370-316e-41df-bf27-1985af47a4e0
keywords:
- Direct3D WDK Windows 2000 display , operation codes
- operation codes WDK Direct3D
- D3dDrawPrimitives2
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Operation Code Handling


## <span id="ddk_opcode_handling_gg"></span><span id="DDK_OPCODE_HANDLING_GG"></span>


A display driver handles requests to render graphics primitives and processes state changes in its [**D3dDrawPrimitives2**](https://msdn.microsoft.com/library/windows/hardware/ff544704) function. The driver receives these requests as [**D3DHAL\_DP2OPERATION**](https://msdn.microsoft.com/library/windows/hardware/ff545678) operation codes. The following topics describe how the driver processes operation codes and how its performance can be improved during such processing:

[Command Stream](command-stream.md)

[Improving Performance of Operation Handling](improving-performance-of-operation-handling.md)

In order to support the Microsoft DirectX 7.0 and later Direct3D driver model, driver writers need to make their drivers respond to a number of new operation codes in their implementation of [**D3dDrawPrimitives2**](https://msdn.microsoft.com/library/windows/hardware/ff544704). Some of these operation codes replace callback functions, and others provide new functionality. The most important new operation codes are summarized in the following table, beginning with those that replace callbacks.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Operation Code</th>
<th align="left">Condition/Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>D3DDP2OP_SETRENDERTARGET</p></td>
<td align="left"><p><strong>Always required.</strong> Maps a new rendering target surface and depth buffer in the current context. Replaces <em>D3dSetRenderTarget</em>.</p></td>
</tr>
<tr class="even">
<td align="left"><p>D3DDP2OP_CLEAR</p></td>
<td align="left"><p><strong>Always required.</strong> Used to clear the context&#39;s render target, Z-buffer. Replaces <em>D3dClear2</em>. Also used to clear hardware stencil buffers, and depth buffers that cannot be cleared properly by a depth fill bit-block transfer.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>D3DDP2OP_SETPALETTE</p></td>
<td align="left"><p>Used to map an association between a palette handle and a surface handle, and specify the characteristics of the palette. Only needed for drivers that support paletted textures; otherwise this should be no operation (NOP).</p></td>
</tr>
<tr class="even">
<td align="left"><p>D3DDP2OP_UPDATEPALETTE</p></td>
<td align="left"><p>Used to make alterations to a texture palette, for drivers that support paletted textures. Otherwise, this should be a NOP.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>D3DDP2OP_TEXBLT</p></td>
<td align="left"><p>Specifies a blt operation from a source texture to a destination texture.</p></td>
</tr>
</tbody>
</table>

 

 

 





