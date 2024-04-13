---
title: "wrmsr (Write MSR)"
description: "The wrmsr command writes a value to a Model-Specific Register (MSR) at the specified address."
keywords: ["wrmsr (Write MSR) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- wrmsr (Write MSR)
api_type:
- NA
---

# wrmsr (Write MSR)

The **wrmsr** command writes a value to a Model-Specific Register (MSR) at the specified address.

`wrmsr Address Value`

## <span id="ddk_cmd_write_msr_dbg"></span><span id="DDK_CMD_WRITE_MSR_DBG"></span>Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the address of the MSR.

<span id="_______Value______"></span><span id="_______value______"></span><span id="_______VALUE______"></span> *Value*   
Specifies the 64-bit hexadecimal value to write to the MSR.

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
<td align="left"><p>All</p></td>
</tr>
</tbody>
</table>

 

## Remarks

The **wrmsr** command can set MSR's on x86-based and x64-based platforms. The MSR definitions are platform-specific.

## See also


[**rdmsr (Read MSR)**](rdmsr--read-msr-.md)


