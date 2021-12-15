---
title: Bug Check 1DA HAL_BLOCKED_PROCESSOR_INTERNAL_ERROR
description: The HAL_BLOCKED_PROCESSOR_INTERNAL_ERROR has a value of 0x000001DA.
keywords: ["Bug Check 0x1DA HAL_BLOCKED_PROCESSOR_INTERNAL_ERROR", "HAL_BLOCKED_PROCESSOR_INTERNAL_ERROR"]
ms.date: 02/20/2020
topic_type:
- apiref
api_name:
- HAL_BLOCKED_PROCESSOR_INTERNAL_ERROR
api_type:
- NA
---

# Bug Check 0x1DA: HAL\_BLOCKED\_PROCESSOR\_INTERNAL\_ERROR

> [!IMPORTANT]
> This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).

The HAL\_BLOCKED\_PROCESSOR\_INTERNAL\_ERROR has a value of 0x000001DA. It indicates that an internal error was detected in the blocked processor library.

## HAL\_BLOCKED\_PROCESSOR\_INTERNAL\_ERROR Parameters

The following parameters are displayed on the blue screen.

| Parameter |                        Description              |
|-----------|-------------------------------------------------|
|     1     | Type of failure - See below                     |
|     2     | See below.                                      |
|     3     | See below.                                      |
|     4     | See below.                                      |

## Parameter One Values

```plaintext
            0x01 : Library initialization failure
                2 - NT status code
            0x02 : Processor start failure
                2 - Processor index
                3 - APIC ID
            0x03 : PPM package ID query failure
                2 - Processor index
            0x04 : PPM operation failure
                2 - Operation
                    0x01 : MSR read
                    0x02 : MSR write
                    0x03 : I/O port read
                    0x04 : I/O port write
                    0x05 : Idle state registration
                3 - Processor index
                4 - PPM mailbox
            0x05 : A blocked processor has encountered a fatal exception.
                2 - Processor index
                3 - Vector number
                4 - Trap frame
            0x06 : PPM operation timeout
                2 - Operation
                    0x01 : MSR read
                    0x02 : MSR write
                    0x03 : I/O port read
                    0x04 : I/O port write
                    0x05 : Idle state registration
                3 - Processor index
                4 - PPM mailbox
```
