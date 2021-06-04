---
title: Bug Check 0x1A5 USB_DRIPS_BLOCKER_SURPRISE_REMOVAL_LIVEDUMP
description: The USB_DRIPS_BLOCKER_SURPRISE_REMOVAL_LIVEDUMP bug check has a value of 0x000001A5. It indicates that a USB device will be surprise removed because it is blocking DRIPS.
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

The USB\_DRIPS\_BLOCKER\_SURPRISE\_REMOVAL\_LIVEDUMP bug check has a value of 0x000001A5. It indicates that a USB device will be surprise removed because it is blocking DRIPS.

> [!IMPORTANT]
> This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


## USB\_DRIPS\_BLOCKER\_SURPRISE\_REMOVAL\_LIVEDUMP Parameters

|Parameter|Description|
|--- |--- |
|1| PDO for the blocking device.|
|2| Reserved. |
|3| Reserved. |
|4| Reserved. |

## ## Cause

A USB device is blocking the top level controller from powering down during modern standby and will be surprise removed as a result.

(This code can never be used for a real bugcheck; it is used to identify live dumps.)


## ## See Also-

[Bug Check Code Reference](bug-check-code-reference2.md)

