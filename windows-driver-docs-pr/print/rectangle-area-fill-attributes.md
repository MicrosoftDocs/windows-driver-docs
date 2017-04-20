---
title: Rectangle Area Fill Attributes
author: windows-driver-content
description: Rectangle Area Fill Attributes
ms.assetid: 287e8805-4aec-490b-88da-00576a2f4fbf
keywords:
- rectangular area fill attibutes WDK Unidrv
- filling rectangular areas WDK Unidrv
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Rectangle Area Fill Attributes


## <a href="" id="ddk-rectangle-area-fill-attributes-gg"></a>


The following table lists attributes describing the printer's support for filling rectangle areas.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Attribute Name</th>
<th>Attribute Parameter</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>*<strong>CursorXAfterRectFill</strong></p></td>
<td><p>AT_RECT_X_ORIGIN or AT_RECT_X_END, indicating where the cursor's x-coordinate is after the printer fills a rectangle area.</p></td>
<td><p>Optional. If not specified, the default value is AT_RECT_X_ORIGIN.</p></td>
</tr>
<tr class="even">
<td><p>*<strong>CursorYAfterRectFill</strong></p></td>
<td><p>AT_RECT_Y_ORIGIN or AT_RECT_Y_END, indicating where the cursor's y-coordinate is after the printer fills a rectangle area.</p></td>
<td><p>Optional. If not specified, the default value is AT_RECT_Y_ORIGIN.</p></td>
</tr>
<tr class="odd">
<td><p>*<strong>MaxGrayFill</strong></p></td>
<td><p>Numeric value representing the maximum gray fill percentage allowed as an argument to the CmdRectGrayFill command.</p></td>
<td><p>Optional. If not specified, the default value is 100 (percent).</p></td>
</tr>
<tr class="even">
<td><p>*<strong>MinGrayFill</strong></p></td>
<td><p>Numeric value representing the minimum gray fill percentage allowed as an argument to the CmdRectGrayFill command.</p></td>
<td><p>Optional. If not specified, the default value is 1 (percent).</p></td>
</tr>
</tbody>
</table>

 

For information about commands associated with a printer's rectangle area fill capabilities, see [Rectangle Area Fill Commands](rectangle-area-fill-commands.md).

For examples, see the [sample GPD files](sample-gpd-files.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Rectangle%20Area%20Fill%20Attributes%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


