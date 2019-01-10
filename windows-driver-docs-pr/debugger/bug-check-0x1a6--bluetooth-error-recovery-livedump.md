---
title: Bug Check 0x1A6 BLUETOOTH_ERROR_RECOVERY_LIVEDUMP
description: The BLUETOOTH_ERROR_RECOVERY_LIVEDUMP bug check has a value of 0x000001A6. It indicates that a  Bluetooth radio (device) has attempted an error recovery.

keywords: ["Bug Check 0x1A6 BLUETOOTH_ERROR_RECOVERY_LIVEDUMP", "BLUETOOTH_ERROR_RECOVERY_LIVEDUMP"]
ms.date: 01/10/2019
topic_type:
- apiref
api_name:
- BLUETOOTH_ERROR_RECOVERY_LIVEDUMP
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x1A6: BLUETOOTH\_ERROR\_RECOVERY\_LIVEDUMP

The BLUETOOTH\_ERROR\_RECOVERY\_LIVEDUMP bug check has a value of 0x000001A6. It indicates that a Bluetooth radio (device) has attempted an error recovery.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).
 

## BLUETOOTH\_ERROR\_RECOVERY\_LIVEDUMP Parameters

|Parameter|Description|
|--- |--- |
|1| PDO for the Bluetooth radio (device).|
|2| Reserved.|
|3| Reserved.|
|4| Reserved.|

## Cause
-----

A Bluetooth device has attempted an error recovery operation as a result of an irremediable internal condition.

(This code can never be used for a real bugcheck; it is used to identify live dumps.)


## See Also
----------

[Bug Check Code Reference](bug-check-code-reference2.md)

