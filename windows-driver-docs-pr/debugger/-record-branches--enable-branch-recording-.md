---
title: .record_branches (Enable Branch Recording)
description: The .record_branches command enables the recording of branches that the target's code executed.
ms.assetid: 522eeba5-b6c5-473c-9c8e-8ef4c941079f
keywords: ["Enable Branch Recording (.record_branches) command", ".record_branches (Enable Branch Recording) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- .record_branches (Enable Branch Recording)
api_type:
- NA
ms.localizationpriority: medium
---

# .record\_branches (Enable Branch Recording)


The **.record\_branches** command enables the recording of branches that the target's code executed.

```dbgcmd
.record_branches {1|0} 
.record_branches
```

## <span id="ddk_meta_enable_branch_recording_dbg"></span><span id="DDK_META_ENABLE_BRANCH_RECORDING_DBG"></span>


### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>User mode, kernel mode</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>Live debugging only</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>x64-based only</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The **.record\_branches 1** command enables the recording of branches in the target's code. The **.record\_branches 0** command disables this recording.

Without parameters, **.record\_branches** displays the current status of this setting.

 

 





