---
title: .pagein (Page In Memory)
description: "The .pagein command pages in the specified region of memory."
keywords: ["Page In Memory (.pagein) command", "memory, Page In Memory (.pagein) command", ".pagein (Page In Memory) Windows Debugging"]
ms.date: 08/29/2023
topic_type:
- apiref
ms.topic: reference
api_name:
- .pagein (Page In Memory)
api_type:
- NA
---

# .pagein (Page In Memory)

The **.pagein** command pages in the specified region of memory.

```dbgcmd
.pagein [Options] Address
```

## Parameters

*Options*

Any of the following options:

**/p** *Process*  

Specifies the address of the process that owns the memory that you want to page in. (More precisely, this parameter specifies the address of the EPROCESS block for the process.) If you omit *Process* or specify zero, the debugger uses the current process setting. For more information about the process setting, see [**.process (Set Process Context)**](-process--set-process-context-.md)

**/f**  
Forces the memory to be paged in, even if the address is in kernel memory and the version of Windows does not support this action.

*Address*

Specifies the address to page in.

### Environment

| Item      | Description                                              |
|-----------|----------------------------------------------------------|
| Modes     | Kernel mode only (but not during local kernel debugging) |
| Targets   | Live debugging only                                      |
| Platforms | All                                                      |

## Remarks

After you run the **.pagein** command, you must use the [**g (Go)**](g--go-.md) command to resume program execution. After a brief time, the target computer automatically breaks into the debugger again.

At this point, the address that you specify is paged in. If you use the **/p** option, the process context is also set to the specified process, exactly as if you used the [**.process /i Process**](-process--set-process-context-.md) command.

If the address is already paged in, the **.pagein** command still checks that the address is paged in and then breaks back into the debugger. If the address is invalid, this command only breaks back into the debugger.

## Requirements

Supported in Windows XP and later versions of Windows.
