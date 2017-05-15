---
title: Buffer DbgPrint Output
description: Buffer DbgPrint Output
ms.assetid: af97c484-3a37-4c86-8828-12a0ea1c8c0e
keywords: ["Buffer DbgPrint Output (global flag)"]
---

# Buffer DbgPrint Output


## <span id="ddk_buffer_dbgprint_output_dtools"></span><span id="DDK_BUFFER_DBGPRINT_OUTPUT_DTOOLS"></span>


The **Buffer DbgPrint Output** flag suppresses debugger output from **DbgPrint**, **DbgPrintEx**, **KdPrint**, and **KdPrintEx** calls.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Abbreviation</strong></p></td>
<td align="left"><p>ddp</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Hexadecimal value</strong></p></td>
<td align="left"><p>0x08000000</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Symbolic Name</strong></p></td>
<td align="left"><p>FLG_DISABLE_DBGPRINT</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Destination</strong></p></td>
<td align="left"><p>System-wide registry entry, kernel flag</p></td>
</tr>
</tbody>
</table>

 

### <span id="comments"></span><span id="COMMENTS"></span>Comments

When debugger output is suppressed, it does not automatically appear in the kernel debugger. However, the message is always sent to the DbgPrint buffer, where it can be accessed by using the [**!dbgprint**](-dbgprint.md) debugger extension.

For information about the functions that communicate with the debugger, see [Sending Output to the Debugger](sending-output-to-the-debugger.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Buffer%20DbgPrint%20Output%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




