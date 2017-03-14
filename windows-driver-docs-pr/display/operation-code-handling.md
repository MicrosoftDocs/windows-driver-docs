---
title: Operation Code Handling
description: Operation Code Handling
ms.assetid: 97de8370-316e-41df-bf27-1985af47a4e0
keywords: ["Direct3D WDK Windows 2000 display , operation codes", "operation codes WDK Direct3D", "D3dDrawPrimitives2"]
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
<td align="left"><p><strong>Always required.</strong> Used to clear the context's render target, Z-buffer. Replaces <em>D3dClear2</em>. Also used to clear hardware stencil buffers, and depth buffers that cannot be cleared properly by a depth fill bit-block transfer.</p></td>
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

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Operation%20Code%20Handling%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




