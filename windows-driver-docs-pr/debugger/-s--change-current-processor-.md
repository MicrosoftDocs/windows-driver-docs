---
title: ~s (Change Current Processor)
description: The ~s command sets which processor is debugged on a multiprocessor system.In kernel mode, ~s changes the current processor.
ms.assetid: bd036a25-1e3c-4b57-9c7c-5f1730008cd7
keywords: ["Change Current Processor (~s) command", "multiprocessor computer, Change Current Processor (~s) command", "processors", "~s (Change Current Processor) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- ~s (Change Current Processor)
api_type:
- NA
ms.localizationpriority: medium
---

# ~s (Change Current Processor)


The **~s** command sets which processor is debugged on a multiprocessor system.

In kernel mode, **~s** changes the current processor. Do not confuse this command with the [**~s (Set Current Thread)**](-s--set-current-thread-.md) command (which works only in user mode), the [**|s (Set Current Process)**](-s--set-current-process-.md) command, the [**||s (Set Current System)**](--s--set-current-system-.md) command, or the [**s (Search Memory)**](s--search-memory-.md) command.

```dbgcmd
~Processor s
```

## <span id="ddk_cmd_change_current_processor_dbg"></span><span id="DDK_CMD_CHANGE_CURRENT_PROCESSOR_DBG"></span>Parameters


<span id="_______Processor______"></span><span id="_______processor______"></span><span id="_______PROCESSOR______"></span> *Processor*   
Specifies the number of the processor to debug.

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>Kernel mode only</p></td>
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

 

Remarks
-------

You can specify processors only in kernel mode. In user mode, the tilde (~) refers to a thread.

You can immediately tell when you are working on a multiple processor system by the shape of the kernel debugging prompt. In the following example, 0: means that you are debugging the first processor in the computer.

```dbgcmd
0: kd>
```

Use the following command to switch between processors:

```dbgcmd
0: kd> ~1s
1: kd>
```

Now the second processor in the computer that is being debugged.

## <span id="see_also"></span>See also


[Multiprocessor Syntax](multiprocessor-syntax.md)

 

 






