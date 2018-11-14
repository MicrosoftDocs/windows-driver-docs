---
title: up (Unassemble from Physical Memory)
description: The up command displays an assembly translation of the specified program code in physical memory.
ms.assetid: 4db66566-b7b8-4f1e-9492-b4b78016b45a
keywords: ["up (Unassemble from Physical Memory) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- up (Unassemble from Physical Memory)
api_type:
- NA
ms.localizationpriority: medium
---

# up (Unassemble from Physical Memory)


The **up** command displays an assembly translation of the specified program code in physical memory.

```dbgcmd
up Range 
up Address 
up 
```

## <span id="ddk_cmd_unassemble_dbg"></span><span id="DDK_CMD_UNASSEMBLE_DBG"></span>Parameters


<span id="_______Range______"></span><span id="_______range______"></span><span id="_______RANGE______"></span> *Range*   
Specifies the memory range in physical memory that contains the instructions to disassemble. For more information about the syntax, see [Address and Address Range Syntax](address-and-address-range-syntax.md).

<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the beginning of the memory range in physical memory to disassemble. Eight instructions (on an x86-based processor) or nine instructions (on an Itanium-based processor) are unassembled. For more information about the syntax, see [Address and Address Range Syntax](address-and-address-range-syntax.md).

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>User mode, kernel mode</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>Live, crash dump</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>All</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information about assembly debugging and related commands, see [Debugging in Assembly Mode](debugging-in-assembly-mode.md).

Remarks
-------

If you do not specify a parameter for the **up** command, the disassembly begins at the current address and extends eight instructions (on an x86-based processor) or nine instructions (on an Itanium-based processor).

Do not confuse this command with the [**u (Unassemble)**](u--unassemble-.md). The **up** command disassembles only physical memory, while the **u** command disassembles only virtual memory.

 

 





