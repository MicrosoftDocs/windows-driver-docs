---
title: YUV-RGB data range conversions
ms.assetid: 0A439686-0BAE-4E4D-AA23-06A6EF72C4B3
description: 
---

# <span id="display.yuv-rgb_data_range_conversions"></span>YUV-RGB data range conversions


If you want to convert from RGB or YUV inputs to YUV or RGB outputs, the expected behavior depends on the input data range:

<table>
<colgroup>
<col width="11%" />
<col width="11%" />
<col width="11%" />
<col width="11%" />
<col width="11%" />
<col width="11%" />
<col width="11%" />
<col width="11%" />
<col width="11%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Input</th>
<th align="left">Input</th>
<th align="left">Input</th>
<th align="left">Input</th>
<th align="left">Output</th>
<th align="left">Output</th>
<th align="left">Output</th>
<th align="left">Output</th>
<th align="left">Operation</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">data</td>
<td align="left">format</td>
<td align="left">RGB</td>
<td align="left">nominal</td>
<td align="left">RGB</td>
<td align="left">nominal</td>
<td align="left">format</td>
<td align="left">data</td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left">range</td>
<td align="left"></td>
<td align="left">range</td>
<td align="left">range</td>
<td align="left">range</td>
<td align="left">range</td>
<td align="left"></td>
<td align="left">range</td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left">0-255</td>
<td align="left">YUV</td>
<td align="left">N/A</td>
<td align="left">2</td>
<td align="left">N/A</td>
<td align="left">2</td>
<td align="left">YUV</td>
<td align="left">0-255</td>
<td align="left">None</td>
</tr>
<tr class="even">
<td align="left">16-235</td>
<td align="left">YUV</td>
<td align="left">N/A</td>
<td align="left">1</td>
<td align="left">N/A</td>
<td align="left">1</td>
<td align="left">YUV</td>
<td align="left">16-235</td>
<td align="left">None</td>
</tr>
<tr class="odd">
<td align="left">16-235</td>
<td align="left">YUV</td>
<td align="left">N/A</td>
<td align="left">1</td>
<td align="left">N/A</td>
<td align="left">2</td>
<td align="left">YUV</td>
<td align="left">0-255</td>
<td align="left">Scale</td>
</tr>
<tr class="even">
<td align="left">0-255</td>
<td align="left">YUV</td>
<td align="left">N/A</td>
<td align="left">2</td>
<td align="left">N/A</td>
<td align="left">1</td>
<td align="left">YUV</td>
<td align="left">16-235</td>
<td align="left">Scale</td>
</tr>
<tr class="odd">
<td align="left">0-255</td>
<td align="left">RGB</td>
<td align="left">0</td>
<td align="left">N/A</td>
<td align="left">N/A</td>
<td align="left">1</td>
<td align="left">YUV</td>
<td align="left">16-235</td>
<td align="left">RGBtoYUV</td>
</tr>
<tr class="even">
<td align="left">0-255</td>
<td align="left">RGB</td>
<td align="left">0</td>
<td align="left">N/A</td>
<td align="left">N/A</td>
<td align="left">2</td>
<td align="left">YUV</td>
<td align="left">0-255</td>
<td align="left">RGBtoYUV</td>
</tr>
<tr class="odd">
<td align="left">16-235</td>
<td align="left">YUV</td>
<td align="left">N/A</td>
<td align="left">1</td>
<td align="left">0</td>
<td align="left">N/A</td>
<td align="left">RGB</td>
<td align="left">0-255</td>
<td align="left">YUVtoRGB</td>
</tr>
<tr class="even">
<td align="left">0-255</td>
<td align="left">YUV</td>
<td align="left">N/A</td>
<td align="left">2</td>
<td align="left">0</td>
<td align="left">N/A</td>
<td align="left">RGB</td>
<td align="left">0-255</td>
<td align="left">YUVtoRGB</td>
</tr>
</tbody>
</table>

 

In this case the "nominal range" is the constant value from the [**DXVAHDDDI\_NOMINAL\_RANGE**](https://msdn.microsoft.com/library/windows/hardware/dn265432) enumeration.

See [YUV format ranges in Windows 8.1](yuv-format-ranges.md) for definitions of YUV format ranges.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20YUV-RGB%20data%20range%20conversions%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




