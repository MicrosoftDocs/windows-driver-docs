---
title: Rectangle Area Fill Attributes
description: Rectangle Area Fill Attributes
ms.assetid: 287e8805-4aec-490b-88da-00576a2f4fbf
keywords:
- rectangular area fill attibutes WDK Unidrv
- filling rectangular areas WDK Unidrv
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Rectangle Area Fill Attributes





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
<td><p><em><strong>CursorXAfterRectFill</strong></p></td>
<td><p>AT_RECT_X_ORIGIN or AT_RECT_X_END, indicating where the cursor&#39;s x-coordinate is after the printer fills a rectangle area.</p></td>
<td><p>Optional. If not specified, the default value is AT_RECT_X_ORIGIN.</p></td>
</tr>
<tr class="even">
<td><p></em><strong>CursorYAfterRectFill</strong></p></td>
<td><p>AT_RECT_Y_ORIGIN or AT_RECT_Y_END, indicating where the cursor&#39;s y-coordinate is after the printer fills a rectangle area.</p></td>
<td><p>Optional. If not specified, the default value is AT_RECT_Y_ORIGIN.</p></td>
</tr>
<tr class="odd">
<td><p><em><strong>MaxGrayFill</strong></p></td>
<td><p>Numeric value representing the maximum gray fill percentage allowed as an argument to the CmdRectGrayFill command.</p></td>
<td><p>Optional. If not specified, the default value is 100 (percent).</p></td>
</tr>
<tr class="even">
<td><p></em><strong>MinGrayFill</strong></p></td>
<td><p>Numeric value representing the minimum gray fill percentage allowed as an argument to the CmdRectGrayFill command.</p></td>
<td><p>Optional. If not specified, the default value is 1 (percent).</p></td>
</tr>
</tbody>
</table>

 

For information about commands associated with a printer's rectangle area fill capabilities, see [Rectangle Area Fill Commands](rectangle-area-fill-commands.md).

For examples, see the [sample GPD files](sample-gpd-files.md).

 

 




