---
title: .wake (Wake Debugger)
description: The .wake command causes sleep mode to end. This command is used only when you are controlling the user-mode debugger from the kernel debugger.
ms.assetid: 01aead7e-1f46-46cf-a697-ab5ff6329ac7
keywords: ["Wake Debugger (.wake) command", "controlling the user-mode debugger from the kernel debugger, Wake Debugger (.wake) command", ".wake (Wake Debugger) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- .wake (Wake Debugger)
api_type:
- NA
ms.localizationpriority: medium
---

# .wake (Wake Debugger)


The **.wake** command causes sleep mode to end. This command is used only when you are controlling the user-mode debugger from the kernel debugger.

```dbgcmd
.wake PID
```

## <span id="ddk_meta_wake_debugger_dbg"></span><span id="DDK_META_WAKE_DEBUGGER_DBG"></span>Parameters


<span id="_______PID______"></span><span id="_______pid______"></span> *PID*   
The process ID of the user-mode debugger.

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

For more details, see [Controlling the User-Mode Debugger from the Kernel Debugger](controlling-the-user-mode-debugger-from-the-kernel-debugger.md). For information about how to find the process ID of the debugger, see [Finding the Process ID](finding-the-process-id.md).

Remarks
-------

When you are controlling the user-mode debugger from the kernel debugger and the system is in sleep mode, this command can be used to wake up the debugger before the sleep timer runs out.

This command is not issued in the user-mode debugger on the target machine, nor in the kernel debugger on the host machine. It must be issued from a third debugger (KD, CDB, or NTSD) running on the target machine.

This debugger can be started expressly for this purpose, or can be another debugger that happens to be running. However, if there is no other debugger already running, it is easier just to use CDB with the **-wake** [**command-line option**](cdb-command-line-options.md).

 

 





