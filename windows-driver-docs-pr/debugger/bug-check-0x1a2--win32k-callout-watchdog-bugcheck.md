---
title: Bug Check 1A2 WIN32K_CALLOUT_WATCHDOG_BUGCHECK
description: The WIN32K_CALLOUT_WATCHDOG_BUGCHECK live dump has a value of 0x000001A2.
keywords: ["Bug Check 0x1A2 WIN32K_CALLOUT_WATCHDOG_BUGCHECK", "WIN32K_CALLOUT_WATCHDOG_BUGCHECK"]
ms.date: 02/12/2020
topic_type:
- apiref
ms.topic: reference
api_name:
- WIN32K_CALLOUT_WATCHDOG_BUGCHECK
api_type:
- NA
---

# Bug Check 0x1A2: WIN32K\_CALLOUT\_WATCHDOG\_BUGCHECK

> [!IMPORTANT]
> This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).

The WIN32K\_CALLOUT\_WATCHDOG\_BUGCHECK live dump has a value of 0x000001A2. It indicates that a callout to Win32k did not return promptly.

## WIN32K\_CALLOUT\_WATCHDOG\_BUGCHECK Parameters

The following parameters are displayed on the blue screen.

| Parameter |                        Description                    |
|-----------|-------------------------------------------------------|
|     1     | Thread blocking prompt return from a Win32k callout.  |
|     2     | Reserved.                                             |
|     3     | Reserved.                                             |
|     4     | Reserved.                                             |


## See also

[Bug Check Code Reference](bug-check-code-reference2.md)
