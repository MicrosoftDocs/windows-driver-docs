---
title: .dbgdbg (Debug Current Debugger)
description: The .dbgdbg command launches a new instance of CDB; this new debugger takes the current debugger as its target.
ms.assetid: a90392b5-d8ae-495d-8074-060e4ec89037
keywords: [".dbgdbg (Debug Current Debugger) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- .dbgdbg (Debug Current Debugger)
api_type:
- NA
ms.localizationpriority: medium
---

# .dbgdbg (Debug Current Debugger)


The **.dbgdbg** command launches a new instance of CDB; this new debugger takes the current debugger as its target.

```dbgcmd
.dbgdbg 
```

## <span id="ddk_meta_debug_current_debugger_dbg"></span><span id="DDK_META_DEBUG_CURRENT_DEBUGGER_DBG"></span>


### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

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

The **.dbgdbg** command is similar to the [**CTRL+P (Debug Current Debugger)**](ctrl-p--debug-current-debugger-.md) control key. However, **.dbgdbg** is more versatile, because it can be used from WinDbg as well as KD and CDB, and it can be used to debug a debugging server on a remote computer.

 

 





