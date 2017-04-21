---
title: Commands for Simulated Fonts
author: windows-driver-content
description: Commands for Simulated Fonts
ms.assetid: 3bfdcf86-35ac-4b95-9efd-31f79a8b9871
keywords:
- simulated font commands WDK Unidrv
- font commands WDK Unidrv
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Commands for Simulated Fonts


## <a href="" id="ddk-commands-for-simulated-fonts-gg"></a>


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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Commands%20for%20Simulated%20Fonts%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


