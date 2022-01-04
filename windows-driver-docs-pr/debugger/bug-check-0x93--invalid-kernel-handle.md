---
title: Bug Check 0x93 INVALID_KERNEL_HANDLE
description: The INVALID_KERNEL_HANDLE bug check has a value of 0x00000093. This bug check indicates that an invalid or protected handle was passed to NtClose.
keywords: ["Bug Check 0x93 INVALID_KERNEL_HANDLE", "INVALID_KERNEL_HANDLE"]
ms.date: 10/10/2019
topic_type:
- apiref
api_name:
- INVALID_KERNEL_HANDLE
api_type:
- NA
---

# Bug Check 0x93: INVALID\_KERNEL\_HANDLE

The INVALID\_KERNEL\_HANDLE bug check has a value of 0x00000093. This bug check indicates that an invalid or protected handle was passed to **NtClose**.

> [!IMPORTANT]
> This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).

## INVALID\_KERNEL\_HANDLE Parameters

|Parameter 1|Parameter 2|Parameter 3|Parameter 4|Cause of Error|
|--- |--- |--- |--- |--- |
|The handle that NtClose was called with |0                |0   | 0  | A protected handle was closed.|
|The handle that NtClose was called with |1                |0   | 0  | An invalid handle was closed or referenced.|
|The handle that was referenced          |The handle table |0   | 1  | The error occurred referencing an invalid kernel handle and bad handle detection was enabled.|

## Cause

The INVALID_KERNEL_HANDLE bug check indicates that some kernel code (for example, a server, redirector, or another driver) tried to close an invalid handle or a protected handle.

If parameter 4 has a value of 1, this indicates that the error occurred referencing an invalid kernel handle and bad handle detection was enabled.

This message occurs if kernel code attempts to close or reference a handle that is not a valid handle. Only invalid or protected handles passed to NtClose will cause this bugcheck, unless bad handle detection is enabled.
