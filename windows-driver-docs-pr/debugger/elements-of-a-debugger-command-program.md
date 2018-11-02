---
title: Elements of a Debugger Command Program
description: Elements of a Debugger Command Program
ms.assetid: f964e358-2f3f-4780-87ea-e1374ae861e6
keywords: ["debugger command program, elements"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Elements of a Debugger Command Program


## <span id="ddk_elements_of_a_debugger_command_program_dbg"></span><span id="DDK_ELEMENTS_OF_A_DEBUGGER_COMMAND_PROGRAM_DBG"></span>


A *debugger command program* is a small application that consists of debugger commands and control flow tokens, such as **.if**, **.for**, and **.while**. (For a full list of control flow tokens and their syntax, see [Control Flow Tokens](control-flow-tokens.md).)

You can use braces ( **{ }** ) to enclose a block of statements within a larger command block. When you enter each block, all aliases within the block are evaluated. If you later alter the value of an alias within a command block, commands after that point do not use the new alias value unless they are within a subordinate block.

You cannot create a block by using a pair of braces. You must add a control flow token before the opening brace. If you want to create a block only to evaluate aliases, you should use the [**.block**](-block.md) token before the opening brace.

A debugger command program can use [user-named aliases or fixed-name aliases](using-aliases.md) as its local variables. If you want to use numeric or typed variables, you can use the **$t***n*[pseudo-registers](pseudo-register-syntax.md).

User-named aliases are evaluated only if they are not next to other text. If you want to evaluate an alias that is next to other text, use the [**${ } (Alias Interpreter)**](-------alias-interpreter-.md) token. This token has optional switches that enable you to evaluate the alias in a variety of ways.

You can add comments to a debugger command program by using two dollar signs ([**$$ (Comment Specifier)**](-----comment-specifier-.md)). You should not insert a comment between a token and its elements (such as braces or conditions).

**Note**   You should not use an asterisk ([**\* (Comment Line Specifier)**](----comment-line-specifier-.md)). Because comments that are specified with an asterisk do not end with a semicolon, the rest of the program is disregarded.

 

Typically, you should use MASM syntax within a debugger command program. When you have to use C++ elements (such as specifying a member of a structure or class), you can use the **@@c++( )** token to switch to C++ syntax for that clause.

The **$scmp**, **$sicmp**, and **$spat** string operators in MASM syntax are particularly useful. For more information about these operators, see [MASM Numbers and Operators](masm-numbers-and-operators.md).

 

 





