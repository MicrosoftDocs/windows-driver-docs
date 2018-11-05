---
title: CTRL+D (Toggle Debug Info)
description: The CTRL+D key toggles debugger internal information flow on and off. This is used to restart communication in cases where the debugger is not communicating properly.
ms.assetid: fcc5d597-6a3f-4d6c-82f9-3624efb4f434
keywords: ["CTRL+D (Toggle Debug Info) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- CTRL+D (Toggle Debug Info)
api_type:
- NA
ms.localizationpriority: medium
---

# CTRL+D (Toggle Debug Info)


The CTRL+D key toggles debugger internal information flow on and off. This is used to restart communication between the target computer and the host computer in cases where the debugger is not communicating properly.

KD Syntax

```dbgcmd
CTRL+D  ENTER 
```

WinDbg Syntax

```dbgcmd
CTRL+ALT+D 
```

## <span id="ddk_meta_ctrl_d_dbg"></span><span id="DDK_META_CTRL_D_DBG"></span>


### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Debuggers</strong></p></td>
<td align="left"><p>KD and WinDbg only</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>kernel mode only</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>live debugging only</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>all</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

When this is toggled on, the debugger outputs information about the communication between the host computer and the target computer.

This key can be used to test whether the debugger has crashed. If you suspect that either the debugger or the target is frozen, use this key. If you see packets being sent, the target is still working. If you see time-out messages, then the target is not responding. If there are no messages at all, the debugger has crashed.

If the target is not responding, use CTRL+R ENTER CTRL+C. If time-out messages continue to appear, the target has crashed (or the debugger was misconfigured).

This is also useful for debugging the KD debugger itself.

 

 





