---
title: Printer Configuration Commands
author: windows-driver-content
description: Printer Configuration Commands
ms.assetid: ed5102e7-1651-4188-8042-f0d544a54a1d
keywords:
- printer commands WDK Unidrv , configuration
- configuration commands WDK Unidrv
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Printer Configuration Commands


## <a href="" id="ddk-printer-configuration-commands-gg"></a>


The following table lists the printer configuration commands. All commands are specified using the [command entry format](command-entry-format.md).

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
<td><p>CmdStartJob</p></td>
<td><p>Command to initialize a print job.</p></td>
<td><p>Optional. [Command execution order](command-execution-order.md) must be specified.</p></td>
</tr>
<tr class="even">
<td><p>CmdStartDoc</p></td>
<td><p>Command to initialize a document.</p></td>
<td><p>Optional. [Command execution order](command-execution-order.md) must be specified.</p></td>
</tr>
<tr class="odd">
<td><p>CmdStartPage</p></td>
<td><p>Command to initialize a page and set the cursor position to (0,0) in cursor coordinates.</p></td>
<td><p>Optional. [Command execution order](command-execution-order.md) must be specified.</p></td>
</tr>
<tr class="even">
<td><p>CmdEndPage</p></td>
<td><p>Command to finish printing a page.</p></td>
<td><p>Optional. [Command execution order](command-execution-order.md) must be specified.</p></td>
</tr>
<tr class="odd">
<td><p>CmdEndDoc</p></td>
<td><p>Command to finish printing a document.</p></td>
<td><p>Optional. [Command execution order](command-execution-order.md) must be specified.</p></td>
</tr>
<tr class="even">
<td><p>CmdEndJob</p></td>
<td><p>Command to complete a print job.</p></td>
<td><p>Optional. [Command execution order](command-execution-order.md) must be specified.</p></td>
</tr>
<tr class="odd">
<td><p>CmdCopies</p></td>
<td><p>Command to specify the number of copies to print.</p></td>
<td><p>Optional. [Command execution order](command-execution-order.md) must be specified.</p></td>
</tr>
<tr class="even">
<td><p>CmdSleepTimeOut</p></td>
<td><p>Command to specify the number of minutes for the printer to wait before entering power-save mode.</p></td>
<td><p>Optional. [Command execution order](command-execution-order.md) must be specified.</p></td>
</tr>
</tbody>
</table>

 

For examples, see the [sample GPD files](sample-gpd-files.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Printer%20Configuration%20Commands%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


