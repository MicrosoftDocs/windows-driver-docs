---
title: ~s (Set Current Thread)
description: The ~s command sets or displays the current thread number.
ms.assetid: 689d578b-8d31-4049-a374-19ae94d452a9
keywords: ["~s (Set Current Thread) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- ~s (Set Current Thread)
api_type:
- NA
ms.localizationpriority: medium
---

# ~s (Set Current Thread)


The **~s** command sets or displays the current thread number.

In user mode, **~s** sets the current thread. Do not confuse this command confused with the [**~s (Change Current Processor)**](-s--change-current-processor-.md) command (which works only in kernel mode), the [**|s (Set Current Process)**](-s--set-current-process-.md) command, the [**||s (Set Current System)**](--s--set-current-system-.md) command, or the [**s (Search Memory)**](s--search-memory-.md) command.

```dbgcmd
~Thread s 
~ s 
```

## <span id="ddk_cmd_set_current_thread_dbg"></span><span id="DDK_CMD_SET_CURRENT_THREAD_DBG"></span>Parameters


<span id="_______Thread______"></span><span id="_______thread______"></span><span id="_______THREAD______"></span> *Thread*   
Specifies the thread to set or display. For more information about the syntax, see [Thread Syntax](thread-syntax.md).

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

You can specify threads only in user mode. In kernel mode, the tilde (~) refers to a processor.

If you use the **~s** syntax, the debugger displays information about the current thread.

This command also disassembles the current instruction for the current system, process, and thread.

 

 





