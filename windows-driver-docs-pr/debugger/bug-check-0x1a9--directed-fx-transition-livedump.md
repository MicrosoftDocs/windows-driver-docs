---
title: Bug Check 0x1A9 DIRECTED_FX_TRANSITION_LIVEDUMP 
description: The DIRECTED_FX_TRANSITION_LIVEDUMP live dump has a value of 0x000001A9. It indicates that a  device has failed its Directed Fx transition call.
keywords: ["Bug Check 0x1A9 DIRECTED_FX_TRANSITION_LIVEDUMP ", "DIRECTED_FX_TRANSITION_LIVEDUMP "]
ms.date: 03/09/2022
topic_type:
- apiref
api_name:
- DIRECTED_FX_TRANSITION_LIVEDUMP 
api_type:
- NA
---

# Bug Check 0x1A9: DIRECTED\_FX\_TRANSITION\_LIVEDUMP

The DIRECTED\_FX\_TRANSITION\_LIVEDUMP live dump has a value of 0x000001A9. It indicates that a device has failed its Directed Fx transition call. For more information about Directed Fx, see [Introduction to the Directed Power Management Framework](../kernel/introduction-to-the-directed-power-management-framework.md).

(This code can never be used for a real bugcheck; it is used to identify live dumps.)

## DIRECTED\_FX\_TRANSITION\_LIVEDUMP Parameters

| Parameter | Description                                                                 |
|-----------|-----------------------------------------------------------------------------|
| 1         | A pointer to the POP_FX_DEVICE object instance.                             |
| 2         | 1 if this transition was a power down, 0 if this transition was a power up. |
| 3         | Reserved.                                                                   |
| 4         | Reserved.                                                                   |

## Cause

A device has failed its Directed Fx transition call.

## See Also

[Kernel Live Dump Code Reference](bug-check-code-reference-live-dump.md)

[Bug Check Code Reference](bug-check-code-reference2.md)