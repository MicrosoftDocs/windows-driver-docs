---
title: DEBUG\_SYMBOL\_XXX
description: The DEBUG\_SYMBOL\_XXX constants are used for the symbol flags bit-set. The symbol flags describe (in part) a symbol in a symbol group.
ms.assetid: de1988f8-6a4d-43a3-856a-0543ecaaf06f
ms.author: domars
ms.date: 12/07/2017
topic_type:
- apiref
api_name:
- DEBUG_SYMBOL_EXPANDED
- DEBUG_SYMBOL_READ_ONLY
- DEBUG_SYMBOL_IS_ARRAY
- DEBUG_SYMBOL_IS_FLOAT
- DEBUG_SYMBOL_IS_ARGUMENT
- DEBUG_SYMBOL_IS_LOCAL
api_location:
- DbgEng.h
api_type:
- HeaderDef
ms.localizationpriority: medium
---

# DEBUG\_SYMBOL\_XXX


The DEBUG\_SYMBOL\_*XXX* constants are used for the symbol flags bit-set. The symbol flags describe (in part) a symbol in a symbol group.

The least significant bits of the symbol flags--the bits found in DEBUG\_SYMBOL\_EXPANSION\_LEVEL\_MASK--form a number that represents the expansion depth of the symbol within the symbol group. The depth of a child symbol is always one more than the depth of its parent symbol. For example, to find the depth of a symbol whose flags are contained in the variable *flags*, use the following statement:

```dbgcmd
depth = flags &amp; DEBUG_SYMBOL_EXPANSION_LEVEL_MASK;
```

The rest of the symbol flags' bit-set can contain the following bit-flags.

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
<td align="left"><span id="DEBUG_SYMBOL_EXPANDED"></span><span id="debug_symbol_expanded"></span>
<strong>DEBUG_SYMBOL_EXPANDED</strong></td>
<td align="left"><p>The children of the symbol are part of the symbol group.</p></td>
</tr>
<tr class="even">
<td align="left"><span id="DEBUG_SYMBOL_READ_ONLY"></span><span id="debug_symbol_read_only"></span>
<strong>DEBUG_SYMBOL_READ_ONLY</strong></td>
<td align="left"><p>The symbol represents a read-only variable.</p></td>
</tr>
<tr class="odd">
<td align="left"><span id="DEBUG_SYMBOL_IS_ARRAY"></span><span id="debug_symbol_is_array"></span>
<strong>DEBUG_SYMBOL_IS_ARRAY</strong></td>
<td align="left"><p>The symbol represents an array variable.</p></td>
</tr>
<tr class="even">
<td align="left"><span id="DEBUG_SYMBOL_IS_FLOAT"></span><span id="debug_symbol_is_float"></span>
<strong>DEBUG_SYMBOL_IS_FLOAT</strong></td>
<td align="left"><p>The symbol represents a floating-point variable.</p></td>
</tr>
<tr class="odd">
<td align="left"><span id="DEBUG_SYMBOL_IS_ARGUMENT"></span><span id="debug_symbol_is_argument"></span>
<strong>DEBUG_SYMBOL_IS_ARGUMENT</strong></td>
<td align="left"><p>The symbol represents an argument passed to a function.</p></td>
</tr>
<tr class="even">
<td align="left"><span id="DEBUG_SYMBOL_IS_LOCAL"></span><span id="debug_symbol_is_local"></span>
<strong>DEBUG_SYMBOL_IS_LOCAL</strong></td>
<td align="left"><p>The symbol represents a local variable in a scope.</p></td>
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

## <span id="see_also"></span>See also


[**DEBUG\_SYMBOL\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff541673)

 

 






