---
title: DVD 4 3 Pan-Scan Within 16 9 Pictures Example
description: DVD 4 3 Pan-Scan Within 16 9 Pictures Example
ms.assetid: f00489e7-809d-4a5b-87c8-b2421bd6ca93
keywords:
- alpha-blend combination WDK DirectX VA , DVD 4 3 pan-scan example
- blended pictures WDK DirectX VA , DVD 4 3 pan-scan example
- DVD 4 3 pan-scan example WDK DirectX VA
- 4 3 pan-scan example WDK DirectX VA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# DVD 4:3 Pan-Scan Within 16:9 Pictures Example


## <span id="ddk_dvd_4_3_pan_scan_within_16_9_pictures_example_gg"></span><span id="DDK_DVD_4_3_PAN_SCAN_WITHIN_16_9_PICTURES_EXAMPLE_GG"></span>


In DVD use of MPEG-2 for 4:3 pan-scan within 16:9 pictures, the pan-scan MPEG-2 variables must not violate the restrictions specified in the [**DXVA\_BlendCombination**](https://msdn.microsoft.com/library/windows/hardware/ff563120) structure. These variables must also maintain the following restrictions required by the DVD specification.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">MPEG-2 Variable</th>
<th align="left">Value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><em>horizontal_size</em></p></td>
<td align="left"><p>720 or 704</p></td>
</tr>
<tr class="even">
<td align="left"><p><em>vertical_size</em></p></td>
<td align="left"><p>480 or 576</p></td>
</tr>
<tr class="odd">
<td align="left"><p><em>display_horizontal_size</em></p></td>
<td align="left"><p>540</p></td>
</tr>
<tr class="even">
<td align="left"><p><em>display_vertical_size</em></p></td>
<td align="left"><p><em>vertical_size</em></p></td>
</tr>
<tr class="odd">
<td align="left"><p><em>frame_centre_vertical_offset</em></p></td>
<td align="left"><p>Zero</p></td>
</tr>
<tr class="even">
<td align="left"><p><em>frame_centre_horizontal_offset</em></p></td>
<td align="left"><p>Less than or equal to 1440 for <em>horizontal_size</em> = 720</p>
<p>Less than or equal to 1312 for <em>horizontal_size</em> = 704</p></td>
</tr>
</tbody>
</table>

 

The formulation described in [MPEG-2 Pan-Scan Example](mpeg-2-pan-scan-example.md) can then be applied directly in this case.

 

 





