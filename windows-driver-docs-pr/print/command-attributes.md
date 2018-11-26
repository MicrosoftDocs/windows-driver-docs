---
title: Command Attributes
description: Command Attributes
ms.assetid: 8ce2c668-a130-428e-bf5f-0eab2dcd3fdb
keywords:
- printer attributes WDK Unidrv , commands
- commands WDK Unidrv
- printer commands WDK Unidrv , attributes
- CallbackID
- Cmd
- NoPageEject
- Order
- Params
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Command Attributes





When specifying a printer command, you use attributes to provide Unidrv with the following information:

-   The escape sequence that causes the hardware to perform the operation, if the operation is implemented in printer hardware.

-   The callback identifier and parameters required by the [**IPrintOemUni::CommandCallback**](https://msdn.microsoft.com/library/windows/hardware/ff554216) method, if the operation is implemented in a [rendering plug-in](rendering-plug-ins.md).

-   The order in which the command should be sent, relative to other commands.

The following table lists the command attributes in alphabetic order and describes their parameters.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Attribute Name</th>
<th>Attribute Parameter</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong><em>CallbackID</strong></p></td>
<td><p>Positive numeric value, passed to the rendering plug-in&#39;s <a href="https://msdn.microsoft.com/library/windows/hardware/ff554216" data-raw-source="[&lt;strong&gt;IPrintOemUni::CommandCallback&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554216)"><strong>IPrintOemUni::CommandCallback</strong></a> method as its <em>dCmdCbID</em> argument.</p></td>
<td><p>Required for <a href="dynamically-generated-printer-commands.md" data-raw-source="[dynamically generated printer commands](dynamically-generated-printer-commands.md)">dynamically generated printer commands</a>. Not valid if <strong></em>Cmd</strong> is specified.</p></td>
</tr>
<tr class="even">
<td><p><strong><em>Cmd</strong></p></td>
<td><p>Text string containing a printer command escape sequence, specified using the <a href="command-string-format.md" data-raw-source="[command string format](command-string-format.md)">command string format</a>.</p></td>
<td><p>Required unless <strong></em>CallbackID</strong> is specified.</p></td>
</tr>
<tr class="odd">
<td><p><strong><em>NoPageEject?</strong></p></td>
<td><p><strong>TRUE</strong> or <strong>FALSE</strong>, indicating whether executing the command causes the printer to eject the current physical page.</p>
<p>Used only if <strong></em>Order</strong> specifies the DOC_SETUP section and if DUPLEX printing is enabled. To avoid premature page ejection between duplexed document pages, Unidrv only issues commands with this attribute set to <strong>TRUE</strong>, if possible.</p></td>
<td><p>Optional. If not specified, the default value is <strong>FALSE</strong>, meaning the command might cause page ejection.</p>
<p>Must not be <strong>TRUE</strong> if a command causes side effects (that is, if the command modifies printer settings outside of those controlled by commands with <strong><em>NoPageEject?</strong> set to <strong>TRUE</strong>).</p></td>
</tr>
<tr class="even">
<td><p><strong></em>Order</strong></p></td>
<td><p>Section name and order number, as described in <a href="command-execution-order.md" data-raw-source="[Command Execution Order](command-execution-order.md)">Command Execution Order</a>.</p></td>
<td><p>Valid only with configuration commands and customized option commands, unless stated in the command description.</p></td>
</tr>
<tr class="odd">
<td><p><strong><em>Params</strong></p></td>
<td><p><a href="lists.md" data-raw-source="[List](lists.md)">List</a> of <a href="standard-variables.md" data-raw-source="[standard variables](standard-variables.md)">standard variables</a>, passed to the rendering plug-in&#39;s IPrintOemUni::CommandCallback method in the EXTRAPARAM structure that is passed as its <em>pdwParams</em> argument.</p></td>
<td><p>Valid only if <strong></em>CallbackID</strong> is also specified.</p></td>
</tr>
</tbody>
</table>

 

For examples, see the [sample GPD files](sample-gpd-files.md).

 

 




