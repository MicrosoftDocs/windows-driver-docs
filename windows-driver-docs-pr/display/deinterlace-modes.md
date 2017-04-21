---
title: Deinterlace Modes
description: Deinterlace Modes
ms.assetid: 0418ab48-94f3-4914-b07a-ed22dc893544
keywords:
- deinterlacing WDK DirectX VA , modes
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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
<td align="left"><p>[Bob](bob-deinterlacing.md) (line doubling)</p></td>
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

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Deinterlace%20Modes%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




