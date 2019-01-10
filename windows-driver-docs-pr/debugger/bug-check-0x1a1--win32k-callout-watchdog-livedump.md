---
title: Bug Check 0x1A1 WIN32K_CALLOUT_WATCHDOG_LIVEDUMP
description: The WIN32K_CALLOUT_WATCHDOG_LIVEDUMP bug check has a value of 0x000001A1. It indicates that a callout to Win32k did not return promptly.
keywords: ["Bug Check 0x1A1 WIN32K_CALLOUT_WATCHDOG_LIVEDUMP", "WIN32K_CALLOUT_WATCHDOG_LIVEDUMP"]
ms.date: 01/10/2019
topic_type:
- apiref
api_name:
- WIN32K_CALLOUT_WATCHDOG_LIVEDUMP
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x1A1: WIN32K\_CALLOUT\_WATCHDOG\_LIVEDUMP

The WIN32K\_CALLOUT\_WATCHDOG\_LIVEDUMP bug check has a value of 0x000001A1. It indicates that a callout to Win32k did not return promptly.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).
 

## WIN32K\_CALLOUT\_WATCHDOG\_LIVEDUMP Parameters

|Parameter|Description|
|--- |--- |
|1| Thread blocking prompt return from a Win32k callout.|
|2| Reserved.|
|3| Reserved.|
|4| Reserved. |

## Cause
-----

A callout to Win32k did not return promptly.

(This code can never be used for a real bugcheck; it is used to identify live dumps.)


## See Also
----------

[Bug Check Code Reference](bug-check-code-reference2.md)

