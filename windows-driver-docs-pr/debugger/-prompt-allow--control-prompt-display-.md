---
title: .prompt_allow (Control Prompt Display)
description: The .prompt_allow command controls what information is displayed during stepping and tracing and whenever the target's execution stops.
ms.assetid: 916114f9-0a68-4423-ba28-a5f0da8a1af9
keywords: [".prompt_allow (Control Prompt Display) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- .prompt_allow (Control Prompt Display)
api_type:
- NA
ms.localizationpriority: medium
---

# .prompt\_allow (Control Prompt Display)


The **.prompt\_allow** command controls what information is displayed during stepping and tracing and whenever the target's execution stops.

```dbgcmd
.prompt_allow {+|-}Item [...] 
.prompt_allow 
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="______________"></span> **+**   
Displays the specified item at the stepping, tracing, and execution prompt. You must add a space before the plus sign (+), but you cannot add a space after it.

<span id="_______-______"></span> **-**   
Prevents the specified item from being displayed at the stepping, tracing, and execution prompt. You must add a space before the minus sign (-), but you cannot add a space after it.

<span id="_______Item______"></span><span id="_______item______"></span><span id="_______ITEM______"></span> *Item*   
Specifies an item to display or not display. You can specify any number of items. Separate multiple items by spaces. You must add a plus sign (+) or minus sign (-) before each item. You can use the following items:

<span id="dis"></span><span id="DIS"></span>**dis**  
The disassembled instructions at the current location.

<span id="ea"></span><span id="EA"></span>**ea**  
The effective address for the current instruction.

<span id="reg"></span><span id="REG"></span>**reg**  
The current state of the most important registers. You can disable register display by using the [**pr**](p--step-.md), [**tr**](t--trace-.md), or .prompt\_allow -reg command. All three of these commands control the same setting, and you can use any of them to override any previous use of these commands.

You can also disable register display by using the l-os command. This setting is separate from the other three commands, as described in the following Remarks section. To control which registers and flags are displayed, use the [**rm (Register Mask)**](rm--register-mask-.md) command.

<span id="src"></span><span id="SRC"></span>**src**  
The source line that corresponds to the current instruction. You can disable source line display by using the l-ls or .prompt\_allow -src; commands. You must enable source line display through both mechanisms to be visible.

<span id="sym"></span><span id="SYM"></span>**sym**  
The symbol for the current instruction. This symbol includes the current module, function name, and offset.

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

For more information about commands that affect execution, see [Controlling the Target](controlling-the-target.md).

Remarks
-------

You can use the **.prompt\_allow** command without parameters to show which items are displayed and are not displayed. Every time that you run **.prompt\_allow**, the debugger changes the status of only the specified items.

By default, all items are displayed.

If you have used the l+os option, this option overrides any of the **.prompt\_allow** options other than **src**.

You can also use a complex command such as the following example.

```dbgcmd
0:000> .prompt_allow -reg -dis +ea 
Allow the following information to be displayed at the prompt:
(Other settings can affect whether the information is actually displayed)
   sym - Symbol for current instruction
    ea - Effective address for current instruction
   src - Source info for current instruction
Do not allow the following information to be displayed at the prompt:
   dis - Disassembly of current instruction
   reg - Register state
```

 

 





