---
title: .force_tb (Forcibly Allow Branch Tracing)
description: The .force_tb command forces the processor to trace branches early in the boot process.
keywords: [".force_tb (Forcibly Allow Branch Tracing) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- .force_tb (Forcibly Allow Branch Tracing)
api_type:
- NA
---

# .force\_tb (Forcibly Allow Branch Tracing)


The **.force\_tb** command forces the processor to trace branches early in the boot process.

```dbgcmd
.force_tb 
```

## <span id="ddk_meta_forcibly_allow_branch_tracing_dbg"></span><span id="DDK_META_FORCIBLY_ALLOW_BRANCH_TRACING_DBG"></span>


### Environment

|  Item  | Description          |
|--------|----------------------|
|Modes   |User mode, kernel mode|
|Targets |Live, crash dump      |
|Platforms|All                  |

 

## Remarks

Typically, branch tracing is enabled after the debugger initializes the processor control block (PRCB). This initialization occurs early in the boot process.

However, if you have to use the [**tb (Trace to Next Branch)**](tb--trace-to-next-branch-.md) command before this initialization, you can use the **.force\_tb** command to enable branch tracing earlier. Use this command carefully because it can corrupt your processor state.

 

 





