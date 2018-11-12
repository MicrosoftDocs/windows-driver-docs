---
title: uf (Unassemble Function)
description: The uf command displays an assembly translation of the specified function in memory.
ms.assetid: 344e3afd-6b8d-48f2-9e07-dd7e1937f71b
keywords: ["uf (Unassemble Function) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- uf (Unassemble Function)
api_type:
- NA
ms.localizationpriority: medium
---

# uf (Unassemble Function)


The **uf** command displays an assembly translation of the specified function in memory.

```dbgcmd
uf [Options] Address
```

## <span id="ddk_cmd_unassemble_function_dbg"></span><span id="DDK_CMD_UNASSEMBLE_FUNCTION_DBG"></span>Parameters


<span id="_______Options______"></span><span id="_______options______"></span><span id="_______OPTIONS______"></span> *Options*   
One or more of the following options:

<span id="_c"></span><span id="_C"></span>**/c**  
Displays only the call instructions in a routine instead of the full disassembly. Call instructions can be useful for determination of caller and callee relationships from disassembled code.

<span id="_D"></span><span id="_d"></span>**/D**  
Creates linked callee names for navigation of the call graph.

<span id="_m"></span><span id="_M"></span>**/m**  
Relaxes the blocking requirements to permit multiple exits.

<span id="_o"></span><span id="_O"></span>**/o**  
Sorts the display by address instead of by function offset. This option presents a memory-layout view of a full function.

<span id="_O"></span><span id="_o"></span>**/O**  
Creates linked call lines for accessing call information and creating breakpoints.

<span id="_i"></span><span id="_I"></span>**/i**  
Displays the number of instructions in a routine.

<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the address of the function to disassemble. For more information about the syntax, see [Address and Address Range Syntax](address-and-address-range-syntax.md).

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

The display shows the whole function, according to the function order.

 

 





