---
title: Breaking Into the Debugger
description: Breaking Into the Debugger
ms.assetid: c52c99a2-5db0-49e8-88a7-db075a32c26b
keywords:
- debugging drivers WDK , breaking into the debugger
- breaking into the debugger WDK
- user-mode break routines WDK
- kernel-mode break routines WDK
- break routines WDK
- conditional break macros WDK
- break macros WDK
- routines WDK debugging , break
ms.date: 06/04/2020
ms.localizationpriority: medium
---

# Breaking Into the Debugger

User-mode and kernel-mode drivers use different routines to break into the debugger.

> [!NOTE]
> Checked builds were available on older versions of Windows, before Windows 10 version 1803.
> Use tools such as Driver Verifier and GFlags to check driver code in later versions of Windows.

## User-Mode Break Routines

A break routine causes an exception to occur in the current process, so that the calling thread can signal the debugger associated with the calling process.

To break into a debugger from a user-mode program, use the **DebugBreak** routine. Its prototype is as follows:

```cpp
VOID DebugBreak(VOID);
```

This routine can be called by any user-mode driver that includes the windows.h header. For complete documentation of this routine and other user-mode routines useful for debugging, see the Microsoft Windows SDK.

When a user-mode program calls **DebugBreak**, the following possible actions will occur:

1. If a user-mode debugger is attached, the program will break into the debugger. This means that the program will pause and the debugger will become active.

1. If a user-mode debugger is not attached, but kernel-mode debugging was enabled at boot time, the entire computer will break into the kernel debugger. If a kernel debugger is not attached, the computer will freeze and await a kernel debugger.

1. If a user-mode debugger is not attached, and kernel-mode debugging is not enabled, the program will terminate with an unhandled exception, and the post-mortem (just-in-time) debugger will be activated. By default, the postmortem debugger is Dr. Watson, which will create a crash dump file and then ask you if you want to send this crash dump file to Microsoft.

## Kernel-Mode Break Routines

When a kernel-mode program breaks into the debugger, the entire operating system freezes until the kernel debugger allows execution to resume. If a kernel debugger is not present, this is treated as a bug check.

The [**DbgBreakPoint**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nf-wdm-dbgbreakpoint) routine works in kernel-mode code, but is otherwise similar to the **DebugBreak** user-mode routine.

The [**DbgBreakPointWithStatus**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nf-wdm-dbgbreakpointwithstatus) routine also causes a break, but it additionally sends a 32-bit status code to the debugger.

The [**KdBreakPoint**](https://docs.microsoft.com/previous-versions/windows/hardware/previsioning-framework/ff548063(v=vs.85)) and [**KdBreakPointWithStatus**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nf-wdm-kdbreakpointwithstatus) routines are identical to **DbgBreakPoint** and **DbgBreakPointWithStatus**, respectively, when compiled in the checked build environment. When compiled in the free build environment, they have no effect.

## Kernel-Mode Conditional Break Macros

Two conditional break macros are available for kernel-mode drivers:

- The [**ASSERT**](https://docs.microsoft.com/previous-versions/windows/hardware/previsioning-framework/ff542107(v=vs.85)) macro tests a logical expression. If the expression is false, execution halts and the debugger becomes active. The failed expression and its location in the program are displayed in the debugger.

- The [**ASSERTMSG**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nf-wdm-assertmsg) macro is identical to **ASSERT** except that it allows an additional message to be sent to the debugger.

**ASSERT** and **ASSERTMSG** are only active when compiled in the checked build environment. When compiled in the free build environment, they have no effect.
