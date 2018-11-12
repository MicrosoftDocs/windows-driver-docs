---
title: .for
description: The .for token behaves like the for keyword in C, except that multiple increment commands must be separated by semicolons, not by commas.
ms.assetid: 35f54c4c-e7f5-42a9-b579-1e4958b7286b
keywords: [".for Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- .for
api_type:
- NA
ms.localizationpriority: medium
---

# .for


The **.for** token behaves like the **for** keyword in C, except that multiple increment commands must be separated by semicolons, not by commas.

```dbgcmd
.for (InitialCommand ; Condition ; IncrementCommands) { Commands } 
```

## <span id="ddk_token_for_dbg"></span><span id="DDK_TOKEN_FOR_DBG"></span>Syntax Elements


<span id="_______InitialCommand______"></span><span id="_______initialcommand______"></span><span id="_______INITIALCOMMAND______"></span> *InitialCommand*   
Specifies a command that will be executed before the loop begins. Only a single initial command is permitted.

<span id="_______Condition______"></span><span id="_______condition______"></span><span id="_______CONDITION______"></span> *Condition*   
Specifies a condition. If this evaluates to zero, it is treated as false; otherwise it is true. Enclosing *Condition* in parentheses is optional. *Condition* must be an expression, not a debugger command. It will be evaluated by the default expression evaluator (MASM or C++). For details, see [Numerical Expression Syntax](numerical-expression-syntax.md).

<span id="_______IncrementCommands______"></span><span id="_______incrementcommands______"></span><span id="_______INCREMENTCOMMANDS______"></span> *IncrementCommands*   
Specifies one or more commands that will be executed at the conclusion of each loop. If you wish to use multiple increment commands, separate them by semicolons but do not enclose them in braces.

<span id="_______Commands______"></span><span id="_______commands______"></span><span id="_______COMMANDS______"></span> *Commands*   
Specifies one or more commands that will be executed repeatedly as long as the condition is true. This block of commands needs to be enclosed in braces, even if it consists of a single command. Multiple commands should be separated by semicolons, but the final command before the closing brace does not need to be followed by a semicolon.

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For information about other control flow tokens and their use in debugger command programs, see [Using Debugger Command Programs](using-debugger-command-programs.md).

Remarks
-------

If all the work is being done by the increment commands, you can omit *Condition* entirely and simply use an empty pair of braces.

Here is an example of a **.for** statement with multiple increment commands:

```dbgcmd
0:000> .for (r eax=0; @eax < 7; r eax=@eax+1; r ebx=@ebx+1) { .... }
```

The [**.break**](https://msdn.microsoft.com/library/windows/hardware/ff556242) and [**.continue**](-continue.md) tokens can be used to exit or restart the *Commands* block.

 

 





