---
title: g (Go)
description: The g command starts executing the given process or thread. Execution will halt at the end of the program, when BreakAddress is hit, or when another event causes the debugger to stop.
ms.assetid: 9b6aac94-6c53-40c2-a8de-2ad106678c65
keywords: ["g (Go) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- g (Go)
api_type:
- NA
ms.localizationpriority: medium
---

# g (Go)


The **g** command starts executing the given process or thread. Execution will halt at the end of the program, when *BreakAddress* is hit, or when another event causes the debugger to stop.

User-Mode Syntax

```dbgcmd
[~Thread] g[a] [= StartAddress] [BreakAddress ... [; BreakCommands]]
```

Kernel-Mode Syntax

```dbgcmd
g[a] [= StartAddress] [BreakAddress ... [; BreakCommands]] 
```

## <span id="ddk_cmd_go_dbg"></span><span id="DDK_CMD_GO_DBG"></span>Parameters


<span id="_______Thread______"></span><span id="_______thread______"></span><span id="_______THREAD______"></span> *Thread*   
(User mode only) Specifies the thread to execute. For syntax details, see [Thread Syntax](thread-syntax.md).

<span id="_______a______"></span><span id="_______A______"></span> **a**   
Causes any breakpoint created by this command to be a processor breakpoint (like those created by [**ba**](ba--break-on-access-.md)) rather than a software breakpoint (like those created by [**bp**](bp--bu--bm--set-breakpoint-.md) and **bm**). If *BreakAddress* is not specified, no breakpoint is created and the **a** flag has no effect.

<span id="_______StartAddress______"></span><span id="_______startaddress______"></span><span id="_______STARTADDRESS______"></span> *StartAddress*   
Specifies the address where execution should begin. If this is not specified, the debugger passes execution to the address specified by the current value of the instruction pointer. For more syntax details, see [Address and Address Range Syntax](address-and-address-range-syntax.md).

<span id="_______BreakAddress______"></span><span id="_______breakaddress______"></span><span id="_______BREAKADDRESS______"></span> *BreakAddress*   
Specifies the address for a breakpoint. If *BreakAddress* is specified, it must specify an instruction address (that is, the address must contain the first byte of an instruction). Up to ten break addresses, in any order, can be specified at one time. If *BreakAddress* cannot be resolved, it is stored as an [unresolved breakpoint](unresolved-breakpoints---bu-breakpoints-.md). For more syntax details, see [Address and Address Range Syntax](address-and-address-range-syntax.md).

<span id="_______BreakCommands______"></span><span id="_______breakcommands______"></span><span id="_______BREAKCOMMANDS______"></span> *BreakCommands*   
Specifies one or more commands to be automatically executed when the breakpoint specified by *BreakAddress* is hit. The *BreakCommands* parameter must be preceded by a semicolon. If multiple *BreakAddress* values are specified, *BreakCommands* applies to all of them.

**Note**   The *BreakCommands* parameter is only available when you are embedding this command within a command string used by another command -- for example, within another breakpoint command or within an except or event setting. On a command line, the semicolon will terminate the **g** command, and any additional commands listed after the semicolon will be executed immediately after the **g** command is done.

 

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>user mode, kernel mode</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>live debugging only</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>all</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For other methods of issuing this command and an overview of related commands, see [Controlling the Target](controlling-the-target.md).

Remarks
-------

If *Thread* is specified, then the **g** command is executed with the specified thread unfrozen and all others frozen. For example, if the **~123g**, **~\#g**, or **~\*g** command is specified, the specified threads are unfrozen and all others are frozen.

 

 





