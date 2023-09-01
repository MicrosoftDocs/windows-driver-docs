---
title: Processor Breakpoints (ba Breakpoints)
description: Processor Breakpoints (ba Breakpoints)
keywords: ["breakpoints, processor breakpoints", "breakpoints, data breakpoints", "breakpoints, software breakpoints", "breakpoints, BP versus BA", "software breakpoint", "software breakpoint, overview", "software breakpoint, limitations", "processor breakpoint", "processor breakpoint, overview"]
ms.date: 08/29/2023
---

# Processor Breakpoints (ba Breakpoints)

Breakpoints that are controlled by the processor at the request of the debugger are known as *processor breakpoints* or *data breakpoints*. Breakpoints that are controlled directly by the debugger are known as *software breakpoints*.

**Note**   Although the term *data breakpoint* is commonly used as a synonym for *processor breakpoint*, this term can be misleading. There are two fundamental types of breakpoints: processor breakpoints, which are controlled by the processor, and software breakpoints, which are controlled by the debugger. Processor breakpoints are usually set on program data -- this is the reason they are called "data breakpoints" -- but they can also be set on executable code. Software breakpoints are usually set on executable code, but they can also be set on program data. Unfortunately, it is common in debugging literature to refer to processor breakpoints as "data breakpoints", even when they are set on executable code.

## Processor Breakpoints

A processor breakpoint is triggered when a specific memory location is accessed. There are four types of processor breakpoints, corresponding to the kind of memory access that triggers it:

|Breakpoint type|Action|
|-------------- |----- |
|e (execute)|Triggered when the processor retrieves an instruction from the specified address.|
|r (read/write)|Triggered when the processor reads or writes memory at the specified address.|
|w (write)|Triggered when the processor writes memory at the specified address.|
|i (i/o)|Triggered when the I/O port at the specified Address is accessed.|

Each processor breakpoint has a size associated with it. For example, a **w** (write) processor breakpoint could be set at the address 0x70001008 with a size of four bytes. This would monitor the block of addresses from 0x70001008 to 0x7000100B, inclusive. If this block of memory is written to, the breakpoint will be triggered.

It can happen that the processor performs an operation on a memory region that overlaps with, but is not identical to, the specified region. In the example given in the preceding paragraph, a single write operation that includes the range 0x70001000 to 0x7000100F, or a write operation that includes only the byte at 0x70001009, would be an overlapping operation. In such a situation, whether the breakpoint is triggered is processor-dependent. For details of how this situation is handled on a specific processor, consult the processor archictecture manual and look for "debug register" or "debug control register". To take one specific processor type as an example, on an x86 processor, a read or write breakpoint is triggered whenever the accessed range overlaps the breakpoint range.

Similarly, if an **e** (execute) breakpoint is set on the address 0x00401003, and then a two-byte instruction spanning the addresses 0x00401002 and 0x00401003 is executed, the result is processor-dependent. Again, consult the processor architecture manual for details.

The processor distinguishes between breakpoints set by a user-mode debugger and breakpoints set by a kernel-mode debugger. A user-mode processor breakpoint does not affect any kernel-mode processes. A kernel-mode processor breakpoint might or might not affect a user-mode process, depending on whether the user-mode code is using the debug register state and whether there is a user-mode debugger that is attached.

To apply the current process' existing data breakpoints to a different register context, use the [**.apply\_dbp (Apply Data Breakpoint to Context)**](-apply-dbp--apply-data-breakpoint-to-context-.md) command.

On a multiprocessor computer, each processor breakpoint applies to all processors. For example, if the current processor is 3 and you use the command `ba e1 MyAddress` to put a breakpoint at **MyAddress**, any processor -- not only processor 3 -- that executes at that address triggers the breakpoint. This holds for software breakpoints as well.

## Software Breakpoints

Software breakpoints, unlike processor breakpoints, are controlled by the debugger. When the debugger sets a software breakpoint at some location, it temporarily replaces the contents of that memory location with a break instruction. The debugger remembers the original contents of this location, so that if this memory is displayed in the debugger, the debugger will show the original contents of that memory location, not the break instruction. When the target process executes the code at this location, the break instruction causes the process to break into the debugger. After you have performed whatever actions you choose, you can cause the target to resume execution, and execution will resume with the instruction that was originally in that location.

## Availability of Processor Breakpoint Types

The **i** (i/o) option is available only during kernel-mode debugging.

Not all data sizes can be used with all processor breakpoint types. The permitted sizes depend on the processor of the target computer. For details, see [**ba (Break on Access)**](ba--break-on-access-.md).

## Limitations of Software Breakpoints and Processor Breakpoints

It is possible to specify a data address rather than a program address when using the [**bp**](bp--bu--bm--set-breakpoint-.md) or bm /a commands. However, even if a data location is specified, these commands create software breakpoints, not processor breakpoints. When the debugger places a software breakpoint at some location, it temporarily replaces the contents of that memory location with a break instruction. This does not corrupt the executable image, because the debugger remembers the original contents of this location, and when the target process attempts to execute this code the debugger can respond appropriately. But when a software breakpoint is set in a data location, the resulting overwrite can lead to data corruption. Therefore, setting a software breakpoint on a data location is safe only if you are certain that this location will be used only as executable code.

The **bp**, **bu**, and **bm** commands set software breakpoints by replacing the processor instruction with a break instruction. Therefore these cannot be used in read-only code or any other code that cannot be overwritten. To set a breakpoint in such code, you must use [**ba (Break on Access)**](ba--break-on-access-.md) with the **e** (execute) option.

You cannot create multiple processor breakpoints at the same address that differ only in the command that is automatically executed when the breakpoint is triggered. However, you can create multiple breakpoints at the same address that differ in their other restrictions (for example, you can create multiple breakpoints at the same address by using the **ba** command with different values of the **/p**, **/t**, **/c**, and **/C** options).

The initial breakpoint in a user-mode process (typically set on the **main** function or its equivalent) cannot be a processor breakpoint.

The number of processor breakpoints that are supported depends on the target processor architecture.

## Controlling Software Breakpoints and Processor Breakpoints

Software breakpoints can be created with the [**bp (Set Breakpoint)**](bp--bu--bm--set-breakpoint-.md), **bm (Set Symbol Breakpoint)**, and **bu (Set Unresolved Breakpoint)** commands. Processor breakpoints can be created with the [**ba (Break on Access)**](ba--break-on-access-.md) command. Commands that disable, enable, and modify breakpoints apply to all kinds of breakpoints. Commands that display a list of breakpoints include all breakpoints, and indicate the type of each. For a listing of these commands, see [Methods of Controlling Breakpoints](methods-of-controlling-breakpoints.md).

The WinDbg **Breakpoints** dialog box displays all breakpoints, indicating processor breakpoints with the notation "e", "r", "w", or "i' followed by the size of the block. This dialog box can be used to modify any breakpoint. The **Command** text box on this dialog box can be used to create any type of breakpoint.If a processor breakpoint is desired, begin the input with "ba". When you set a breakpoint by using the mouse in the WinDbg [Disassembly window](disassembly-window.md) or [Source window](source-window.md), the debugger creates an unresolved software breakpoint.

Processor breakpoints are stored in the processor's debug registers. It is possible to set a breakpoint by manually editing a debug register value, but this is strongly discouraged.
