---
title: Bug Check 0x1A5 USB_DRIPS_BLOCKER_SURPRISE_REMOVAL_LIVEDUMP
description: The USB_DRIPS_BLOCKER_SURPRISE_REMOVAL_LIVEDUMP bug check has a value of 0x000001A5. It indicates that one or more critical user mode components failed to satisfy a health check.
keywords: ["Bug Check 0x1A5 USB_DRIPS_BLOCKER_SURPRISE_REMOVAL_LIVEDUMP", "USB_DRIPS_BLOCKER_SURPRISE_REMOVAL_LIVEDUMP"]
ms.date: 01/10/2019
topic_type:
- apiref
api_name:
- USB_DRIPS_BLOCKER_SURPRISE_REMOVAL_LIVEDUMP
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x1A5: USB\_DRIPS\_BLOCKER\_SURPRISE\_REMOVAL\_LIVEDUMP

The USB\_DRIPS\_BLOCKER\_SURPRISE\_REMOVAL\_LIVEDUMP bug check has a value of 0x000001A5. It indicates that one or more critical user mode components failed to satisfy a health check.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## UUSB\_DRIPS\_BLOCKER\_SURPRISE\_REMOVAL\_LIVEDUMP Parameters

|Parameter|Description|
|--- |--- |
|1| Process that failed to satisfy a health check within the configured timeout.|
|2| Health monitoring timeout (seconds).|
|3| .|
|4| Reserved. |


## Cause
-----

One or more critical user mode components failed to satisfy a health check.


(This code can never be used for a real bugcheck; it is used to identify live dumps.)


## See Also
----------

[Bug Check Code Reference](bug-check-code-reference2.md)

