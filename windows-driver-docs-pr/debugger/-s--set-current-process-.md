---
title: s (Set Current Process)
description: The s command sets or displays the current process number.
ms.assetid: 6b4d8e00-426c-496b-9c52-c60faeb0c975
keywords: ["s (Set Current Process) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- s (Set Current Process)
api_type:
- NA
ms.localizationpriority: medium
---

# |s (Set Current Process)


The **|s** command sets or displays the current process number.

Do not confuse this command with the [**s (Search Memory)**](s--search-memory-.md), [**~s (Change Current Processor)**](-s--change-current-processor-.md), [**~s (Set Current Thread)**](-s--set-current-thread-.md), or [**||s (Set Current System)**](--s--set-current-system-.md) command.

```dbgcmd
|Process s 
| s 
```

## <span id="ddk_cmd_set_current_process_dbg"></span><span id="DDK_CMD_SET_CURRENT_PROCESS_DBG"></span>Parameters


<span id="_______Process______"></span><span id="_______process______"></span><span id="_______PROCESS______"></span> *Process*   
Specifies the process to set or display. For more information about the syntax, see [Process Syntax](process-syntax.md).

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

For more information about other methods of displaying or controlling processes and threads, see [Controlling Processes and Threads](controlling-processes-and-threads.md).

Remarks
-------

You can specify processes only in user mode.

If you use the **|s** syntax, the debugger displays information about the current process.

This command also disassembles the current instruction for the current system, process, and thread.

 

 





