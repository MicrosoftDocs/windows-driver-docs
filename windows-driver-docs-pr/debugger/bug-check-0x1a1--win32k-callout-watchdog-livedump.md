---
title: Bug Check 0x1A2 WIN32K_CALLOUT_WATCHDOG_LIVEDUMP
description: The WIN32K_CALLOUT_WATCHDOG_LIVEDUMP bug check has a value of 0x000001A2. It indicates that the terminal topology manager detected that for the configured timeouts some device specific operations did not complete.
keywords: ["Bug Check 0x1A2 WIN32K_CALLOUT_WATCHDOG_LIVEDUMP", "WIN32K_CALLOUT_WATCHDOG_LIVEDUMP"]
ms.date: 01/09/2019
topic_type:
- apiref
api_name:
- WIN32K_CALLOUT_WATCHDOG_LIVEDUMP
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x1A2: WIN32K\_CALLOUT\_WATCHDOG\_LIVEDUMP

The WIN32K\_CALLOUT\_WATCHDOG\_LIVEDUMP bug check has a value of 0x000001A2. It indicates that the terminal topology manager detected that for the configured timeouts some device specific operations did not complete.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).
 

## WIN32K\_CALLOUT\_WATCHDOG\_LIVEDUMP Parameters

|Parameter|Description|
|--- |--- |
|1| Failure type - values listed below.|
|2| Pointer to the device. |
|3| Pointer to the worker thread.|
|4| Pointer to the callout routine. |

**Failure type**


## Cause
-----

The terminal topology manager detected that for the configured timeouts some device specific operations did not complete.


## See Also
----------

[Bug Check Code Reference](bug-check-code-reference2.md)

