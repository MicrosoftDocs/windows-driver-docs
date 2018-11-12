---
title: .sleep (Pause Debugger)
description: The .sleep command causes the user-mode debugger to pause and the target computer to become active. This command is only used when you are controlling the user-mode debugger from the kernel debugger.
ms.assetid: bc3ee17f-e3b8-4bdb-8c80-6b1fef29000e
keywords: ["Pause Debugger (.sleep) command", "controlling the user-mode debugger from the kernel debugger, Pause Debugger (.sleep) command", ".sleep (Pause Debugger) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- .sleep (Pause Debugger)
api_type:
- NA
ms.localizationpriority: medium
---

# .sleep (Pause Debugger)


The **.sleep** command causes the user-mode debugger to pause and the target computer to become active. This command is only used when you are controlling the user-mode debugger from the kernel debugger.

```dbgcmd
.sleep milliseconds
```

## <span id="ddk_meta_pause_debugger_dbg"></span><span id="DDK_META_PAUSE_DEBUGGER_DBG"></span>Parameters


<span id="_______milliseconds______"></span><span id="_______MILLISECONDS______"></span> *milliseconds*   
Specifies the length of the pause, in milliseconds.

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>controlling the user-mode debugger from the kernel debugger</p></td>
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

For details and information about how to wake up a debugger in sleep mode, see [Controlling the User-Mode Debugger from the Kernel Debugger](controlling-the-user-mode-debugger-from-the-kernel-debugger.md).

Remarks
-------

When you are controlling the user-mode debugger from the kernel debugger, and the user-mode debugger prompt is visible in the kernel debugger, this command will activate sleep mode. The kernel debugger, the user-mode debugger, and the target application will all freeze, but the rest of the target computer will become active.

If you use this command in any other scenario, it will simply freeze the debugger for a period of time.

The sleep time is in milliseconds and interpreted according to the default radix, unless a prefix such as **0n** is used. Thus, if the default radix is 16, the following command will cause about 65 seconds of sleep:

```dbgcmd
0:000> .sleep 10000
```

 

 





