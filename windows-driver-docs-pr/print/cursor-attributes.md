---
title: Cursor Attributes
author: windows-driver-content
description: Cursor Attributes
ms.assetid: 43646e2a-bc40-430e-ac7e-6fe4cb353309
keywords:
- cursor attributes WDK Unidrv
- general printer attributes WDK Unidrv , cursor
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Cursor Attributes


## <a href="" id="ddk-cursor-attributes-gg"></a>


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
<td><p><strong>*AbsXMovesRightOnly?</strong></p></td>
<td><p><strong>TRUE</strong> or <strong>FALSE</strong>. This parameter is used to specify that a device can accept only absolute move commands that move the current position to the right. If a move to the left of the current position is required, Unidrv first sends a carriage return so that the absolute command that is sent is to the right of the new current position.</p></td>
<td><p>Optional. If not specified, the default value is <strong>FALSE</strong>.</p></td>
</tr>
<tr class="even">
<td><p><strong>*BadCursorMoveInGrxMode</strong></p></td>
<td><p></p>
[LIST](lists.md) of values representing illegal cursor movements in raster graphics mode. Can be one or more of:
X_PORTRAIT
X_LANDSCAPE
Y_PORTRAIT
Y_LANDSCAPE</td>
<td><p>Optional. If not specified, the default is no restrictions. As an example, LIST(X_PORTRAIT) indicates x-direction movement is not allowed for portrait orientation.</p></td>
</tr>
<tr class="odd">
<td><p><strong>*CursorXAfterCR</strong></p></td>
<td><p></p>
One of: AT_PRINTABLE_X_ORIGIN
AT_CURSOR_X_ORIGIN
<p>Indicates cursor's x-position after a carriage return.</p></td>
<td><p>Optional. If not specified, the default value is AT_CURSOR_X_ORIGIN, which is the physical zero position.</p></td>
</tr>
<tr class="even">
<td><p><strong>*EjectPageWithFF?</strong></p></td>
<td><p><strong>TRUE</strong> or <strong>FALSE</strong>. Indicates whether the printer uses form-feed to eject a page.</p></td>
<td><p>Optional. If not specified, the default value is <strong>FALSE</strong>.</p></td>
</tr>
<tr class="odd">
<td><p><strong>*LineSpacingMoveUnit</strong></p></td>
<td><p>Positive integer value. Specifies the move units for the CmdSetLineSpacing command. Units are expressed in dots per inch. For a printer whose line spacing move unit is 1/60th of an inch, this entry should be 60.</p>
<p>Note that the line spacing move unit must divide evenly into the master Y unit.</p>
<p>The *MaxLineSpacing parameter is still in master units independent of whether *<strong>LineSpacingMoveUnit</strong> is specified.</p></td>
<td><p>Optional. The default value is 1 master unit.</p></td>
</tr>
<tr class="even">
<td><p><strong>*MaxLineSpacing</strong></p></td>
<td><p>Numeric value representing the maximum line spacing, in y-master units.</p></td>
<td><p>Optional. If not specified, Unidrv assumes there is no maximum value.</p></td>
</tr>
<tr class="odd">
<td><p><strong>*UseSpaceForXMove?</strong></p></td>
<td><p><strong>TRUE</strong> or <strong>FALSE</strong>. Indicates whether space characters can be used to perform cursor x-direction movements.</p></td>
<td><p>Optional. If not specified, the default value is <strong>TRUE</strong>.</p>
<p>If <strong>TRUE</strong>, Unidrv uses spaces for coarse moves and NULLs for fine moves. If <strong>FALSE</strong>, Unidrv uses NULLs for all moves.</p></td>
</tr>
<tr class="even">
<td><p><strong>*XMoveThreshold</strong></p></td>
<td><p>Numeric value, in x-master units, representing the movement threshold beyond which <strong>CmdXMoveAbsolute</strong> should be used instead of <strong>CmdXMoveRelLeft</strong> or <strong>CmdXMoveRelRight</strong>.</p></td>
<td><p>Optional. If not specified, the default value is zero, meaning <strong>CmdXMoveAbsolute</strong> should always be used. Only applicable if all three x-movement commands are specified.</p></td>
</tr>
<tr class="odd">
<td><p><strong>*XMoveUnit</strong></p></td>
<td><p>Numeric value, in dots per inch, representing the smallest horizontal movement the printer is capable of. For example, if the movement unit is 1/600th of an inch, the specified value is 600.</p></td>
<td><p>Required if the printer supports horizontal movement [cursor commands](cursor-commands.md). (If specified, include this value when calculating [master units](master-units.md).)</p></td>
</tr>
<tr class="even">
<td><p><strong>*YMoveAttributes</strong></p></td>
<td><p></p>
LIST of values indicating y-movement attributes. Can be one or more of:
FAV_LF (favor LF spacing)
SEND_CR_FIRST</td>
<td><p>Optional. If not specified, no attributes are assumed.</p></td>
</tr>
<tr class="odd">
<td><p><strong>*YMoveThreshold</strong></p></td>
<td><p>Numeric value, in y-master units, representing the movement threshold beyond which <strong>CmdYMoveAbsolute</strong> should be used instead of <strong>CmdYMoveRelLeft</strong> or <strong>CmdYMoveRelRight</strong>.</p></td>
<td><p>Optional. If not specified, the default value is zero, meaning <strong>CmdYMoveAbsolute</strong> should always be used. Only applicable if all three y-movement commands are specified.</p></td>
</tr>
<tr class="even">
<td><p><strong>*YMoveUnit</strong></p></td>
<td><p>Numeric value, in dots per inch, representing the smallest vertical movement the printer is capable of. For example, if the movement unit is 1/600th of an inch, the specified value is 600.</p></td>
<td><p>Required if the printer supports vertical movement [cursor commands](cursor-commands.md). (If specified, include this value when calculating [master units](master-units.md).)</p></td>
</tr>
</tbody>
</table>

 

For examples, see the [sample GPD files](sample-gpd-files.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Cursor%20Attributes%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


