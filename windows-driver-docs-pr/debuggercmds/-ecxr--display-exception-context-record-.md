---
title: ".ecxr (Display Exception Context Record)"
description: "The .ecxr command displays the context record that is associated with the current exception."
keywords: ["Display Exception Context Record (.cxr) command", "exceptions, exception context record", ".ecxr (Display Exception Context Record) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- .ecxr (Display Exception Context Record)
api_type:
- NA
---

# .ecxr (Display Exception Context Record)

The **.ecxr** command displays the context record that is associated with the current exception.

```dbgcmd
.ecxr
```

## Environment

| Item      | Description                      |
|-----------|----------------------------------|
| Modes     | User mode                        |
| Targets   | Crash dump only (minidumps only) |
| Platforms | All                              |

### Additional Information

For more information about the register context and other context settings, see [Changing Contexts](../debugger/changing-contexts.md).

## Remarks

The **.ecxr** command locates the current exception's context information and displays the important registers for the specified context record.

This command also instructs the debugger to use the context record that is associated with the current exception as the register context. After you run **.ecxr**, the debugger can access the most important registers and the stack trace for this thread. This register context persists until you enable the target to execute, change the current process or thread, or use another register context command ([**.cxr**](-cxr--display-context-record-.md) or **.ecxr**). For more information about register contexts, see [Register Context](../debugger/changing-contexts.md#register-context).

The [**.excr**](-excr--display-exception-context-record-.md) command is a synonym command and has identical functionality.

## See also

[**.excr**](-excr--display-exception-context-record-.md)

[Changing Contexts](../debugger/changing-contexts.md)

[Register Context](../debugger/changing-contexts.md#register-context)

