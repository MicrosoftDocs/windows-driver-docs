---
title: ~n (Suspend Thread)
description: The ~n command suspends execution of the specified thread.Do not confuse this command with the n (Set Number Base) command.
ms.assetid: 4b1063ad-edba-4cd3-9084-dc6c08c69f55
keywords: ["~n (Suspend Thread) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- ~n (Suspend Thread)
api_type:
- NA
ms.localizationpriority: medium
---

# ~n (Suspend Thread)


The **~n** command suspends execution of the specified thread.

Do not confuse this command with the [**n (Set Number Base)**](n--set-number-base-.md) command.

```dbgcmd
~Thread n 
```

## <span id="ddk_cmd_suspend_thread_dbg"></span><span id="DDK_CMD_SUSPEND_THREAD_DBG"></span>Parameters


<span id="_______Thread______"></span><span id="_______thread______"></span><span id="_______THREAD______"></span> *Thread*   
Specifies the thread or threads to suspend. For more information about the syntax, see [Thread Syntax](thread-syntax.md).

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
<td align="left"><p>Live debugging only</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>All</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information about the suspend count and how suspended threads behave and for a list of other commands that control the suspending and freezing of threads, see [Controlling Processes and Threads](controlling-processes-and-threads.md).

Remarks
-------

You can specify threads only in user mode. In kernel mode, the tilde (~) refers to a processor.

Every time that you use the **~n** command, the thread's suspend count is increased by one.

The thread's start address is displayed when you use this command.

 

 





