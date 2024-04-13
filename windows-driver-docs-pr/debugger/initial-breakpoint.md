---
title: Initial Breakpoint
description: Initial Breakpoint
keywords: ["initial breakpoint", "breakpoints, initial breakpoint"]
ms.date: 06/26/2023
---

# Initial Breakpoint

When the debugger starts a new target application, an initial breakpoint automatically occurs after the main image and all statically-linked DLLs are loaded before any DLL initialization routines are called.

When the debugger attaches to an existing user-mode application, an initial [breakpoint](using-breakpoints.md) occurs immediately.

The **-g** command-line option causes WinDbg or CDB to ignore the initial breakpoint. You can automatically execute a command at this point. For more information about this situation, see [Controlling Exceptions and Events](controlling-exceptions-and-events.md).

If you want to start a new target and break into it when the execution of the actual application is about to begin, do not use the **-g** option. Instead, let the initial breakpoint occur. After the debugger is active, set a breakpoint on the **main** or **winmain** routine and then use the [**g (Go)**](../debuggercmds/g--go-.md) command. All of the initialization procedures then run, and the application stops when execution of the main application is about to begin.

For more information about automatic breakpoints in kernel mode, see [Crashing and Rebooting the Target Computer](crashing-and-rebooting-the-target-computer.md).

## See also

[Using Breakpoints](using-breakpoints.md)

[Breakpoint Syntax](breakpoint-syntax.md)

[bp, bu, bm (Set Breakpoint)](../debuggercmds/bp--bu--bm--set-breakpoint-.md)

[Ambiguous breakpoint resolution](ambiguous-breakpoint-resolution.md)

[Unresolved Breakpoints (bu Breakpoints)](unresolved-breakpoints---bu-breakpoints-.md)
