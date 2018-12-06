---
title: Commands for Downloaded Fonts
description: Commands for Downloaded Fonts
ms.assetid: 5cf6b2bd-5378-4e90-8959-ced978dee02f
keywords:
- downloaded font commands WDK Unidrv
- font commands WDK Unidrv
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Commands for Downloaded Fonts





The following table lists the commands for controlling downloaded fonts. All commands are specified using the [command entry format](command-entry-format.md).

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Command</th>
<th>Description</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>CmdDeleteFont</strong></p></td>
<td><p>Command to delete a soft font by specifying its identifier.</p></td>
<td><p>Optional. Specify this command only if a deleted font&#39;s allocated memory can be immediately reclaimed.</p></td>
</tr>
<tr class="even">
<td><p><strong>CmdDeselectFontID</strong></p></td>
<td><p>Command to deselect the current font ID in order to make the font inactive.</p></td>
<td><p>Optional. If not present, the current font does not need to be deselected when a new font is selected.</p></td>
</tr>
<tr class="odd">
<td><p><strong>CmdSelectFontHeight</strong></p></td>
<td><p>Command to select the height of a downloaded font.</p></td>
<td><p>Optional. If not present, the printer does not support scalable, downloadable True Type outline fonts. This command is needed for HPPCL_OUTLINE format.</p></td>
</tr>
<tr class="even">
<td><p><strong>CmdSelectFontID</strong></p></td>
<td><p>Command to select the current font ID in order to make the font active.</p></td>
<td><p>Required if the printer supports downloaded fonts.</p></td>
</tr>
<tr class="odd">
<td><p><strong>CmdSelectFontWidth</strong></p></td>
<td><p>Command to select the width of a downloaded font.</p></td>
<td><p>Optional. If not present, the width of the downloaded font is scaled proportionally its height.</p></td>
</tr>
<tr class="even">
<td><p><strong>CmdSetCharCode</strong></p></td>
<td><p>Command to specify the character code of the next character to be downloaded or deleted.</p></td>
<td><p>Required if the printer supports downloaded fonts.</p></td>
</tr>
<tr class="odd">
<td><p><strong>CmdSetFontID</strong></p></td>
<td><p>Command to set the current font ID.</p></td>
<td><p>Required if the printer supports downloaded fonts.</p></td>
</tr>
</tbody>
</table>

 

For examples, see the [sample GPD files](sample-gpd-files.md).

 

 




