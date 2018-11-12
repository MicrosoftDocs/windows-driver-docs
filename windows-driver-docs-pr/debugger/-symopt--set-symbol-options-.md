---
title: .symopt (Set Symbol Options)
description: The .symopt command sets or displays the symbol options.
ms.assetid: 0793baa3-14f7-48df-8773-736b6a5470e6
keywords: [".symopt (Set Symbol Options) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- .symopt (Set Symbol Options)
api_type:
- NA
ms.localizationpriority: medium
---

# .symopt (Set Symbol Options)


The **.symopt** command sets or displays the symbol options.

```dbgcmd
.symopt+ Flags 
.symopt- Flags 
.symopt 
```

## <span id="ddk_meta_set_symbol_options_dbg"></span><span id="DDK_META_SET_SYMBOL_OPTIONS_DBG"></span>Parameters


<span id="______________"></span> **+**   
Causes the symbol options specified by *Flags* to be set. If **.symopt** is used with *Flags* but no plus or minus sign, a plus sign is assumed.

<span id="_______-______"></span> **-**   
Causes the symbol options specified by *Flags* to be cleared.

<span id="_______Flags______"></span><span id="_______flags______"></span><span id="_______FLAGS______"></span> *Flags*   
Specifies the symbol options to be changed. *Flags* must be the sum of the bit flags of these symbol options.

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

For a list and description of each symbol option, its bit flag, and other methods of setting and clearing these options, see [Setting Symbol Options](symbol-options.md).

Remarks
-------

Without any arguments, **.symopt** displays the current symbol options.

 

 





