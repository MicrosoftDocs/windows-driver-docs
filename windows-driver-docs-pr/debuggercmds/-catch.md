---
title: ".catch (WinDbg)"
description: "The .catch token is used to prevent a program from terminating if an error occurs.It does not behave like the catch keyword in C++."
keywords: [".catch Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- .catch
api_type:
- NA
---

# .catch


The **.catch** token is used to prevent a program from terminating if an error occurs.

It does not behave like the **catch** keyword in C++.

```dbgsyntax
    Commands ; .catch { Commands } ; Commands 
```

## <span id="ddk_token_catch_dbg"></span><span id="DDK_TOKEN_CATCH_DBG"></span>


## Additional Information

For information about other control flow tokens and their use in debugger command programs, see [Using Debugger Command Programs](../debugger/using-debugger-command-programs.md).

## Remarks

The **.catch** token is followed by braces enclosing one or more commands.

If a command within a **.catch** block generates an error, the error message is displayed, all remaining commands within the braces are ignored, and execution resumes with the first command after the closing brace.

If **.catch** is not used, an error will terminate the entire debugger command program.

You can use [**.leave**](-leave.md) to exit from a **.catch** block.

