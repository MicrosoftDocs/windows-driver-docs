---
title: "ux (Unassemble x86 BIOS)"
description: "The ux command displays the instruction set of the x86-based BIOS code."
keywords: ["ux (Unassemble x86 BIOS) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- ux (Unassemble x86 BIOS)
api_type:
- NA
---

# ux (Unassemble x86 BIOS)


The **ux** command displays the instruction set of the x86-based BIOS code.

`ux [Address]`

## <span id="ddk_cmd_unassemble_x86_bios_dbg"></span><span id="DDK_CMD_UNASSEMBLE_X86_BIOS_DBG"></span>Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the memory offset within the x86-based BIOS code. If you omit this parameter or specify zero, the default offset is the beginning of the BIOS.

## Environment

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

 

## Additional Information

For more information about how to debug BIOS code, see [Debugging BIOS Code](../debugger/debugging-bios-code.md).

## Remarks

The debugger displays the instructions that are generated from the first eight lines of code, beginning at the *Address* offset.

To make the **ux** command work correctly, HAL symbols must be available to the debugger. If the debugger cannot find these symbols, the debugger displays a "couldn't resolve" error.

