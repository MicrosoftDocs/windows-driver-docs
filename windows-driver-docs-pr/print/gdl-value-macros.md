---
title: GDL Value Macros
author: windows-driver-content
description: GDL Value Macros
MS-HAID:
- 'gplfiles\_c2bc2917-b208-44e3-bdd4-8e358bb9bbbd.xml'
- 'print.gdl\_value\_macros'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 171245ef-d9ab-4c1d-86b9-f53ae10033b3
keywords: ["GDL WDK , macros", "macros WDK GDL , value macros", "value macros WDK GDL", "values WDK GDL , value macros", "Macros directive WDK GDL", "macros WDK GDL , examples"]
---

# GDL Value Macros


*Value macros* are used to represent all or part of a value. They are defined within the \*Macros construct. You can define multiple macros within one construct.

Each entry within the \*Macros construct is a separate macro. The keyword of the entry becomes the name of the value macro, and the value of the entry becomes the contents of that value macro. The macro name must be a symbol name type. The contents of a value macro can be anything that adheres to valid GDL syntax for a value.

Value macros can reference other value macros. The instance name of the \*Macros construct can hold a tag that is followed by a parenthesis-enclosed formal argument list. Any reference to any formal argument by any of the macro definitions in the \*Macros construct is symbolically replaced by the corresponding parameter that is passed in when the value macro is actually referenced.

**Note**  The declarations and references of arguments that will be used to pass value macro references are prefixed with the equal sign (=) to signify that the argument type is a value macro.
All references to value macros are also prefixed with the equal sign (=) to signify the reference is to a value macro instead of a block macro. The equal sign must be immediately followed by the value macro name, and no intervening whitespace is allowed. References to value macros can nest parameter lists to arbitrary depth.

 

### <a href="" id="macro-examples"></a> Macro Examples

All value macro definitions must be recognized as complete, valid value entity.

The following code example shows how to use value macros.

```
*Macros:
{
    InvalidMacro: "First Half of a string
}
```

InvalidMacro is not valid because the quoted string context must be terminated with a double quote. This unterminated string is not a complete value.

If you want to represent an incomplete value entity, use the following code example.

```
*Macros:
{
    FirstHalf: <BeginValue:Q>"This is the first half <EndValue:Q>
    SecondHalf:  <BeginValue:Q>of the string."<EndValue:Q>
}
*FullString: =FirstHalf=SecondHalf
*%  *FullString now expands to generate the complete string:
*FullString: "This is the first half of the string."
```

The following code shows how to use macro arguments.

```
*Macros: FormalArgs(=arg1, =arg2)
{
result1: disappointed
result2: pleased
result3: impressed
result4: awestruck
result5: restrained


adverb1: very =arg1 and =arg2
   adverb2: while remaining =arg1
   String1:  The audience was =arg1 with today&#39;s performance.
}
```

The following code shows how to use macro references with parameters.

```
*BadOutput: =String1(=result1)
*GoodOutput: =String1(=adverb1(=adverb1(=result2, =result3), =adverb2(=result5)))
```

The parser will expand the preceding macro references to produce the following code.

```
*BadOutput: The audience was disappointed with today&#39;s performance.
*GoodOutput: The audience was very very pleased and impressed and while remaining restrained with today&#39;s performance.
```

Value macro references are not recognized in all value contexts. For example, value macros are not recognized within the arbitrary value or quoted string contexts. But value macros are recognized within hex string contexts that might reside within the quoted string context.

To provide backward compatibility with GPD, the percent sign (%) is interpreted to mean it introduces a command parameter context when the percent sign is used in a non-literal whitespace value context within the contents of a value macro definition. In other words, avoid using the percent sign within a value macro definition unless you are defining a command parameter or the percent sign is contained within a literal whitespace context, such as &lt;Begin/EndValue&gt;.

The contents of a macro definition are actually interpreted only when the macro is referenced outside of any macro definition. At that time, the macro that is referenced is replaced by its contents, and the contents are actually interpreted. If the contents contain a macro reference, that reference is replaced by its contents and interpretation continues with the contents of that macro.

You should think of the parser as acting on a single input stream. When a macro reference is detected outside of any macro definition, the macro reference is removed from the input stream and replaced by its contents, and parsing of the input stream continues with the contents of the macro.

Consider the following macro.

```
*Macros:
{
quote: <BeginValue:x>"<EndValue:x>
first_half: =quote This is enclosed
second_half:  by quotes.=quote
whole_string: =first_half <not a hex string!> =second_half
}
*Print1: =quote
*Print2: =first_half
*Print3: =second_half
*Print4: =whole_string
```

The preceding macro will expand to the following code.

```
*Print1:  "
*Print2:  " This is enclosed
*Print3:  by quotes."
*Print4:  " This is enclosed <not a hex string!> by quotes."
```

Note that the expanded result is not syntactically legal GDL.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20GDL%20Value%20Macros%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


