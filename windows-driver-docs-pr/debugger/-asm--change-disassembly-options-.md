---
title: .asm (Change Disassembly Options)
description: The .asm command controls how disassembly code will be displayed.
ms.assetid: c963c4f2-3bfc-4551-9b7b-74473a63eb11
keywords: ["Change Disassembly Options (.asm) command", "assembly debugging, Change Disassembly Options (.asm) command", ".asm (Change Disassembly Options) Windows Debugging"]
ms.author: domars
ms.date: 09/17/2018
topic_type:
- apiref
api_name:
- .asm (Change Disassembly Options)
api_type:
- NA
ms.localizationpriority: medium
---

# .asm (Change Disassembly Options)


The **.asm** command controls how disassembly code will be displayed.

```dbgcmd
    .asm 
    .asm[-] Options
```

## <span id="ddk_meta_change_disassembly_options_dbg"></span><span id="DDK_META_CHANGE_DISASSEMBLY_OPTIONS_DBG"></span>Parameters


<span id="_______-______"></span> **-**   
Causes the specified options to be disabled. If no minus sign is used, the specified options will be enabled.

<span id="_______Options______"></span><span id="_______options______"></span><span id="_______OPTIONS______"></span> *Options*   
Can be any number of the following options:

<span id="ignore_output_width"></span><span id="IGNORE_OUTPUT_WIDTH"></span>**ignore\_output\_width**  
Prevents the debugger from checking the width of lines in the disassembly display.

<span id="no_code_bytes"></span><span id="NO_CODE_BYTES"></span>**no\_code\_bytes**  
(x86 and x64 targets only) Suppresses the display of raw bytes.

<span id="source_line"></span><span id="SOURCE_LINE"></span>**source\_line**  
Prefixes each line of disassembly with the line number of the source code.

<span id="verbose"></span><span id="VERBOSE"></span>**verbose**  
(Itanium target only) Causes bundle-type information to be displayed along with the standard disassembly information.

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>user mode, kernel mode</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>live, crash dump</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>all</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For a description of assembly debugging and related commands, see [Debugging in Assembly Mode](debugging-in-assembly-mode.md).

Remarks
-------

Using **.asm** by itself displays the current state of the options.

This command affects the display of any disassembly instructions in the Debugger Command window. In WinDbg it also changes the contents of the Disassembly window.

 

 





