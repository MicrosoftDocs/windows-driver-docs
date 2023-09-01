---
title: .else (WinDbg)
description: The .else token behaves like the else keyword in C.
keywords: [".else Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- .else
api_type:
- NA
---

# .else


The **.else** token behaves like the **else** keyword in C.

```dbgcmd
.if (Condition) { Commands } .else { Commands } 

.if (Condition) { Commands } .elsif (Condition) { Commands } .else { Commands } 
```

## <span id="ddk_token_else_dbg"></span><span id="DDK_TOKEN_ELSE_DBG"></span>Syntax Elements


<span id="_______Commands______"></span><span id="_______commands______"></span><span id="_______COMMANDS______"></span> *Commands*   
Specifies one or more commands that will be executed conditionally. This block of commands needs to be enclosed in braces, even if it consists of a single command. Multiple commands should be separated by semicolons, but the final command before the closing brace does not need to be followed by a semicolon.

### Additional Information

For information about other control flow tokens and their use in debugger command programs, see [Using Debugger Command Programs](using-debugger-command-programs.md).

 

 





