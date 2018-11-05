---
title: (Process Status)
description: The pipe ( ) command displays status for the specified process, or for all processes that you are currently debugging.Do not confuse this command with the (System Status) command.
ms.assetid: 78f53049-e949-4431-b6b1-0710da047ced
keywords: ["(Process Status) Windows Debugging"]
ms.author: domars
ms.date: 09/17/2018
topic_type:
- apiref
api_name:
- (Process Status)
api_type:
- NA
ms.localizationpriority: medium
---

# | (Process Status)


The pipe (**|**) command displays status for the specified process, or for all processes that you are currently debugging.

Do not confuse this command with the [**|| (System Status)**](----system-status-.md) command.

```dbgcmd
    | Process
```

## <span id="ddk_cmd_process_status_dbg"></span><span id="DDK_CMD_PROCESS_STATUS_DBG"></span>Parameters


<span id="_______Process______"></span><span id="_______process______"></span><span id="_______PROCESS______"></span> *Process*   
Specifies the process to display. If you omit this parameter, all processes that you are debugging are displayed. For more information about the syntax, see [Process Syntax](process-syntax.md).

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

For more information and other methods of displaying or controlling processes and threads, see [Controlling Processes and Threads](controlling-processes-and-threads.md).

Remarks
-------

You can specify processes only in user mode.

You can add a process symbol before many commands. For more information about the meaning of a pipe (**|**) followed by a command, see the entry for the command itself.

Unless you enabled the debugging of child processes when you started the debugging session, there is only one process that is available to the debugger.

The following examples show you how to use this command. The following command displays all processes.

```dbgcmd
2:005> |
```

The following command also displays all processes.

```dbgcmd
2:005> |*
```

The following command displays the currently active process.

```dbgcmd
2:005> |.
```

The following command displays the process that originally caused the exception (or that the debugger originally attached to).

```dbgcmd
2:005> |#
```

The following command displays process number 2.

```dbgcmd
2:005> |2
```

The previous command displays the following output.

```dbgcmd
0:002> |
#  0 id: 224   name: myprog.exe 
   1 id: 228   name: onechild.exe 
. 2 id: 22c   name: anotherchild.exe 
```

On the first line of this output, 0 is the decimal process number, 224 is the hexadecimal process ID, and *Myprog.exe* is the application name of the process. The period (.) before process 2 means that this process is the current process. The number sign (\#) before process 0 means that this process was the one that originally caused the exception or that the debugger attached to.

 

 





