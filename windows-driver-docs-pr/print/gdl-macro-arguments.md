---
title: GDL Macro Arguments
author: windows-driver-content
description: GDL Macro Arguments
MS-HAID:
- 'gplfiles\_c3a6acf2-768e-48f9-ac04-9888d609970b.xml'
- 'print.gdl\_macro\_arguments'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 2aeaf2fd-39e3-4661-85d1-ccb855a73044
keywords: ["GDL WDK , macros", "macros WDK GDL , arguments", "macros WDK GDL , examples"]
---

# GDL Macro Arguments


The contents of a macro definition can reference all, some, or none of its formal arguments, especially for value macro definitions, where multiple value macro definitions can occur within one \*Macros construct with a single formal argument list that is shared by all of the definitions. In this case, one definition can reference some of the formal arguments, while another references none.

If a macro definition omits references to one or more formal arguments, the parameter list that is supplied when the macro is referenced can indicate those missing parameters by commas (,) that separate nothing.

For example, the following macro reference uses only the fifth argument. The first four are omitted.

```
*Attribute: =Macro(,,,, =PassedInMacroRef)
```

You do not need to indicate trailing omitted parameters at all. If the macro in the previous example declared 10 formal arguments but referenced only the fifth argument, the preceding example would still be a valid way to reference the macro.

For value macros, no whitespace is allowed between the macro reference and its parameter list. This syntax enables the parser to distinguish between a macro reference that uses no arguments that happens to be followed by something that looks like a parameter list from a macro reference that uses a parameter list.

For example, consider the following code example.

```
*Attrib:   =Macro1 (=Macro2)       *%  is 2 separate macro references
    while
*Attrib:   =Macro1(=Macro2)        *% you are passing Macro2 as a 
    *%  parameter  to Macro1.
```

If macro definitions are nested, the formal arguments can be used only by the contents of the macro that declared the arguments. The contents of nested macro definitions cannot reference the arguments that the enclosing macro define.

Macro references that occur within a macro definition can contain parameter lists that name macros that themselves require parameters lists. However, a parameter list cannot be supplied for references to formal arguments. For example, the following entry within a block macro definition is acceptable.

```
*Attrib1: =Macro1(=Macro2(=Macro3(=Arg1, =Arg2)))
```

In the preceding example, =MacroN represents a reference to a previously defined value macro and =ArgN represents a reference to a formal argument.

However, the following code example is not an acceptable entry.

```
*Attrib2: =Arg1(=Arg2, =Arg3(=Macro1, =Macro2))   *%  Not Valid !
```

If a macro reference matches a formal argument name that the macro declares, you can assume that it is a reference to that formal argument, regardless of whether a real macro exists with that name. You can avoid such ambiguities by using a namespace qualifier with the macro reference. However, you cannot use namespace qualifiers with formal arguments.

For value macros, if no formal argument list was declared in the \*Macros construct, any reference to the macros that are defined within should not be followed with a parameter list. Such a list will not be considered part of the macro reference.

For example, consider if =Macro1 is defined by the following code example.

```
*Macros:   NoArgList
{
Macro1:  "a Value macro with no argument list"
Macro2:  "a Value macro with no argument list"
Macro3:  "a Value macro with no argument list"
}
```

Then, the following macro reference will be interpreted as three separate and unrelated macro references.

```
*attribute:  =Macro1(=Macro2, =Macro3)
```

The parser will not interpret (=Macro2, =Macro3) to be a parameter list for =Macro1. This behavior preserves backward compatibility with current GPDs.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20GDL%20Macro%20Arguments%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


