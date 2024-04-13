---
title: Bug Check 0x1A6 BLUETOOTH_ERROR_RECOVERY_LIVEDUMP
description: The BLUETOOTH_ERROR_RECOVERY_LIVEDUMP live dump has a value of 0x000001A6. It indicates that the Bluetooth radio driver has initiated error recovery to attempt to reset the radio from an irremediable condition.
keywords: ["Bug Check 0x1A6 BLUETOOTH_ERROR_RECOVERY_LIVEDUMP", "BLUETOOTH_ERROR_RECOVERY_LIVEDUMP"]
ms.date: 01/28/2019
topic_type:
- apiref
ms.topic: reference
api_name:
- BLUETOOTH_ERROR_RECOVERY_LIVEDUMP
api_type:
- NA
---

# Bug Check 0x1A6: BLUETOOTH\_ERROR\_RECOVERY\_LIVEDUMP

The BLUETOOTH\_ERROR\_RECOVERY\_LIVEDUMP live dump has a value of 0x000001A6. It indicates that the Bluetooth radio driver (bthport.sys) has initiated error recovery to attempt to recover and reset the radio from an irremediable internal condition.

## BLUETOOTH\_ERROR\_RECOVERY\_LIVEDUMP Parameters

|Parameter|Description|
|--- |--- |
|1| PDO for the Bluetooth radio (device).|
|2| Reserved.|
|3| Reserved.|
|4| Reserved.|

## Cause

The Bluetooth radio driver (bthport.sys) has initiated error recovery to attempt to recover and reset the radio from an irremediable internal condition.

(This code can never be used for a real bugcheck; it is used to identify live dumps.)


## See Also

[Kernel Live Dump Code Reference](bug-check-code-reference-live-dump.md)

[Bug Check Code Reference](bug-check-code-reference2.md)

