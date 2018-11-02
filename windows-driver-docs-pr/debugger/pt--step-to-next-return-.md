---
title: pt (Step to Next Return)
description: The pt command executes the program until a return instruction is reached.
ms.assetid: f4388953-4cb2-4df5-af8b-150e50ce765b
keywords: ["pt (Step to Next Return) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- pt (Step to Next Return)
api_type:
- NA
ms.localizationpriority: medium
---

# pt (Step to Next Return)


The **pt** command executes the program until a return instruction is reached.

User-Mode

```dbgcmd
[~Thread] pt [r] [= StartAddress] [Count] ["Command"]
```

Kernel-Mode

```dbgcmd
pt [r] [= StartAddress] [Count] ["Command"]
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______Thread______"></span><span id="_______thread______"></span><span id="_______THREAD______"></span> *Thread*   
Specifies threads to continue executing. All other threads are frozen. For more information about the syntax, see [Thread Syntax](thread-syntax.md). You can specify threads only in user mode.

<span id="_______r______"></span><span id="_______R______"></span> **r**   
Turns on and off the display of registers and flags. By default, the registers and flags are displayed. You can disable register display by using the **ptr**, [**pr**](p--step-.md), [**tr**](t--trace-.md), or .prompt\_allow -reg commands. All of these commands control the same setting and you can use any of them to override any previous use of these commands.

You can also disable register display by using the l-os command. This setting is separate from the other three commands. To control which registers and flags are displayed, use the [**rm (Register Mask)**](rm--register-mask-.md) command.

<span id="_______StartAddress______"></span><span id="_______startaddress______"></span><span id="_______STARTADDRESS______"></span> *StartAddress*   
Specifies the address where the debugger begins execution. Otherwise, the debugger begins at the instruction that the instruction pointer points to. For more information about the syntax, see [Address and Address Range Syntax](address-and-address-range-syntax.md).

<span id="_______Count______"></span><span id="_______count______"></span><span id="_______COUNT______"></span> *Count*   
Specifies the number of **return** instructions that must be encountered for this command to stop. The default value is one.

<span id="_______Command______"></span><span id="_______command______"></span><span id="_______COMMAND______"></span> *Command*   
Specifies a debugger command to execute after the step is performed. This command is executed before the standard **pt** results are displayed. If you also use *Count*, the specified command is executed after all stepping is complete (but before the results from the final step are displayed).

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

For more information about related commands, see [Controlling the Target](controlling-the-target.md).

Remarks
-------

The **pt** command causes the target to begin executing. This execution continues until a **return** instruction is reached or a breakpoint is encountered.

If the program counter is already on a **return** instruction, the entire return is executed. After this return is returned, execution continues until another **return** is reached. This execution, rather than tracing, of the call is the only difference between **pt** and [**tt (Trace to Next Return)**](tt--trace-to-next-return-.md).

In source mode, you can associate one source line with multiple assembly instructions. The **pt** command does not stop at a **return** instruction that is associated with the current source line.

The following example demonstrates using the **pt** command along with the **kb** command to display the stack trace:

```dbgcmd
0:000> pt "kb"
```

 

 





