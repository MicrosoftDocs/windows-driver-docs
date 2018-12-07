---
title: Commands for Simulated Fonts
description: Commands for Simulated Fonts
ms.assetid: 3bfdcf86-35ac-4b95-9efd-31f79a8b9871
keywords:
- simulated font commands WDK Unidrv
- font commands WDK Unidrv
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Commands for Simulated Fonts





The following table lists the commands for controlling simulated fonts. All commands are specified using the [command entry format](command-entry-format.md).

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
<td><p><strong>CmdBoldOff</strong></p></td>
<td><p>Command to disable bolding.</p></td>
<td><p>Optional. Must be specified if <strong>CmdBoldOn</strong> is specified.</p></td>
</tr>
<tr class="even">
<td><p><strong>CmdBoldOn</strong></p></td>
<td><p>Command to enable bolding.</p></td>
<td><p>Optional. If specified, Unidrv sends this command to enable bolding and sends <strong>CmdBoldOff</strong> to disable bolding.</p></td>
</tr>
<tr class="odd">
<td><p><strong>CmdClearAllFontAttribs</strong></p></td>
<td><p>Single command to disable bold, italic, and underline capabilities.</p></td>
<td><p>Optional. Can be specified if the printer supports bold, italic, or underlining, but supports only a single command to disable them all. Use instead of <strong>CmdBoldOff</strong>, <strong>CmdItalicOff</strong> and <strong>CmdUnderlineOff</strong>.</p></td>
</tr>
<tr class="even">
<td><p><strong>CmdItalicOff</strong></p></td>
<td><p>Command to disable italics.</p></td>
<td><p>Optional. Must be specified if <strong>CmdItalicOn</strong> is specified.</p></td>
</tr>
<tr class="odd">
<td><p><strong>CmdItalicOn</strong></p></td>
<td><p>Command to enable italics.</p></td>
<td><p>Optional. If specified, Unidrv sends this command to enable italics and sends <strong>CmdItalicOff</strong> to disable italics.</p></td>
</tr>
<tr class="even">
<td><p><strong>CmdSelectDoubleByteMode</strong></p></td>
<td><p>Command to enable double-byte printing.</p></td>
<td><p>Optional. Must be specified if <strong>CmdSelectSingleByteMode</strong> is specified.</p></td>
</tr>
<tr class="odd">
<td><p><strong>CmdSelectSingleByteMode</strong></p></td>
<td><p>Command to enable single-byte printing.</p></td>
<td><p>Optional. Must be specified if the printer can be switched between single-byte and double-byte modes.</p></td>
</tr>
<tr class="even">
<td><p><strong>CmdSetFontSim</strong></p></td>
<td><p>Single command to set bold, italic, underline, and strike-through capabilities.</p></td>
<td><p>Optional. Must be specified if font characteristics must be set each time the font is used (for printers that do not store font characteristics).</p></td>
</tr>
<tr class="odd">
<td><p><strong>CmdStrikeThruOff</strong></p></td>
<td><p>Command to disable strike-through.</p></td>
<td><p>Optional. Must be specified if <strong>CmdStrikeThruOn</strong> is specified.</p></td>
</tr>
<tr class="even">
<td><p><strong>CmdStrikeThruOn</strong></p></td>
<td><p>Command to enable strike-through.</p></td>
<td><p>Optional. If specified, Unidrv sends this command to enable strike-through and sends <strong>CmdStrikeThruOff</strong> to disable strike-through.</p></td>
</tr>
<tr class="odd">
<td><p><strong>CmdUnderlineOff</strong></p></td>
<td><p>Command to disable underlining.</p></td>
<td><p>Optional. Must be specified if <strong>CmdUnderlineOn</strong> is specified.</p></td>
</tr>
<tr class="even">
<td><p><strong>CmdUnderlineOn</strong></p></td>
<td><p>Command to enable underlining.</p></td>
<td><p>Optional. If specified, Unidrv sends this command to enable underlining and sends <strong>CmdUnderlineOff</strong> to disable underlining.</p></td>
</tr>
<tr class="odd">
<td><p><strong>CmdVerticalPrintingOff</strong></p></td>
<td><p>Command to disable vertical printing.</p></td>
<td><p>Optional. Must be specified if <strong>CmdVerticalPrintingOn</strong> is specified.</p></td>
</tr>
<tr class="even">
<td><p><strong>CmdVerticalPrintingOn</strong></p></td>
<td><p>Command to enable vertical printing.</p></td>
<td><p>Optional. Must be specified if the printer supports vertical printing.</p></td>
</tr>
<tr class="odd">
<td><p><strong>CmdWhiteTextOff</strong></p></td>
<td><p>Command to disable printing white text.</p></td>
<td><p>Optional. Must be specified if <strong>CmdWhiteTextOn</strong> is specified.</p></td>
</tr>
<tr class="even">
<td><p><strong>CmdWhiteTextOn</strong></p></td>
<td><p>Command to enable printing white text.</p></td>
<td><p>Optional. If specified, Unidrv sends this command to enable printing white text and sends <strong>CmdWhiteTextOff</strong> to disable printing white text. (This command is provided for backwards compatibility with GPC 3.0.)</p></td>
</tr>
</tbody>
</table>

 

For examples, see the [sample GPD files](sample-gpd-files.md).

 

 




