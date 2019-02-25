---
title: GDL Block Macros
description: GDL Block Macros
ms.assetid: c8b8e38d-237f-4c54-a394-148d211237ce
keywords:
- GDL WDK , macros
- macros WDK GDL , block macros
- block macros WDK GDL
- BlockMacros directive WDK GDL
- macros WDK GDL , examples
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# GDL Block Macros


*Block macros* are used to represent one or more GDL entries. They are defined within the \*BlockMacros construct.

The instance name of the \*BlockMacros construct becomes the name of the block macro, and the entries that are contained within the curly braces of the \*BlockMacros construct become the contents of that block macro. The macro name must be a symbol name type. The entries that are contained with a block macro definition must be complete.

If there are any construct entries, they must be completed within the macro definition. In other words, the contents of a block macro definition cannot change the nesting level.

A block macro can contain other block or value macro definitions and namespace directives in addition to normal data entries. The nested macro definitions and namespace directives are evaluated immediately and do not appear in the contents of the block macro.

Block macros can contain references to other block or value macros . The instance name of the \*BlockMacros construct can be followed by a parenthesis-enclosed formal argument list. Any reference to any formal argument within the body of this block macro definition will be symbolically replaced by the corresponding parameter that is passed in when the block macro is actually referenced.

**Note**  The declarations and references of arguments that will be used to pass value macro references are prefixed with the equal sign (=) to signify that the argument type is value macro. All references to value macros are also prefixed with the equal sign to signify the reference is to a value macro instead of a block macro.

 

References to block macros can nest parameter lists to arbitrary depth. Block macros are referenced by using \*InsertBlock: NameOfBlockMacro. The name of the block macro is not prefixed with an equal sign because it is not a reference to a value macro. This syntax differs from the GPD syntax.

The following code example shows how to use block macros.

```cpp
*Macros:
{
  LetterName: Letter
  Quote: <BeginValue:Q>"<EndValue:Q>
}
*BlockMacro: LetterSize
{
*Name: =Quote=LetterName=Quote
  *PaperDimension:  PAIR(8.5 , 11)
}
*BlockMacro: PaperOption(PaperSize, =PaperName)
{
  *Option: =PaperName
  {
    *InsertBlock: PaperSize
  }
}

*InsertBlock: PaperOption(LetterSize, =LetterName)
```

 

 




