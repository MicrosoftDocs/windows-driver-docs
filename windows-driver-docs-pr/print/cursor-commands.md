---
title: Cursor Commands
description: Cursor Commands
ms.assetid: 3ef09c7e-0e88-4236-a4c9-d89eb7ec61cb
keywords:
- printer commands WDK Unidrv , cursors
- cursor commands WDK Unidrv
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Cursor Commands





The [printer commands](printer-commands.md) in the following table control cursor movement. All commands are specified using the [command entry format](command-entry-format.md).

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
<td><p><strong>CmdBackSpace</strong></p></td>
<td><p>Command to move the cursor back over the last printed character.</p></td>
<td><p>Optional. Used only for overstriking.</p></td>
</tr>
<tr class="even">
<td><p><strong>CmdCR</strong></p></td>
<td><p>Command to move the cursor to its left-most x-position.</p></td>
<td><p>Required.</p></td>
</tr>
<tr class="odd">
<td><p><strong>CmdFF</strong></p></td>
<td><p>Command to eject a page.</p></td>
<td><p>Required.</p></td>
</tr>
<tr class="even">
<td><p><strong>CmdLF</strong></p></td>
<td><p>Command to move the cursor to the next line.</p></td>
<td><p>Required. Amount of movement is specified by <strong>CmdSetLineSpacing</strong>.</p></td>
</tr>
<tr class="odd">
<td><p><strong>CmdPopCursor</strong></p></td>
<td><p>Command to pop the last saved cursor position from the stack.</p></td>
<td><p>Required if <strong>CmdPushCursor</strong> is specified.</p></td>
</tr>
<tr class="even">
<td><p><strong>CmdPushCursor</strong></p></td>
<td><p>Command to push the current cursor position onto the stack.</p></td>
<td><p>Optional.</p></td>
</tr>
<tr class="odd">
<td><p><strong>CmdSetAnyRotation</strong></p></td>
<td><p>Command to set the rotation to an arbitrary angle (measured in degrees in the counterclockwise direction).</p></td>
<td><p>Optional. If not present, the printer does not support rotation through arbitrary angles.</p></td>
</tr>
<tr class="even">
<td><p><strong>CmdSetLineSpacing</strong></p></td>
<td><p>Command to set the distance the cursor moves when a <strong>CmdLF</strong> command is issued.</p></td>
<td><p>Optional.</p></td>
</tr>
<tr class="odd">
<td><p><strong>CmdSetSimpleRotation</strong></p></td>
<td><p>Command to set the rotation angle in multiples of 90 degrees in the counterclockwise direction.</p></td>
<td><p>Optional. If the printer supports rotations through angles of arbitrary sizes, the <strong>CmdSetAnyRotation</strong> command can replace this command.</p></td>
</tr>
<tr class="even">
<td><p><strong>CmdUniDirectionOff</strong></p></td>
<td><p>Command to disable unidirectional printing, thereby enabling bidirectional printing.</p></td>
<td><p>Optional.</p></td>
</tr>
<tr class="odd">
<td><p><strong>CmdUniDirectionOn</strong></p></td>
<td><p>Command to enable unidirectional printing.</p></td>
<td><p>Optional. If not present, print in bidirectional mode.</p></td>
</tr>
<tr class="even">
<td><p><strong>CmdXMoveAbsolute</strong></p></td>
<td><p>Command to move the cursor to an absolute x-position.</p></td>
<td><p>Optional. The command string can include only one standard variable, which is used to specify the distance.</p></td>
</tr>
<tr class="odd">
<td><p><strong>CmdXMoveRelLeft</strong></p></td>
<td><p>Command to move the cursor to the left from the current x-position, by the specified amount.</p></td>
<td><p>Optional. The command string can include only one standard variable, which is used to specify the distance.</p></td>
</tr>
<tr class="even">
<td><p><strong>CmdXMoveRelRight</strong></p></td>
<td><p>Command to move the cursor to the right from the current x-position, by the specified amount.</p></td>
<td><p>Optional. The command string can include only one standard variable, which is used to specify the distance.</p></td>
</tr>
<tr class="odd">
<td><p><strong>CmdYMoveAbsolute</strong></p></td>
<td><p>Command to move the cursor to an absolute y-position.</p></td>
<td><p>Optional. The command string can include only one standard variable, which is used to specify the distance.</p></td>
</tr>
<tr class="even">
<td><p><strong>CmdYMoveRelDown</strong></p></td>
<td><p>Command to move the cursor down from the current y-position, by the specified amount.</p></td>
<td><p>Optional. The command string can include only one standard variable, which is used to specify the distance.</p></td>
</tr>
<tr class="odd">
<td><p><strong>CmdYMoveRelUp</strong></p></td>
<td><p>Command to move the cursor up from the current y-position, by the specified amount.</p></td>
<td><p>Optional. The command string can include only one standard variable, which is used to specify the distance.</p></td>
</tr>
</tbody>
</table>

 

For examples, see the [sample GPD files](sample-gpd-files.md).

 

 




