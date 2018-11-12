---
title: Methods of Controlling Breakpoints
description: Methods of Controlling Breakpoints
ms.assetid: 69de05e8-1b41-403a-a628-88da9528e1ab
keywords: ["breakpoints, controlling"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Methods of Controlling Breakpoints


You can specify the location of a breakpoint by virtual address, module and routine offsets, or source file and line number (when in source mode). If you put a breakpoint on a routine without an offset, the breakpoint is activated when that routine is entered.

There are several additional kinds of breakpoints:

-   A breakpoint can be associated with a certain thread.

-   A breakpoint can enable a fixed number of passes through an address before it is triggered.

-   A breakpoint can automatically issue certain commands when it is triggered.

-   A breakpoint can be set on non-executable memory and watch for that location to be read or written to.

If you are debugging more than one process in user mode, the collection of breakpoints depends on the current process. To view or change a process' breakpoints, you must select the process as the current process. For more information about the current process, see [Controlling Processes and Threads](controlling-processes-and-threads.md).

### <span id="methods_of_controlling_and_displaying_breakpoints"></span><span id="METHODS_OF_CONTROLLING_AND_DISPLAYING_BREAKPOINTS"></span>Debugger Commands for Controlling and Displaying Breakpoints

To control or display breakpoints, you can use the following methods:

-   Use the [**bl (Breakpoint List)**](bl--breakpoint-list-.md) command to list existing breakpoints and their current status.

-   Use the [**.bpcmds (Display Breakpoint Commands)**](-bpcmds--display-breakpoint-commands-.md) command to list all breakpoints along with the commands that were used to create them.

-   Use the [**bp (Set Breakpoint)**](bp--bu--bm--set-breakpoint-.md) command to set a new breakpoint.

-   Use the [**bu (Set Unresolved Breakpoint)**](bp--bu--bm--set-breakpoint-.md) command to set a new breakpoint. Breakpoints that are set with **bu** are called unresolved breakpoints; they have different characteristics than breakpoints that are set with **bp**. For complete details, see [Unresolved Breakpoints (bu Breakpoints)](unresolved-breakpoints---bu-breakpoints-.md).

-   Use the [**bm (Set Symbol Breakpoint)**](bp--bu--bm--set-breakpoint-.md) command to set new breakpoints on symbols that match a specified pattern. A breakpoint set with **bm** will be associated with an address (like a **bp** breakpoint) if the **/d** switch is included; it will be unresolved (like a **bu** breakpoint) if this switch is not included.

-   Use the [**ba (Break on Access)**](ba--break-on-access-.md) command to set a *processor breakpoint*, also known as a *data breakpoint*. These breakpoints can be triggered when the memory location is written to, when it is read, when it is executed as code, or when kernel I/O occurs. For complete details, see [Processor Breakpoints (ba Breakpoints)](processor-breakpoints---ba-breakpoints-.md).

-   Use the [**bc (Breakpoint Clear)**](bc--breakpoint-clear-.md) command to permanently remove one or more breakpoints.

-   Use the [**bd (Breakpoint Disable)**](bd--breakpoint-disable-.md) command to temporarily disable one or more breakpoints.

-   Use the [**be (Breakpoint Enable)**](be--breakpoint-enable-.md) command to re-enable one or more disabled breakpoints.

-   Use the [**br (Breakpoint Renumber)**](br--breakpoint-renumber-.md) command to change the ID of an existing breakpoint.

-   Use the [**bs (Update Breakpoint Command)**](bs--update-breakpoint-command-.md) command to change the command associated with an existing breakpoint.

-   Use the [**bsc (Update Conditional Breakpoint)**](bsc--update-conditional-breakpoint-.md) command to change the condition under which an existing conditional breakpoint occurs.

In Visual Studio and WinDbg, there are several user interface elements that facilitate controlling and displaying breakpoints. See [Setting Breakpoints in Visual Studio](setting-breakpoints-in-visual-studio.md) and [Setting Breakpoints in WinDbg](setting-breakpoints-in-windbg.md).

Each breakpoint has a decimal number called the breakpoint ID associated with it. This number identifies the breakpoint in various commands.

### <span id="breakpoint_commands"></span><span id="BREAKPOINT_COMMANDS"></span>Breakpoint Commands

You can include a command in a breakpoint that is automatically executed when the breakpoint is hit. For example, the following command breaks at MyFunction+0x47, writes a dump file, and then resumes execution.

```dbgcmd
0:000> bu MyFunction+0x47 ".dump c:\mydump.dmp; g" 
```

**Note**  If you are controlling the user-mode debugger from the kernel debugger, do not use [**g (Go)**](g--go-.md) in the breakpoint command string. The serial interface might be unable to keep up with this command, and you will be unable to break back into CDB. For more information about this situation, see [Controlling the User-Mode Debugger from the Kernel Debugger](controlling-the-user-mode-debugger-from-the-kernel-debugger.md).

 

### <span id="number_of_breakpoints"></span><span id="NUMBER_OF_BREAKPOINTS"></span>Number of Breakpoints

In kernel mode, you can use a maximum of 32 software breakpoints. In user mode, you can use any number of software breakpoints.

The number of processor breakpoints that are supported depends on the target processor architecture.

### <span id="conditional_breakpoints"></span><span id="CONDITIONAL_BREAKPOINTS"></span>Conditional Breakpoints

You can set a breakpoint that is triggered only under certain conditions. For more information about these kinds of breakpoints, see [Setting a Conditional Breakpoint](setting-a-conditional-breakpoint.md).

 

 





