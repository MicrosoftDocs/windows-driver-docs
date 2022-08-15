---
title: Bug Check 0x1B8 VIDEO_MINIPORT_BLACK_SCREEN_LIVEDUMP
description: The VIDEO_MINIPORT_BLACK_SCREEN_LIVEDUMP live dump has a value of 0x000001B8. It indicates that a user initiated MINIPORT live dump for black screen scenarios has occurred.
keywords: ["Bug Check 0x1B8 VIDEO_MINIPORT_BLACK_SCREEN_LIVEDUMP", "VIDEO_MINIPORT_BLACK_SCREEN_LIVEDUMP"]
ms.date: 02/20/2020
topic_type:
- apiref
api_name:
- VIDEO_MINIPORT_BLACK_SCREEN_LIVEDUMP
api_type:
- NA
---

# Bug Check 0x1B8: VIDEO\_MINIPORT\_BLACK\_SCREEN\_LIVEDUMP

The VIDEO\_MINIPORT\_BLACK\_SCREEN\_LIVEDUMP live dump has a value of 0x000001B8. It indicates that a user initiated MINIPORT live dump for black screen scenarios has occurred.

> [!IMPORTANT]
> This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


## VIDEO\_MINIPORT\_BLACK\_SCREEN\_LIVEDUMP Parameters

|Parameter|Description|
|--- |--- |
|1| Source which triggered the MINIPORT black screen live dump - listed below.|
|2| Reserved. |
|3| Reserved. |
|4| Reserved. |

**Source Values**

0x1: Black screen hotkey generated MINIPORT black screen live dump

0x2: Volume combo key generated MINIPORT black screen live dump

0x4: Internal generated MINIPORT black screen live dump

0x8: Long Power Button Hold (LPBH) generated MINIPORT black screen live dump

## Cause

User initiated MINIPORT live dump for black screen scenarios. See the values for parameter 1 for the source of the triggered live dump.

(This code can never be used for a real bugcheck; it is used to identify live dumps.)

## See Also

[Bug Check Code Reference](bug-check-code-reference2.md)
