---
title: Bug Check 0x1DA HAL_BLOCKED_PROCESSOR_INTERNAL_ERROR
description: The HAL_BLOCKED_PROCESSOR_INTERNAL_ERROR bug check has a value of 0x000001DA. It indicates that that an internal error was detected in the blocked processor library.  
keywords: ["Bug Check 0x1DA HAL_BLOCKED_PROCESSOR_INTERNAL_ERROR", "HAL_BLOCKED_PROCESSOR_INTERNAL_ERROR"]
ms.date: 01/14/2019
topic_type:
- apiref
api_name:
- HAL_BLOCKED_PROCESSOR_INTERNAL_ERROR
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x1DA: HAL\_BLOCKED\_PROCESSOR\_INTERNAL\_ERROR

The HAL\_BLOCKED\_PROCESSOR\_INTERNAL\_ERROR bug check has a value of 0x000001DA. It indicates that an internal error was detected in the blocked processor library.  

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).
 

## HAL\_BLOCKED\_PROCESSOR\_INTERNAL\_ERROR Parameters

|Parameter|Description|
|-------- |---------- |
|1| Indicates the type of failure. See values below.|
|2| See values below. |
|3| See values below. |
|4| See values below. |

**Type of Failure**

```
0x01 : Library initialization failure
    2 - NT status code

0x02 : Processor start failure
    2 - Processor index
    3 - APIC ID

0x03 : PPM package ID query failure
    2 - Processor index

0x04 : PPM operation failure
    2 - Operation
    VALUES:
        0x01 : MSR read
        0x02 : MSR write
        0x03 : I/O port read
        0x04 : I/O port write
        0x05 : Idle state regisration
    END_VALUES
    3 - Processor index
    4 - PPM mailbox

0x05 : A blocked processor has encountered a fatal exception.
    2 - Processor index
    3 - Vector number
    4 - Trap frame

0x06 : PPM operation timeout
    2 - Operation
    VALUES:
        0x01 : MSR read
        0x02 : MSR write
        0x03 : I/O port read
        0x04 : I/O port write
        0x05 : Idle state regisration
    END_VALUES
    3 - Processor index
    4 - PPM mailbox
```

## Cause
-----

An internal error was detected in the blocked processor library.


## See Also
----------

[Bug Check Code Reference](bug-check-code-reference2.md)

