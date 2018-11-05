---
title: ib, iw, id (Input from Port)
description: The ib, iw, and id commands read and display a byte, word, or double word from the selected port.
ms.assetid: 68f9e0c2-3cfd-46e1-a513-5a96c93de63c
keywords: ["ib, iw, id (Input from Port) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- ib, iw, id (Input from Port)
api_type:
- NA
ms.localizationpriority: medium
---

# ib, iw, id (Input from Port)


The **ib**, **iw**, and **id** commands read and display a byte, word, or double word from the selected port.

```dbgcmd
ib Address 
iw Address 
id Address
```

## <span id="ddk_cmd_input_from_port_dbg"></span><span id="DDK_CMD_INPUT_FROM_PORT_DBG"></span>Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
The address of the port.

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
<td align="left"><p>x86-based computer only</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The **ib** command reads a single byte, the **iw** command reads a word, and the **id** command reads a double word.

Make sure that reading an I/O port does not affect the behavior of the device that you are reading from. Some devices change state after a read-only port has been read. You should also not try to read a word or double-word from a port that does not allow values of this length.

## <span id="see_also"></span>See also


[**ob, od, ow (Output to Port)**](ob--ow--od--output-to-port-.md)

 

 






