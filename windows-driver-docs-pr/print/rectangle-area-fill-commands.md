---
title: Rectangle Area Fill Commands
description: Rectangle Area Fill Commands
ms.assetid: b9401126-4173-4187-960a-dc5ce69d3522
keywords: ["rectangular area fill commands WDK Unidrv", "filling rectangular areas WDK Unidrv"]
---

# Rectangle Area Fill Commands


## <a href="" id="ddk-rectangle-area-fill-commands-gg"></a>


The following table lists the rectangle area fill commands. All commands are specified using [command entry format](command-entry-format.md).

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
<td align="left"><p>CmdRectBlackFill</p></td>
<td align="left"><p>Command to black fill a rectangle.</p></td>
<td align="left"><p>Optional. If not specified, Unidrv attempts black fill by specifying the CmdRectGrayFill command with a gray percentage of *MaxGrayFill.</p></td>
</tr>
<tr class="even">
<td align="left"><p>CmdRectGrayFill</p></td>
<td align="left"><p>Command to gray fill a rectangle. (Does not erase the background.)</p></td>
<td align="left"><p>Optional. If not specified, Unidrv assumes no gray fill capability. Command string typically includes the GrayPercentage variable.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>CmdRectWhiteFill</p></td>
<td align="left"><p>Command to white fill a rectangle. (Erases the background.)</p></td>
<td align="left"><p>Optional. If not specified, Unidrv assumes no erasing white fill. In that case, Unidrv returns failure if an application requests white fill, because gray fill cannot erase the background.</p></td>
</tr>
<tr class="even">
<td align="left"><p>CmdSetRectHeight</p></td>
<td align="left"><p>Command to set the rectangle height.</p></td>
<td align="left"><p>Optional. Must be specified if CmdSetRectWidth is specified.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>CmdSetRectSize</p></td>
<td align="left"><p>Command to set the rectangle width and height.</p>
<p>Not supported for Windows 2000 or later.</p></td>
<td align="left"><p>Optional. Used for printers that set the width and height in one command.</p></td>
</tr>
<tr class="even">
<td align="left"><p>CmdSetRectWidth</p></td>
<td align="left"><p>Command to set the rectangle width.</p></td>
<td align="left"><p>Optional. Must be specified if CmdSetRectHeight is specified.</p></td>
</tr>
</tbody>
</table>

 

For examples, see the [sample GPD files](sample-gpd-files.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Rectangle%20Area%20Fill%20Commands%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




