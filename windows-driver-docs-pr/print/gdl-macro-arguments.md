---
title: GDL Macro Arguments
description: GDL Macro Arguments
ms.assetid: 2aeaf2fd-39e3-4661-85d1-ccb855a73044
keywords:
- GDL WDK , macros
- macros WDK GDL , arguments
- macros WDK GDL , examples
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# GDL Macro Arguments


The contents of a macro definition can reference all, some, or none of its formal arguments, especially for value macro definitions, where multiple value macro definitions can occur within one \*Macros construct with a single formal argument list that is shared by all of the definitions. In this case, one definition can reference some of the formal arguments, while another references none.

If a macro definition omits references to one or more formal arguments, the parameter list that is supplied when the macro is referenced can indicate those missing parameters by commas (,) that separate nothing.

For example, the following macro reference uses only the fifth argument. The first four are omitted.

```cpp
*Attribute: =Macro(,,,, =PassedInMacroRef)
```

You do not need to indicate trailing omitted parameters at all. If the macro in the previous example declared 10 formal arguments but referenced only the fifth argument, the preceding example would still be a valid way to reference the macro.

For value macros, no whitespace is allowed between the macro reference and its parameter list. This syntax enables the parser to distinguish between a macro reference that uses no arguments that happens to be followed by something that looks like a parameter list from a macro reference that uses a parameter list.

For example, consider the following code example.

```cpp
*Attrib:   =Macro1 (=Macro2)       *%  is 2 separate macro references
    while
*Attrib:   =Macro1(=Macro2)        *% you are passing Macro2 as a 
    *%  parameter  to Macro1.
```

If macro definitions are nested, the formal arguments can be used only by the contents of the macro that declared the arguments. The contents of nested macro definitions cannot reference the arguments that the enclosing macro define.

Macro references that occur within a macro definition can contain parameter lists that name macros that themselves require parameters lists. However, a parameter list cannot be supplied for references to formal arguments. For example, the following entry within a block macro definition is acceptable.

```cpp
*Attrib1: =Macro1(=Macro2(=Macro3(=Arg1, =Arg2)))
```

In the preceding example, =MacroN represents a reference to a previously defined value macro and =ArgN represents a reference to a formal argument.

However, the following code example is not an acceptable entry.

```cpp
*Attrib2: =Arg1(=Arg2, =Arg3(=Macro1, =Macro2))   *%  Not Valid !
```

If a macro reference matches a formal argument name that the macro declares, you can assume that it is a reference to that formal argument, regardless of whether a real macro exists with that name. You can avoid such ambiguities by using a namespace qualifier with the macro reference. However, you cannot use namespace qualifiers with formal arguments.

For value macros, if no formal argument list was declared in the \*Macros construct, any reference to the macros that are defined within should not be followed with a parameter list. Such a list will not be considered part of the macro reference.

For example, consider if =Macro1 is defined by the following code example.

```cpp
*Macros:   NoArgList
{
Macro1:  "a Value macro with no argument list"
Macro2:  "a Value macro with no argument list"
Macro3:  "a Value macro with no argument list"
}
```

Then, the following macro reference will be interpreted as three separate and unrelated macro references.

```cpp
*attribute:  =Macro1(=Macro2, =Macro3)
```

The parser will not interpret (=Macro2, =Macro3) to be a parameter list for =Macro1. This behavior preserves backward compatibility with current GPDs.

 

 




