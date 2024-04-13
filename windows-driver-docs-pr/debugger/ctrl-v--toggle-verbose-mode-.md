---
title: CTRL+V (Toggle Verbose Mode)
description: The CTRL+V key toggles verbose mode on and off.
keywords: ["CTRL+V (Toggle Verbose Mode) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- CTRL+V (Toggle Verbose Mode)
api_type:
- NA
---

# CTRL+V (Toggle Verbose Mode)


The CTRL+V key toggles verbose mode on and off.

CDB / KD Syntax

```dbgcmd
CTRL+V  ENTER 
```

WinDbg Syntax

```dbgcmd
CTRL+ALT+V 
```

## <span id="ddk_meta_ctrl_v_dbg"></span><span id="DDK_META_CTRL_V_DBG"></span>


### Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Debuggers</strong></p></td>
<td align="left"><p>CDB, KD, WinDbg</p></td>
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

When verbose mode is turned on, some display commands (such as register dumping) produce more detailed output. Every MODULE LOAD operation that is sent to the debugger will be displayed. And every time a driver or DLL is loaded by the operating system, the debugger will be notified.

In WinDbg, this can also be accomplished by selecting **View | Verbose Output**.

 

 