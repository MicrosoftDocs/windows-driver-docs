---
title: Bug Check 0x1CA SYNTHETIC_WATCHDOG_TIMEOUT
description: The SYNTHETIC_WATCHDOG_TIMEOUT bug check has a value of 0x000001CA. A system wide watchdog has expired. This indicates that the system is hung and not processing timer ticks.
keywords: ["Bug Check 0x1CA SYNTHETIC_WATCHDOG_TIMEOUT", "SYNTHETIC_WATCHDOG_TIMEOUT"]
ms.date: 01/29/2021
topic_type:
- apiref
api_name:
- SYNTHETIC_WATCHDOG_TIMEOUT
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x1CA: SYNTHETIC\_WATCHDOG\_TIMEOUT

The SYNTHETIC\_WATCHDOG\_TIMEOUT bug check has a value of 0x000001CA. A system wide watchdog has expired. This indicates that the system is hung and not processing timer ticks.

> [!IMPORTANT]
> This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).

## SYNTHETIC\_WATCHDOG\_TIMEOUT Parameters

|Parameter|Description|
|-------- |---------- |
|1|The time since the watchdog was last reset, in interrupt time.|
|2| The current interrupt time. |
|3| The current QPC timestamp. |
|4| The index of the clock processor. |

## Cause

A system wide watchdog has expired. This indicates that the system is hung and not processing timer ticks.

## Resolution

The [**!analyze**](-analyze.md) debugger extension displays information about the bug check and can be helpful in determining the root cause. For more information about WinDbg and **!analyze**, see [Using the !analyze extension](using-the--analyze-extension.md) and [!analyze](-analyze.md).


## See Also

[Bug Check Code Reference](bug-check-code-reference2.md)
