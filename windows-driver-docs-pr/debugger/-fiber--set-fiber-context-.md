---
title: .fiber (Set Fiber Context)
description: The .fiber command specifies which fiber is used for the fiber context.
keywords: ["Set Fiber Context (.fiber) command", "context, Set Fiber Context (.fiber) command", "fibers", ".fiber (Set Fiber Context) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- .fiber (Set Fiber Context)
api_type:
- NA
---

# .fiber (Set Fiber Context)


The **.fiber** command specifies which fiber is used for the fiber context.

```dbgcmd
.fiber [Address]
```

## <span id="ddk_meta_set_fiber_context_dbg"></span><span id="DDK_META_SET_FIBER_CONTEXT_DBG"></span>Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the address of the fiber. If you omit this parameter or specify zero, the fiber context is reset to the current fiber.

### Environment

|  Item  | Description          |
|--------|----------------------|
|Modes   |User mode, kernel mode|
|Targets |Live, crash dump      |
|Platforms|All                  |

 

### Additional Information

For more information about the process context, the register context, and the local context, see [Changing Contexts](changing-contexts.md).

 

 





