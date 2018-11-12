---
title: t (Trace)
description: The t command executes a single instruction or source line and optionally displays the resulting values of all registers and flags. 
ms.assetid: 0cb3ac96-5d5c-4ebd-8ef1-2fbb066e6458
keywords: ["t (Trace) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- t (Trace)
api_type:
- NA
ms.localizationpriority: medium
---

# t (Trace)


The **t** command executes a single instruction or source line and optionally displays the resulting values of all registers and flags. When subroutine calls or interrupts occur, each of their steps is also traced.

User-Mode

```dbgcmd
[~Thread] t [r] [= StartAddress] [Count] ["Command"] 
```

Kernel-Mode

```dbgcmd
t [r] [= StartAddress] [Count] ["Command"] 
```

## <span id="ddk_cmd_trace_dbg"></span><span id="DDK_CMD_TRACE_DBG"></span>Parameters


<span id="_______Thread______"></span><span id="_______thread______"></span><span id="_______THREAD______"></span> *Thread*   
Specifies threads to thaw. All other threads are frozen. For more information about this syntax, see [Thread Syntax](thread-syntax.md). You can specify threads only in user mode.

<span id="_______r______"></span><span id="_______R______"></span> **r**   
Turns on and off the display of registers and flags. By default, the registers and flags are displayed. You can disable register display by using the [**pr**](p--step-.md), **tr**, or .prompt\_allow -reg commands. All three of these commands control the same setting and you can use any of them to override any previous use of these commands.

You can also disable register display by using the l-os command. This setting is separate from the other three commands. To control which registers and flags are displayed, use the [**rm (Register Mask)**](rm--register-mask-.md) command.

<span id="_______StartAddress______"></span><span id="_______startaddress______"></span><span id="_______STARTADDRESS______"></span> *StartAddress*   
Specifies the address where execution should begin. If you do not use *StartAddress*, execution begins at the instruction that the instruction pointer points to. For more information about the syntax, see [Address and Address Range Syntax](address-and-address-range-syntax.md).

<span id="_______Count______"></span><span id="_______count______"></span><span id="_______COUNT______"></span> *Count*   
Specifies the number of instructions or source lines to trace through before stopping. Each step is displayed as a separate action in the [Debugger Command window](debugger-command-window.md). The default value is one.

<span id="_______Command______"></span><span id="_______command______"></span><span id="_______COMMAND______"></span> *Command*   
Specifies a debugger command to execute after the trace is performed. This command is executed before the standard **t** results are displayed. If you also use *Count*, this command is executed after all tracing is complete (but before the results from the final trace are displayed).

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

For more information about how to issue the **t** command and an overview of related commands, see [Controlling the Target](controlling-the-target.md).

Remarks
-------

When you specify *Count*, each instruction is displayed as it is stepped through.

Each trace executes a single assembly instruction or a single source line, depending on whether the debugger is in assembly mode or source mode. Use the [**l+t**](l---l---set-source-options-.md) and l-t commands or the buttons on the WinDbg toolbar to switch between these modes.

If you want to trace most function calls but skip certain calls, you can use [**.step\_filter (Set Step Filter)**](-step-filter--set-step-filter-.md) to indicate which calls to step over.

You can use the **t** command to trace instructions in ROM.

When you are quickly tracing many times in WinDbg, the debugging information windows are updated after each trace. If this update causes slower response time, use [**.suspend\_ui (Suspend WinDbg Interface)**](-suspend-ui--suspend-windbg-interface-.md) to temporarily suspend the updating of these windows.

 

 





