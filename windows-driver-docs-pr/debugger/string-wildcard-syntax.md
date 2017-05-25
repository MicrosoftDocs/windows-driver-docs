---
title: String Wildcard Syntax
description: This topic covers string wildcard syntax. Some debugger commands have string parameters that accept a variety of wildcard characters.
ms.assetid: 11e73f81-5d5c-4d9a-8380-ec767b27f603
keywords: ["string wildcards", "expressions, string wildcards", "regular expressions", "regular expressions, See "string wildcards"", "syntax rules for commands, string wildcards"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# String Wildcard Syntax


## <span id="ddk_string_wildcard_syntax_dbg"></span><span id="DDK_STRING_WILDCARD_SYNTAX_DBG"></span>


Some debugger commands have string parameters that accept a variety of wildcard characters. These parameters are noted on their respective reference pages.

These kinds of parameters support the following syntax features:

-   An asterisk (\*) represents zero or more characters.

-   A question mark (?) represents any single character.

-   Brackets ( \[ \] ) that contain a list of characters represent any single character in the list. Exactly one character in the list is matched. Within these brackets, you can use a hyphen (-) to specify a range. For example, **Prog\[er-t7\]am** matches "Progeam", "Program", "Progsam", "Progtam", and "Prog7am".

-   A number sign (\#) represents zero or more of the preceding characters. For example, **Lo\#p** matches "Lp", "Lop", "Loop", "Looop", and so on. You can also combine a number sign with brackets, so **m\[ia\]\#n** matches "mn", "min", "man", "maan", "main", "mian", "miin", "miain", and so on.

-   A plus sign (+) represents one or more of the preceding characters. For example, **Lo+p** is the same as **Lo\#p**, except that **Lo+p** does not match "Lp". Similarly, **m\[ia\]+n** is the same as **m\[ia\]\#n**, except that m**\[ia\]+n** does not match "mn". **a?+b** is also the same as **a\*b**, except that **a?+b** does not match "ab".

-   If you have to specify a literal number sign (\#), question mark (?), opening bracket (\[), closing bracket (\]), asterisk (\*), or plus sign (+) character, you must add a backslash ( \\ ) in front of the character. Hyphens are always literal when you do not enclose them in brackets. But you cannot specify a literal hyphen within a bracketed list.

Parameters that specify symbols also support some additional features. In addition to the standard string wildcard characters, you can use an underscore (\_) before a text expression that you use to specify a symbol. When matching this expression to a symbol, the debugger treats the underscore as any quantity of underscores, even zero. This feature applies only when you are matching symbols. It does not apply to string wildcard expressions in general. For more information about symbol syntax, see [Symbol Syntax and Symbol Matching](symbol-syntax-and-symbol-matching.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20String%20Wildcard%20Syntax%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




