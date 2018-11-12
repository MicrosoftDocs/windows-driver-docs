---
title: CTRL+R (Re-synchronize)
description: The CTRL+R key synchronizes with the target computer.
ms.assetid: 95ffa380-af90-4d56-b973-038e7ccc6760
keywords: ["CTRL+R (Re-synchronize) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- CTRL+R (Re-synchronize)
api_type:
- NA
ms.localizationpriority: medium
---

# CTRL+R (Re-synchronize)


The CTRL+R key synchronizes with the target computer.

KD Syntax

```dbgcmd
CTRL+R  ENTER 
```

WinDbg Syntax

```dbgcmd
CTRL+ALT+R 
```

## <span id="ddk_meta_ctrl_r_dbg"></span><span id="DDK_META_CTRL_R_DBG"></span>


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

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For other methods of re-establishing contact with the target, see [Synchronizing with the Target Computer](synchronizing-with-the-target-computer.md).

Remarks
-------

This attempts to synchronize the host computer with the target computer. Use this key if the target is not responding.

If you are using a 1394 kernel connection, resynchronization may not always be successful.

 

 





