---
title: Methods of Controlling Breakpoints
description: Methods of Controlling Breakpoints
keywords: ["breakpoints, controlling"]
ms.date: 06/26/2023
---

# Methods of Controlling Breakpoints

You can specify the location of a breakpoint by virtual address, module and routine offsets, or source file and line number (when in source mode). If you put a breakpoint on a routine without an offset, the breakpoint is activated when that routine is entered.

There are several additional kinds of breakpoints:

- A breakpoint can be associated with a certain thread.

- A breakpoint can enable a fixed number of passes through an address before it is triggered.

- A breakpoint can automatically issue certain commands when it is triggered.

- A breakpoint can be set on non-executable memory and watch for that location to be read or written to.

If you are debugging more than one process in user mode, the collection of breakpoints depends on the current process. To view or change a process' breakpoints, you must select the process as the current process. For more information about the current process, see [Controlling Processes and Threads](controlling-processes-and-threads.md).

### Debugger Commands for Controlling and Displaying Breakpoints

To control or display breakpoints, you can use the following methods:

-   Use the [**bl (Breakpoint List)**](../debuggercmds/bl--breakpoint-list-.md) command to list existing breakpoints and their current status.

-   Use the [**.bpcmds (Display Breakpoint Commands)**](../debuggercmds/-bpcmds--display-breakpoint-commands-.md) command to list all breakpoints along with the commands that were used to create them.

-   Use the [**bp (Set Breakpoint)**](../debuggercmds/bp--bu--bm--set-breakpoint-.md) command to set a new breakpoint.

-   Use the [**bu (Set Unresolved Breakpoint)**](../debuggercmds/bp--bu--bm--set-breakpoint-.md) command to set a new breakpoint. Breakpoints that are set with **bu** are called unresolved breakpoints; they have different characteristics than breakpoints that are set with **bp**. For complete details, see [Unresolved Breakpoints (bu Breakpoints)](unresolved-breakpoints---bu-breakpoints-.md).

-   Use the [**bm (Set Symbol Breakpoint)**](../debuggercmds/bp--bu--bm--set-breakpoint-.md) command to set new breakpoints on symbols that match a specified pattern. A breakpoint set with **bm** will be associated with an address (like a **bp** breakpoint) if the **/d** switch is included; it will be unresolved (like a **bu** breakpoint) if this switch is not included.

-   Use the [**ba (Break on Access)**](../debuggercmds/ba--break-on-access-.md) command to set a *processor breakpoint*, also known as a *data breakpoint*. These breakpoints can be triggered when the memory location is written to, when it is read, when it is executed as code, or when kernel I/O occurs. For complete details, see [Processor Breakpoints (ba Breakpoints)](processor-breakpoints---ba-breakpoints-.md).

-   Use the [**bc (Breakpoint Clear)**](../debuggercmds/bc--breakpoint-clear-.md) command to permanently remove one or more breakpoints.

-   Use the [**bd (Breakpoint Disable)**](../debuggercmds/bd--breakpoint-disable-.md) command to temporarily disable one or more breakpoints.

-   Use the [**be (Breakpoint Enable)**](../debuggercmds/be--breakpoint-enable-.md) command to re-enable one or more disabled breakpoints.

-   Use the [**br (Breakpoint Renumber)**](../debuggercmds/br--breakpoint-renumber-.md) command to change the ID of an existing breakpoint.

-   Use the [**bs (Update Breakpoint Command)**](../debuggercmds/bs--update-breakpoint-command-.md) command to change the command associated with an existing breakpoint.

-   Use the [**bsc (Update Conditional Breakpoint)**](../debuggercmds/bsc--update-conditional-breakpoint-.md) command to change the condition under which an existing conditional breakpoint occurs.

In WinDbg, there are several user interface elements that facilitate controlling and displaying breakpoints. See [Setting Breakpoints in WinDbg (Classic)](setting-breakpoints-in-windbg.md).

Each breakpoint has a decimal number called the breakpoint ID associated with it. This number identifies the breakpoint in various commands.

### Breakpoint Commands

You can include a command in a breakpoint that is automatically executed when the breakpoint is hit. For example, the following command breaks at MyFunction+0x47, writes a dump file, and then resumes execution.

```dbgcmd
0:000> bu MyFunction+0x47 ".dump c:\mydump.dmp; g" 
```

**Note**  If you are controlling the user-mode debugger from the kernel debugger, do not use [**g (Go)**](../debuggercmds/g--go-.md) in the breakpoint command string. The serial interface might be unable to keep up with this command, and you will be unable to break back into CDB. For more information about this situation, see [Controlling the User-Mode Debugger from the Kernel Debugger](controlling-the-user-mode-debugger-from-the-kernel-debugger.md).

### Number of Breakpoints

In kernel mode, you can use a maximum of 32 software breakpoints. In user mode, you can use any number of software breakpoints.

The number of processor breakpoints that are supported depends on the target processor architecture.

### Conditional Breakpoints

You can set a breakpoint that is triggered only under certain conditions. For more information about these kinds of breakpoints, see [Setting a Conditional Breakpoint](setting-a-conditional-breakpoint.md).

### Ambiguous Breakpoints

In version 10.0.25310.1001 and later of the debugger engine, ambiguous breakpoint resolution is now supported. Ambiguous breakpoints allow for the debugger to set breakpoints in certain scenarios where a breakpoint expression resolves to multiple locations. For more information, see [Ambiguous breakpoint resolution](ambiguous-breakpoint-resolution.md).

## See also

[Using Breakpoints](using-breakpoints.md)

[Breakpoint Syntax](breakpoint-syntax.md)

[bp, bu, bm (Set Breakpoint)](../debuggercmds/bp--bu--bm--set-breakpoint-.md)

[Unresolved Breakpoints (bu Breakpoints)](unresolved-breakpoints---bu-breakpoints-.md)
