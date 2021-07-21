---
title: Bug Check 0x1A0 TTM_WATCHDOG_TIMEOUT
description: The TTM_WATCHDOG_TIMEOUT bug check has a value of 0x000001A0. It indicates that the terminal topology manager detected that for the configured timeouts some device specific operations did not complete.
keywords: ["Bug Check 0x1A0 TTM_WATCHDOG_TIMEOUT", "TTM_WATCHDOG_TIMEOUT"]
ms.date: 01/04/2019
topic_type:
- apiref
api_name:
- TTM_WATCHDOG_TIMEOUT
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x1A0: TTM\_WATCHDOG\_TIMEOUT

The TTM\_WATCHDOG\_TIMEOUT bug check has a value of 0x000001A0. It indicates that the terminal topology manager detected that for the configured timeouts some device specific operations did not complete.

> [!IMPORTANT]
> This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).

 

## TTM\_WATCHDOG\_TIMEOUT Parameters

|Parameter|Description|
|--- |--- |
|1| Failure type - values listed below.|
|2| Pointer to the device. |
|3| Pointer to the worker thread.|
|4| Pointer to the callout routine. |

**Failure type**

0x1 : A device assignment to a terminal is not making progress.

0x2 : Device's close callback is not making progress.

0x3 : Device's set-input-mode callback is not making progress.

0x4 : Device's set-display-state callback is not making progress.

0x5 : Setting device's built-in panel state is not making progress.

0x6 : Updating device's primary display visible state is not making progress.

## ## Cause

The terminal topology manager detected that for the configured timeouts some device specific operations did not complete.


## ## See Also-

[Bug Check Code Reference](bug-check-code-reference2.md)

