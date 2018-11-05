---
title: .elsif
description: The .elsif token behaves like the else if keyword combination in C.
ms.assetid: f5612326-9fcf-4f2e-9692-cc75e7ff4664
keywords: [".elsif Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- .elsif
api_type:
- NA
ms.localizationpriority: medium
---

# .elsif


The **.elsif** token behaves like the **else if** keyword combination in C.

```dbgcmd
.if (Condition) { Commands } .elsif (Condition) { Commands } 

.if (Condition) { Commands } .elsif (Condition) { Commands } .else { Commands } 
```

## <span id="ddk_token_elsif_dbg"></span><span id="DDK_TOKEN_ELSIF_DBG"></span>Syntax Elements


<span id="_______Condition______"></span><span id="_______condition______"></span><span id="_______CONDITION______"></span> *Condition*   
Specifies a condition. If this evaluates to zero, it is treated as false; otherwise it is true. Enclosing *Condition* in parentheses is optional. *Condition* must be an expression, not a debugger command. It will be evaluated by the default expression evaluator (MASM or C++). For details, see [Numerical Expression Syntax](numerical-expression-syntax.md).

<span id="_______Commands______"></span><span id="_______commands______"></span><span id="_______COMMANDS______"></span> *Commands*   
Specifies one or more commands that will be executed conditionally. This block of commands needs to be enclosed in braces, even if it consists of a single command. Multiple commands should be separated by semicolons, but the final command before the closing brace does not need to be followed by a semicolon.

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For information about other control flow tokens and their use in debugger command programs, see [Using Debugger Command Programs](using-debugger-command-programs.md).

 

 





