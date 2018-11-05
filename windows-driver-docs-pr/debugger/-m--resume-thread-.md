---
title: ~m (Resume Thread)
description: The ~m command resumes execution of the specified thread.Do not confuse this command with the m (Move Memory) command.
ms.assetid: fc4eec45-2a28-4571-abf5-3896b77a52c9
keywords: ["~m (Resume Thread) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- ~m (Resume Thread)
api_type:
- NA
ms.localizationpriority: medium
---

# ~m (Resume Thread)


The **~m** command resumes execution of the specified thread.

Do not confuse this command with the [**m (Move Memory)**](m--move-memory-.md) command.

```dbgcmd
~Thread m 
```

## <span id="ddk_cmd_resume_thread_dbg"></span><span id="DDK_CMD_RESUME_THREAD_DBG"></span>Parameters


<span id="_______Thread______"></span><span id="_______thread______"></span><span id="_______THREAD______"></span> *Thread*   
Specifies the thread or threads to resume. For more information about the syntax, see [Thread Syntax](thread-syntax.md).

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

Every time that you use the **~m** command, the thread's suspend count is decreased by one.

 

 





