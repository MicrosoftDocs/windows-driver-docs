---
title: Bug Check 1CC EXRESOURCE_TIMEOUT_LIVEDUMP 
description: The EXRESOURCE_TIMEOUT_LIVEDUMP live dump has a value of 0x000001CC.
keywords: ["Bug Check 0x1CC EXRESOURCE_TIMEOUT_LIVEDUMP", "EXRESOURCE_TIMEOUT_LIVEDUMP"]
ms.date: 04/19/2018
topic_type:
- apiref
ms.topic: reference
api_name:
- EXRESOURCE_TIMEOUT_LIVEDUMP
api_type:
- NA
---

# Bug Check 0x1CC: EXRESOURCE\_TIMEOUT\_LIVEDUMP

The EXRESOURCE_TIMEOUT_LIVEDUMP live dump has a value of 0x000001CC.

A kernel ERESOURCE has timed out. This can indicate a deadlock condition or heavy contention which can cause performance issues.

(This code can never be used for a real bug check; it is used to identify live dumps.)

## EXRESOURCE\_TIMEOUT\_LIVEDUMP Parameters

The following parameters are displayed on the blue screen.

Parameter | Description 
|---------|--------------|
1 | The ERESOURCE that has timed out.
2 | The thread that detected the timeout
3 | The ERESOURCE contention count
4 | The configured timeout in seconds


## See Also

[Kernel Live Dump Code Reference](bug-check-code-reference-live-dump.md)

[Bug Check Code Reference](bug-check-code-reference2.md)

