---
title: Raster Data Compression Commands
description: Raster Data Compression Commands
ms.assetid: fd88d009-7612-49cc-810a-b0d09b4b75b3
keywords:
- data compression raster printing commands WDK Unidrv
- compression raster printing commands WDK Unidrv
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Raster Data Compression Commands





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
<th>Command</th>
<th>Description</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>CmdDisableCompression</p></td>
<td><p>Command to disable the printer&#39;s acceptance of all compressed data types.</p></td>
<td><p>Optional.</p></td>
</tr>
<tr class="even">
<td><p>CmdEnableDRC</p></td>
<td><p>Command to enable the printer&#39;s acceptance of DRC-compressed data.</p></td>
<td><p>Optional. If not specified, Unidrv does not use Delta-Row compression.</p></td>
</tr>
<tr class="odd">
<td><p>CmdEnableFE_RLE</p></td>
<td><p>Command to enable the printer&#39;s acceptance of FE-RLE-compressed data.</p></td>
<td><p>Optional. If not specified, Unidrv does not use FE-RLE compression.</p></td>
</tr>
<tr class="even">
<td><p>CmdEnableOEMComp</p></td>
<td><p>Command to enable the printer&#39;s acceptance of a customized compressed data type.</p></td>
<td><p>Optional. If not specified, Unidrv does not use customized data compression.</p></td>
</tr>
<tr class="odd">
<td><p>CmdEnableTIFF4</p></td>
<td><p>Command to enable the printer&#39;s acceptance of TIFF 4.0-compressed data.</p></td>
<td><p>Optional. If not specified, Unidrv does not use TIFF4.0 compression.</p></td>
</tr>
</tbody>
</table>

 

For examples, see the [sample GPD files](sample-gpd-files.md).

 

 




