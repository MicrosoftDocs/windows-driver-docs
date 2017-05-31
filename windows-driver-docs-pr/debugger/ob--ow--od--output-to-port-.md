---
title: ob, ow, od (Output to Port)
description: The ob, ow, and od commands send a byte, word, or double word to the selected port.
ms.assetid: 04133df7-4b60-4709-a9e1-5946c8d30f8c
keywords: ["ob, ow, od (Output to Port) Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- ob, ow, od (Output to Port)
api_type:
- NA
---

# ob, ow, od (Output to Port)


The **ob**, **ow**, and **od** commands send a byte, word, or double word to the selected port.

```
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20ob,%20ow,%20od%20%28Output%20to%20Port%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





