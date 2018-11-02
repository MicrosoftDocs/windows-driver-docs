---
title: Buffer DbgPrint Output
description: Buffer DbgPrint Output
ms.assetid: af97c484-3a37-4c86-8828-12a0ea1c8c0e
keywords: ["Buffer DbgPrint Output (global flag)"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
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

 

 





