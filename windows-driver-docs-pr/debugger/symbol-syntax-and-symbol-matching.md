---
title: Symbol Syntax and Symbol Matching
description: Symbol Syntax and Symbol Matching
ms.assetid: 7fda24bf-57be-4c7d-9eff-bd688de7cf1b
keywords: ["symbols, symbol syntax", "symbols, symbol matching", "symbols, symbol suffix", "syntax rules for commands, $ (local symbol identifier)", "$ (local symbol identifier)", "local symbol identifier ( $ )", "local variables, local symbol identifier ( $ )"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Symbol Syntax and Symbol Matching


## <span id="ddk_symbol_syntax_and_symbol_matching_dbg"></span><span id="DDK_SYMBOL_SYNTAX_AND_SYMBOL_MATCHING_DBG"></span>


Symbols allow you to directly manipulate tokens that are used by the program being debugged. For example, you can set a breakpoint at the function **main** with the command **bp main**, or display the integer variable **MyInt** with the command **dd MyInt L1**.

In many cases, symbols can be used as parameters in debugger commands. This is supported for most numerical parameters, and is also supported in some text parameters. In addition to general rules for symbol syntax, there are also symbol syntax rules that apply in each of these cases.

### <span id="general_symbol_syntax_rules"></span><span id="GENERAL_SYMBOL_SYNTAX_RULES"></span>General Symbol Syntax Rules

A symbol name consists of one or more characters, but always begins with a letter, underscore (**\_**), question mark (**?**), or dollar sign (**$**).

A symbol name may be qualified by a module name. An exclamation mark (**!**) separates the module name from the symbol (for instance, **mymodule!main**). If no module name is used, the symbol can still be prefixed with an exclamation mark. Using an exclamation mark with no module name can be especially useful, even for local variables, to indicate to a debugger command that a parameter is a name and not a hexadecimal number. For example, the variable **fade** will be read by the [**dt (Display Type)**](dt--display-type-.md) command as an address, unless it is prefixed by an exclamation mark or the -n option is used. However, to specify that a symbol is local, precede it with a dollar sign ( $ ) and an exclamation point ( ! ), as in **$!lime**.

Symbol names are completely case-insensitive. This means that the presence of a **myInt** and a **MyInt** in your program will not be correctly understood by the debuggers; any command that references one of these may access the other one, regardless of how the command is capitalized.

### <span id="symbol_syntax_in_numerical_expressions"></span><span id="SYMBOL_SYNTAX_IN_NUMERICAL_EXPRESSIONS"></span>Symbol Syntax in Numerical Expressions

The debugger understands two different kinds of expressions: Microsoft Macro Assembler (MASM) expressions and C++ expressions. As far as symbols are concerned, these two forms of syntax differ as follows:

-   In MASM expressions, each symbol is interpreted as an address. Depending on what the symbol refers to, this will be the address of a global variable, local variable, function, segment, module, or any other recognized label.

-   In C++ expressions, each symbol is interpreted according to its type. Depending on what the symbol refers to, it may be interpreted as an integer, a data structure, a function pointer, or any other data type. A symbol that does not correspond to a C++ data type (such as an unmodified module name) will result in a syntax error.

For an explanation of when and how to use each type of syntax, see [Evaluating Expressions](evaluating-expressions.md).

If you are using MASM expression syntax, any symbol that could be interpreted as a hexadecimal number or as a register (e.g., **BadFeed**, **ebX**) should always be prefixed by an exclamation point. This makes sure the debugger recognizes it as a symbol.

The [**ss (Set Symbol Suffix)**](ss--set-symbol-suffix-.md) command can be used to set the symbol suffix. This instructs the debugger to automatically append "A" or "W" to any symbol name it cannot find otherwise.

Many Win32 routines exist in both ASCII and Unicode versions. These routines often have an "A" or "W" appended to the end of their names, respectively. Using a symbol suffix will aid the debugger when searching for these symbols.

Suffix matching is not active by default.

### <span id="symbol_syntax_in_text_expressions"></span><span id="SYMBOL_SYNTAX_IN_TEXT_EXPRESSIONS"></span>Symbol Syntax in Text Expressions

Symbols can be used in the text parameters of some commands -- for example, [**bm (Set Breakpoint)**](bp--bu--bm--set-breakpoint-.md) and [**x (Examine Symbols)**](x--examine-symbols-.md).

These text parameters support a variety of wildcards and specifiers. See [String Wildcard Syntax](string-wildcard-syntax.md) for details. In addition to the standard string wildcards, a text expression used to specify a symbol can be prefixed with a leading underscore. When matching this to a symbol, the debugger will treat this as any quantity of underscores, even zero.

The symbol suffix is not used when matching symbols in text expressions.

 

 





