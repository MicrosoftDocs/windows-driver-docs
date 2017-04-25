---
title: Elements of a Debugger Command Program
description: Elements of a Debugger Command Program
ms.assetid: f964e358-2f3f-4780-87ea-e1374ae861e6
keywords: ["debugger command program, elements"]
---

# Elements of a Debugger Command Program


## <span id="ddk_elements_of_a_debugger_command_program_dbg"></span><span id="DDK_ELEMENTS_OF_A_DEBUGGER_COMMAND_PROGRAM_DBG"></span>


A *debugger command program* is a small application that consists of debugger commands and control flow tokens, such as **.if**, **.for**, and **.while**. (For a full list of control flow tokens and their syntax, see [Control Flow Tokens](control-flow-tokens.md).)

You can use braces ( **{ }** ) to enclose a block of statements within a larger command block. When you enter each block, all aliases within the block are evaluated. If you later alter the value of an alias within a command block, commands after that point do not use the new alias value unless they are within a subordinate block.

You cannot create a block by using a pair of braces. You must add a control flow token before the opening brace. If you want to create a block only to evaluate aliases, you should use the [**.block**](https://msdn.microsoft.com/library/windows/hardware/ff562148) token before the opening brace.

A debugger command program can use [user-named aliases or fixed-name aliases](using-aliases.md) as its local variables. If you want to use numeric or typed variables, you can use the **$t***n*[pseudo-registers](https://msdn.microsoft.com/library/windows/hardware/ff553485).

User-named aliases are evaluated only if they are not next to other text. If you want to evaluate an alias that is next to other text, use the [**${ } (Alias Interpreter)**](https://msdn.microsoft.com/library/windows/hardware/ff566259) token. This token has optional switches that enable you to evaluate the alias in a variety of ways.

You can add comments to a debugger command program by using two dollar signs ([**$$ (Comment Specifier)**](https://msdn.microsoft.com/library/windows/hardware/ff566255)). You should not insert a comment between a token and its elements (such as braces or conditions).

**Note**   You should not use an asterisk ([**\* (Comment Line Specifier)**](https://msdn.microsoft.com/library/windows/hardware/ff566249)). Because comments that are specified with an asterisk do not end with a semicolon, the rest of the program is disregarded.

 

Typically, you should use MASM syntax within a debugger command program. When you have to use C++ elements (such as specifying a member of a structure or class), you can use the **@@c++( )** token to switch to C++ syntax for that clause.

The **$scmp**, **$sicmp**, and **$spat** string operators in MASM syntax are particularly useful. For more information about these operators, see [MASM Numbers and Operators](https://msdn.microsoft.com/library/windows/hardware/ff552157).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Elements%20of%20a%20Debugger%20Command%20Program%20%20RELEASE:%20%284/24/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




