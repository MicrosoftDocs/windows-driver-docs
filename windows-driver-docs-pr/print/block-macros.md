---
title: Block Macros
author: windows-driver-content
description: Block Macros
MS-HAID:
- 'nt5gpd\_862ce812-d388-44a3-98a6-3500e0040aa1.xml'
- 'print.block\_macros'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: da2f6161-072a-4d3c-94a8-1020520de524
keywords: ["block macros WDK GPD files", "referencing macros"]
---

# Block Macros


## <a href="" id="ddk-block-macros-gg"></a>


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

```
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

```
*Option: Env9
{
    *InsertBlock: =EnvelopeDefaults
}
```

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Block%20Macros%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


