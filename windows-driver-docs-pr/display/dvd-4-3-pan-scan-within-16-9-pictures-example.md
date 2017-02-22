---
title: DVD 4 3 Pan-Scan Within 16 9 Pictures Example
description: DVD 4 3 Pan-Scan Within 16 9 Pictures Example
ms.assetid: f00489e7-809d-4a5b-87c8-b2421bd6ca93
keywords: ["alpha-blend combination WDK DirectX VA , DVD 4 3 pan-scan example", "blended pictures WDK DirectX VA , DVD 4 3 pan-scan example", "DVD 4 3 pan-scan example WDK DirectX VA", "4 3 pan-scan example WDK DirectX VA"]
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20DVD%204:3%20Pan-Scan%20Within%2016:9%20Pictures%20Example%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




