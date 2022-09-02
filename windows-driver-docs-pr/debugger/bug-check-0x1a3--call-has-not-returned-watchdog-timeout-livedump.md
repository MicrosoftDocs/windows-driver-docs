---
title: Bug Check 1A3 CALL_HAS_NOT_RETURNED_WATCHDOG_TIMEOUT_LIVEDUMP
description: The CALL_HAS_NOT_RETURNED_WATCHDOG_TIMEOUT_LIVEDUMP live dump has a value of 0x000001A3.
keywords: ["Bug Check 0x1A3 CALL_HAS_NOT_RETURNED_WATCHDOG_TIMEOUT_LIVEDUMP", "CALL_HAS_NOT_RETURNED_WATCHDOG_TIMEOUT_LIVEDUMP"]
ms.date: 05/25/2018
topic_type:
- apiref
api_name:
- CALL_HAS_NOT_RETURNED_WATCHDOG_TIMEOUT_LIVEDUMP
api_type:
- NA
---

# Bug Check 0x1A3: CALL\_HAS\_NOT\_RETURNED\_WATCHDOG\_TIMEOUT\_LIVEDUMP 

A call has not returned within the timeout period.

The CALL_HAS_NOT_RETURNED_WATCHDOG_TIMEOUT_LIVEDUMP live dump has a value of 0x000001A3. 

(This code can never be used for a real bugcheck; it is used to identify live dumps.)

## CALL\_HAS\_NOT\_RETURNED\_WATCHDOG\_TIMEOUT\_LIVEDUMP Parameters

The following parameters are displayed on the blue screen.


| Parameter |                        Description                        |
|-----------|-----------------------------------------------------------|
|     1     | Process of a thread whose call has not returned promptly. |
|     2     |       Thread whose call has not returned promptly.        |
|     3     |                 Timeout in milliseconds.                  |
|     4     |    dt nt!_PO_CALL_HAS_NOT_RETURNED_WATCHDOG <address>     |

