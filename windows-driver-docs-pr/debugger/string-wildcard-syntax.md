---
title: String Wildcard Syntax
description: This topic covers string wildcard syntax. Some debugger commands have string parameters that accept a variety of wildcard characters.
ms.assetid: 11e73f81-5d5c-4d9a-8380-ec767b27f603
keywords: string wildcards, expressions, regular expressions, syntax rules for commands
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# String Wildcard Syntax


## <span id="ddk_string_wildcard_syntax_dbg"></span><span id="DDK_STRING_WILDCARD_SYNTAX_DBG"></span>


Some debugger commands have string parameters that accept a variety of wildcard characters. These parameters are noted on their respective reference pages.

These kinds of parameters support the following syntax features:

- An asterisk (\*) represents zero or more characters.

- A question mark (?) represents any single character.

- Brackets ( \[ \] ) that contain a list of characters represent any single character in the list. Exactly one character in the list is matched. Within these brackets, you can use a hyphen (-) to specify a range. For example, **Prog\[er-t7\]am** matches "Progeam", "Program", "Progsam", "Progtam", and "Prog7am".

- A number sign (\#) represents zero or more of the preceding characters. For example, **Lo\#p** matches "Lp", "Lop", "Loop", "Looop", and so on. You can also combine a number sign with brackets, so **m\[ia\]\#n** matches "mn", "min", "man", "maan", "main", "mian", "miin", "miain", and so on.

- A plus sign (+) represents one or more of the preceding characters. For example, **Lo+p** is the same as **Lo\#p**, except that **Lo+p** does not match "Lp". Similarly, **m\[ia\]+n** is the same as **m\[ia\]\#n**, except that m<strong>\[ia\]+n</strong> does not match "mn". **a?+b** is also the same as **a\*b**, except that **a?+b** does not match "ab".

- If you have to specify a literal number sign (\#), question mark (?), opening bracket (\[), closing bracket (\]), asterisk (\*), or plus sign (+) character, you must add a backslash ( \\ ) in front of the character. Hyphens are always literal when you do not enclose them in brackets. But you cannot specify a literal hyphen within a bracketed list.

Parameters that specify symbols also support some additional features. In addition to the standard string wildcard characters, you can use an underscore (\_) before a text expression that you use to specify a symbol. When matching this expression to a symbol, the debugger treats the underscore as any quantity of underscores, even zero. This feature applies only when you are matching symbols. It does not apply to string wildcard expressions in general. For more information about symbol syntax, see [Symbol Syntax and Symbol Matching](symbol-syntax-and-symbol-matching.md).

 

 





