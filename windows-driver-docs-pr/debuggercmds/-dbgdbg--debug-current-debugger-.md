---
title: .dbgdbg (Debug Current Debugger)
description: The .dbgdbg command launches a new instance of CDB; this new debugger takes the current debugger as its target.
keywords: [".dbgdbg (Debug Current Debugger) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- .dbgdbg (Debug Current Debugger)
api_type:
- NA
---

# .dbgdbg (Debug Current Debugger)


The **.dbgdbg** command launches a new instance of CDB; this new debugger takes the current debugger as its target.

```dbgcmd
.dbgdbg 
```

## <span id="ddk_meta_debug_current_debugger_dbg"></span><span id="DDK_META_DEBUG_CURRENT_DEBUGGER_DBG"></span>


### Environment

|  Item  | Description          |
|--------|----------------------|
|Modes   |User mode, kernel mode|
|Targets |Live, crash dump      |
|Platforms|All                  |

 

## Remarks

The **.dbgdbg** command is similar to the [**CTRL+P (Debug Current Debugger)**](../debugger/ctrl-p--debug-current-debugger-.md) control key. However, **.dbgdbg** is more versatile, because it can be used from WinDbg as well as KD and CDB, and it can be used to debug a debugging server on a remote computer.

 

 





