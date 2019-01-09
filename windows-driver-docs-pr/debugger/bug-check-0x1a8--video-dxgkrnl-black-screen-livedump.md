---
title: Bug Check 0x1A8 VIDEO_DXGKRNL_BLACK_SCREEN_LIVEDUMP
description: The VIDEO_DXGKRNL_BLACK_SCREEN_LIVEDUMP bug check has a value of 0x0000001B. It indicates that a memory management page frame number (PFN) database element has a corrupted share count. This bug check appears very infrequently.
ms.assetid: 7af4f639-2412-4312-84a7-66354d300ec6
keywords: ["Bug Check 0x1A8 VIDEO_DXGKRNL_BLACK_SCREEN_LIVEDUMP", "VIDEO_DXGKRNL_BLACK_SCREEN_LIVEDUMP"]
ms.date: 01/08/2018
topic_type:
- apiref
api_name:
- VIDEO_DXGKRNL_BLACK_SCREEN_LIVEDUMP
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x1A8: VIDEO\_DXGKRNL\_BLACK\_SCREEN\_LIVEDUMP

The VIDEO\_DXGKRNL\_BLACK\_SCREEN\_LIVEDUMP bug check has a value of 0x0000001B.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).


## VIDEO\_DXGKRNL\_BLACK\_SCREEN\_LIVEDUMP Parameters

|Parameter|Description|
|--- |--- |
|1| .|
|2| Reserved.|
|3| Reserved. |
|4| Reserved. |

## Cause
-----



## See Also
----------

[Bug Check Code Reference](bug-check-code-reference2.md)


User initiated DXGKRNL black screen live dump.

PARAMETERS
    1 - Source which triggered the DXGKRNL black screen live dump.
    VALUES:
        0x1: Blackscreen hotkey generated DXGKRNL black screen live dump
        0x2: Volume combo key generated DXGKRNL black screen live dump
        0x4: Internal generated DXGKRNL black screen live dump
        0x8: LPBH generated DXGKRNL black screen live dump
    END_VALUES
    2 - Reserved.
    3 - Reserved.
    4 - Reserved.

DESCRIPTION
User initiated DXGKRNL live dump for black screen scenarios.
(This code can never be used for a real bugcheck; it is used to identify live dumps.)



 




