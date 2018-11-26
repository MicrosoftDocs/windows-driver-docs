---
title: Cursor Attributes
description: Cursor Attributes
ms.assetid: 43646e2a-bc40-430e-ac7e-6fe4cb353309
keywords:
- cursor attributes WDK Unidrv
- general printer attributes WDK Unidrv , cursor
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Cursor Attributes





Cursor attributes are [general printing attributes](general-printing-attributes.md) that specify characteristics of a printer's cursor.

The following table lists the cursor attributes.

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
<td><p><strong><em>AbsXMovesRightOnly?</strong></p></td>
<td><p><strong>TRUE</strong> or <strong>FALSE</strong>. This parameter is used to specify that a device can accept only absolute move commands that move the current position to the right. If a move to the left of the current position is required, Unidrv first sends a carriage return so that the absolute command that is sent is to the right of the new current position.</p></td>
<td><p>Optional. If not specified, the default value is <strong>FALSE</strong>.</p></td>
</tr>
<tr class="even">
<td><p><strong></em>BadCursorMoveInGrxMode</strong></p></td>
<td><p></p>
<a href="lists.md" data-raw-source="[LIST](lists.md)">LIST</a> of values representing illegal cursor movements in raster graphics mode. Can be one or more of:
X_PORTRAIT
X_LANDSCAPE
Y_PORTRAIT
Y_LANDSCAPE</td>
<td><p>Optional. If not specified, the default is no restrictions. As an example, LIST(X_PORTRAIT) indicates x-direction movement is not allowed for portrait orientation.</p></td>
</tr>
<tr class="odd">
<td><p><strong><em>CursorXAfterCR</strong></p></td>
<td><p></p>
One of: AT_PRINTABLE_X_ORIGIN
AT_CURSOR_X_ORIGIN
<p>Indicates cursor&#39;s x-position after a carriage return.</p></td>
<td><p>Optional. If not specified, the default value is AT_CURSOR_X_ORIGIN, which is the physical zero position.</p></td>
</tr>
<tr class="even">
<td><p><strong></em>EjectPageWithFF?</strong></p></td>
<td><p><strong>TRUE</strong> or <strong>FALSE</strong>. Indicates whether the printer uses form-feed to eject a page.</p></td>
<td><p>Optional. If not specified, the default value is <strong>FALSE</strong>.</p></td>
</tr>
<tr class="odd">
<td><p><strong><em>LineSpacingMoveUnit</strong></p></td>
<td><p>Positive integer value. Specifies the move units for the CmdSetLineSpacing command. Units are expressed in dots per inch. For a printer whose line spacing move unit is 1/60th of an inch, this entry should be 60.</p>
<p>Note that the line spacing move unit must divide evenly into the master Y unit.</p>
<p>The *MaxLineSpacing parameter is still in master units independent of whether *<strong>LineSpacingMoveUnit</strong> is specified.</p></td>
<td><p>Optional. The default value is 1 master unit.</p></td>
</tr>
<tr class="even">
<td><p><strong></em>MaxLineSpacing</strong></p></td>
<td><p>Numeric value representing the maximum line spacing, in y-master units.</p></td>
<td><p>Optional. If not specified, Unidrv assumes there is no maximum value.</p></td>
</tr>
<tr class="odd">
<td><p><strong><em>UseSpaceForXMove?</strong></p></td>
<td><p><strong>TRUE</strong> or <strong>FALSE</strong>. Indicates whether space characters can be used to perform cursor x-direction movements.</p></td>
<td><p>Optional. If not specified, the default value is <strong>TRUE</strong>.</p>
<p>If <strong>TRUE</strong>, Unidrv uses spaces for coarse moves and NULLs for fine moves. If <strong>FALSE</strong>, Unidrv uses NULLs for all moves.</p></td>
</tr>
<tr class="even">
<td><p><strong></em>XMoveThreshold</strong></p></td>
<td><p>Numeric value, in x-master units, representing the movement threshold beyond which <strong>CmdXMoveAbsolute</strong> should be used instead of <strong>CmdXMoveRelLeft</strong> or <strong>CmdXMoveRelRight</strong>.</p></td>
<td><p>Optional. If not specified, the default value is zero, meaning <strong>CmdXMoveAbsolute</strong> should always be used. Only applicable if all three x-movement commands are specified.</p></td>
</tr>
<tr class="odd">
<td><p><strong><em>XMoveUnit</strong></p></td>
<td><p>Numeric value, in dots per inch, representing the smallest horizontal movement the printer is capable of. For example, if the movement unit is 1/600th of an inch, the specified value is 600.</p></td>
<td><p>Required if the printer supports horizontal movement <a href="cursor-commands.md" data-raw-source="[cursor commands](cursor-commands.md)">cursor commands</a>. (If specified, include this value when calculating <a href="master-units.md" data-raw-source="[master units](master-units.md)">master units</a>.)</p></td>
</tr>
<tr class="even">
<td><p><strong></em>YMoveAttributes</strong></p></td>
<td><p></p>
LIST of values indicating y-movement attributes. Can be one or more of:
FAV_LF (favor LF spacing)
SEND_CR_FIRST</td>
<td><p>Optional. If not specified, no attributes are assumed.</p></td>
</tr>
<tr class="odd">
<td><p><strong><em>YMoveThreshold</strong></p></td>
<td><p>Numeric value, in y-master units, representing the movement threshold beyond which <strong>CmdYMoveAbsolute</strong> should be used instead of <strong>CmdYMoveRelLeft</strong> or <strong>CmdYMoveRelRight</strong>.</p></td>
<td><p>Optional. If not specified, the default value is zero, meaning <strong>CmdYMoveAbsolute</strong> should always be used. Only applicable if all three y-movement commands are specified.</p></td>
</tr>
<tr class="even">
<td><p><strong></em>YMoveUnit</strong></p></td>
<td><p>Numeric value, in dots per inch, representing the smallest vertical movement the printer is capable of. For example, if the movement unit is 1/600th of an inch, the specified value is 600.</p></td>
<td><p>Required if the printer supports vertical movement <a href="cursor-commands.md" data-raw-source="[cursor commands](cursor-commands.md)">cursor commands</a>. (If specified, include this value when calculating <a href="master-units.md" data-raw-source="[master units](master-units.md)">master units</a>.)</p></td>
</tr>
</tbody>
</table>

 

For examples, see the [sample GPD files](sample-gpd-files.md).

 

 




