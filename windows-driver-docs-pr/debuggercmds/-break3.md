---
title: ".break (WinDbg)"
description: "The .break token behaves like the break keyword in C."
keywords: [".break Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- .break
api_type:
- NA
---

# .break


The **.break** token behaves like the **break** keyword in C.

```dbgcmd
 .for (...) { ... ; .if (Condition) .break ; ...} 

.while (...) { ... ; .if (Condition) .break ; ...} 

.do { ... ; .if (Condition) .break ; ...} (...) 
```

## <span id="ddk_token_break_dbg"></span><span id="DDK_TOKEN_BREAK_DBG"></span>


## Additional Information

For information about other control flow tokens and their use in debugger command programs, see [Using Debugger Command Programs](../debugger/using-debugger-command-programs.md).

## Remarks

The **.break** token can be used within any [**.for**](-for.md), [**.while**](-while.md), or [**.do**](-do.md) loop.

Since there is no control flow token equivalent to the C **goto** statement, you will usually use the **.break** token within an [**.if**](-if.md) conditional, as shown in the syntax examples above. However, this is not actually required.

