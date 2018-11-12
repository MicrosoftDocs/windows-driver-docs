---
title: ba (Break on Access)
description: The ba command sets a processor breakpoint (often called, less accurately, a data breakpoint). This breakpoint is triggered when the specified memory is accessed.
ms.assetid: 0d39d883-363e-421b-a1b8-08bf2d216724
keywords: ["ba (Break on Access) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- ba (Break on Access)
api_type:
- NA
ms.localizationpriority: medium
---

# ba (Break on Access)


The **ba** command sets a processor breakpoint (often called, less accurately, a *data breakpoint*). This breakpoint is triggered when the specified memory is accessed.

User-Mode

```dbgcmd
[~Thread] ba[ID] Access Size [Options] [Address [Passes]] ["CommandString"]
```

Kernel-Mode

```dbgcmd
ba[ID] Access Size [Options] [Address [Passes]] ["CommandString"]
```

## <span id="ddk_cmd_break_on_access_dbg"></span><span id="DDK_CMD_BREAK_ON_ACCESS_DBG"></span>Parameters


<span id="_______Thread______"></span><span id="_______thread______"></span><span id="_______THREAD______"></span> *Thread*   
Specifies the thread that the breakpoint applies to. For more information about syntax, see [Thread Syntax](thread-syntax.md). You can specify threads only in user mode.

<span id="_______ID______"></span><span id="_______id______"></span> *ID*   
Specifies an optional number that identifies the breakpoint. If you do not specify *ID*, the first available breakpoint number is used. You cannot add space between **ba** and the ID number. Each processor supports only a limited number of processor breakpoints, but there is no restriction on the value of the *ID* number. If you enclose *ID* in square brackets (\[\]), *ID* can include any expression. For more information about the syntax, see [Numerical Expression Syntax](numerical-expression-syntax.md).

<span id="_______Access______"></span><span id="_______access______"></span><span id="_______ACCESS______"></span> *Access*   
Specifies the type of access that satisfies the breakpoint. This parameter can be one of the following values.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Option</th>
<th align="left">Action</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>e</strong> (execute)</p></td>
<td align="left"><p>Breaks into the debugger when the CPU retrieves an instruction from the specified address.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>r</strong> (read/write)</p></td>
<td align="left"><p>Breaks into the debugger when the CPU reads or writes at the specified address.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>w</strong> (write)</p></td>
<td align="left"><p>Breaks into the debugger when the CPU writes at the specified address.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>i</strong> (i/o)</p></td>
<td align="left"><p>(Microsoft Windows XP and later versions, kernel mode only, x86-based systems only) Breaks into the debugger when the I/O port at the specified <em>Address</em> is accessed.</p></td>
</tr>
</tbody>
</table>

 

<span id="_______Size______"></span><span id="_______size______"></span><span id="_______SIZE______"></span> *Size*   
Specifies the size of the location, in bytes, to monitor for access. On an x86-based processor, this parameter can be 1, 2, or 4. However, if *Access* equals **e**, *Size* must be 1.

On an x64-based processor, this parameter can be 1, 2, 4, or 8. However, if *Access* equals **e**, *Size* must be 1.

<span id="_______Options______"></span><span id="_______options______"></span><span id="_______OPTIONS______"></span> *Options*   
Specifies breakpoint options. You can use any number of the following options, except as indicated:

<span id="_1"></span>**/1**  
Creates a "one-shot" breakpoint. After this breakpoint is triggered, the breakpoint is permanently removed from the breakpoint list.

<span id="_p_EProcess"></span><span id="_p_eprocess"></span><span id="_P_EPROCESS"></span>**/p** *EProcess*  
(Kernel mode only) Specifies a process that is associated with this breakpoint. *EProcess* should be the actual address of the EPROCESS structure, not the PID. The breakpoint is triggered only if it is encountered in the context of this process.

<span id="_t_EThread"></span><span id="_t_ethread"></span><span id="_T_ETHREAD"></span>**/t** *EThread*  
(Kernel mode only) Specifies a thread that is associated with this breakpoint. *EThread* should be the actual address of the ETHREAD structure, not the thread ID. The breakpoint is triggered only if it is encountered in the context of this thread. If you use **/p** *EProcess* and **/t** *EThread* , you can enter them in either order.

<span id="_c_MaxCallStackDepth"></span><span id="_c_maxcallstackdepth"></span><span id="_C_MAXCALLSTACKDEPTH"></span>**/c** *MaxCallStackDepth*  
Causes the breakpoint to be active only when the call stack depth is less than *MaxCallStackDepth*. You cannot combine this option together with **/C**.

<span id="_C_MinCallStackDepth"></span><span id="_c_mincallstackdepth"></span><span id="_C_MINCALLSTACKDEPTH"></span>**/C** *MinCallStackDepth*  
Causes the breakpoint to be active only when the call stack depth is larger than *MinCallStackDepth*. You cannot combine this option together with **/c**.

<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies any valid address. If the application accesses memory at this address, the debugger stops execution and displays the current values of all registers and flags. This address must be an offset and suitably aligned to match the *Size* parameter. (For example, if *Size* is 4, *Address* must be a multiple of 4.) If you omit *Address*, the current instruction pointer is used. For more information about the syntax, see [Address and Address Range Syntax](address-and-address-range-syntax.md).

<span id="_______Passes______"></span><span id="_______passes______"></span><span id="_______PASSES______"></span> *Passes*   
Specifies the number of times the breakpoint is passed by until it activates. This number can be any 16-bit value. The number of times the program counter passes through this point without breaking is one less than the value of this number. Therefore, omitting this number is the same as setting it equal to 1. Note also that this number counts only the times that the application *executes* past this point. Stepping or tracing past this point does not count. After the full count is reached, you can reset this number only by clearing and resetting the breakpoint.

<span id="_______CommandString______"></span><span id="_______commandstring______"></span><span id="_______COMMANDSTRING______"></span> *CommandString*   
Specifies a list of commands to execute every time that the breakpoint is encountered the specified number of times. These commands are executed only if the breakpoint is hit after you issue a [**g (Go)**](g--go-.md) command, instead of after a [**t (Trace)**](t--trace-.md) or [**p (Step)**](p--step-.md) command. Debugger commands in *CommandString* can include parameters.

You must enclose this command string in quotation marks, and you should separate multiple commands by semicolons. You can use standard C control characters (such as **\\n** and **\\"**). Semicolons that are contained in second-level quotation marks (**\\"**) are interpreted as part of the embedded quoted string.

This parameter is optional.

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>User mode, kernel mode</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>Live debugging only</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>All</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information on processor breakpoints, see [Processor Breakpoints (ba Breakpoints)](processor-breakpoints---ba-breakpoints-.md). For more information about and examples of using breakpoints, other breakpoint commands and methods of controlling breakpoints, and information about how to set breakpoints in user space from a kernel debugger, see [Using Breakpoints](using-breakpoints.md). For more information about conditional breakpoints, see [Setting a Conditional Breakpoint](setting-a-conditional-breakpoint.md).

Remarks
-------

The debugger uses the *ID* number to refer to the breakpoint in later [**bc (Breakpoint Clear)**](bc--breakpoint-clear-.md), [**bd (Breakpoint Disable)**](bd--breakpoint-disable-.md), and [**be (Breakpoint Enable)**](be--breakpoint-enable-.md) commands.

Use the [**bl (Breakpoint List)**](bl--breakpoint-list-.md) command to list all existing breakpoints, their ID numbers, and their status.

Use the [**.bpcmds (Display Breakpoint Commands)**](-bpcmds--display-breakpoint-commands-.md) command to list all existing breakpoints, their ID numbers, and the commands that were used to create them.

Each processor breakpoint has a size associated with it. For example, a **w** (write) processor breakpoint could be set at the address 0x70001008 with a size of four bytes. This would monitor the block of addresses from 0x70001008 to 0x7000100B, inclusive. If this block of memory is written to, the breakpoint will be triggered.

It can happen that the processor performs an operation on a memory region that *overlaps* with, but is not identical to, the specified region. In this example, a single write operation that includes the range 0x70001000 to 0x7000100F, or a write operation that includes only the byte at 0x70001009, would be an overlapping operation. In such a situation, whether the breakpoint is triggered is processor-dependent. You should consult the processor manual for specific details. To take one specific instance, on an x86 processor, a read or write breakpoint is triggered whenever the accessed range overlaps the breakpoint range.

Similarly, if an **e** (execute) breakpoint is set on the address 0x00401003, and then a two-byte instruction spanning the addresses 0x00401002 and 0x00401003 is executed, the result is processor-dependent. Again, consult the processor architecture manual for details.

The processor distinguishes between breakpoints set by a user-mode debugger and breakpoints set by a kernel-mode debugger. A user-mode processor breakpoint does not affect any kernel-mode processes. A kernel-mode processor breakpoint might or might not affect a user-mode process, depending on whether the user-mode code is using the debug register state and whether there is a user-mode debugger that is attached.

To apply the current process' existing data breakpoints to a different register context, use the [**.apply\_dbp (Apply Data Breakpoint to Context)**](-apply-dbp--apply-data-breakpoint-to-context-.md) command.

On a multiprocessor computer, each processor breakpoint applies to all processors. For example, if the current processor is 3 and you use the command `ba e1 MyAddress` to put a breakpoint at MyAddress, any processor -- not only processor 3 -- that executes at that address triggers the breakpoint. (This holds for software breakpoints as well.)

You cannot create multiple processor breakpoints at the same address that differ only in their *CommandString* values. However, you can create multiple breakpoints at the same address that have different restrictions (for example, different values of the **/p**, **/t**, **/c**, and **/C** options).

For more details on processor breakpoints, and additional restrictions that apply to them, see [Processor Breakpoints (ba Breakpoints)](processor-breakpoints---ba-breakpoints-.md).

The following examples show the **ba** command. The following command sets a breakpoint for read access on 4 bytes of the variable myVar.

```dbgcmd
0:000> ba r4 myVar
```

The following command adds a breakpoint on all serial ports with addresses from 0x3F8 through 0x3FB. This breakpoint is triggered if anything is read or written to these ports.

```dbgcmd
kd> ba i4 3f8
```

 

 





