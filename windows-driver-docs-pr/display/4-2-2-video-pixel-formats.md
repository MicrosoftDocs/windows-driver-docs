---
title: 4 2 2 Video Pixel Formats
description: 4 2 2 Video Pixel Formats
ms.assetid: 7064c7bd-bc7d-4b71-8876-ccb3a5808e45
keywords: ["uncompressed video pixel formats WDK DirectX VA", "pixel formats for uncompressed video WDK DirectX VA", "compressed picture decoding WDK DirectX VA , pixel formats for uncompressed video", "picture decoding WDK DirectX VA , compressed", "4 2 2 video WDK DirectX VA"]
---

# 4:2:2 Video Pixel Formats


## <span id="ddk_4_2_2_video_pixel_formats_gg"></span><span id="DDK_4_2_2_VIDEO_PIXEL_FORMATS_GG"></span>


To decode compressed 4:2:2 video, use one of the following uncompressed pixel formats.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Pixel Format</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>YUY2</p></td>
<td align="left"><p>Data is found in memory as an array of unsigned characters in which the first byte contains the first sample of Y, the second byte contains the first sample of Cb, the third byte contains the second sample of Y, the fourth byte contains the first sample of Cr; and so on. If data is addressed as an array of two little-endian WORD type variables, the first WORD contains Y₀ in the least significant bits and Cb in the most significant bits, and the second WORD contains Y₁ in the least significant bits and Cr in the most significant bits. YUY2 is the preferred DirectX VA 4:2:2 pixel format.</p></td>
</tr>
<tr class="even">
<td align="left"><p>UYVY</p></td>
<td align="left"><p>The same as YUY2, except for swapping the byte order in each WORD. If data is addressed as an array of two little-endian WORD type variables, the first WORD contains Cb in the least significant bits and Y₀ in the most significant bits, and the second WORD contains Cr in the least significant bits and Y₁ in the most significant bits.</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%204:2:2%20Video%20Pixel%20Formats%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




