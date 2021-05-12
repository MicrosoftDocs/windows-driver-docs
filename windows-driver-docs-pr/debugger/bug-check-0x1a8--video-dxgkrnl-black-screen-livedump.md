---
title: Bug Check 0x1A8 VIDEO_DXGKRNL_BLACK_SCREEN_LIVEDUMP
description: The VIDEO_DXGKRNL_BLACK_SCREEN_LIVEDUMP bug check has a value of 0x000001A8. It indicates that a user initiated DXGKRNL live dump for black screen scenarios has occurred.
keywords: ["Bug Check 0x1A8 VIDEO_DXGKRNL_BLACK_SCREEN_LIVEDUMP", "VIDEO_DXGKRNL_BLACK_SCREEN_LIVEDUMP"]
ms.date: 01/28/2018
topic_type:
- apiref
api_name:
- VIDEO_DXGKRNL_BLACK_SCREEN_LIVEDUMP
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x1A8: VIDEO\_DXGKRNL\_BLACK\_SCREEN\_LIVEDUMP

The VIDEO\_DXGKRNL\_BLACK\_SCREEN\_LIVEDUMP bug check has a value of 0x000001A8. It indicates that a user initiated DXGKRNL live dump for black screen scenarios has occurred.

> [!IMPORTANT]
> This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


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

## ## Cause

User initiated DXGKRNL live dump for black screen scenarios. See the values for parameter 1 for the source of the triggered live dump. 

(This code can never be used for a real bugcheck; it is used to identify live dumps.)

## ## See Also-

[Bug Check Code Reference](bug-check-code-reference2.md)
