---
title: DEBUG\_OUTPUT\_XXX
description: The DEBUG\_OUTPUT\_XXX constants are output flags. The output flags form a bit field that indicates the type of the output that accompanies them.
ms.assetid: 0c500a2e-0817-45de-8607-4cd4a29d5813
ms.author: windowsdriverdev
ms.date: 12/07/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- DEBUG_OUTPUT_NORMAL
- DEBUG_OUTPUT_ERROR
- DEBUG_OUTPUT_WARNING
- DEBUG_OUTPUT_VERBOSE
- DEBUG_OUTPUT_PROMPT
- DEBUG_OUTPUT_PROMPT_REGISTERS
- DEBUG_OUTPUT_EXTENSION_WARNING
- DEBUG_OUTPUT_DEBUGGEE
- DEBUG_OUTPUT_DEBUGGEE_PROMPT
- DEBUG_OUTPUT_SYMBOLS
api_location:
- DbgEng.h
api_type:
- HeaderDef
---

# DEBUG\_OUTPUT\_XXX


The DEBUG\_OUTPUT\_*XXX* constants are output flags. The output flags form a bit field that indicates the type of the output that accompanies them.

The possible values include the following.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Constant</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><span id="DEBUG_OUTPUT_NORMAL"></span><span id="debug_output_normal"></span>
<strong>DEBUG_OUTPUT_NORMAL</strong></td>
<td align="left"><p>Normal output.</p></td>
</tr>
<tr class="even">
<td align="left"><span id="DEBUG_OUTPUT_ERROR"></span><span id="debug_output_error"></span>
<strong>DEBUG_OUTPUT_ERROR</strong></td>
<td align="left"><p>Error output.</p></td>
</tr>
<tr class="odd">
<td align="left"><span id="DEBUG_OUTPUT_WARNING"></span><span id="debug_output_warning"></span>
<strong>DEBUG_OUTPUT_WARNING</strong></td>
<td align="left"><p>Warnings.</p></td>
</tr>
<tr class="even">
<td align="left"><span id="DEBUG_OUTPUT_VERBOSE"></span><span id="debug_output_verbose"></span>
<strong>DEBUG_OUTPUT_VERBOSE</strong></td>
<td align="left"><p>Additional output.</p></td>
</tr>
<tr class="odd">
<td align="left"><span id="DEBUG_OUTPUT_PROMPT"></span><span id="debug_output_prompt"></span>
<strong>DEBUG_OUTPUT_PROMPT</strong></td>
<td align="left"><p>Prompt output.</p></td>
</tr>
<tr class="even">
<td align="left"><span id="DEBUG_OUTPUT_PROMPT_REGISTERS"></span><span id="debug_output_prompt_registers"></span>
<strong>DEBUG_OUTPUT_PROMPT_REGISTERS</strong></td>
<td align="left"><p>Register dump before prompt.</p></td>
</tr>
<tr class="odd">
<td align="left"><span id="DEBUG_OUTPUT_EXTENSION_WARNING"></span><span id="debug_output_extension_warning"></span>
<strong>DEBUG_OUTPUT_EXTENSION_WARNING</strong></td>
<td align="left"><p>Warnings specific to extension operation.</p></td>
</tr>
<tr class="even">
<td align="left"><span id="DEBUG_OUTPUT_DEBUGGEE"></span><span id="debug_output_debuggee"></span>
<strong>DEBUG_OUTPUT_DEBUGGEE</strong></td>
<td align="left"><p>Debug output from the target (for example, <strong>OutputDebugString</strong> or <strong>DbgPrint</strong>).</p></td>
</tr>
<tr class="odd">
<td align="left"><span id="DEBUG_OUTPUT_DEBUGGEE_PROMPT"></span><span id="debug_output_debuggee_prompt"></span>
<strong>DEBUG_OUTPUT_DEBUGGEE_PROMPT</strong></td>
<td align="left"><p>Debug input expected by the target (for example, <strong>DbgPrompt</strong>).</p></td>
</tr>
<tr class="even">
<td align="left"><span id="DEBUG_OUTPUT_SYMBOLS"></span><span id="debug_output_symbols"></span>
<strong>DEBUG_OUTPUT_SYMBOLS</strong></td>
<td align="left"><p>Symbol messages (for example, <strong>!sym noisy</strong>).</p></td>
</tr>
</tbody>
</table>

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20DEBUG_OUTPUT_XXX%20%20RELEASE:%20%2811/30/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




