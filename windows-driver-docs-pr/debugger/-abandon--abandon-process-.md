---
title: .abandon (Abandon Process)
description: The .abandon command ends the debugging session, but leaves the target application in a debugging state. This returns the debugger to dormant mode.
keywords: [".abandon (Abandon Process) Windows Debugging"]
ms.date: 08/30/2023
topic_type:
- apiref
ms.topic: reference
api_name:
- .abandon (Abandon Process)
api_type:
- NA
---

# .abandon (Abandon Process)

The **.abandon** command ends the debugging session, but leaves the target application in a debugging state. This returns the debugger to dormant mode.

```dbgcmd
.abandon [/h|/n] 
```

## Parameters

**/h**   

Any outstanding debug event will be continued and marked as handled. This is the default.

**/n**

Any outstanding debug event will be continued unhandled.

### Environment

This command is only supported in Windows XP and later versions of Windows.

|  Item  | Description          |
|--------|----------------------|
|Modes | user mode only |
|Targets | live debugging only |
|Platforms | all  |

### Additional Information

If the target is left in a debugging state, a new debugger can be attached to it. See [Re-attaching to the Target Application](reattaching-to-the-target-application.md) for details. However, after a process has been abandoned once, it can never be restored to a running state without a debugger attached.
