---
title: "gu (Go Up)"
description: "The gu command causes the target to execute until the current function is complete."
keywords: ["gu (Go Up) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- gu (Go Up)
api_type:
- NA
---

# gu (Go Up)


The **gu** command causes the target to execute until the current function is complete.

User-Mode Syntax

```dbgcmd
[~Thread] gu 
```

Kernel-Mode Syntax

```dbgcmd
gu
```

## <span id="ddk_cmd_go_up_dbg"></span><span id="DDK_CMD_GO_UP_DBG"></span>Parameters


<span id="_______Thread______"></span><span id="_______thread______"></span><span id="_______THREAD______"></span> *Thread*   
(User mode only) Specifies the thread to execute. This thread must have been stopped by an exception. For syntax details, see [Thread Syntax](thread-syntax.md).

## Environment

|  Item       | Description               |
|-----------|------------------------|
| Modes     | user mode, kernel mode |
| Targets   | live debugging only    |
| Platforms | all                    |

 

## Additional Information

For other methods of issuing this command and an overview of related commands, see [Controlling the Target](../debugger/controlling-the-target.md).

## Remarks

The **gu** command executes the target until the current function call returns.

If the current function is called recursively, the **gu** command will not halt execution until the *current instance* of the current function returns. In this way, **gu** differs from **g @$ra**, which will halt any time the return address of this function is hit.

**Note**   The **gu** command distinguishes different instances of a function by measuring the call stack depth. Executing this command in assembly mode after the arguments have been pushed to the stack and just before the call is made may cause this measurement to be incorrect. Function returns that are optimized away by the compiler may similarly cause this command to stop at the wrong instance of this return. These errors are rare, and can only happen during recursive function calls.

 

If *Thread* is specified, then the **gu** command is executed with the specified thread unfrozen and all others frozen. For example, if the **~123gu**, **~\#gu**, or **~\*gu** command is specified, the specified threads are unfrozen and all others are frozen.

