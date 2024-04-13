---
title: CTRL+ALT+\ (Debug Current Debugger)
description: The CTRL+ALT+\ key combination launches a new instance of CDB; this new debugger takes the current debugger as its target.
keywords: ["CTRL+ALT+\ (Debug Current Debugger) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- CTRL+ALT+\ (Debug Current Debugger)
api_type:
- NA
---

# CTRL+ALT+\\ (Debug Current Debugger)


The **CTRL+ALT+\\** key launches a new instance of CDB; this new debugger takes the current debugger as its target.

```dbgcmd
CTRL+ALT+\ 
```

## <span id="ddk_meta_ctrl_p_dbg"></span><span id="DDK_META_CTRL_P_DBG"></span>


### Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><strong>Debuggers</strong></td>
<td align="left"><p>WinDbg</p></td>
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

This is equivalent to launching a new CDB through the [**remote.exe**](the-remote-exe-utility.md) utility, and using it to debug the debugger that you are already running.

**CTRL+ALT+\\** is similar to the [**.dbgdbg (Debug Current Debugger)**](../debuggercmds/-dbgdbg--debug-current-debugger-.md) command, however **CTRL+ALT+\\** has the advantage that it can be used when no debugger command line is available.

 

 