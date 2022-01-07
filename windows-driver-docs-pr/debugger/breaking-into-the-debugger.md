---
title: Breaking Into the Debugger
description: Breaking Into the Debugger
keywords: ["breaking into the debugger", "DebugBreak function", "DbgBreakPoint function", "KdBreakPoint function", "DbgBreakPointWithStatus function", "KdBreakPointWithStatus function", "ASSERT macro", "ASSERTMSG macro"]
ms.date: 07/20/2020
---

# Breaking Into the Debugger

User-mode and kernel-mode code use different routines to break into the debugger.

## User-Mode Break Routines

A break routine causes an exception to occur in the current process, so that the calling thread can signal the debugger associated with the calling process.

To break into a debugger from a user-mode program, use the [DebugBreak function](/windows/win32/api/debugapi/nf-debugapi-debugbreak). Its prototype is as follows:

```cpp
VOID DebugBreak(VOID);
```

When a user-mode program calls **DebugBreak**, the following possible actions will occur:

1. If a user-mode debugger is attached, the program will break into the debugger. This means that the program will pause and the debugger will become active.

2. If a user-mode debugger is not attached, but kernel-mode debugging was enabled at boot time, the entire computer will break into the kernel debugger. If a kernel debugger is not attached, the computer will freeze and await a kernel debugger.

3. If a user-mode debugger is not attached, and kernel-mode debugging is not enabled, the program will terminate with an unhandled exception, and the post-mortem (just-in-time) debugger will be activated. For more information, see [Enabling Postmortem Debugging](enabling-postmortem-debugging.md).

## Kernel-Mode Break Routines

When a kernel-mode program breaks into the debugger, the entire operating system freezes until the kernel debugger allows execution to resume. If no kernel debugger is present, this is treated as a bug check.

The [**DbgBreakPoint**](/windows-hardware/drivers/ddi/wdm/nf-wdm-dbgbreakpoint) routine works in kernel-mode code, but is otherwise similar to the **DebugBreak** user-mode routine.

The [**DbgBreakPointWithStatus**](/windows-hardware/drivers/ddi/wdm/nf-wdm-dbgbreakpointwithstatus) routine also causes a break, but it additionally sends a 32-bit status code to the debugger.

The [**KdBreakPoint**](/previous-versions/windows/hardware/previsioning-framework/ff548063(v=vs.85)) and [**KdBreakPointWithStatus**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kdbreakpointwithstatus) routines are identical to **DbgBreakPoint** and **DbgBreakPointWithStatus**, respectively, when compiled in the checked build environment. When compiled in the free build environment, they have no effect.

## Kernel-Mode Conditional Break Routines

Two conditional break routines are available for kernel-mode code. These routines test a logical expression. If the expression is false, execution halts and the debugger becomes active.

- The [**ASSERT**](/previous-versions/windows/hardware/previsioning-framework/ff542107(v=vs.85)) macro tests a logical expression. If the expression is false, execution halts and the debugger becomes active. The failed expression and its location in the program are displayed in the debugger.

- The [**ASSERTMSG**](/windows-hardware/drivers/ddi/wdm/nf-wdm-assertmsg) macro is identical to **ASSERT** except that it allows an additional message to be sent to the debugger.

**ASSERT** and **ASSERTMSG** are only active when compiled in the checked build environment. When compiled in the free build environment, they have no effect.
