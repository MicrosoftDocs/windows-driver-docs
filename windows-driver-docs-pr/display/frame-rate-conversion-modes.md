---
title: Frame-Rate Conversion Modes
description: Frame-Rate Conversion Modes
ms.assetid: cbb609b5-6021-4f47-855d-24882533a7a0
keywords: ["frame-rate conversion WDK DirectX VA"]
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

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Frame-Rate%20Conversion%20Modes%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




