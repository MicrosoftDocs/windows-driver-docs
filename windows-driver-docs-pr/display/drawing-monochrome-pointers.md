---
title: Drawing Monochrome Pointers
description: Drawing Monochrome Pointers
ms.assetid: b3e436d2-b804-42fb-89ca-ecf66dcb584e
keywords:
- drawing pointers WDK Windows 2000 display
- display drivers WDK Windows 2000 , pointers
- pointers WDK Windows 2000 display
- monochrome pointers WDK Windows 2000 display
- black-and-white pointers WDK Windows 2000 display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Drawing Monochrome Pointers


## <span id="ddk_drawing_monochrome_pointers_gg"></span><span id="DDK_DRAWING_MONOCHROME_POINTERS_GG"></span>


A monochrome bitmap consists of two parts: the first defines the AND mask for the pointer; the second defines the XOR mask. Together these masks provide two bits of information for each pixel of the pointer image. The following table describes the result that is displayed for the indicated values in the AND and XOR masks.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">AND mask value</th>
<th align="left">XOR mask value</th>
<th align="left">Result displayed</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>Pixel is black</p></td>
</tr>
<tr class="even">
<td align="left"><p>0</p></td>
<td align="left"><p>1</p></td>
<td align="left"><p>Pixel is white</p></td>
</tr>
<tr class="odd">
<td align="left"><p>1</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>Pixel is unchanged (transparent)</p></td>
</tr>
<tr class="even">
<td align="left"><p>1</p></td>
<td align="left"><p>1</p></td>
<td align="left"><p>Pixel color is inverted</p></td>
</tr>
</tbody>
</table>

 

This bitmap definition and usage supplies a black-and-white image, while providing support for transparency and inversion of the pixels that make up the pointer.

 

 





