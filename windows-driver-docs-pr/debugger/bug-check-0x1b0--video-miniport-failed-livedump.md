---
title: Bug Check 0x1B0 VIDEO_MINIPORT_FAILED_LIVEDUMP
description: The VIDEO_MINIPORT_FAILED_LIVEDUMP bug check has a value of 0x0000001B. It indicates that a memory management page frame number (PFN) database element has a corrupted share count. This bug check appears very infrequently.
keywords: ["Bug Check 0x1B0 VIDEO_MINIPORT_FAILED_LIVEDUMP", "VIDEO_MINIPORT_FAILED_LIVEDUMP"]
ms.date: 01/08/2018
topic_type:
- apiref
api_name:
- VIDEO_MINIPORT_FAILED_LIVEDUMP
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x1B0: VIDEO\_MINIPORT\_FAILED\_LIVEDUMP

The VIDEO\_MINIPORT\_FAILED\_LIVEDUMP bug check has a value of 0x000001B0.


**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## VIDEO\_MINIPORT\_FAILED\_LIVEDUMP Parameters

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

 
The DXGKRNL detected a problem and has captured a live dump to collect debug information.

PARAMETERS
    1 - Reason Code
      VALUES:
          0x1 : Add device failed
          0x2 : Start device failed
      END_VALUES

    2 - NTSTATUS
    3 - Reserved
    4 - Reserved

DESCRIPTION
Livedumps triggered by dxgkrnl when a miniport driver failed

 




