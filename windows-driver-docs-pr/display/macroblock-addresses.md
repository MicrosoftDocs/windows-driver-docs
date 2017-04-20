---
title: Macroblock Addresses
description: Macroblock Addresses
ms.assetid: f04c5462-db7c-4917-b8ef-22a630c82994
keywords:
- macroblocks WDK DirectX VA , addresses
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Macroblock%20Addresses%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




