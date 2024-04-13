---
title: "th (Trace to Next Branching Instruction)"
description: "The th command executes the program until it reaches any kind of branching instruction, including conditional or unconditional branches, calls, returns, and system calls."
keywords: ["th (Trace to Next Branching Instruction) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- th (Trace to Next Branching Instruction)
api_type:
- NA
---

# th (Trace to Next Branching Instruction)


The **th** command executes the program until it reaches any kind of branching instruction, including conditional or unconditional branches, calls, returns, and system calls.

User-Mode

```dbgcmd
[~Thread] th [r] [= StartAddress] [Count] 
```

Kernel-Mode

```dbgcmd
th [r] [= StartAddress] [Count] 
```

## Parameters


<span id="_______Thread______"></span><span id="_______thread______"></span><span id="_______THREAD______"></span> *Thread*   
Specifies threads to continue executing. All other threads are frozen. For more information about the syntax, see [Thread Syntax](thread-syntax.md). You can specify threads only in user mode.

<span id="_______r______"></span><span id="_______R______"></span> **r**   
Turns on and off the display of registers and flags. By default, the registers and flags are displayed. You can disable register display by using the **thr**, [**pr**](p--step-.md), [**tr**](t--trace-.md), or .prompt\_allow -reg commands. All of these commands control the same setting and you can use any of them to override any previous use of these commands.

You can also disable register display by using the l-os command. This setting is separate from the other four commands. To control which registers and flags are displayed, use the [**rm (Register Mask)**](rm--register-mask-.md) command.

<span id="_______StartAddress______"></span><span id="_______startaddress______"></span><span id="_______STARTADDRESS______"></span> *StartAddress*   
Specifies the address where the debugger begins execution. If you do not use *StartAddress*, execution begins at the instruction that the instruction pointer points to. For more information about the syntax, see [Address and Address Range Syntax](address-and-address-range-syntax.md).

<span id="_______Count______"></span><span id="_______count______"></span><span id="_______COUNT______"></span> *Count*   
Specifies the number of branching instructions that the debugger must encounter for the **th** command to end. The default value is one.

## Environment

|  Item       | Description               |
|-----------|------------------------|
| Modes     | user mode, kernel mode |
| Targets   | live debugging only    |
| Platforms | all                    |

 

## Additional Information

For more information about related commands, see [Controlling the Target](../debugger/controlling-the-target.md).

## Remarks

The **th** command causes the target to begin executing. Execution continues until the debugger reaches a branching instruction or encounters a breakpoint.

If the program counter is already on a branching instruction, the debugger traces into the branching instruction and continues executing until another branching instruction is reached. This tracing, rather than execution, of the call is the only difference between **th** and [**ph (Step to Next Branching Instruction)**](ph--step-to-next-branching-instruction-.md).

**th** is available for all live sessions. This availability is the primary difference between **th** and [**tb (Trace to Next Branch)**](tb--trace-to-next-branch-.md).

In source mode, you can associate one source line with multiple assembly instructions. This command does not stop at a branching instruction that is associated with the current source line.

