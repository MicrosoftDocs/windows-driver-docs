---
title: k, kb, kc, kd, kp, kP, kv (Display Stack Backtrace)
description: Learn how the k* commands display the stack frame of the given thread, together with related information.
keywords: ["k, kb, kc, kd, kp, kP, kv (Display Stack Backtrace) Windows Debugging"]
ms.date: 07/05/2023
topic_type:
- apiref
ms.topic: reference
api_name:
- k, kb, kc, kd, kp, kP, kv (Display Stack Backtrace)
api_type:
- NA
---

# k, kb, kc, kd, kp, kP, kv (Display Stack Backtrace)

The **k\*** commands display the stack frame of the given thread with related information.

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

## Parameters

*Thread*  
Specifies the thread stack to be displayed. If you omit this parameter, the stack of the current thread is displayed. For more information about thread syntax, see [Thread syntax](thread-syntax.md). You can specify threads only in user mode.

*Processor*  
Specifies the processor whose stack is to be displayed. For more information about processor syntax, see [Multiprocessor Syntax](multiprocessor-syntax.md).

b  
Displays the first three parameters that are passed to each function in the stack trace.

c  
Displays a clean stack trace. Each display line includes only the module name and the function name.

p  
Displays all of the parameters for each function that's called in the stack trace. The parameter list includes each parameter's data type, name, and value. The `p` option is case sensitive. This parameter requires full symbol information.

P  
Displays all of the parameters for each function that's called in the stack trace, like the `p` parameter. However, for `P`, the function parameters are printed on a second line of the display, instead of on the same line as the rest of the data.

v  
Displays frame pointer omission (FPO) information. On x86-based processors, the display also includes calling convention information.

n  
Displays frame numbers.

f  
Displays the distance between adjacent frames. This distance is the number of bytes that separate the frames on the actual stack.

L  
Hides source lines in the display. `L` is case sensitive.

M  
Displays the output using [Debugger markup language](../debugger/debugger-markup-language-commands.md). Each frame number in the display is a link that you can select to set the local context and display local variables. For information about the local context, see [.frame](-frame--set-local-context-.md).

*FrameCount*  
Specifies the number of stack frames to display. You should specify this number in hexadecimal format unless you've changed the radix by using the [n (set number base)](n--set-number-base-.md) command. Use the [.kframes (set stack length)](-kframes--set-stack-length-.md) command to display the default and to change the value.

*BasePtr*  
Specifies the base pointer for the stack trace. The `BasePtr` parameter is available only if there's an equal sign (=) after the command.

*StackPtr*  
Specifies the stack pointer for the stack trace. If you omit `StackPtr` and `InstructionPtr`, the command uses the stack pointer that the rsp (or esp) register specifies and the instruction pointer that the rip (or eip) register specifies.

*InstructionPtr*  
Specifies the instruction pointer for the stack trace. If you omit `StackPtr` and `InstructionPtr`, the command uses the stack pointer that the rsp (or esp) register specifies and the instruction pointer that the rip (or eip) register specifies.

*WordCount*  
Specifies the number of DWORD_PTR values in the stack to dump.

| Environment | &nbsp; |
|---|---|
| Modes | User mode, kernel mode |
| Targets | Live, crash dump |
| Platforms | All |

## Remarks

When you issue the `k`, `kb`, `kp`, `kP`, or `kv` commands, a stack trace is displayed in a tabular format. If line loading is enabled, source modules and line numbers are also displayed.

The stack trace includes the base pointer for the stack frame, the return address, and the function names.

If you use the `kp` or `kP` commands, the full parameters for each function that's called in the stack trace are displayed. The parameter list includes each parameter's data type, name, and value.

The command might be slow. For example, when `MyFunction1` calls `MyFunction2`, the debugger must have full symbol information for `MyFunction1` to display the parameters that are passed in this call. This command doesn't fully display internal Microsoft Windows routines that aren't exposed in public symbols.

If you use the `kb` or `kv` commands, the first three parameters that are passed to each function are displayed. If you use the `kv` command, FPO data is also displayed.

On an x86-based processor, the `kv` command also displays calling convention information.

When you use the `kv` command, the FPO information is added at the end of the line in the following format.

| FPO text | Meaning |
|---|---|
| FPO: [non-Fpo] | No FPO data for the frame. |
| FPO: [N1,N2,N3] | *N1* is the total number of parameters. </p> *N2* is the number of DWORD values for the local variables. </p> *N3* is the number of registers that are saved. |
| FPO: [N1,N2] TrapFrame @ Address | *N1* is the total number of parameters. </p> *N2* is the number of DWORD values for the locals. </p> *Address* is the address of the trap frame. |
| FPO: TaskGate Segment:0 | *Segment* is the segment selector for the task gate. |
| FPO: [EBP 0xBase] | *Base* is the base pointer for the frame. |

The `kd` command displays the raw stack data. Each DWORD value is displayed on a separate line. Symbol information is displayed for those lines together with associated symbols. This format creates a more detailed list than the other `k*` commands. The `kd` command is equivalent to a [dds (display memory)](d--da--db--dc--dd--dd--df--dp--dq--du--dw--dw--dyb--dyd--display-memor.md) command that uses the stack address as its parameter.

If you use the `k` command at the beginning of a function (before the function prolog has been executed), you receive incorrect results. The debugger uses the frame register to compute the current backtrace, and this register isn't set correctly for a function until its prolog has been executed.

In user mode, the stack trace is based on the stack of the current thread. For more information about threads, see [Controlling processes and threads](../debugger/controlling-processes-and-threads.md).

In kernel mode, the stack trace is based on the current [register context](../debugger/changing-contexts.md#register-context). You can set the register context to match a specific thread, context record, or trap frame.

## Additional information

For more information about the Register context and other context settings, see [Changing contexts](../debugger/changing-contexts.md).
