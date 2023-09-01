---
title: .detach (Detach from Process)
description: The .detach command ends the debugging session, but leaves any user-mode target application running.
keywords: [".detach (Detach from Process) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- .detach (Detach from Process)
api_type:
- NA
---

# .detach (Detach from Process)


The **.detach** command ends the debugging session, but leaves any user-mode target application running.

```dbgcmd
.detach [ /h | /n ]
```

## <span id="ddk_meta_detach_from_process_dbg"></span><span id="DDK_META_DETACH_FROM_PROCESS_DBG"></span>Parameters


<span id="________h______"></span><span id="________H______"></span> **/h**   
Any outstanding debug event will be continued and marked as handled. This is the default.

<span id="________n______"></span><span id="________N______"></span> **/n**   
Any outstanding debug event will be continued without being marked as handled.

### Environment

For live user-mode debugging, this command is only supported in Windows XP and later versions of Windows.

|  Item  | Description          |
|--------|----------------------|
|Modes   |User mode, kernel mode|
|Targets |Live, crash dump      |
|Platforms|All                  |

 

## Remarks

This command will end the debugging session in any of the following scenarios:

-   When you are debugging a user-mode or kernel-mode dump file.

-   When you are debugging a live user-mode target.

-   When you are noninvasively debugging a user-mode target.

If you are only debugging a single target, the debugger will return to dormant mode after it detaches.

If you are [debugging multiple targets](debugging-multiple-targets.md), the debugging session will continue with the remaining targets.

 

 





