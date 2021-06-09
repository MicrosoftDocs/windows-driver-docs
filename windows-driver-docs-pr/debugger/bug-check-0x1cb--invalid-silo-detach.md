---
title: Bug Check 0x1CB INVALID_SILO_DETACH
description: The INVALID_SILO_DETACH bug check has a value of 0x000001CB. It indicates that a thread failed to detach from a silo before exiting.
keywords: ["Bug Check 0x1CB INVALID_SILO_DETACH", "INVALID_SILO_DETACH"]
ms.date: 02/21/2019
topic_type:
- apiref
api_name:
- INVALID_SILO_DETACH
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x1CB: INVALID\_SILO\_DETACH

The INVALID\_SILO\_DETACH bug check has a value of 0x000001CB. It indicates that a thread failed to detach from a silo before exiting.

> [!IMPORTANT]
> This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).

 

## INVALID\_SILO\_DETACH Parameters

|Parameter|Description|
|-------- |---------- |
|1| Pointer to the attached thread. |
|2| Previously attached silo. |
|3| Pointer to the thread's process. |
|4| Reserved. |


## ## Cause
A thread failed to detach from a silo before exiting. 



## ## See Also-

[Bug Check Code Reference](bug-check-code-reference2.md)

