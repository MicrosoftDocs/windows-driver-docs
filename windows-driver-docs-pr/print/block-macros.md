---
title: Block Macros
description: Block Macros
ms.assetid: da2f6161-072a-4d3c-94a8-1020520de524
keywords:
- block macros WDK GPD files
- referencing macros
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Block Macros





A block macro is used to delimit a set of GPD file entries that you want to insert repeatedly into a GPD file. You can include any entry type in a block macro definition, such as feature and option statements, attribute specifications, and references to value macros or other block macros.

The following rules apply to the use of block macros:

-   A block macro definition within a GPD file must be located before any references to it.

-   A block macro defined at root level (that is, not inside braces) is available through the GPD file that defines it, after it is defined. Otherwise, the scope of a block macro is the set of left and right braces containing its definition.

-   A block macro definition can contain definitions of additional block macros and value macros.

-   A block macro definition can reference other previously-defined block macros and value macros, but it cannot reference itself.

-   Block macros do not accept arguments.

-   If braces are included in a macro body, they must be paired (that is, there must be an equal number of left and right braces).

-   If you create two block macros with the same name, the first definition is in effect until the GPD parser encounters the second definition. The second definition then replaces the first. If the scope of the second definition ends, the first definition is reinstated.

### Block Macro Format

To define a block macro in a GPD file, use the following format:

<table>
<colgroup>
<col width="100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>*<strong>BlockMacro</strong>: <em>BlockMacroName</em> {<em>BlockMacroBody</em>}</p></td>
</tr>
</tbody>
</table>

 

where *BlockMacroName* is a unique name, and *BlockMacroBody* is a set of one or more [GPD file entries](gpd-file-entries.md). If *BlockMacroBody* contains braces, equal numbers of left and right braces ( {, } ) must be included.

For example, you might define a block macro named EnvelopeDefaults, which is defined as follows:

```cpp
*BlockMacro: EnvelopeDefaults
{
    *PrintableArea: PAIR(4646, 6738)
    *PrintableOrigin: PAIR(150, 150)
    *RotateSize: TRUE
}
```

### Referencing Block Macros

To reference a block macro, use the following format:

<table>
<colgroup>
<col width="100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>*InsertBlock</strong>: =BlockMacroName</p></td>
</tr>
</tbody>
</table>

 

where *BlockMacroName* is a unique name, previously specified in the **\*BlockMacro** entry that defines the macro.

For example, to reference the EnvelopeDefaults macro within an option specification, you could use the following entries:

```cpp
*Option: Env9
{
    *InsertBlock: =EnvelopeDefaults
}
```

 

 




