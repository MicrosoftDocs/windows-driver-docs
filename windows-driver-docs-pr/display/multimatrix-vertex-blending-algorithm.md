---
title: Multimatrix Vertex Blending Algorithm
description: Multimatrix Vertex Blending Algorithm
ms.assetid: 78ea0a92-a026-4c8d-a0ff-8be17b0a6424
keywords:
- multimatrix vertex blending WDK Direct3D , algorithm
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Multimatrix Vertex Blending Algorithm


## <span id="ddk_multimatrix_vertex_blending_algorithm_gg"></span><span id="DDK_MULTIMATRIX_VERTEX_BLENDING_ALGORITHM_GG"></span>


The multimatrix vertex blending algorithm assumes that only two matrices are being used.

On matrix change, update the following four matrices:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Matrix</th>
<th align="left">Computation</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Current Transform Matrix (CTM)</p></td>
<td align="left"><p>CTM = WORLD * VIEW * PROJ</p></td>
</tr>
<tr class="even">
<td align="left"><p>Secondary CTM (parent coordinates)</p></td>
<td align="left"><p>CTM2 = WORLD1 * VIEW * PROJ</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Inverse transpose of CTM</p></td>
<td align="left"><p>ITCTM = (CTM<sup>T</sup>)⁻¹</p></td>
</tr>
<tr class="even">
<td align="left"><p>Inverse transpose of CTM2 (required if lighting)</p></td>
<td align="left"><p>ITCTM2 = (CTM2<sup>T</sup>)⁻¹</p></td>
</tr>
</tbody>
</table>

 

In some cases it may be more efficient to blend the matrices first using the vertex's weights, and then do only one (matrix)X(vertex) multiplication.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Multimatrix%20Vertex%20Blending%20Algorithm%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




