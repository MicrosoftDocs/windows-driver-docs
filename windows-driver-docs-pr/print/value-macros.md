---
title: Value Macros
author: windows-driver-content
description: Value Macros
MS-HAID:
- 'nt5gpd\_1ef27636-aa46-498d-93c6-eddb390fdb56.xml'
- 'print.value\_macros'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 265b2d35-5e91-4c47-a145-1e9f8c497c2c
keywords: ["value macros WDK GPD files", "referencing macros"]
---

# Value Macros


## <a href="" id="ddk-value-macros-gg"></a>


A value macro is used to specify a set of one or more values that you want to insert individually and repeatedly into a GPD file. Values can be any of the [GPD value types](gpd-value-types.md).

The following rules apply to the use of value macros:

-   A value macro definition within a GPD file must be located before any references to it.

-   A value macro defined at root level (that is, not inside braces) is available through the GPD file that defines it, after it is defined. Otherwise, the scope of a value macro is the set of left and right braces containing its definition.

-   A value macro must resolve to one of the [GPD value types](gpd-value-types.md).

-   A value macro definition can reference other previously-defined value macros if all values are text strings, but a value macro cannot reference itself.

-   Value macros do not accept arguments.

-   If you create two value macros with the same name, the first definition is in effect until the GPD parser encounters the second definition. The second definition then replaces the first. If the scope of the second definition ends, the first definition is reinstated.

### Value Macro Format

To define one or more value macros in a GPD file, use the following format:

<table>
<colgroup>
<col width="100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>*Macros: <em>ValueMacroGroupName</em> { <em>ValueMacroBody</em> }</p></td>
</tr>
</tbody>
</table>

 

where *ValueMacroGroupName* is a unique name, and *ValueMacroBody* is a set of unique value names and associated values, as follows:

*ValueMacroName* : *MacroValue*

where *ValueMacroName* is a unique macro name, and *MacroValue* represents a [GPD value type](gpd-value-types.md). (*MacroValue* can include references to previously-defined value macros, as long as the resolved string represents a GPD value type.)

As an example, you might define value macros for a set of frequently used command prefixes as follows:

```
*Macros: HP4L
{
    LetterCmdPrefix: "<1B>&l2a8c1E<1B>*p0x0Y"
    A4CmdPrefix: "<1B>&l26a8c1E<1B>*p0x0Y"
    Env10CmdPrefix: "<1B>&l81a8c1E<1B>*p0x0Y"
}
```

Note that *ValueMacroGroupName* (HP4L in the example) is optional and treated as a comment.

### Referencing Value Macros

To reference a value macro, use the following format:

= *ValueMacroName*

where *ValueMacroName* is a unique name, previously specified in the \*Macros entry that defines the macro.

For example, to reference one of the HP4L macros within a command specification, you could use the following entries:

```
*Command: CmdSelect
{
    *Cmd: =LetterCmdPrefix "<1B>*c0t5760x7680Y"
}
```

The only time you can assign a value by combining macro references with nonmacro values is when all macro definitions and other values represent text or command substrings, as illustrated in the example. In all other cases, the macro reference must represent the entire value to be assigned.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Value%20Macros%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


