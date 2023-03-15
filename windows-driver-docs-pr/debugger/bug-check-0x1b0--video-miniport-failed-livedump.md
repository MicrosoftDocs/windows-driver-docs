---
title: Bug Check 0x1B0 VIDEO_MINIPORT_FAILED_LIVEDUMP
description: The VIDEO_MINIPORT_FAILED_LIVEDUMP live dump has a value of 0x000001B0. It indicates that the DXGKRNL detected a problem with a video miniport driver and has captured a live dump to collect debug information.
keywords: ["Bug Check 0x1B0 VIDEO_MINIPORT_FAILED_LIVEDUMP", "VIDEO_MINIPORT_FAILED_LIVEDUMP"]
ms.date: 01/08/2018
topic_type:
- apiref
ms.topic: reference
api_name:
- VIDEO_MINIPORT_FAILED_LIVEDUMP
api_type:
- NA
---

# Bug Check 0x1B0: VIDEO\_MINIPORT\_FAILED\_LIVEDUMP

The VIDEO\_MINIPORT\_FAILED\_LIVEDUMP live dump has a value of 0x000001B0.

## VIDEO\_MINIPORT\_FAILED\_LIVEDUMP Parameters

|Parameter|Description|
|--- |--- |
|1| Reason Code. VALUES: 0x1 : *Add device failed.* 0x2 : *Start device failed.*|
|2| NTSTATUS|
|3| Reserved. |
|4| Reserved. |


## Cause
The DXGKRNL detected a problem and has captured a live dump to collect debug information. These livedumps are triggered by dxgkrnl when a video miniport driver failed.

(This code can never be used for a real bugcheck; it is used to identify live dumps.)


## See Also

[Kernel Live Dump Code Reference](bug-check-code-reference-live-dump.md)

[Bug Check Code Reference](bug-check-code-reference2.md)

 


 




