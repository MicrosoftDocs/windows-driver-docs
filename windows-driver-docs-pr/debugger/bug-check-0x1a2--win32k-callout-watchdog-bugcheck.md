---
title: Bug Check 0x1A2 WIN32K_CALLOUT_WATCHDOG_BUGCHECK
description: The WIN32K_CALLOUT_WATCHDOG_BUGCHECK bug check has a value of 0x000001A2. It indicates that a callout to Win32k did not return promptly.
keywords: ["Bug Check 0x1A2 WIN32K_CALLOUT_WATCHDOG_BUGCHECK", "WIN32K_CALLOUT_WATCHDOG_BUGCHECK"]
ms.date: 01/10/2019
topic_type:
- apiref
api_name:
- WIN32K_CALLOUT_WATCHDOG_BUGCHECK
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x1A2: WIN32K\_CALLOUT\_WATCHDOG\_BUGCHECK

The WIN32K\_CALLOUT\_WATCHDOG\_BUGCHECK has a value of 0x000001A2.  It indicates that a callout to Win32k did not return promptly.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).
 

## WIN32K\_CALLOUT\_WATCHDOG\_BUGCHECK Parameters

|Parameter|Description|
|--- |--- |
|1| Thread blocking prompt return from a Win32k callout.|
|2| Reserved.|
|3| Reserved.|
|4| Reserved. |


## Cause
-----

A callout to Win32k did not return promptly.


## See Also
----------

[Bug Check Code Reference](bug-check-code-reference2.md)

