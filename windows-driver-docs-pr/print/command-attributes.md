---
title: Command Attributes
author: windows-driver-content
description: Command Attributes
MS-HAID:
- 'nt5gpd\_45af4f66-21fd-4dcc-b12f-c8df5ba9d2bf.xml'
- 'print.command\_attributes'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 8ce2c668-a130-428e-bf5f-0eab2dcd3fdb
keywords: ["printer attributes WDK Unidrv , commands", "commands WDK Unidrv", "printer commands WDK Unidrv , attributes", "CallbackID", "Cmd", "NoPageEject", "Order", "Params"]
---

# Command Attributes


## <a href="" id="ddk-command-attributes-gg"></a>


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
<td><p><strong>*CallbackID</strong></p></td>
<td><p>Positive numeric value, passed to the rendering plug-in's [<strong>IPrintOemUni::CommandCallback</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554216) method as its <em>dCmdCbID</em> argument.</p></td>
<td><p>Required for [dynamically generated printer commands](dynamically-generated-printer-commands.md). Not valid if <strong>*Cmd</strong> is specified.</p></td>
</tr>
<tr class="even">
<td><p><strong>*Cmd</strong></p></td>
<td><p>Text string containing a printer command escape sequence, specified using the [command string format](command-string-format.md).</p></td>
<td><p>Required unless <strong>*CallbackID</strong> is specified.</p></td>
</tr>
<tr class="odd">
<td><p><strong>*NoPageEject?</strong></p></td>
<td><p><strong>TRUE</strong> or <strong>FALSE</strong>, indicating whether executing the command causes the printer to eject the current physical page.</p>
<p>Used only if <strong>*Order</strong> specifies the DOC_SETUP section and if DUPLEX printing is enabled. To avoid premature page ejection between duplexed document pages, Unidrv only issues commands with this attribute set to <strong>TRUE</strong>, if possible.</p></td>
<td><p>Optional. If not specified, the default value is <strong>FALSE</strong>, meaning the command might cause page ejection.</p>
<p>Must not be <strong>TRUE</strong> if a command causes side effects (that is, if the command modifies printer settings outside of those controlled by commands with <strong>*NoPageEject?</strong> set to <strong>TRUE</strong>).</p></td>
</tr>
<tr class="even">
<td><p><strong>*Order</strong></p></td>
<td><p>Section name and order number, as described in [Command Execution Order](command-execution-order.md).</p></td>
<td><p>Valid only with configuration commands and customized option commands, unless stated in the command description.</p></td>
</tr>
<tr class="odd">
<td><p><strong>*Params</strong></p></td>
<td><p>[List](lists.md) of [standard variables](standard-variables.md), passed to the rendering plug-in's IPrintOemUni::CommandCallback method in the EXTRAPARAM structure that is passed as its <em>pdwParams</em> argument.</p></td>
<td><p>Valid only if <strong>*CallbackID</strong> is also specified.</p></td>
</tr>
</tbody>
</table>

 

For examples, see the [sample GPD files](sample-gpd-files.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Command%20Attributes%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


