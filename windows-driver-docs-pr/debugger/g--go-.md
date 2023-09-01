---
title: g (Go)
description: The g command starts executing the given process or thread. Execution will halt at the end of the program, when BreakAddress is hit, or when another event causes the debugger to stop.
keywords: ["g (Go) Windows Debugging"]
ms.date: 08/29/2023
topic_type:
- apiref
ms.topic: reference
api_name:
- g (Go)
api_type:
- NA
---

# g (Go)

The **g** command starts executing the given process or thread. Execution will halt at the end of the program, when *BreakAddress* is hit, or when another event causes the debugger to stop.

User-Mode Syntax

```dbgcmd
[~Thread] g[a] [= StartAddress] [BreakAddress ... [; BreakCommands]]
```

Kernel-Mode Syntax

```dbgcmd
g[a] [= StartAddress] [BreakAddress ... [; BreakCommands]] 
```

## Parameters

*Thread*

(User mode only) Specifies the thread to execute. For syntax details, see [Thread Syntax](thread-syntax.md).

**a**

Causes any breakpoint created by this command to be a processor breakpoint (like those created by [**ba**](ba--break-on-access-.md)) rather than a software breakpoint (like those created by [**bp**](bp--bu--bm--set-breakpoint-.md) and **bm**). If *BreakAddress* is not specified, no breakpoint is created and the **a** flag has no effect.

*StartAddress*

Specifies the address where execution should begin. If this is not specified, the debugger passes execution to the address specified by the current value of the instruction pointer. For more syntax details, see [Address and Address Range Syntax](address-and-address-range-syntax.md).

*BreakAddress*

Specifies the address for a breakpoint. If *BreakAddress* is specified, it must specify an instruction address (that is, the address must contain the first byte of an instruction). Up to ten break addresses, in any order, can be specified at one time. If *BreakAddress* cannot be resolved, it is stored as an [unresolved breakpoint](unresolved-breakpoints---bu-breakpoints-.md). For more syntax details, see [Address and Address Range Syntax](address-and-address-range-syntax.md).

*BreakCommands*

Specifies one or more commands to be automatically executed when the breakpoint specified by *BreakAddress* is hit. The *BreakCommands* parameter must be preceded by a semicolon. If multiple *BreakAddress* values are specified, *BreakCommands* applies to all of them.

**Note**   The *BreakCommands* parameter is only available when you are embedding this command within a command string used by another command -- for example, within another breakpoint command or within an except or event setting. On a command line, the semicolon will terminate the **g** command, and any additional commands listed after the semicolon will be executed immediately after the **g** command is done.

### Environment

|  Item       | Description               |
|-----------|------------------------|
| Modes     | user mode, kernel mode |
| Targets   | live debugging only    |
| Platforms | all                    |

### Additional Information

For other methods of issuing this command and an overview of related commands, see [Controlling the Target](controlling-the-target.md).

## Remarks

If *Thread* is specified, then the **g** command is executed with the specified thread unfrozen and all others frozen. For example, if the **~123g**, **~\#g**, or **~\*g** command is specified, the specified threads are unfrozen and all others are frozen.

## See also

[gu (Go Up)](gu--go-up-.md)

[gh (Go with Exception Handled)](gh--go-with-exception-handled-.md)