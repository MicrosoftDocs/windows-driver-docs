---
title: Example of Handle Assignments
description: Example of Handle Assignments
ms.assetid: 44239e13-ebe7-48c4-83b2-40f603dc1c98
keywords:
- multiple-head hardware WDK DirectX 9.0 , handle assignments
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Example%20of%20Handle%20Assignments%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




