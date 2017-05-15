---
title: Breaking Into the Debugger
description: Breaking Into the Debugger
ms.assetid: 4fec7170-7480-4a8a-b060-1c8a8c3fb9dc
keywords: ["breaking into the debugger", "DebugBreak function", "DbgBreakPoint function", "KdBreakPoint function", "DbgBreakPointWithStatus function", "KdBreakPointWithStatus function", "ASSERT macro", "ASSERTMSG macro"]
---

# Breaking Into the Debugger


## <span id="ddk_breaking_into_the_debugger_dbg"></span><span id="DDK_BREAKING_INTO_THE_DEBUGGER_DBG"></span>


User-mode and kernel-mode code use different routines to break into the debugger.

### <span id="user_mode_break_routines"></span><span id="USER_MODE_BREAK_ROUTINES"></span>User-Mode Break Routines

A break routine causes an exception to occur in the current process, so that the calling thread can signal the debugger associated with the calling process.

To break into a debugger from a user-mode program, use the **DebugBreak** routine. For complete documentation of this routine, see the Microsoft Windows SDK.

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Breaking%20Into%20the%20Debugger%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




