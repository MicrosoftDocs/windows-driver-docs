---
title: Bug check 0x101 CLOCK_WATCHDOG_TIMEOUT
description: Learn how the CLOCK_WATCHDOG_TIMEOUT bug check indicates that an expected clock interrupt on a secondary processor isn't received within the allocated interval.
keywords: ["Bug Check 0x101 CLOCK_WATCHDOG_TIMEOUT", "CLOCK_WATCHDOG_TIMEOUT"]
ms.date: 02/24/2023
topic_type:
- apiref
api_name:
- CLOCK_WATCHDOG_TIMEOUT
api_type:
- NA
---

# Bug check 0x101: CLOCK_WATCHDOG_TIMEOUT

The CLOCK_WATCHDOG_TIMEOUT bug check has a value of 0x00000101. This bug check indicates that an expected clock interrupt on a secondary processor, in a multi-processor system, wasn't received within the allocated interval.

> [!IMPORTANT]
> This article is for programmers. If you're a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).

## CLOCK_WATCHDOG_TIMEOUT parameters

| Parameter | Description                                                                       |
|-----------|-----------------------------------------------------------------------------------|
| 1         | Clock interrupt time-out interval, in nominal clock ticks.                        |
| 2         | 0                                                                                 |
| 3         | The address of the processor control block (PRCB) for the unresponsive processor. |
| 4         | The index of the hung processor.                                                  |

## Cause

The specified processor isn't processing interrupts. Typically, this bug check occurs when the processor is nonresponsive or is deadlocked.


## Resolution

The following debugger commands can be used to investigate the processor states, IRQL level, and code that is running, to attempt to determine which piece of code is not allowing forward execution.

[!analyze](-analyze.md)

[k, kb, kc, kd, kp, kP, kv (Display Stack Backtrace)](k--kb--kc--kd--kp--kp--kv--display-stack-backtrace-.md)

[!pcr](-pcr.md)

[!prcb](-prcb.md)

[!irql](-irql.md)

## See Also

[Bug Check Code Reference](bug-check-code-reference2.md)
