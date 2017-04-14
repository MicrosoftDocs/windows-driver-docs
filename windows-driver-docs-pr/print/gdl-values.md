---
title: GDL Values
author: windows-driver-content
description: GDL Values
ms.assetid: 0e634646-d334-4b9c-b9d2-36026f617575
keywords: ["GDL WDK , values", "values WDK GDL , about GDL values", "values WDK GDL , characters", "GDL WDK , contexts", "GDL WDK , Value Macro References", "Value Macro References WDK GDL", "values WDK GDL , examples", "contexts WDK GDL"]
---

# GDL Values


A *GDL value* is a character string that begins with the first non-whitespace character in a GDL attribute that is found after the colon delimiter and typically ends when a linebreak sequence or a construct delimiter is reached.

There are a few [GDL contexts](gdl-contexts.md) when a linebreak sequence or a construct delimiter does not terminate the value. These special contexts include when:

-   Construct delimiter characters occur as part of a comment.

-   Termination characters occur as part of a quoted string.

-   Termination characters occur within a [nested context](gdl-nested-contexts.md).

-   Termination characters occur within an [arbitrary value](gdl-arbitrary-value-contexts.md).

A value can contain zero, one, or more of these special contexts. A single context type can appear multiple times in one value. Any of the preceding special contexts can also appear outside of any other context. Some contexts might appear within another context; these cases are noted in the descriptions of each context. All contexts must be exited before the value can be terminated by either a linebreak sequence or a construct delimiter.

The terminating linebreak sequence or a construct delimiter is not considered part of the value.

Values are optional in a [GDL attribute](gdl-attributes.md).

*Value Macro References* might appear anywhere in a GDL value that non-literal whitespace is permitted; these references begin with the equal sign (=). When the equal sign is used in such a context and it is not intended to introduce a Value Macro Reference, the equal sign must be followed by a non-symbol character (such as whitespace). For more information about value macros, see [GDL Value Macros](gdl-value-macros.md).

For more information about GDL contexts, see [GDL Contexts](gdl-contexts.md).

The following code examples show values that are acceptable to the GDL parser.

```
*Value: *%  Null Value - only a comment

*Value: "Quoted String"

*Value: "Quoted String with Hex substring: <48 65 78> see?"

*Value: "Hex substring with comment and macro reference <48 *% comment
65 78 =MacroRef > see?"   *% note continuation linebreak was automatically assumed

*Value: tokens (parenthesis context) [followed by square brackets context] "ending in quoted string"

*Value: tokens (parenthesis context {with nested curly braces context})

*Value:  tokens <BeginValue:anything> no special characters or contexts recognized within an arbitrary value context.  " } ) * % < > anything goes, sorry  =MacroRefs not recognized
*Keyword:  looks like a new entry but its still within the Arbitrary Value context.
+  not continuation chars, *% this is not a comment  <EndValue:anything>
```

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20GDL%20Values%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


