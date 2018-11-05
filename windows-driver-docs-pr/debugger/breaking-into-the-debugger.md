---
title: Breaking Into the Debugger
description: Breaking Into the Debugger
ms.assetid: 4fec7170-7480-4a8a-b060-1c8a8c3fb9dc
keywords: ["breaking into the debugger", "DebugBreak function", "DbgBreakPoint function", "KdBreakPoint function", "DbgBreakPointWithStatus function", "KdBreakPointWithStatus function", "ASSERT macro", "ASSERTMSG macro"]
ms.author: domars
ms.date: 08/16/2017
ms.localizationpriority: medium
---

# Breaking Into the Debugger


## <span id="ddk_breaking_into_the_debugger_dbg"></span><span id="DDK_BREAKING_INTO_THE_DEBUGGER_DBG"></span>

User-mode and kernel-mode code use different routines to break into the debugger.

### <span id="user_mode_break_routines"></span><span id="USER_MODE_BREAK_ROUTINES"></span>User-Mode Break Routines

A break routine causes an exception to occur in the current process, so that the calling thread can signal the debugger associated with the calling process.

To break into a debugger from a user-mode program, use the [DebugBreak function](https://msdn.microsoft.com/library/windows/desktop/ms679297(v=vs.85).aspx). 

When a user-mode program calls **DebugBreak**, the following possible actions will occur:

1.  If a user-mode debugger is attached, the program will break into the debugger. This means that the program will pause and the debugger will become active.

2.  If no user-mode debugger is attached, but kernel-mode debugging was enabled at boot time, the entire computer will break into the kernel debugger. If no kernel debugger is attached, the computer will freeze and await a kernel debugger.

3.  If no user-mode debugger is attached, and kernel-mode debugging is not enabled, the program will terminate with an unhandled exception, and the post-mortem (just-in-time) debugger will be activated. For more information, see [Enabling Postmortem Debugging](enabling-postmortem-debugging.md).

### <span id="kernel_mode_break_routines"></span><span id="KERNEL_MODE_BREAK_ROUTINES"></span>Kernel-Mode Break Routines

When a kernel-mode program breaks into the debugger, the entire operating system freezes until the kernel debugger allows execution to resume. If no kernel debugger is present, this is treated as a bug check.

The **DbgBreakPoint** routine works in kernel-mode code, but is otherwise similar to the **DebugBreak** user-mode routine.

**DbgBreakPointWithStatus** also causes a break, but it additionally sends a 32-bit status code to the debugger.

**KdBreakPoint** and **KdBreakPointWithStatus** are identical to **DbgBreakPoint** and **DbgBreakPointWithStatus**, respectively, when compiled in the checked build environment. When compiled in the free build environment, they have no effect.

For complete documentation of these routines, as well as the build environment, see the Windows Driver Kit.

### <span id="kernel_mode_conditional_break_routines"></span><span id="KERNEL_MODE_CONDITIONAL_BREAK_ROUTINES"></span>Kernel-Mode Conditional Break Routines

Two conditional break routines are available for kernel-mode code. These routines test a logical expression. If the expression is false, execution halts and the debugger becomes active.

The **ASSERT** macro causes the debugger to display the failed expression and its location in the program. The **ASSERTMSG** macro is similar, but allows an additional message to be sent to the debugger.

**ASSERT** and **ASSERTMSG** are only active when compiled in the checked build environment. When compiled in the free build environment, they have no effect.

For complete documentation of these routines, as well as the build environment, see the Windows Driver Kit.

 

 





