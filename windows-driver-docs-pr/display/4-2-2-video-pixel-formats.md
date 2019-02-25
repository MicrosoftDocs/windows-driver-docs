---
title: 4 2 2 Video Pixel Formats
description: 4 2 2 Video Pixel Formats
ms.assetid: 7064c7bd-bc7d-4b71-8876-ccb3a5808e45
keywords:
- uncompressed video pixel formats WDK DirectX VA
- pixel formats for uncompressed video WDK DirectX VA
- compressed picture decoding WDK DirectX VA , pixel formats for uncompressed video
- picture decoding WDK DirectX VA , compressed
- 4 2 2 video WDK DirectX VA
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 

 





