---
title: DEBUG\_SYMBOL\_XXX
description: The DEBUG\_SYMBOL\_XXX constants are used for the symbol flags bit-set. The symbol flags describe (in part) a symbol in a symbol group.
ms.assetid: de1988f8-6a4d-43a3-856a-0543ecaaf06f
ms.author: domars
ms.date: 12/07/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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
---

# DEBUG\_SYMBOL\_XXX


The DEBUG\_SYMBOL\_*XXX* constants are used for the symbol flags bit-set. The symbol flags describe (in part) a symbol in a symbol group.

The least significant bits of the symbol flags--the bits found in DEBUG\_SYMBOL\_EXPANSION\_LEVEL\_MASK--form a number that represents the expansion depth of the symbol within the symbol group. The depth of a child symbol is always one more than the depth of its parent symbol. For example, to find the depth of a symbol whose flags are contained in the variable *flags*, use the following statement:

```
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20DEBUG_SYMBOL_XXX%20%20RELEASE:%20%2811/30/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





