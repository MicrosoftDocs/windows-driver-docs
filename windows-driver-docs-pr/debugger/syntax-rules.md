---
title: Syntax Rules
description: This section describes the syntax rules that you must follow to use debugger commands.
ms.assetid: bd1605f9-8e98-4d80-8742-acba222872ef
keywords: commands, syntax rules, meta-commands 
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Syntax Rules


## <span id="ddk_syntax_rules_dbg"></span><span id="DDK_SYNTAX_RULES_DBG"></span>


This section describes the syntax rules that you must follow to use debugger commands.

When you are debugging, you should obey the following general syntax rules:

-   You can use any combination of uppercase and lowercase letters in commands and arguments, except when specifically noted in the topics in this section.

-   You can separate multiple command parameters by one or more spaces or by a comma (**,**).

-   You can typically omit the space between a command and its first parameter . You can frequently omit other spaces if this omission does not cause any ambiguity.

The command reference topics in this section use the following items:

- Characters in **bold** font style indicate items that you must literally type.

- Characters in *italic* font style indicate parameters that are explained in the "Parameters" section of the reference topic.

- Parameters in brackets (**\[**<em>xxx</em>**\]**) are optional. Brackets with a vertical bar (**\[**<em>xxx</em>**|**<em>yyy</em>**\]**) indicate that you can use one, or none, of the enclosed parameters.

- Braces with vertical bars (**{**<em>xxx</em>**|**<em>yyy</em>**}**) indicate that you must use exactly one of the enclosed parameters .

The following topics describe the syntax that the following parameter types use:

[Numerical Expression Syntax](numerical-expression-syntax.md)

[String Wildcard Syntax](string-wildcard-syntax.md)

[Register Syntax](register-syntax.md)

[Pseudo-Register Syntax](pseudo-register-syntax.md)

[Source Line Syntax](source-line-syntax.md)

[Address and Address Range Syntax](address-and-address-range-syntax.md)

[Thread Syntax](thread-syntax.md)

[Process Syntax](process-syntax.md)

[System Syntax](system-syntax.md)

[Multiprocessor Syntax](multiprocessor-syntax.md)

Syntax also plays an important role in using symbols. For further details, see [Symbol Syntax and Symbol Matching](symbol-syntax-and-symbol-matching.md).

 

 





