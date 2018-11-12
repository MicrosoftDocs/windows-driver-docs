---
title: .detach (Detach from Process)
description: The .detach command ends the debugging session, but leaves any user-mode target application running.
ms.assetid: 4f0fbd8b-3037-4549-99da-be40a091a363
keywords: [".detach (Detach from Process) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- .detach (Detach from Process)
api_type:
- NA
ms.localizationpriority: medium
---

# .detach (Detach from Process)


The **.detach** command ends the debugging session, but leaves any user-mode target application running.

```dbgcmd
.detach [ /h | /n ]
```

## <span id="ddk_meta_detach_from_process_dbg"></span><span id="DDK_META_DETACH_FROM_PROCESS_DBG"></span>Parameters


<span id="________h______"></span><span id="________H______"></span> **/h**   
Any outstanding debug event will be continued and marked as handled. This is the default.

<span id="________n______"></span><span id="________N______"></span> **/n**   
Any outstanding debug event will be continued without being marked as handled.

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

For live user-mode debugging, this command is only supported in Windows XP and later versions of Windows.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>user mode, kernel mode</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>live, crash dump</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>all</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

This command will end the debugging session in any of the following scenarios:

-   When you are debugging a user-mode or kernel-mode dump file.

-   (Windows XP and later) When you are debugging a live user-mode target.

-   When you are noninvasively debugging a user-mode target.

If you are only debugging a single target, the debugger will return to dormant mode after it detaches.

If you are [debugging multiple targets](debugging-multiple-targets.md), the debugging session will continue with the remaining targets.

 

 





