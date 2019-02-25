---
title: Frame-Rate Conversion Modes
description: Frame-Rate Conversion Modes
ms.assetid: cbb609b5-6021-4f47-855d-24882533a7a0
keywords:
- frame-rate conversion WDK DirectX VA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Frame-Rate Conversion Modes


## <span id="ddk_frame_rate_conversion_modes_gg"></span><span id="DDK_FRAME_RATE_CONVERSION_MODES_GG"></span>


Following are examples of the frame-rate conversion modes that can be supported by the DDI.

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
<td align="left"><p>Frame Repeat/Drop</p></td>
<td align="left"><p>This is not a recommended mode, because it uses extra memory by copying the selected source sample into the destination surface.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Linear Temporal Interpolation</p></td>
<td align="left"><p>A future and a previous reference field are alpha blended together to produce a new frame.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Motion Vector Steered</p></td>
<td align="left"><p>Motion vectors of the different objects in a scene are used to align individual movements to the time axis before interpolation takes place.</p></td>
</tr>
</tbody>
</table>

 

 

 





