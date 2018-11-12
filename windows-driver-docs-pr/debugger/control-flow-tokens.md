---
title: Control Flow Tokens
description: Control Flow Tokens
ms.assetid: c38852aa-3dfe-4f70-9ef4-8c86e4a8334d
keywords: ["script file, control flow tokens", "control flow tokens", "debugger command program, control flow tokens"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Control Flow Tokens


## <span id="ddk_control_flow_tokens_dbg"></span><span id="DDK_CONTROL_FLOW_TOKENS_DBG"></span>


You can use *control flow tokens* to create conditional execution and execution loops within debugger command programs.

Control flow tokens behave like their counterparts in C and C++, with the following general exceptions:

-   You must enclose each block of commands that is executed conditionally or repeatedly in braces, even if there is only one such command. For example, you cannot omit the braces in the following command.

    ```dbgcmd
    0:000> .if (ebx>0) { r ebx }
    ```

-   Each condition must be a expression. Commands are not permitted. For example, the following example produces a syntax error.

    ```dbgcmd
    0:000> .while (r ebx) { .... }
    ```

-   The final command before a closing brace does not have to be followed by a semicolon.

The following control flow tokens are supported within a debugger command program. For more information about the syntax of each token, see the individual reference topics.

-   The [**.if**](-if.md) token behaves like the **if** keyword in C.

-   The [**.else**](-else.md) token behaves like the **else** keyword in C.

-   The [**.elsif**](-elsif.md) token behaves like the **else if** keyword combination in C.

-   The [**.foreach**](-foreach.md) token parses the output of debugger commands, a string, or a text file. This token then takes each item that it finds and uses them as the input to a specified list of debugger commands.

-   The [**.for**](-for.md) token behaves like the **for** keyword in C, except that you must separate multiple increment commands by semicolons, not by commas.

-   The [**.while**](-while.md) token behaves like the **while** keyword in C.

-   The [**.do**](-do.md) token behaves like the **do** keyword in C, except that you cannot use the word "while" before the condition.

-   The [**.break**](https://msdn.microsoft.com/library/windows/hardware/ff556242) token behaves like the **break** keyword in C. You can use this token within any **.for**, **.while**, or **.do** loop.

-   The [**.continue**](-continue.md) token behaves like the **continue** keyword in C. You can use this token within any **.for**, **.while**, or **.do** loop.

-   The [**.catch**](-catch.md) token prevents a program from ending if an error occurs. The **.catch** token is followed by braces that enclose one or more commands. If one of these commands generates an error, the error message is displayed, all remaining commands within the braces are ignored, and execution resumes with the first command after the closing brace.

-   The [**.leave**](-leave.md) token is used to exit from a **.catch** block.

-   The [**.printf**](-printf.md) token behaves like the **printf** statement in C.

-   The [**.block**](-block.md) token performs no action. You should use this token only to introduce a block, because you cannot create a block by only using a pair of braces. You must add a control flow token before the opening brace.

The [**!for\_each\_module**](-for-each-module.md), [**!for\_each\_frame**](-for-each-frame.md), and [**!for\_each\_local**](-for-each-local.md) extensions are also useful with a debugger command program.

 

 





