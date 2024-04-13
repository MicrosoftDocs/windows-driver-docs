---
title: ".f+, .f- (Shift Local Context)"
description: "The .f+ command shifts the frame index to the next frame in the current stack. The .f- command shifts the frame index to the previous frame in the current stack."
keywords: [".f+, .f- (Shift Local Context) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- .f+, .f- (Shift Local Context)
api_type:
- NA
---

# .f+, .f- (Shift Local Context)


The **.f+** command shifts the frame index to the next frame in the current stack. The **.f-** command shifts the frame index to the previous frame in the current stack.

```dbgcmd
.f+  
.f-  
```

## Environment

|  Item  | Description          |
|--------|----------------------|
|Modes   |User mode, kernel mode|
|Targets |Live, crash dump      |
|Platforms|All                  |

 

## Additional Information

For more information about the local context and other context settings, see [Changing Contexts](../debugger/changing-contexts.md). For more information about how to display local variables and other memory-related commands, see [Reading and Writing Memory](../debugger/reading-and-writing-memory.md).

## Remarks

The *frame* specifies the local context (scope) that the debugger uses to interpret local variables

The **.f+** and .f- commands are shortcuts for moving to the next and previous frames in the current stack. These commands are equivalent to the following [**.frame**](-frame--set-local-context-.md) commands, but the **.f** commands are shorter for convenience:

-   **.f+** is the same as **.frame @$frame + 1**.

-   **.f-** is the same as **.frame @$frame - 1**.

The dollar sign ($) identifies the frame value as a [pseudo-register](pseudo-register-syntax.md). The at sign (@ causes the debugger to access the value more quickly, because it notifies the debugger that a string is a register or pseudo-register.

When an application is running, the meaning of local variables depends on the location of the program counter, because the scope of such variables extends only to the function that they are defined in. Unless you use an **.f+** or **.f-** command (or a [**.frame**](-frame--set-local-context-.md) command), the debugger uses the scope of the current function (the current frame on the stack) as the local context.

The *frame number* is the position of the stack frame within the stack trace. You can view this stack trace by using the [**k, kb, kc, kd, kp, kP, kv (Display Stack Backtrace)**](k--kb--kc--kd--kp--kp--kv--display-stack-backtrace-.md) command or the [Calls window](../debugger/calls-window.md). The first line (the current frame) represents frame number 0. The subsequent lines represent frame numbers 1, 2, 3, and so on.

You can set the local context to a different stack frame to view new local variable information. However, the actual variables that are available depend on the code that is executed.

The debugger resets the local context to the scope of the program counter if any program execution occurs. The local context is reset to the top stack frame if the register context is changed.

