---
title: bp, bu, bm (Set Breakpoint)
description: The bp, bu, and bm commands set one or more software breakpoints. You can combine locations, conditions, and options to set different kinds of software breakpoints.
ms.assetid: 77d095fe-06d1-4842-ad49-8420ab4d5d72
keywords: ["bp, bu, bm (Set Breakpoint) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- bp, bu, bm (Set Breakpoint)
api_type:
- NA
ms.localizationpriority: medium
---

# bp, bu, bm (Set Breakpoint)


The **bp**, **bu**, and **bm** commands set one or more software breakpoints. You can combine locations, conditions, and options to set different kinds of software breakpoints.

User-Mode

```dbgcmd
[~Thread] bp[ID] [Options] [Address [Passes]] ["CommandString"] 
[~Thread] bu[ID] [Options] [Address [Passes]] ["CommandString"] 
[~Thread] bm [Options] SymbolPattern [Passes] ["CommandString"]
```

Kernel-Mode

```dbgcmd
bp[ID] [Options] [Address [Passes]] ["CommandString"] 
bu[ID] [Options] [Address [Passes]] ["CommandString"] 
bm [Options] SymbolPattern [Passes] ["CommandString"]
```

## <span id="ddk_cmd_set_breakpoint_dbg"></span><span id="DDK_CMD_SET_BREAKPOINT_DBG"></span>Parameters


<span id="_______Thread______"></span><span id="_______thread______"></span><span id="_______THREAD______"></span> *Thread*   
Specifies the thread that the breakpoint applies to. For more information about the syntax, see [Thread Syntax](thread-syntax.md). You can specify threads only in user mode. If you do not specify a thread, the breakpoint applies to all threads.

<span id="_______ID______"></span><span id="_______id______"></span> *ID*   
Specifies a decimal number that identifies a breakpoint.

The debugger assigns the *ID* when it creates the breakpoint, but you can change it by using the [**br (Breakpoint Renumber)**](br--breakpoint-renumber-.md) command. You can use the *ID* to refer to the breakpoint in later debugger commands. To display the *ID* of a breakpoint, use the [**bl (Breakpoint List)**](bl--breakpoint-list-.md) command.

When you use *ID* in a command, do not type a space between the command (**bp** or **bu**) and the ID number.

The *ID* parameter is always optional. If you do not specify *ID*, the debugger uses the first available breakpoint number. In kernel mode, you can set only 32 breakpoints. In user mode, you can set any number of breakpoints. In either case, there is no restriction on the value of the *ID* number. If you enclose *ID* in square brackets (**\[\]**), *ID* can include any expression. For more information about the syntax, see [Numerical Expression Syntax](numerical-expression-syntax.md).

<span id="_______Options______"></span><span id="_______options______"></span><span id="_______OPTIONS______"></span> *Options*   
Specifies breakpoint options. You can specify any number of the following options, except as indicated:

<span id="_1"></span>**/1**  
Creates a "one-shot" breakpoint. After this breakpoint is triggered, it is deleted from the breakpoint list.

<span id="_f_PredNum"></span><span id="_f_prednum"></span><span id="_F_PREDNUM"></span>**/f** *PredNum*  
(Itanium-based only, user mode only) Specifies a predicate number. The breakpoint is predicated with the corresponding predicate register. (For example, **bp /f 4** *address* sets a breakpoint that is predicated with the **p4** predicate register.)

<span id="_p_EProcess"></span><span id="_p_eprocess"></span><span id="_P_EPROCESS"></span>**/p** *EProcess*  
(Kernel-mode only) Specifies a process that is associated with this breakpoint. *EProcess* should be the actual address of the EPROCESS structure, not the PID. The breakpoint is triggered only if it is encountered in the context of this process.

<span id="_t_EThread"></span><span id="_t_ethread"></span><span id="_T_ETHREAD"></span>**/t** *EThread*  
(Kernel-mode only) Specifies a thread that is associated with this breakpoint. *EThread* should be the actual address of the ETHREAD structure, not the thread ID. The breakpoint is triggered only if it is encountered in the context of this thread. If you use **/p** *EProcess* and **/t** *EThread*, you can enter them in any order.

<span id="_c_MaxCallStackDepth"></span><span id="_c_maxcallstackdepth"></span><span id="_C_MAXCALLSTACKDEPTH"></span>**/c** *MaxCallStackDepth*  
Activates the breakpoint only when the call stack depth is less than *MaxCallStackDepth*. You cannot use this option together with **/C**.

<span id="_C_MinCallStackDepth"></span><span id="_c_mincallstackdepth"></span><span id="_C_MINCALLSTACKDEPTH"></span>**/C** *MinCallStackDepth*  
Activates the breakpoint only when the call stack depth is larger than *MinCallStackDepth*. You cannot use this option together with **/c**.

<span id="_a"></span><span id="_A"></span>**/a**  
(For **bm** only) Sets breakpoints on all of the specified locations, whether they are in data space or code space. Because breakpoints on data can cause program failures, use this option only on locations that are known to be safe.

<span id="_d"></span><span id="_D"></span>**/d**  
(For **bm** only) Converts the breakpoint locations to addresses. Therefore, if the code is moved, the breakpoints remain at the same address, instead of being set according to *SymbolPattern*. Use **/d** to avoid reevaluating changes to breakpoints when modules are loaded or unloaded.

<span id="__"></span>**/(**  
(For **bm** only) Includes parameter list information in the symbol string that *SymbolString* defines.

This feature enables you to set breakpoints on overloaded functions that have the same name but different parameter lists. For example, bm /( myFunc sets breakpoints on both **myFunc(int a)** and **myFunc(char a)**. Without "/(", a breakpoint that is set on **myFunc** fails because it does not indicate which **myFunc** function the breakpoint is intended for.

<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the first byte of the instruction where the breakpoint is set. If you omit *Address*, the current instruction pointer is used. For more information about the syntax, see [Address and Address Range Syntax](address-and-address-range-syntax.md).

<span id="_______Passes______"></span><span id="_______passes______"></span><span id="_______PASSES______"></span> *Passes*   
Specifies the number of the execution pass that the breakpoint is activated on. The debugger skips the breakpoint location until it reaches the specified pass. The value of *Passes* can be any 16-bit or 32-bit value.

By default, the breakpoint is active the first time that the application executes the code that contains the breakpoint location. This default situation is equivalent to a value of **1** for *Passes*. To activate the breakpoint only after the application executes the code at least one time, enter a value of **2** or more. For example, a value of **2** activates the breakpoint the second time that the code is executed.

This parameter creates a counter that is decremented on each pass through the code. To see the initial and current values of the *Passes* counter, use [**bl (Breakpoint List)**](bl--breakpoint-list-.md).

The *Passes* counter is decremented only when the application *executes* past the breakpoint in response to a [**g (Go)**](g--go-.md) command. The counter is not decremented if you are stepping through the code or tracing past it. When the *Passes* counter reaches **1**, you can reset it only by clearing and resetting the breakpoint.

<span id="_______CommandString______"></span><span id="_______commandstring______"></span><span id="_______COMMANDSTRING______"></span> *CommandString*   
Specifies a list of commands that are executed every time that the breakpoint is encountered the specified number of times. You must enclose the *CommandString* parameter in quotation marks. Use semicolons to separate multiple commands.

Debugger commands in *CommandString* can include parameters. You can use standard C-control characters (such as **\\n** and **\\"**). Semicolons that are contained in second-level quotation marks (**\\"**) are interpreted as part of the embedded quoted string.

The *CommandString* commands are executed only if the breakpoint is reached while the application is *executing* in response to a [**g (Go)**](g--go-.md) command. The commands are not executed if you are stepping through the code or tracing past this point.

Any command that resumes program execution after a breakpoint (such as **g** or **t**) ends the execution of the command list.

<span id="_______SymbolPattern______"></span><span id="_______symbolpattern______"></span><span id="_______SYMBOLPATTERN______"></span> *SymbolPattern*   
Specifies a pattern. The debugger tries to match this pattern to existing symbols and to set breakpoints on all pattern matches. *SymbolPattern* can contain a variety of wildcard characters and specifiers. For more information about this syntax, see [String Wildcard Syntax](string-wildcard-syntax.md). Because these characters are being matched to symbols, the match is not case sensitive, and a single leading underscore (\_) represents any quantity of leading underscores.

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

For more information about and examples of how to use breakpoints, other breakpoint commands and methods of controlling breakpoints, and how to set breakpoints in user space from a kernel debugger, see [Using Breakpoints](using-breakpoints.md). For more information about conditional breakpoints, see [Setting a Conditional Breakpoint](setting-a-conditional-breakpoint.md).

Remarks
-------

The **bp**, **bu**, and **bm** commands set new breakpoints, but they have different characteristics:

-   The **bp (Set Breakpoint)** command sets a new breakpoint at the *address* of the breakpoint location that is specified in the command. If the debugger cannot resolve the address expression of the breakpoint location when the breakpoint is set, the **bp** breakpoint is automatically converted to a **bu** breakpoint. Use a **bp** command to create a breakpoint that is no longer active if the module is unloaded.

-   The **bu (Set Unresolved Breakpoint)** command sets a *deferred* or *unresolved* breakpoint. A **bu** breakpoint is set on a symbolic reference to the breakpoint location that is specified in the command (not on an address) and is activated whenever the module with the reference is resolved. For more information about these breakpoints, see [Unresolved Breakpoints (bu Breakpoints)](unresolved-breakpoints---bu-breakpoints-.md).

-   The **bm (Set Symbol Breakpoint)** command sets a new breakpoint on symbols that match a specified pattern. This command can create more than one breakpoint. By default, after the pattern is matched, **bm** breakpoints are the same as **bu** breakpoints. That is, **bm** breakpoints are deferred breakpoints that are set on a symbolic reference. However, a bm /d command creates one or more **bp** breakpoints. Each breakpoint is set on the address of a matched location and does not track module state.

If you are not sure what command was used to set an existing breakpoint, use [**.bpcmds (Display Breakpoint Commands)**](-bpcmds--display-breakpoint-commands-.md) to list all breakpoints along with the commands that were used to create them.

There are three primary differences between **bp** breakpoints and **bu** breakpoints:

-   A **bp** breakpoint location is always converted to an address. If a module change moves the code at which a **bp** breakpoint was set, the breakpoint remains at the same address. On the other hand, a **bu** breakpoint remains associated with the symbolic value (typically a symbol plus an offset) that was used, and it tracks this symbolic location even if its address changes.

-   If a **bp** breakpoint address is found in a loaded module, and if that module is later unloaded, the breakpoint is removed from the breakpoint list. On the other hand, **bu** breakpoints persist after repeated unloads and loads.

-   Breakpoints that you set with **bp** are not saved in WinDbg [workspaces](using-workspaces.md). Breakpoints that are set with **bu** are saved in workspaces.

The **bm** command is useful when you want to use wildcard characters in the symbol pattern for a breakpoint. The **bm** *SymbolPattern* syntax is equivalent to using [**x SymbolPattern**](x--examine-symbols-.md) and then using **bu** on each result. For example, to set breakpoints on all of the symbols in the *Myprogram* module that begin with the string "mem," use the following command.

Example

```dbgcmd
0:000> bm myprogram!mem* 
  4: 0040d070 MyProgram!memcpy
 5: 0040c560 MyProgram!memmove
  6: 00408960 MyProgram!memset
```

Because the **bm** command sets software breakpoints (not processor breakpoints), it automatically excludes data location when it sets breakpoints to avoid corrupting the data.

It is possible to specify a data address rather than a program address when using the **bp** or bm /a commands. However, even if a data location is specified, these commands create software breakpoints, not processor breakpoints. If a software breakpoint is placed in program data instead of executable code, it can lead to data corruption. Therefore you should use these commands in a data location only if you are certain that the memory stored in that location will be used as executable code and not as program data. Otherwise, you should use the [**ba (Break on Access)**](ba--break-on-access-.md) command instead. For more details, see [Processor Breakpoints (ba Breakpoints)](processor-breakpoints---ba-breakpoints-.md).

For details on how to set a breakpoint on a location specified by a more complicated syntax, such as a member of a C++ public class, or an arbitrary text string containing otherwise restricted characters, see [Breakpoint Syntax](breakpoint-syntax.md).

If a single logical source line spans multiple physical lines, the breakpoint is set on the last physical line of the statement or call. If the debugger cannot set a breakpoint at the requested position, it puts the breakpoint in the next allowed position.

If you specify *Thread*, breakpoints are set on the specified threads. For example, the **~\*bp** command sets breakpoints on all threads, **~\#bp** sets a breakpoint on the thread that causes the current exception, and **~123bp** sets a breakpoint on thread 123. The **~bp** and **~.bp** commands both set a breakpoint on the current thread.

When you are debugging a multiprocessor system in kernel mode, breakpoints that you set by using **bp** or [**ba (Break on Access)**](ba--break-on-access-.md) apply to all processors. For example, if the current processor is 3 and you type **bp MemoryAddress** to put a breakpoint at **MemoryAddress**. Any processor that is executing at that address (not only processor 3) causes a breakpoint trap.

The **bp**, **bu**, and **bm** commands set software breakpoints by replacing the processor instruction with a break instruction. To debug read-only code or code that cannot be changed, use a ba e command, where **e** represents execute-only access.

The following command sets a breakpoint 12 bytes past the beginning of the function **MyTest**. This breakpoint is ignored for the first six passes through the code, but execution stops on the seventh pass through the code.

```dbgcmd
0:000> bp MyTest+0xb 7 
```

The following command sets a breakpoint at **RtlRaiseException**, displays the **eax** register, displays the value of the symbol **MyVar**, and continues.

```dbgcmd
kd> bp ntdll!RtlRaiseException "r eax; dt MyVar; g"
```

The following two **bm** commands set three breakpoints. When the commands are executed, the displayed result does not distinguish between breakpoints created with the **/d** switch and those created without it. The [**.bpcmds (Display Breakpoint Commands)**](-bpcmds--display-breakpoint-commands-.md) can be used to distinguish between these two types. If the breakpoint was created by **bm** without the **/d** switch, the **.bpcmds** display indicates the breakpoint type as **bu**, followed by the evaluated symbol enclosed in the **@!""** token (which indicates it is a literal symbol and not a numeric expression or register). If the breakpoint was created by **bm** with the **/d** switch, the **.bpcmds** display indicates the breakpoint type as **bp**.

```dbgcmd
0:000> bm myprog!openf* 
  0: 00421200 @!"myprog!openFile"
  1: 00427800 @!"myprog!openFilter"

0:000> bm /d myprog!closef* 
  2: 00421600 @!"myprog!closeFile"

0:000> .bpcmds
bu0 @!"myprog!openFile";
bu1 @!"myprog!openFilter";
bp2 0x00421600 ;
```

 

 





