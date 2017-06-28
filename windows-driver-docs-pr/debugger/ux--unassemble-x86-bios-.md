---
title: ux (Unassemble x86 BIOS)
description: The ux command displays the instruction set of the x86-based BIOS code.
ms.assetid: d3616255-1a07-4a5d-8171-c8316179a7dc
keywords: ["ux (Unassemble x86 BIOS) Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- ux (Unassemble x86 BIOS)
api_type:
- NA
---

# ux (Unassemble x86 BIOS)


The **ux** command displays the instruction set of the x86-based BIOS code.

```
ux [Address]
```

## <span id="ddk_cmd_unassemble_x86_bios_dbg"></span><span id="DDK_CMD_UNASSEMBLE_X86_BIOS_DBG"></span>Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the memory offset within the x86-based BIOS code. If you omit this parameter or specify zero, the default offset is the beginning of the BIOS.

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

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information about how to debug BIOS code, see [Debugging BIOS Code](debugging-bios-code.md).

Remarks
-------

The debugger displays the instructions that are generated from the first eight lines of code, beginning at the *Address* offset.

To make the **ux** command work correctly, HAL symbols must be available to the debugger. If the debugger cannot find these symbols, the debugger displays a "couldn't resolve" error.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20ux%20%28Unassemble%20x86%20BIOS%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




