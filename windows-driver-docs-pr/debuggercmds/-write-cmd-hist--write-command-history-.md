---
title: .write_cmd_hist (Write Command History)
description: The .write_cmd_hist command writes the entire history of the Debugger Command window to a file.
keywords: [".write_cmd_hist (Write Command History) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- .write_cmd_hist (Write Command History)
api_type:
- NA
---

# .write\_cmd\_hist (Write Command History)


The **.write\_cmd\_hist** command writes the entire history of the Debugger Command window to a file.

```dbgcmd
.write_cmd_hist Filename 
```

## <span id="ddk_meta_cmd_hist_write_command_history_dbg"></span><span id="DDK_META_CMD_HIST_WRITE_COMMAND_HISTORY_DBG"></span>Parameters


<span id="_______Filename______"></span><span id="_______filename______"></span><span id="_______FILENAME______"></span> *Filename*   
Specifies the path and filename of the file that will be created.

### Environment

This command is available only in WinDbg and cannot be used in script files.

|  Item  | Description          |
|--------|----------------------|
|Modes   |User mode, kernel mode|
|Targets |Live, crash dump      |
|Platforms|All                  |

 

 

 





