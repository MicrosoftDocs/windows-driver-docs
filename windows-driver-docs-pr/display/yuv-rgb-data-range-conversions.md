---
title: YUV-RGB data range conversions
ms.assetid: 0A439686-0BAE-4E4D-AA23-06A6EF72C4B3
description: Effect of input data range on expected video conversion behavior
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 





