---
title: Commands for Downloaded Fonts
author: windows-driver-content
description: Commands for Downloaded Fonts
ms.assetid: 5cf6b2bd-5378-4e90-8959-ced978dee02f
keywords:
- downloaded font commands WDK Unidrv
- font commands WDK Unidrv
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Commands for Downloaded Fonts


## <a href="" id="ddk-commands-for-downloaded-fonts-gg"></a>


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
<td><p>Optional. Specify this command only if a deleted font's allocated memory can be immediately reclaimed.</p></td>
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Commands%20for%20Downloaded%20Fonts%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


