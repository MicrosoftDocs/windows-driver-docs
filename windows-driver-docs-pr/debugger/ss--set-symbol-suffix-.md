---
title: ss (Set Symbol Suffix)
description: The ss command sets or displays the current suffix value that is used for symbol matching in numeric expressions.
ms.assetid: acf4cf2e-5b09-4d46-aa42-e539ee968685
keywords: ["ss (Set Symbol Suffix) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- ss (Set Symbol Suffix)
api_type:
- NA
ms.localizationpriority: medium
---

# ss (Set Symbol Suffix)


The **ss** command sets or displays the current suffix value that is used for symbol matching in numeric expressions.

```dbgcmd
ss [a|w|n] 
```

## <span id="ddk_cmd_set_symbol_suffix_dbg"></span><span id="DDK_CMD_SET_SYMBOL_SUFFIX_DBG"></span>Parameters


<span id="_______a______"></span><span id="_______A______"></span> **a**   
Specifies that the symbol suffix should be "A", matching many ASCII symbols.

<span id="_______w______"></span><span id="_______W______"></span> **w**   
Specifies that the symbol suffix should be "W", matching many Unicode symbols.

<span id="_______n______"></span><span id="_______N______"></span> **n**   
Specifies that the debugger should not use a symbol suffix. (This parameter is the default behavior.)

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

For more information about symbol matching, see [Symbol Syntax and Symbol Matching](symbol-syntax-and-symbol-matching.md).

Remarks
-------

If you specify the **ss** command together with no parameters, the current state of the suffix value is displayed.

 

 





