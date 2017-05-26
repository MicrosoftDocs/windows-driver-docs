---
title: Syntax Rules
description: This section describes the syntax rules that you must follow to use debugger commands.
ms.assetid: bd1605f9-8e98-4d80-8742-acba222872ef
keywords: ["commands, syntax rules", "meta-commands ("." commands), syntax rules", "syntax rules for commands"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Syntax Rules


## <span id="ddk_syntax_rules_dbg"></span><span id="DDK_SYNTAX_RULES_DBG"></span>


This section describes the syntax rules that you must follow to use debugger commands.

When you are debugging, you should obey the following general syntax rules:

-   You can use any combination of uppercase and lowercase letters in commands and arguments, except when specifically noted in the topics in this section.

-   You can separate multiple command parameters by one or more spaces or by a comma (**,**).

-   You can typically omit the space between a command and its first parameter . You can frequently omit other spaces if this omission does not cause any ambiguity.

The command reference topics in this section use the following items:

-   Characters in **bold** font style indicate items that you must literally type.

-   Characters in *italic* font style indicate parameters that are explained in the "Parameters" section of the reference topic.

-   Parameters in brackets (**\[***xxx***\]**) are optional. Brackets with a vertical bar (**\[***xxx***|***yyy***\]**) indicate that you can use one, or none, of the enclosed parameters.

-   Braces with vertical bars (**{***xxx***|***yyy***}**) indicate that you must use exactly one of the enclosed parameters .

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Syntax%20Rules%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




