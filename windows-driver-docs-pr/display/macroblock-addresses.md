---
title: Macroblock Addresses
description: Macroblock Addresses
ms.assetid: f04c5462-db7c-4917-b8ef-22a630c82994
keywords:
- macroblocks WDK DirectX VA , addresses
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Macroblock Addresses


## <span id="ddk_macroblock_addresses_gg"></span><span id="DDK_MACROBLOCK_ADDRESSES_GG"></span>


A macroblock address is the position of the macroblock in raster-scan order within the picture. The horizontal and vertical position of the macroblock in the picture is determined from the macroblock address using the specified width and height of the picture, which is defined by the **wPicWidthInMBminus1** and **wPicHeightInMBminus1** members of the [**DXVA\_PictureParameters**](https://msdn.microsoft.com/library/windows/hardware/ff564012) structure. Following are some examples of macroblock addresses.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Macroblock</th>
<th align="left">Address</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>top-left</p></td>
<td align="left"><p>Zero</p></td>
</tr>
<tr class="even">
<td align="left"><p>top-right</p></td>
<td align="left"><p><strong>wPicWidthInMBminus1</strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p>lower-left</p></td>
<td align="left"><p><strong>wPicHeightInMBminus1</strong> x (<strong>wPicWidthInMBminus1</strong> + 1)</p></td>
</tr>
<tr class="even">
<td align="left"><p>lower-right</p></td>
<td align="left"><p>(<strong>wPicHeightInMBminus1</strong> + 1) x (<strong>wPicWidthInMBminus1</strong> + 1) - 1</p></td>
</tr>
</tbody>
</table>

 

 

 





