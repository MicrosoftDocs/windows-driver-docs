---
title: ob, ow, od (Output to Port)
description: The ob, ow, and od commands send a byte, word, or double word to the selected port.
ms.assetid: 04133df7-4b60-4709-a9e1-5946c8d30f8c
keywords: ["ob, ow, od (Output to Port) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- ob, ow, od (Output to Port)
api_type:
- NA
ms.localizationpriority: medium
---

# ob, ow, od (Output to Port)


The **ob**, **ow**, and **od** commands send a byte, word, or double word to the selected port.

```dbgcmd
ob Address Value 
ow Address Value 
od Address Value 
```

## <span id="ddk_cmd_output_to_port_dbg"></span><span id="DDK_CMD_OUTPUT_TO_PORT_DBG"></span>Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the address of the port.

<span id="_______Value______"></span><span id="_______value______"></span><span id="_______VALUE______"></span> *Value*   
Specifies the hexadecimal value to write to the port.

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>Kernel mode only</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>Live debugging only</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>x86-based only</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The **ob** command writes a single byte, the **ow** command writes a word, and the **od** command writes a double word.

Make sure that you do not send a word or a double-word to a port that does not support this size.

## <span id="see_also"></span>See also


[**ib, id, iw (Input from Port)**](ib--iw--id--input-from-port-.md)

 

 






