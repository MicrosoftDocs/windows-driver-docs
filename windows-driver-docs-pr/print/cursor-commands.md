---
title: Cursor Commands
description: Cursor Commands
ms.assetid: 3ef09c7e-0e88-4236-a4c9-d89eb7ec61cb
keywords: ["printer commands WDK Unidrv , cursors", "cursor commands WDK Unidrv"]
---

# Cursor Commands


## <a href="" id="ddk-cursor-commands-gg"></a>


The [printer commands](printer-commands.md) in the following table control cursor movement. All commands are specified using the [command entry format](command-entry-format.md).

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Command</th>
<th align="left">Description</th>
<th align="left">Comments</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>CmdBackSpace</strong></p></td>
<td align="left"><p>Command to move the cursor back over the last printed character.</p></td>
<td align="left"><p>Optional. Used only for overstriking.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>CmdCR</strong></p></td>
<td align="left"><p>Command to move the cursor to its left-most x-position.</p></td>
<td align="left"><p>Required.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>CmdFF</strong></p></td>
<td align="left"><p>Command to eject a page.</p></td>
<td align="left"><p>Required.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>CmdLF</strong></p></td>
<td align="left"><p>Command to move the cursor to the next line.</p></td>
<td align="left"><p>Required. Amount of movement is specified by <strong>CmdSetLineSpacing</strong>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>CmdPopCursor</strong></p></td>
<td align="left"><p>Command to pop the last saved cursor position from the stack.</p></td>
<td align="left"><p>Required if <strong>CmdPushCursor</strong> is specified.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>CmdPushCursor</strong></p></td>
<td align="left"><p>Command to push the current cursor position onto the stack.</p></td>
<td align="left"><p>Optional.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>CmdSetAnyRotation</strong></p></td>
<td align="left"><p>Command to set the rotation to an arbitrary angle (measured in degrees in the counterclockwise direction).</p></td>
<td align="left"><p>Optional. If not present, the printer does not support rotation through arbitrary angles.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>CmdSetLineSpacing</strong></p></td>
<td align="left"><p>Command to set the distance the cursor moves when a <strong>CmdLF</strong> command is issued.</p></td>
<td align="left"><p>Optional.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>CmdSetSimpleRotation</strong></p></td>
<td align="left"><p>Command to set the rotation angle in multiples of 90 degrees in the counterclockwise direction.</p></td>
<td align="left"><p>Optional. If the printer supports rotations through angles of arbitrary sizes, the <strong>CmdSetAnyRotation</strong> command can replace this command.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>CmdUniDirectionOff</strong></p></td>
<td align="left"><p>Command to disable unidirectional printing, thereby enabling bidirectional printing.</p></td>
<td align="left"><p>Optional.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>CmdUniDirectionOn</strong></p></td>
<td align="left"><p>Command to enable unidirectional printing.</p></td>
<td align="left"><p>Optional. If not present, print in bidirectional mode.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>CmdXMoveAbsolute</strong></p></td>
<td align="left"><p>Command to move the cursor to an absolute x-position.</p></td>
<td align="left"><p>Optional. The command string can include only one standard variable, which is used to specify the distance.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>CmdXMoveRelLeft</strong></p></td>
<td align="left"><p>Command to move the cursor to the left from the current x-position, by the specified amount.</p></td>
<td align="left"><p>Optional. The command string can include only one standard variable, which is used to specify the distance.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>CmdXMoveRelRight</strong></p></td>
<td align="left"><p>Command to move the cursor to the right from the current x-position, by the specified amount.</p></td>
<td align="left"><p>Optional. The command string can include only one standard variable, which is used to specify the distance.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>CmdYMoveAbsolute</strong></p></td>
<td align="left"><p>Command to move the cursor to an absolute y-position.</p></td>
<td align="left"><p>Optional. The command string can include only one standard variable, which is used to specify the distance.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>CmdYMoveRelDown</strong></p></td>
<td align="left"><p>Command to move the cursor down from the current y-position, by the specified amount.</p></td>
<td align="left"><p>Optional. The command string can include only one standard variable, which is used to specify the distance.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>CmdYMoveRelUp</strong></p></td>
<td align="left"><p>Command to move the cursor up from the current y-position, by the specified amount.</p></td>
<td align="left"><p>Optional. The command string can include only one standard variable, which is used to specify the distance.</p></td>
</tr>
</tbody>
</table>

 

For examples, see the [sample GPD files](sample-gpd-files.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Cursor%20Commands%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




