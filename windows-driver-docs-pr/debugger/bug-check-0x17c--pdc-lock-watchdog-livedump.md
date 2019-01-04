---
title: Bug Check 0x1B PDC_LOCK_WATCHDOG_LIVEDUMP
description: The PDC_LOCK_WATCHDOG_LIVEDUMP bug check has a value of 0x0000001B. It indicates that a memory management page frame number (PFN) database element has a corrupted share count. This bug check appears very infrequently.
keywords: ["Bug Check 0x1B PDC_LOCK_WATCHDOG_LIVEDUMP", "PDC_LOCK_WATCHDOG_LIVEDUMP"]
ms.date: 01/04/2019
topic_type:
- apiref
api_name:
- PDC_LOCK_WATCHDOG_LIVEDUMP
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x1B: PDC\_LOCK\_WATCHDOG\_LIVEDUMP


The PDC\_LOCK\_WATCHDOG\_LIVEDUMP bug check has a value of 0x0000001B. This indicates that a thread has been holding the PDC lock for too long.

                   (0x17C)


PARAMETERS
    1 - The thread holding the PDC lock.
    2 - Lock watchdog timeout in milliseconds.
    3 - Reserved.
    4 - Reserved.

DESCRIPTION
(This code can never be used for a real bugcheck.)
**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

 ## COREMSGCALL\_INTERNAL\_ERROR Parameters

|Parameter|Description|
|--- |--- |
|1| .|
|2| . |
|3| Reserved |
|4| Reserved |

## Cause
-----



## See Also
----------

[Bug Check Code Reference](bug-check-code-reference2.md)

 




