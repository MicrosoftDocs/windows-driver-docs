---
title: "pct (Step to Next Call or Return)"
description: "The pct command executes the program until it reaches a call instruction or a return instruction."
keywords: ["pct (Step to Next Call or Return) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- pct (Step to Next Call or Return)
api_type:
- NA
---

# pct (Step to Next Call or Return)


The **pct** command executes the program until it reaches a call instruction or a return instruction.

User-Mode

```dbgcmd
[~Thread] pct [r] [= StartAddress] [Count] 
```

Kernel-Mode

```dbgcmd
pct [r] [= StartAddress] [Count] 
```

## Parameters


<span id="_______Thread______"></span><span id="_______thread______"></span><span id="_______THREAD______"></span> *Thread*   
Specifies threads to continue executing. All other threads are frozen. For more information about the syntax, see [Thread Syntax](thread-syntax.md). You can specify threads only in user mode.

<span id="_______r______"></span><span id="_______R______"></span> **r**   
Turns on and off the display of registers and flags. By default, the registers and flags are displayed. You can disable register display through the **pctr**, [**pr**](p--step-.md), [**tr**](t--trace-.md), or .prompt\_allow -reg commands. All of these commands control the same setting and you can use any of them to override any previous use of these commands.

You can also disable register display by using the l-os command. This setting is separate from the other three commands. To control which registers and flags are displayed, use the [**rm (Register Mask)**](rm--register-mask-.md) command.

<span id="_______StartAddress______"></span><span id="_______startaddress______"></span><span id="_______STARTADDRESS______"></span> *StartAddress*   
Specifies the address where the debugger begins execution. Otherwise, the debugger begins at the instruction that the instruction pointer points to. For more information about the syntax, see [Address and Address Range Syntax](address-and-address-range-syntax.md).

<span id="_______Count______"></span><span id="_______count______"></span><span id="_______COUNT______"></span> *Count*   
Specifies the number of **call** or **return** instructions that must be encountered for this command to stop. The default value is one.

## Environment

|  Item       | Description               |
|-----------|------------------------|
| Modes     | user mode, kernel mode |
| Targets   | live debugging only    |
| Platforms | all                    |

 

## Additional Information

For more information about related commands, see [Controlling the Target](../debugger/controlling-the-target.md).

## Remarks

The **pct** command causes the target to begin executing. This execution continues until a call or **return** instruction is reached or a breakpoint is encountered.

If the program counter is already on a **call** or **return** instruction, the entire call or return is executed. After this call or return is returned, execution continues until another **call** or **return** is reached. This execution, rather than tracing, of the call is the only difference between **pct** and [**tct (Trace to Next Call or Return)**](tct--trace-to-next-call-or-return-.md).

In source mode, you can associate one source line with multiple assembly instructions. The **pct** command does not stop at a **call** or **return** instruction that is associated with the current source line.

