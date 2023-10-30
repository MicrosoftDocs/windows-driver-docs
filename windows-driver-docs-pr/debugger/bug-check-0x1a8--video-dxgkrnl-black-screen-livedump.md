---
title: Bug Check 0x1A8 VIDEO_DXGKRNL_BLACK_SCREEN_LIVEDUMP
description: The VIDEO_DXGKRNL_BLACK_SCREEN_LIVEDUMP live dump has a value of 0x000001A8. It indicates that a user initiated DXGKRNL live dump for black screen scenarios has occurred.
keywords: ["Bug Check 0x1A8 VIDEO_DXGKRNL_BLACK_SCREEN_LIVEDUMP", "VIDEO_DXGKRNL_BLACK_SCREEN_LIVEDUMP"]
ms.date: 01/28/2018
topic_type:
- apiref
ms.topic: reference
api_name:
- VIDEO_DXGKRNL_BLACK_SCREEN_LIVEDUMP
api_type:
- NA
---

# Bug Check 0x1A8: VIDEO\_DXGKRNL\_BLACK\_SCREEN\_LIVEDUMP

The VIDEO\_DXGKRNL\_BLACK\_SCREEN\_LIVEDUMP live dump has a value of 0x000001A8. It indicates that a user initiated DXGKRNL live dump for black screen scenarios has occurred.

## VIDEO\_DXGKRNL\_BLACK\_SCREEN\_LIVEDUMP Parameters

|Parameter|Description|
|--- |--- |
|1| Source which triggered the DXGKRNL black screen live dump - listed below.|
|2| Reserved. |
|3| Reserved. |
|4| Reserved. |

**Source Values**


0x1: Black screen hotkey generated DXGKRNL black screen live dump

0x2: Volume combo key generated DXGKRNL black screen live dump

0x4: Internal generated DXGKRNL black screen live dump

0x8: Long Power Button Hold (LPBH) generated DXGKRNL black screen live dump

## Cause

User initiated DXGKRNL live dump for black screen scenarios. See the values for parameter 1 for the source of the triggered live dump. 

(This code can never be used for a real bugcheck; it is used to identify live dumps.)

## See Also

[Kernel Live Dump Code Reference](bug-check-code-reference-live-dump.md)

[Bug Check Code Reference](bug-check-code-reference2.md)
