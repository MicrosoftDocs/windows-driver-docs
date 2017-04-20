---
title: GDL Block Macros
author: windows-driver-content
description: GDL Block Macros
ms.assetid: c8b8e38d-237f-4c54-a394-148d211237ce
keywords:
- GDL WDK , macros
- macros WDK GDL , block macros
- block macros WDK GDL
- BlockMacros directive WDK GDL
- macros WDK GDL , examples
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

```
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20GDL%20Block%20Macros%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


