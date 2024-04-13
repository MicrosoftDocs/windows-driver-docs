---
title: Bug Check 0x161 LIVE_SYSTEM_DUMP
description: The LIVE_SYSTEM_DUMP live dump has a value of 0x00000161. This indicates that the system administrator requested the collection of a live system memory dump.
keywords: ["Bug Check 0x161 LIVE_SYSTEM_DUMP", "LIVE_SYSTEM_DUMP"]
ms.date: 01/30/2023
topic_type:
- apiref
ms.topic: reference
api_name:
- LIVE_SYSTEM_DUMP
api_type:
- NA
---

# Bug Check 0x161: LIVE\_SYSTEM\_DUMP

The LIVE\_SYSTEM\_DUMP live dump has a value of 0x00000161. This indicates that the system administrator requested the collection of a live system memory dump.

(This code can never be used for a real bug check; it is used to identify live dumps.)

## LIVE\_SYSTEM\_DUMP Parameters

| Parameter | Description                  |
|-----------|------------------------------|
| 1         | 0x005461736b6d6772, which is a hexadecimal encoding of the text string 'Taskmgr'.   |
| 2         | Reserved |
| 3         | Reserved |
| 4         | Reserved |

## Remarks

Starting in Windows 22H2, version 25276, Task manger can be used to create a live system memory dump. For more information, see [Task Manager live memory dump](task-manager-live-dump.md).



## See also

[Task Manager live memory dump](task-manager-live-dump.md)

[Kernel Live Dump Code Reference](bug-check-code-reference-live-dump.md)
