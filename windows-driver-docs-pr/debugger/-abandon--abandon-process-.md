---
title: .abandon (Abandon Process)
description: The .abandon command ends the debugging session, but leaves the target application in a debugging state. This returns the debugger to dormant mode.
ms.assetid: e44ae9b8-b6a2-4648-911d-61ff3c94527c
keywords: [".abandon (Abandon Process) Windows Debugging"]
ms.author: domars
ms.date: 09/17/2018
topic_type:
- apiref
api_name:
- .abandon (Abandon Process)
api_type:
- NA
ms.localizationpriority: medium
---

# .abandon (Abandon Process)


The **.abandon** command ends the debugging session, but leaves the target application in a debugging state. This returns the debugger to dormant mode.

```dbgcmd
.abandon [/h|/n] 
```

## <span id="ddk_meta_abandon_process_dbg"></span><span id="DDK_META_ABANDON_PROCESS_DBG"></span>Parameters


<span id="________h______"></span><span id="________H______"></span> **/h**   
Any outstanding debug event will be continued and marked as handled. This is the default.

<span id="________n______"></span><span id="________N______"></span> **/n**   
Any outstanding debug event will be continued unhandled.

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

This command is only supported in Windows XP and later versions of Windows.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>user mode only</p></td>
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

If the target is left in a debugging state, a new debugger can be attached to it. See [Re-attaching to the Target Application](reattaching-to-the-target-application.md) for details. However, after a process has been abandoned once, it can never be restored to a running state without a debugger attached.

 

 





