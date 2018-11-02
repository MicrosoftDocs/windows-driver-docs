---
title: .pcmd (Set Prompt Command)
description: The .pcmd command causes the debugger to issue a command whenever the target stops executing and to display a prompt in the Debugger Command window with register or target state information.
ms.assetid: 8cda10c3-860c-453d-9fdd-0dfc74d71c53
keywords: [".pcmd (Set Prompt Command) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- .pcmd (Set Prompt Command)
api_type:
- NA
ms.localizationpriority: medium
---

# .pcmd (Set Prompt Command)


The **.pcmd** command causes the debugger to issue a command whenever the target stops executing and to display a prompt in the [Debugger Command window](debugger-command-window.md) with register or target state information.

```dbgcmd
.pcmd -s CommandString 
.pcmd -c 
.pcmd 
```

## <span id="ddk_meta_set_prompt_command_dbg"></span><span id="DDK_META_SET_PROMPT_COMMAND_DBG"></span>Parameters


<span id="_______-s_______CommandString______"></span><span id="_______-s_______commandstring______"></span><span id="_______-S_______COMMANDSTRING______"></span> **-s** **** *CommandString*   
Specifies a new prompt command string. Whenever the target stops executing, the debugger issues and immediately runs the *CommandString* command. If *CommandString* contains spaces or semicolons, you must enclose it in quotation marks.

<span id="_______-c______"></span><span id="_______-C______"></span> **-c**   
Deletes any existing prompt command string.

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
<td align="left"><p>Live, crash dump</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>All</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information about the Debugger Command window prompt, see [Using Debugger Commands](using-debugger-commands.md).

Remarks
-------

If you use the **.pcmd** command without parameters, the current prompt command is displayed.

When you set a prompt command by using **.pcmd -s**, the specified *CommandString* is issued whenever the target stops executing (for example, when a [**g**](g--go-.md), [**p**](p--step-.md), or [**t**](t--trace-.md) command ends). The *CommandString* command is not issued when you use a non-execution command, unless that command displays registers or target state information.

In the following example, the first use of **.pcmd** sets a fixed string that appears with the prompt. The second use of **.pcmd** causes the debugger to display the target's current process ID and thread ID every time that the prompt appears. The special prompt does not appear after the [**.ttime**](-ttime--display-thread-times-.md) command is used, because that command does not involve execution.

```dbgcmd
0:000> .pcmd
No per-prompt command

0:000> .pcmd -s ".echo Execution is done."
Per-prompt command is '.echo Execution is done.'

0:000> t
Prymes!isPrime+0xd0:
004016c0 837dc400      cmp dword ptr [ebp-0x3c],0x0 ss:0023:0012fe70=00000002
Execution is done.

0:000> t
Prymes!isPrime+0xd4:
004016c4 7507             jnz     Prymes!isPrime+0xdd (004016cd)
 [br=1]
Execution is done.

0:000> .ttime
Created: Thu Aug 21 13:18:59 2003
Kernel:  0 days 0:00:00.031
User:    0 days 0:00:00.000

0:000> .pcmd -s "r $tpid, $tid"
Per-prompt command is 'r $tpid, $tid'

0:000> t
Prymes!isPrime+0xdd:
004016cd ebc0             jmp     Prymes!isPrime+0x9f (0040168f)
$tpid=0000080c $tid=00000514

0:000> t
Prymes!isPrime+0x9f:
0040168f 8b55fc           mov     edx,[ebp-0x4]     ss:0023:0012fea8=00000005
$tpid=0000080c $tid=00000514
```

 

 





