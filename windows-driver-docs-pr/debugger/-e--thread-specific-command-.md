---
title: ~e (Thread-Specific Command)
description: The ~e command executes one or more commands for a specific thread or for all threads in the target process.Do not confuse this command with the e (Enter Values) command.
ms.assetid: a14f0a5f-48f9-46dd-baa6-b7d91b15772c
keywords: ["Thread-Specific Command (~e) command", "thread, Thread-Specific Command (~e) command", "~e (Thread-Specific Command) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- ~e (Thread-Specific Command)
api_type:
- NA
ms.localizationpriority: medium
---

# ~e (Thread-Specific Command)


The **~e** command executes one or more commands for a specific thread or for all threads in the target process.

Do not confuse this command with the [**e (Enter Values)**](e--ea--eb--ed--ed--ef--ep--eq--eu--ew--eza--ezu--enter-values-.md) command.

```dbgcmd
~Thread e CommandString
```

## <span id="ddk_cmd_thread_specific_command_dbg"></span><span id="DDK_CMD_THREAD_SPECIFIC_COMMAND_DBG"></span>Parameters


<span id="_______Thread______"></span><span id="_______thread______"></span><span id="_______THREAD______"></span> *Thread*   
Specifies the thread or threads that the debugger will execute *CommandString* for. For more information about the syntax, see [Thread Syntax](thread-syntax.md).

<span id="_______CommandString______"></span><span id="_______commandstring______"></span><span id="_______COMMANDSTRING______"></span> *CommandString*   
Specifies one or more commands to execute. You should separate multiple commands by using semicolons. *CommandString* includes the rest of the input line. All of the text that follows the letter "e" is interpreted as part of this string. Do not enclose *CommandString* in quotation marks.

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>User mode only</p></td>
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

For more information about other commands that control threads, see [Controlling Processes and Threads](controlling-processes-and-threads.md).

Remarks
-------

You can specify threads only in user mode. In kernel mode, the tilde (~) refers to a processor.

When you use the **~e** command together with one thread, the **~e** command only saves some typing. For example, the following two commands are equivalent.

```dbgcmd
0:000> ~2e r; k; kd 

0:000> ~2r; ~2k; ~2kd 
```

However, you can use the **~e** qualifier to repeat a command or extension command several times. When you use the qualifier in this manner, it can eliminate extra typing. For example, the following command repeats the [**!gle**](-gle.md) extension command for every thread that you are debugging.

```dbgcmd
0:000> ~*e !gle 
```

If an error occurs in the execution of one command, execution continues with the next command.

You cannot use the **~e** qualifier together with execution commands ([**g**](g--go-.md), [**gh**](gh--go-with-exception-handled-.md), [**gn**](gn--gn--go-with-exception-not-handled-.md), **gN**, [**gu**](gu--go-up-.md), [**p**](p--step-.md), [**pa**](pa--step-to-address-.md), [**pc**](pc--step-to-next-call-.md), [**t**](t--trace-.md), [**ta**](ta--trace-to-address-.md), [**tb**](tb--trace-to-next-branch-.md), [**tc**](tc--trace-to-next-call-.md), [**wt**](wt--trace-and-watch-data-.md)).

You cannot use the **~e** qualifier together with the [**j (Execute If-Else)**](j--execute-if---else-.md) or [**z (Execute While)**](z--execute-while-.md) conditional commands.

If you are debugging more than one process, you cannot use the **~e** command to access the virtual memory space for a inactive process.

 

 





