---
title: Value Macros
description: A value macro is used to specify a set of one or more values that you want to insert individually and repeatedly into a GPD file.
keywords:
- value macros WDK GPD files
- referencing macros
ms.date: 12/19/2024
ms.topic: concept-article
---

# Value macros

[!include[Print Support Apps](../includes/print-support-apps.md)]

A value macro is used to specify a set of one or more values that you want to insert individually and repeatedly into a Generic Printer Description (GPD) file. Values can be any of the [GPD value types](gpd-value-types.md).

The following rules apply to the use of value macros:

- A value macro definition within a GPD file must be located before any references to it.

- A value macro defined at root level (that is, not inside braces) is available through the GPD file that defines it, after it's defined. Otherwise, the scope of a value macro is the set of left and right braces containing its definition.

- A value macro must resolve to one of the [GPD value types](gpd-value-types.md).

- A value macro definition can reference other previously defined value macros if all values are text strings, but a value macro can't reference itself.

- Value macros don't accept arguments.

- If you create two value macros with the same name, the first definition is in effect until the GPD parser encounters the second definition. The second definition then replaces the first. If the scope of the second definition ends, the first definition is reinstated.

## Value macro format

To define one or more value macros in a GPD file, use the following format:

\*Macros: **ValueMacroGroupName* { *ValueMacroBody* }

Where *ValueMacroGroupName* is a unique name, and *ValueMacroBody* is a set of unique value names and associated values, as follows:

*ValueMacroName* : *MacroValue*

Where *ValueMacroName* is a unique macro name, and *MacroValue* represents a [GPD value type](gpd-value-types.md). (*MacroValue* can include references to previously defined value macros, as long as the resolved string represents a GPD value type.)

As an example, you might define value macros for a set of frequently used command prefixes as follows:

```GPD
*Macros: HP4L
{
    LetterCmdPrefix: "<1B>&l2a8c1E<1B>*p0x0Y"
    A4CmdPrefix: "<1B>&l26a8c1E<1B>*p0x0Y"
    Env10CmdPrefix: "<1B>&l81a8c1E<1B>*p0x0Y"
}
```

*ValueMacroGroupName* (HP4L in the example) is optional and treated as a comment.

## Referencing value macros

To reference a value macro, use the following format:

= *ValueMacroName*

Where *ValueMacroName* is a unique name, previously specified in the \*Macros entry that defines the macro.

For example, to reference one of the HP4L macros within a command specification, you could use the following entries:

```GPD
*Command: CmdSelect
{
    *Cmd: =LetterCmdPrefix "<1B>*c0t5760x7680Y"
}
```

The only time you can assign a value by combining macro references with non-macro values is when all macro definitions and other values represent text or command substrings, as illustrated in the example. In all other cases, the macro reference must represent the entire value to be assigned.
