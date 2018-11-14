---
title: ~ (Thread Status)
description: The tilde (~) command displays status for the specified thread or for all threads in the current process.
ms.assetid: c27e4c72-86da-459d-833f-d27d26bdea0e
keywords: ["~ (Thread Status) Windows Debugging"]
ms.author: domars
ms.date: 09/17/2018
topic_type:
- apiref
api_name:
- ~ (Thread Status)
api_type:
- NA
ms.localizationpriority: medium
---

# ~ (Thread Status)


The tilde (**~**) command displays status for the specified thread or for all threads in the current process.

```dbgcmd
~ Thread
```

## <span id="ddk_cmd_thread_status_dbg"></span><span id="DDK_CMD_THREAD_STATUS_DBG"></span>Parameters


<span id="_______Thread______"></span><span id="_______thread______"></span><span id="_______THREAD______"></span> *Thread*   
Specifies the thread to display. If you omit this parameter, all threads are displayed. For more information about the syntax, see [Thread Syntax](thread-syntax.md).

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

You can specify threads only in user mode. In kernel mode, the tilde (**~**) refers to a processor.

You can add a thread symbol before many commands. For more information about the meaning of a tilde (**~**) followed by a command, see the entry for the command itself.

The following examples show you how to use this command. The following command displays all threads.

```dbgcmd
0:001> ~
```

The following command also displays all threads.

```dbgcmd
0:001> ~*
```

The following command displays the currently active thread.

```dbgcmd
0:001> ~.
```

The following command displays the thread that originally caused the exception (or that was active when the debugger attached to the process).

```dbgcmd
0:001> ~#
```

The following command displays thread number 2.

```dbgcmd
0:001> ~2
```

The previous command displays the following output.

```dbgcmd
0:001> ~
   0 id: 4dc.470 Suspend: 0 Teb 7ffde000 Unfrozen
. 1 id: 4dc.534 Suspend: 0 Teb 7ffdd000 Unfrozen
#  2 id: 4dc.5a8 Suspend: 0 Teb 7ffdc000 Unfrozen
```

On the first line of this output, 0 is the decimal thread number, 4DC is the hexadecimal process ID, 470 is the hexadecimal thread ID, 0x7FFDE000 is the address of the TEB, and **Unfrozen** is the thread status. The period (.) before thread 1 means this thread is the current thread. The number sign (\#) before thread 2 means this thread was the one that originally caused the exception or it was active when the debugger attached to the process.

 

 





