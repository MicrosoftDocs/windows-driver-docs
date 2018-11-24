---
title: Deinterlace Modes
description: Deinterlace Modes
ms.assetid: 0418ab48-94f3-4914-b07a-ed22dc893544
keywords:
- deinterlacing WDK DirectX VA , modes
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Deinterlace Modes


## <span id="ddk_deinterlace_modes_gg"></span><span id="DDK_DEINTERLACE_MODES_GG"></span>


Following are examples of the deinterlace modes that can be supported by the DDI.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Mode</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><a href="bob-deinterlacing.md" data-raw-source="[Bob](bob-deinterlacing.md)">Bob</a> (line doubling)</p></td>
<td align="left"><p>This mode uses a bit-block transfer (blt). This mode should always be available.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Simple Switching Adaptive</p></td>
<td align="left"><p>Either a blend of two adjacent fields if low motion is detected for that field, or bobbing if high motion is detected.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Motion Vector Steered</p></td>
<td align="left"><p>Motion vectors of the different objects in the surface are used to align individual movements to the time axis before interpolation takes place.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Advanced 3D Adaptive</p></td>
<td align="left"><p>The missing lines are generated through some adaptive process that is proprietary to the hardware. The process may use several reference samples to aid generation of the missing lines. The reference samples may be in the past or future. Three-dimensional linear filtering falls into this category.</p></td>
</tr>
</tbody>
</table>

 

 

 





