---
title: k, kb, kc, kd, kp, kP, kv (Display Stack Backtrace)
description: The k* commands display the stack frame of the given thread, together with related information.
ms.assetid: 1061015f-cb0c-490b-b256-e0dedb659f22
keywords: ["k, kb, kc, kd, kp, kP, kv (Display Stack Backtrace) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- k, kb, kc, kd, kp, kP, kv (Display Stack Backtrace)
api_type:
- NA
ms.localizationpriority: medium
---

# k, kb, kc, kd, kp, kP, kv (Display Stack Backtrace)


The <strong>k*\\</strong>** commands display the stack frame of the given thread, together with related information..

User-Mode, x86 Processor

```dbgcmd
[~Thread] k[b|p|P|v] [c] [n] [f] [L] [M] [FrameCount]
[~Thread] k[b|p|P|v] [c] [n] [f] [L] [M] = BasePtr [FrameCount]
[~Thread] k[b|p|P|v] [c] [n] [f] [L] [M] = BasePtr StackPtr InstructionPtr
[~Thread] kd [WordCount]
```

Kernel-Mode, x86 Processor

```dbgcmd
[Processor] k[b|p|P|v] [c] [n] [f] [L] [M] [FrameCount]
[Processor] k[b|p|P|v] [c] [n] [f] [L] [M] = StackPtr FrameCount
[Processor] k[b|p|P|v] [c] [n] [f] [L] [M] = BasePtr StackPtr InstructionPtr
[Processor] kd [WordCount]
```

User-Mode, x64 Processor

```dbgcmd
[~Thread] k[b|p|P|v] [c] [n] [f] [L] [M] [FrameCount]
[~Thread] k[b|p|P|v] [c] [n] [f] [L] [M] = StackPtr FrameCount
[~Thread] k[b|p|P|v] [c] [n] [f] [L] [M] = StackPtr InstructionPtr FrameCount
[~Thread] kd [WordCount]
```

Kernel-Mode, x64 Processor

```dbgcmd
[Processor] k[b|p|P|v] [c] [n] [f] [L] [M] [FrameCount]
[Processor] k[b|p|P|v] [c] [n] [f] [L] [M] = StackPtr FrameCount
[Processor] k[b|p|P|v] [c] [n] [f] [L] [M] = StackPtr InstructionPtr FrameCount
[Processor] kd [WordCount]
```

User-Mode, ARM Processor

```dbgcmd
[~Thread] k[b|p|P|v] [c] [n] [f] [L] [M] [FrameCount]
[~Thread] k[b|p|P|v] [c] [n] [f] [L] [M] = StackPtr FrameCount
[~Thread] k[b|p|P|v] [c] [n] [f] [L] [M] = StackPtr InstructionPtr FrameCount
[~Thread] kd [WordCount]
```

Kernel-Mode, ARM Processor

```dbgcmd
[Processor] k[b|p|P|v] [c] [n] [f] [L] [M] [FrameCount]
[Processor] k[b|p|P|v] [c] [n] [f] [L] [M] = StackPtr FrameCount
[Processor] k[b|p|P|v] [c] [n] [f] [L] [M] = StackPtr InstructionPtr FrameCount
[Processor] kd [WordCount]
```

## <span id="ddk_cmd_display_stack_backtrace_dbg"></span><span id="DDK_CMD_DISPLAY_STACK_BACKTRACE_DBG"></span>Parameters


<span id="_______Thread______"></span><span id="_______thread______"></span><span id="_______THREAD______"></span> *Thread*   
Specifies the thread whose stack is to be displayed. If you omit this parameter, the stack of the current thread is displayed. For more information about thread syntax, see [Thread Syntax](thread-syntax.md). You can specify threads only in user mode.

<span id="_______Processor______"></span><span id="_______processor______"></span><span id="_______PROCESSOR______"></span> *Processor*   
Specifies the processor whose stack is to be displayed. For more information about processor syntax, see [Multiprocessor Syntax](multiprocessor-syntax.md).

<span id="_______b"></span><span id="_______B"></span> b  
Displays the first three parameters that are passed to each function in the stack trace.

<span id="_______c"></span><span id="_______C"></span> c  
Displays a clean stack trace. Each display line includes only the module name and the function name.

<span id="_______p"></span><span id="_______P"></span> p  
Displays all of the parameters for each function that is called in the stack trace. The parameter list includes each parameter's data type, name, and value. The p option is case sensitive. This parameter requires full symbol information.

<span id="_______P"></span><span id="_______p"></span> P  
Displays all of the parameters for each function that is called in the stack trace, like the p parameter. However, for P, the function parameters are printed on a second line of the display, instead of on the same line as the rest of the data.

<span id="_______v______"></span><span id="_______V______"></span> v   
Displays frame pointer omission (FPO) information. On x86-based processors, the display also includes calling convention information.

<span id="_______n______"></span><span id="_______N______"></span> n   
Displays frame numbers.

<span id="_______f______"></span><span id="_______F______"></span> f   
Displays the distance between adjacent frames. This distance is the number of bytes that separate the frames on the actual stack.

<span id="_______L______"></span><span id="_______l______"></span> L   
Hides source lines in the display. L is case sensitive.

<span id="_______M"></span><span id="_______m"></span> M  
Displays output using [Debugger Markup Language](debugger-markup-language-commands.md). Each frame number in the display is a link that you can click to set the local context and display local variables. For information about the local context, see [**.frame**](-frame--set-local-context-.md).

<span id="_______FrameCount______"></span><span id="_______framecount______"></span><span id="_______FRAMECOUNT______"></span> *FrameCount*   
Specifies the number of stack frames to display. You should specify this number in hexadecimal format, unless you have changed the radix by using the [**n (Set Number Base)**](n--set-number-base-.md) command. The default value is 20 (0x14), unless you have changed the default value by using the [**.kframes (Set Stack Length)**](-kframes--set-stack-length-.md) command.

<span id="_______BasePtr______"></span><span id="_______baseptr______"></span><span id="_______BASEPTR______"></span> *BasePtr*   
Specifies the base pointer for the stack trace. The *BasePtr* parameter is available only if there is an equal sign (=) after the command.

<span id="_______StackPtr______"></span><span id="_______stackptr______"></span><span id="_______STACKPTR______"></span> *StackPtr*   
Specifies the stack pointer for the stack trace. If you omit *StackPtr* and *InstructionPtr*, the command uses the stack pointer that the rsp (or esp) register specifies and the instruction pointer that the rip (or eip) register specifies.

<span id="_______InstructionPtr______"></span><span id="_______instructionptr______"></span><span id="_______INSTRUCTIONPTR______"></span> *InstructionPtr*   
Specifies the instruction pointer for the stack trace. If you omit *StackPtr* and *InstructionPtr*, the command uses the stack pointer that the rsp (or esp) register specifies and the instruction pointer that the rip (or eip) register specifies.

<span id="_______WordCount______"></span><span id="_______wordcount______"></span><span id="_______WORDCOUNT______"></span> *WordCount*   
Specifies the number of DWORD\_PTR values in the stack to dump. The default value is 20 (0x14), unless you changed the default value by using the [**.kframes (Set Stack Length)**](-kframes--set-stack-length-.md) command.

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Modes</p></td>
<td align="left"><p>User mode, kernel mode</p></td>
</tr>
<tr class="even">
<td align="left"><p>Targets</p></td>
<td align="left"><p>Live, crash dump</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Platforms</p></td>
<td align="left"><p>All</p></td>
</tr>
</tbody>
</table>

 

### <span id="additional_information1"></span><span id="ADDITIONAL_INFORMATION1"></span>Additional Information

For more information about the register context and other context settings, see [Changing Contexts](changing-contexts.md).

Remarks
-------

When you issue the **k**, **kb**, **kp**, **kP**, or **kv** command, a stack trace is displayed in a tabular format. If line loading is enabled, source modules and line numbers are also displayed.

The stack trace includes the base pointer for the stack frame, the return address, and function names.

If you use the **kp** or **kP** command, the full parameters for each function that is called in the stack trace are displayed. The parameter list includes each parameter's data type, name, and value.

This command might be slow. For example, when **MyFunction1** calls **MyFunction2**, the debugger must have full symbol information for **MyFunction1** to display the parameters that are passed in this call. This command does not fully display internal Microsoft Windows routines that are not exposed in public symbols.

If you use the **kb** or **kv** command, the first three parameters that are passed to each function are displayed. If you use the **kv** command, FPO data is also displayed.

On an x86-based processor, the **kv** command also displays calling convention information.

When you use the **kv** command, the FPO information is added at the end of the line in the following format.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">FPO text</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">FPO: [non-Fpo]</td>
<td align="left"><p>No FPO data for the frame.</p></td>
</tr>
<tr class="even">
<td align="left">FPO: [N1,N2,N3]</td>
<td align="left"><p><em>N1</em> is the total number of parameters.</p>
<p><em>N2</em> is the number of DWORD values for the local variables.</p>
<p><em>N3</em> is the number of registers that are saved.</p></td>
</tr>
<tr class="odd">
<td align="left">FPO: [N1,N2] TrapFrame @ Address</td>
<td align="left"><p><em>N1</em> is the total number of parameters.</p>
<p><em>N2</em> is the number of DWORD values for the locals.</p>
<p><em>Address</em> is the address of the trap frame.</p></td>
</tr>
<tr class="even">
<td align="left">FPO: TaskGate Segment:0</td>
<td align="left"><p><em>Segment</em> is the segment selector for the task gate.</p></td>
</tr>
<tr class="odd">
<td align="left">FPO: [EBP 0xBase]</td>
<td align="left"><p><em>Base</em> is the base pointer for the frame.</p></td>
</tr>
</tbody>
</table>

 

The **kd** command displays the raw stack data. Each DWORD value is displayed on a separate line. Symbol information is displayed for those lines together with associated symbols. This format creates a more detailed list than the other **k***\** commands. The **kd** command is equivalent to a [**dds (Display Memory)**](d--da--db--dc--dd--dd--df--dp--dq--du--dw--dw--dyb--dyd--display-memor.md) command that uses the stack address as its parameter.

If you use the **k** command at the beginning of a function (before the function prolog has been executed), you receive incorrect results. The debugger uses the frame register to compute the current backtrace, and this register is not set correctly for a function until its prolog has been executed.

In user mode, the stack trace is based on the stack of the current thread. For more information about threads, see [Controlling Processes and Threads](controlling-processes-and-threads.md).

In kernel mode, the stack trace is based on the current [register context](changing-contexts.md#register-context). You can set the register context to match a specific thread, context record, or trap frame.

### <span id="additional_information2"></span><span id="ADDITIONAL_INFORMATION2"></span>Additional Information

For more information about the register context and other context settings, see [Changing Contexts](changing-contexts.md).

 

 





