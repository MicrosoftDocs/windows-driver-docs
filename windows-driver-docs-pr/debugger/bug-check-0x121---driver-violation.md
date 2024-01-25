---
title: Bug Check 0X121 DRIVER_VIOLATION
description: The DRIVER_VIOLATION bug check has a value of 0x00000121. This bug check indicates that a driver has caused a violation.
keywords: ["Bug Check 0x121 DRIVER_VIOLATION", "DRIVER_VIOLATION"]
ms.date: 11/15/2023
topic_type:
- apiref
ms.topic: reference
api_name:
- DRIVER_VIOLATION
api_type:
- NA
---

# Bug Check 0x121: DRIVER\_VIOLATION

The DRIVER\_VIOLATION bug check has a value of 0x00000121. This bug check indicates that a driver has caused a violation.

> [!IMPORTANT]
> This article is for programmers. If you're a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).

## DRIVER\_VIOLATION Parameters

Parameter 1 indicates the type of violation.

| Parameter 1 | Parameter 2       | Parameter 3         | Parameter 4 | Cause                                                                       |
|-------------|-------------------|---------------------|-------------|-----------------------------------------------------------------------------|
| 0x1 | The current IRQL. | The required IRQL.          | Reserved    | A driver has called a function which can only be called at a specific IRQL. |
| 0x2 | The current IRQL. | The maximum allowable IRQL. | Reserved    | A driver has called a function at a greater IRQL than the function can be called at. |

## Remarks

Use a kernel debugger and view the call stack to determine the name of the driver that caused the violation: the [**!analyze**](../debuggercmds/-analyze.md) debug extension displays information about the bug check and can be helpful in determining the root cause, then enter one of the [**k (Display Stack Backtrace)**](../debuggercmds/k--kb--kc--kd--kp--kp--kv--display-stack-backtrace-.md) commands to view the call stack.
