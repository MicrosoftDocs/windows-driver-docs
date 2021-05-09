---
title: Bug Check 0x1DB IPI_WATCHDOG_TIMEOUT
description: The IPI_WATCHDOG_TIMEOUT bug check has a value of 0x000001DB. It indicates that that a processor has been stuck in an IPI loop for more than the allowed time.
keywords: ["Bug Check 0x1DB IPI_WATCHDOG_TIMEOUT", "IPI_WATCHDOG_TIMEOUT"]
ms.date: 01/14/2019
topic_type:
- apiref
api_name:
- IPI_WATCHDOG_TIMEOUT
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x1DB: IPI\_WATCHDOG\_TIMEOUT

The IPI\_WATCHDOG\_TIMEOUT bug check has a value of 0x000001DB. It indicates that a processor has been stuck in an IPI loop for more than the allowed time.

> [!IMPORTANT]
> This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).

 

## IPI\_WATCHDOG\_TIMEOUT Parameters

|Parameter|Description|
|-------- |---------- |
|1| Indicates QPC frequency.  |
|2| Indicates the current QPC. |
|3| Indicates the baseline QPC. |
|4| Reserved. |


## ## Cause

A processor has been stuck in an IPI loop for more than the allowed time.


## ## See Also-

[Bug Check Code Reference](bug-check-code-reference2.md)

