---
title: Raster Data Emission Commands
description: Raster Data Emission Commands
ms.assetid: 31a25de3-f66b-4cf0-90ea-988d75838f68
keywords:
- data emission raster printing commands WDK Unidrv
- emission raster printing commands WDK Unidrv
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Raster Data Emission Commands





The following table lists the raster data emission commands. All commands are specified using the [command entry format](command-entry-format.md).

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
<td><p>CmdBeginRaster</p></td>
<td><p>Command to initialize a raster data transfer.</p></td>
<td><p>Optional. If not specified, Unidrv assumes no initialization is needed.</p></td>
</tr>
<tr class="even">
<td><p>CmdEndRaster</p></td>
<td><p>Command to complete a raster data transfer.</p></td>
<td><p>Optional. If not specified, Unidrv assumes no transfer-completion operations are needed.</p></td>
</tr>
<tr class="odd">
<td><p>CmdSetDestBmpHeight</p></td>
<td><p>Command to set the height of a destination bitmap.</p></td>
<td><p>Optional. Applicable only if the printer supports scalable bitmaps.</p></td>
</tr>
<tr class="even">
<td><p>CmdSetDestBmpWidth</p></td>
<td><p>Command to set the width of a destination bitmap.</p></td>
<td><p>Optional. Applicable only if the printer supports scalable bitmaps.</p></td>
</tr>
<tr class="odd">
<td><p>CmdSetSrcBmpHeight</p></td>
<td><p>Command to set the height of a source bitmap.</p></td>
<td><p>Optional. Applicable only if the printer supports scalable bitmaps.</p></td>
</tr>
<tr class="even">
<td><p>CmdSetSrcBmpWidth</p></td>
<td><p>Command to set the width of a source bitmap.</p></td>
<td><p>Optional. Applicable only if the printer supports scalable bitmaps.</p></td>
</tr>
<tr class="odd">
<td><p>CmdSendBlockData</p></td>
<td><p>Command to deliver a block of data to the printer.</p></td>
<td><p>Required. If *OutputDataFormat is V_BYTE, a block contains the data for one physical pass of the print head. (See *PinsPerPhysPass). If *<strong>OutputDataFormat</strong> is H_BYTE, a block contains the data for one logical pass of the print head. (See *PinsPerLogPass).</p></td>
</tr>
<tr class="even">
<td><p>CmdEndBlockData</p></td>
<td><p>Command to indicate the end of a block of data that was sent using the CmdSendBlockData command.</p></td>
<td><p>Optional. If not specified, Unidrv assumes no command is needed to indicate the end of a block. (Used by some dot-matrix printers.)</p></td>
</tr>
<tr class="odd">
<td><p>CmdSendBlackData</p></td>
<td><p>Command to deliver black plane data to the printer.</p></td>
<td><p>Required if *<strong>UseExpColorSelectCmd?</strong> attribute is <strong>FALSE</strong>.</p></td>
</tr>
<tr class="even">
<td><p>CmdSendBlueData</p></td>
<td><p>Command to deliver blue plane data to the printer.</p></td>
<td><p>Required if *<strong>UseExpColorSelectCmd?</strong> attribute is <strong>FALSE</strong>.</p></td>
</tr>
<tr class="odd">
<td><p>CmdSendCyanData</p></td>
<td><p>Command to deliver cyan plane data to the printer.</p></td>
<td><p>Required if *<strong>UseExpColorSelectCmd?</strong> attribute is <strong>FALSE</strong>.</p></td>
</tr>
<tr class="even">
<td><p>CmdSendGreenData</p></td>
<td><p>Command to deliver green plane data to the printer.</p></td>
<td><p>Required if *<strong>UseExpColorSelectCmd?</strong> attribute is <strong>FALSE</strong>.</p></td>
</tr>
<tr class="odd">
<td><p>CmdSendMagentaData</p></td>
<td><p>Command to deliver magenta plane data to the printer.</p></td>
<td><p>Required if *<strong>UseExpColorSelectCmd?</strong> attribute is <strong>FALSE</strong>.</p></td>
</tr>
<tr class="even">
<td><p>CmdSendRedData</p></td>
<td><p>Command to deliver red plane data to the printer.</p></td>
<td><p>Required if *UseExpColorSelectCmd? attribute is <strong>FALSE</strong>.</p></td>
</tr>
<tr class="odd">
<td><p>CmdSendYellowData</p></td>
<td><p>Command to deliver yellow plane data to the printer.</p></td>
<td><p>Required if *<strong>UseExpColorSelectCmd?</strong> attribute is <strong>FALSE</strong>.</p></td>
</tr>
</tbody>
</table>

 

For examples, see the [sample GPD files](sample-gpd-files.md).

 

 




