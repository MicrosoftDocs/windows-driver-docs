---
title: Raster Data Compression Commands
description: Raster Data Compression Commands
ms.assetid: fd88d009-7612-49cc-810a-b0d09b4b75b3
keywords: ["data compression raster printing commands WDK Unidrv", "compression raster printing commands WDK Unidrv"]
---

# Raster Data Compression Commands


## <a href="" id="ddk-raster-data-compression-commands-gg"></a>


The following table lists the raster data compression commands. All commands are specified using the [command entry format](command-entry-format.md).

For more information about raster data compression commands, see [Compressing Raster Data](compressing-raster-data.md).

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
<td align="left"><p>CmdDisableCompression</p></td>
<td align="left"><p>Command to disable the printer's acceptance of all compressed data types.</p></td>
<td align="left"><p>Optional.</p></td>
</tr>
<tr class="even">
<td align="left"><p>CmdEnableDRC</p></td>
<td align="left"><p>Command to enable the printer's acceptance of DRC-compressed data.</p></td>
<td align="left"><p>Optional. If not specified, Unidrv does not use Delta-Row compression.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>CmdEnableFE_RLE</p></td>
<td align="left"><p>Command to enable the printer's acceptance of FE-RLE-compressed data.</p></td>
<td align="left"><p>Optional. If not specified, Unidrv does not use FE-RLE compression.</p></td>
</tr>
<tr class="even">
<td align="left"><p>CmdEnableOEMComp</p></td>
<td align="left"><p>Command to enable the printer's acceptance of a customized compressed data type.</p></td>
<td align="left"><p>Optional. If not specified, Unidrv does not use customized data compression.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>CmdEnableTIFF4</p></td>
<td align="left"><p>Command to enable the printer's acceptance of TIFF 4.0-compressed data.</p></td>
<td align="left"><p>Optional. If not specified, Unidrv does not use TIFF4.0 compression.</p></td>
</tr>
</tbody>
</table>

 

For examples, see the [sample GPD files](sample-gpd-files.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Raster%20Data%20Compression%20Commands%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




