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
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Drawing%20Monochrome%20Pointers%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




