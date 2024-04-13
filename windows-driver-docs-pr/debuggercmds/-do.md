---
title: ".do (WinDbg)"
description: "The .do token behaves like the do keyword in C, except that the word while is not used before the condition."
keywords: [".do Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- .do
api_type:
- NA
---

# .do

The **.do** token behaves like the **do** keyword in C, except that the word "while" is not used before the condition.

```dbgcmd
.do { Commands } (Condition) 
```

## <span id="ddk_token_do_dbg"></span><span id="DDK_TOKEN_DO_DBG"></span>Syntax Elements


<span id="_______Commands______"></span><span id="_______commands______"></span><span id="_______COMMANDS______"></span> *Commands*   
Specifies one or more commands that will be executed repeatedly as long as the condition is true -- but will always be executed at least once. This block of commands needs to be enclosed in braces, even if it consists of a single command. Multiple commands should be separated by semicolons, but the final command before the closing brace does not need to be followed by a semicolon.

<span id="_______Condition______"></span><span id="_______condition______"></span><span id="_______CONDITION______"></span> *Condition*   
Specifies a condition. If this evaluates to zero, it is treated as false; otherwise it is true. Enclosing *Condition* in parentheses is optional. *Condition* must be an expression, not a debugger command. It will be evaluated by the default expression evaluator (MASM or C++). For details, see [Numerical Expression Syntax](numerical-expression-syntax.md).

## Additional Information

For information about other control flow tokens and their use in debugger command programs, see [Using Debugger Command Programs](../debugger/using-debugger-command-programs.md).

## Remarks

The [**.break**](https://support.microsoft.com/help/833721/available-switch-options-for-the-windows-xp-and-the-windows-server-200) and [**.continue**](-continue.md) tokens can be used to exit or restart the *Commands* block.

 


