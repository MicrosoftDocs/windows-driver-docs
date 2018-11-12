---
title: .write_cmd_hist (Write Command History)
description: The .write_cmd_hist command writes the entire history of the Debugger Command window to a file.
ms.assetid: 7d512f0c-56cd-48e5-b618-d5615113f065
keywords: [".write_cmd_hist (Write Command History) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- .write_cmd_hist (Write Command History)
api_type:
- NA
ms.localizationpriority: medium
---

# .write\_cmd\_hist (Write Command History)


The **.write\_cmd\_hist** command writes the entire history of the Debugger Command window to a file.

```dbgcmd
.write_cmd_hist Filename 
```

## <span id="ddk_meta_cmd_hist_write_command_history_dbg"></span><span id="DDK_META_CMD_HIST_WRITE_COMMAND_HISTORY_DBG"></span>Parameters


<span id="_______Filename______"></span><span id="_______filename______"></span><span id="_______FILENAME______"></span> *Filename*   
Specifies the path and filename of the file that will be created.

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

This command is available only in WinDbg and cannot be used in script files.

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

 

 

 





