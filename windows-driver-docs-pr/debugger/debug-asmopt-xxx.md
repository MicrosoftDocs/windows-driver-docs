---
title: DEBUG\_ASMOPT\_XXX
description: The DEBUG\_ASMOPT\_XXX constants affect how the debugger engine assembles and disassembles processor instructions for the target.
ms.author: domars
ms.date: 08/10/2018
topic_type:
- apiref
api_name:
- DEBUG_ASMOPT_XXX
api_location:
- DbgEng.h
api_type:
- HeaderDef
ms.localizationpriority: medium
---

# DEBUG\_ASMOPT\_XXX

The assembly and disassembly options affect how the debugger engine assembles and disassembles processor instructions for the target.


The options are represented by a bitset with the following bit flags.

<table>
<tr>
<th>Constant</th>
<th>Description</th>
</tr>
<tr VALIGN="top">
<td align="left" width="40%"><a id="DEBUG_ASMOPT_VERBOSE"></a><a id="debug_asmopt_verbose"></a><dl>
<dt><b>DEBUG_ASMOPT_VERBOSE</b></dt>
</dl>
</td>
<td align="left" width="60%">
<p>When this bit is set, additional information is included in the disassembly.</p>
<p>This is equivalent to the <b>verbose</b> option in the <b>.asm</b> command.</p>
</td>
</tr>
<tr VALIGN="top">
<td align="left" width="40%"><a id="DEBUG_ASMOPT_NO_CODE_BYTES"></a><a id="debug_asmopt_no_code_bytes"></a><dl>
<dt><b>DEBUG_ASMOPT_NO_CODE_BYTES</b></dt>
</dl>
</td>
<td align="left" width="60%">
<p>When this bit is set, the raw bytes for an instruction are not included in the disassembly.</p>
<p>This is equivalent to the <b>no_code_bytes</b> option in the <b>.asm</b> command.</p>
</td>
</tr>
<tr VALIGN="top">
<td align="left" width="40%"><a id="DEBUG_ASMOPT_IGNORE_OUTPUT_WIDTH"></a><a id="debug_asmopt_ignore_output_width"></a><dl>
<dt><b>DEBUG_ASMOPT_IGNORE_OUTPUT_WIDTH</b></dt>
</dl>
</td>
<td align="left" width="60%">
<p>When this bit is set, the debugger ignores the width of the output display when formatting instructions during disassembly.</p>
<p>This is equivalent to the <b>ignore_output_width</b> option in the <b>.asm</b> command.</p>
</td>
</tr>
<tr VALIGN="top">
<td align="left" width="40%"><a id="DEBUG_ASMOPT_SOURCE_LINE_NUMBER"></a><a id="debug_asmopt_source_line_number"></a><dl>
<dt><b>DEBUG_ASMOPT_SOURCE_LINE_NUMBER</b></dt>
</dl>
</td>
<td align="left" width="60%">
<p>When this bit is set, each line of the disassembly output is prefixed with the line number of the source code provided by symbol information.</p>
<p>This is equivalent to the <b>source_line</b> option in the <b>.asm</b> command.</p>
</td>
</tr>
</table>


**Remarks**

Additionally, the value DEBUG_ASMOPT_DEFAULT represents the default set of assembly and disassembly options. This means that all the options in the preceding table are turned off. 



Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">DbgEng.h (include DbgEng.h)</td>
</tr>
</tbody>
</table>

 

 





