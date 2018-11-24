---
title: Multimatrix Vertex Blending Algorithm
description: Multimatrix Vertex Blending Algorithm
ms.assetid: 78ea0a92-a026-4c8d-a0ff-8be17b0a6424
keywords:
- multimatrix vertex blending WDK Direct3D , algorithm
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 





