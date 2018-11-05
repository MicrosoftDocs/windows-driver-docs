---
title: .fnent (Display Function Data)
description: The .fnent command displays information about the function table entry for a specified function.
ms.assetid: 914caf55-2fbf-4f30-af6e-e666dc47c7da
keywords: ["Display Function Data (.fnent) command", ".fnent (Display Function Data) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- .fnent (Display Function Data)
api_type:
- NA
ms.localizationpriority: medium
---

# .fnent (Display Function Data)


The **.fnent** command displays information about the function table entry for a specified function.

```dbgcmd
.fnent Address
```

## <span id="ddk_meta_display_function_data_dbg"></span><span id="DDK_META_DISPLAY_FUNCTION_DATA_DBG"></span>Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the address of the function.

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

 

Remarks
-------

The symbol search algorithm for the **.fnent** command is the same as that of the [**ln (List Nearest Symbols)**](ln--list-nearest-symbols-.md) command. The display first shows the nearest symbols. Then, the debugger displays the function entry for the first of these symbols.

If the nearest symbol is not in the function table, no information is displayed.

The following example shows a possible display.

```dbgcmd
0:001> .fnent 77f9f9e7
Debugger function entry 00b61f50 for:
(77f9f9e7)   ntdll!RtlpBreakWithStatusInstruction   |  (77f9fa98)   ntdll!DbgPrintReturnControlC

Params:    1
Locals:    0
Registers: 0

0:001> .fnent 77f9fa98
Debugger function entry 00b61f70 for:
(77f9fa98)   ntdll!DbgPrintReturnControlC   |  (77f9fb21)   ntdll!DbgPrompt

Non-FPO

0:001> .fnent 01005a60
No function entry for 01005a60
```

 

 





