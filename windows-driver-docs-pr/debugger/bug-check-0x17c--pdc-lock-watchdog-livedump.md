---
title: Bug Check 17C PDC_LOCK_WATCHDOG_LIVEDUMP
description: The PDC_LOCK_WATCHDOG_LIVEDUMP live dump has a value of 0x0000017C. This indicates that a thread has been holding the PDC lock for too long.
keywords: ["Bug Check 17C PDC_LOCK_WATCHDOG_LIVEDUMP", "PDC_LOCK_WATCHDOG_LIVEDUMP"]
ms.date: 01/04/2019
topic_type:
- apiref
ms.topic: reference
api_name:
- PDC_LOCK_WATCHDOG_LIVEDUMP
api_type:
- NA
---

# Bug Check 17C: PDC\_LOCK\_WATCHDOG\_LIVEDUMP

The PDC\_LOCK\_WATCHDOG\_LIVEDUMP live dump has a value of 0x0000017C. This indicates that a thread has been holding the PDC lock for too long.

 ## PDC\_LOCK\_WATCHDOG\_LIVEDUMP Parameters

|Parameter|Description|
|--- |--- |
|1| The thread holding the PDC lock.|
|2| Lock watchdog timeout in milliseconds. |
|3| Reserved. |
|4| Reserved. |


## Cause
A thread has been holding the PDC lock for too long. A livedump is created to provide information to investigate. 

(This code can never be used for a real bug check; it is used to identify live dumps.)

## Resolution
-----

Use the debugger [!thread](-thread.md) command to display the thread holding the lock that is provided in parameter 1.  Analyze that code to determine why it is holding the lock beyond the timeout period.


## See Also

[\!thread](-thread.md)

[Kernel Live Dump Code Reference](bug-check-code-reference-live-dump.md)

[Bug Check Code Reference](bug-check-code-reference2.md)


 




