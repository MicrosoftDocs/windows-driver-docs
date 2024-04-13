---
title: CTRL+B (Quit Local Debugger)
description: The CTRL+B key causes the debugger to terminate abruptly. This does not end a remote debugging session.
keywords: ["CTRL+B (Quit Local Debugger) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- CTRL+B (Quit Local Debugger)
api_type:
- NA
---

# CTRL+B (Quit Local Debugger)


The CTRL+B key causes the debugger to terminate abruptly. This does not end a remote debugging session.

```dbgcmd
CTRL+B  ENTER 
```

## <span id="ddk_meta_ctrl_b_dbg"></span><span id="DDK_META_CTRL_B_DBG"></span>


### Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Debuggers</strong></p></td>
<td align="left"><p>CDB and KD only</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>user mode, kernel mode</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>live, crash dump</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>all</p></td>
</tr>
</tbody>
</table>

 

## Remarks

In CDB, the [**q (Quit)**](../debuggercmds/q--qq--quit-.md) command should be used to exit. CTRL+B should only be used if the debugger is not responding.

In KD, the **q** command will end the debugging session and leave the target computer locked. If you need to preserve the debugging session (so a new debugger can connect to it), or if you need to leave the target computer running, you should use CTRL+B.

In WinDbg, the equivalent command is **File | Exit** or ALT+F4.

 

 