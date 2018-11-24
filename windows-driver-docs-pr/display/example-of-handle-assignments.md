---
title: Example of Handle Assignments
description: Example of Handle Assignments
ms.assetid: 44239e13-ebe7-48c4-83b2-40f603dc1c98
keywords:
- multiple-head hardware WDK DirectX 9.0 , handle assignments
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Example of Handle Assignments


## <span id="ddk_example_of_handle_assignments_gg"></span><span id="DDK_EXAMPLE_OF_HANDLE_ASSIGNMENTS_GG"></span>


The following table shows an example arrangement of Direct3D handle values (supplied through [**D3dCreateSurfaceEx**](https://msdn.microsoft.com/library/windows/hardware/ff542840)) that might be present in a two-head scenario. The front, back and depth/stencil surfaces on each head all have unique handles; the master head must work with all of these handles. The master head owns all texture, vertex buffer, and index buffer surfaces; handles for these surfaces are only created on the master head.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Master head handle value</th>
<th align="left">Subordinate head handle value</th>
<th align="left">Surface</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0</p></td>
<td align="left"></td>
<td align="left"><p>Front buffer for master</p></td>
</tr>
<tr class="even">
<td align="left"><p>1</p></td>
<td align="left"></td>
<td align="left"><p>Back buffer for master</p></td>
</tr>
<tr class="odd">
<td align="left"><p>2</p></td>
<td align="left"></td>
<td align="left"><p>Depth buffer for master</p></td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left"><p>3</p></td>
<td align="left"><p>Front buffer for subordinate</p></td>
</tr>
<tr class="odd">
<td align="left"></td>
<td align="left"><p>4</p></td>
<td align="left"><p>Back buffer for subordinate</p></td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left"><p>5</p></td>
<td align="left"><p>Depth buffer for subordinate</p></td>
</tr>
<tr class="odd">
<td align="left"><p>6</p></td>
<td align="left"></td>
<td align="left"><p>Texture 1 for master</p></td>
</tr>
<tr class="even">
<td align="left"><p>7</p></td>
<td align="left"></td>
<td align="left"><p>Texture 2 for master</p></td>
</tr>
<tr class="odd">
<td align="left"><p>8</p></td>
<td align="left"></td>
<td align="left"><p>Texture 3 for master</p></td>
</tr>
</tbody>
</table>

 

 

 





