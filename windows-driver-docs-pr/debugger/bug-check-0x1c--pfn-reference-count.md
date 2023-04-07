---
title: Bug Check 0x1C PFN_REFERENCE_COUNT
description: The PFN_REFERENCE_COUNT bug check has a value of 0x0000001C.This bug check appears very infrequently.
keywords: ["Bug Check 0x1C PFN_REFERENCE_COUNT", "PFN_REFERENCE_COUNT"]
ms.date: 04/06/2023
topic_type:
- apiref
ms.topic: reference
api_name:
- PFN_REFERENCE_COUNT
api_type:
- NA
---

# Bug Check 0x1C: PFN\_REFERENCE\_COUNT

The PFN\_REFERENCE\_COUNT bug check has a value of 0x0000001C. This indicates that a reference count error was detected. It can be caused by counter overflows, underflows, or an object that is used after it has been freed. Examine the stack to determine the fault. Note: This bug check code is used to report multiple types of reference count errors, not necessarily related to Memory Manager Page Frame Numbers (PFNs).

> [!IMPORTANT]
> This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).

## PARAMETERS

| Parameter | Description |
|-----------|-------------|
| 1         | Not used    |
| 2         | Not used    |
| 3         | Not used    |
| 4         | Not used    |

## Resolution

The [**!analyze**](-analyze.md) debug extension displays information about the bug check and can be helpful in determining the root cause.
