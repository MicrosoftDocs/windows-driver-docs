---
title: SeStopImpersonatingClient routine
description: Learn more about the SeStopImpersonatingClient routine.
keywords: ["SeStopImpersonatingClient routine Installable File System Drivers"]
topic_type:
- apiref
api_name:
- SeStopImpersonatingClient
api_location:
- ntifs.h
api_type:
- HeaderDef
ms.date: 03/13/2023
ms.topic: reference
---

# SeStopImpersonatingClient routine

The **SeStopImpersonatingClient** routine ends the calling thread's impersonation of a user.

## Syntax

```ManagedCPlusPlus
VOID SeStopImpersonatingClient(void);
```

## Parameters

This routine has no parameters.

## Return value

None

## Remarks

A server thread can impersonate a user by calling the [**SeImpersonateClientEx**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-seimpersonateclientex) routine. When the thread is done impersonating the user, it calls the **SeStopImpersonatingClient** routine to end the impersonation.

## Requirements

| Requirement type | Requirement |
| ---------------- | ----------- |
| Minimum supported client | Windows XP |
| Header                   | *Ntifs.h* (include *Ntifs.h*) |
| IRQL                     | PASSIVE_LEVEL |

## See also

[**SeImpersonateClientEx**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-seimpersonateclientex)
