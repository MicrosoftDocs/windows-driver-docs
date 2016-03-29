---
title: Color Commands
description: Color Commands
ms.assetid: 752a3c1d-05f1-4f5e-9ef2-e51721ef7cc4
keywords: ["printer commands WDK Unidrv , colors", "color commands WDK Unidrv", "background color options WDK Unidrv", "palettes WDK Unidrv", "patterns WDK Unidrv", "brushes WDK Unidrv"]
---

# Color Commands


## <a href="" id="ddk-color-commands-gg"></a>


This topic describes the color commands for printing, and it contains the following sections:

Commands for Selecting Primary Background Colors

Commands for Controlling Printer Palettes

Commands for Selecting Pattern Brushes

All commands are specified using the [command entry format](command-entry-format.md).

### <a href="" id="ddk-commands-for-selecting-primary-background-colors-gg"></a>Commands for Selecting Primary Background Colors

The [printer commands](printer-commands.md) in the following table are used by printers that do not support programmable color palettes, such as planar color printers (for example, dot matrix printers) and some palette printers (for example, early ink jet printers).

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
<td align="left"><strong>CmdSelectBlackColor</strong></td>
<td align="left"><p>Command to select black background color.</p></td>
<td align="left"><p>Optional.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>CmdSelectBlueColor</strong></td>
<td align="left"><p>Command to select blue background color.</p></td>
<td align="left"><p>Optional.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>CmdSelectCyanColor</strong></td>
<td align="left"><p>Command to select background cyan color.</p></td>
<td align="left"><p>Optional.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>CmdSelectGreenColor</strong></td>
<td align="left"><p>Command to select green background color.</p></td>
<td align="left"><p>Optional.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>CmdSelectMagentaColor</strong></td>
<td align="left"><p>Command to select magenta background color.</p></td>
<td align="left"><p>Optional.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>CmdSelectRedColor</strong></p></td>
<td align="left"><p>Command to select red background color.</p></td>
<td align="left"><p>Optional.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>CmdSelectYellowColor</strong></p></td>
<td align="left"><p>Command to select yellow background color.</p></td>
<td align="left"><p>Optional.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>CmdSelectWhiteColor</strong></p></td>
<td align="left"><p>Command to select background white color.</p></td>
<td align="left"><p>Optional.</p></td>
</tr>
</tbody>
</table>

 

For examples, see the [sample GPD files](sample-gpd-files.md).

### <a href="" id="ddk-commands-for-controlling-printer-palettes-gg"></a>Commands for Controlling Printer Palettes

The [printer commands](printer-commands.md) in the following table are used by printers that support programmable palettes for both foreground (text and vector) printing and for raster printing.

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
<td align="left"><p><strong>CmdBeginPaletteDef</strong></p></td>
<td align="left"><p>Command to initialize a color palette definition.</p></td>
<td align="left"><p>Optional. If not specified, no initialization of palette definitions is needed.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>CmdEndPaletteDef</strong></p></td>
<td align="left"><p>Command to end a palette definition.</p></td>
<td align="left"><p>Optional. If not specified, no command is required to end a palette definition.</p>
<p>The *Order attribute can be specified. If it is not, the <strong>*Order</strong> attribute associated with the most recently executed [option selection command](option-selection-command.md) for the ColorMode feature is used.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>CmdBeginPaletteReDef</strong></p></td>
<td align="left"><p>Command to initialize a color palette redefinition.</p></td>
<td align="left"><p>Optional. If not specified, no initialization of palette redefinitions is needed.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>CmdEndPaletteReDef</strong></p></td>
<td align="left"><p>Command to end a palette redefinition.</p></td>
<td align="left"><p>Optional. If not specified, no command is required to end a palette redefinition.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>CmdDefinePaletteEntry</strong></p></td>
<td align="left"><p>Command to define a palette entry.</p></td>
<td align="left"><p>Required if the printer supports palettes.</p>
<p>In 24 BPP mode, Unidrv allows palettes for which *PaletteSize is 1. This allows GPD developers to implement a direct RGB color selection command for their devices. To do so, set <strong>*PaletteSize</strong> to 1, and specify the selection color command in the <strong>CmdDefinePaletteEntry</strong> command. The CmdSelectPaletteEntry command must also be specified but can be defined as a <strong>NULL</strong> command.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>CmdRedefinePaletteEntry</strong></p></td>
<td align="left"><p>Command to redefine a palette entry.</p></td>
<td align="left"><p>Optional. If not specified, <strong>CmdDefinePaletteEntry</strong> is used to redefined palette entries.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>CmdSelectPaletteEntry</strong></p></td>
<td align="left"><p>Command to select a palette entry as the current color.</p></td>
<td align="left"><p>Required if the printer supports palettes.</p></td>
</tr>
</tbody>
</table>

 

For examples, see the [sample GPD files](sample-gpd-files.md).

### <a href="" id="ddk-commands-for-selecting-pattern-brushes-gg"></a>Commands for Selecting Pattern Brushes

The [printer commands](printer-commands.md) in the following table are used by printers that support downloading and selecting pattern brushes.

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
<td align="left"><p><strong>CmdDownloadPattern</strong></p></td>
<td align="left"><p>Command to deliver a brush pattern to the printer.</p></td>
<td align="left"><p>Optional. If specified, <strong>CmdSelectPattern</strong> must also be specified.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>CmdSelectBlackBrush</strong></p></td>
<td align="left"><p>Command to a solid black brush as the current brush.</p></td>
<td align="left"><p>Required if the printer supports brushes.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>CmdSelectPattern</strong></p></td>
<td align="left"><p>Command to select a downloaded brush pattern.</p></td>
<td align="left"><p>Optional. If specified, <strong>CmdDownloadPattern</strong> must also be specified.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>CmdSelectWhiteBrush</strong></p></td>
<td align="left"><p>Command to select a solid white brush as the current brush.</p></td>
<td align="left"><p>Optional.</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Color%20Commands%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




