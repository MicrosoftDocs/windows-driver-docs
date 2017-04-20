---
title: Raster Data Emission Commands
author: windows-driver-content
description: Raster Data Emission Commands
ms.assetid: 31a25de3-f66b-4cf0-90ea-988d75838f68
keywords:
- data emission raster printing commands WDK Unidrv
- emission raster printing commands WDK Unidrv
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Raster Data Emission Commands


## <a href="" id="ddk-raster-data-emission-commands-gg"></a>


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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Raster%20Data%20Emission%20Commands%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


