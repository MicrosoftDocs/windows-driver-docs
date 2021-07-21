---
title: Bug Check 0x18D SECURE_FAULT_UNHANDLED
description: The SECURE_FAULT_UNHANDLED bug check has a value of 0x0000018D. It indicates that a secure fault originated by the secure kernel could not be handled.
keywords: ["Bug Check 0x18D SECURE_FAULT_UNHANDLED", "SECURE_FAULT_UNHANDLED"]
ms.date: 01/04/2019
topic_type:
- apiref
api_name:
- SECURE_FAULT_UNHANDLED
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x18D: SECURE\_FAULT\_UNHANDLED

The SECURE\_FAULT\_UNHANDLED bug check has a value of 0x0000018D.

This bug check indidates that a secure fault originated by the secure kernel could not be handled.

> [!IMPORTANT]
> This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


 ## SECURE\_FAULT\_UNHANDLED Parameters

| Parameter | Description |
|-----------|-------------|
| 1 | Secure fault code bitmask - values below. |
| 2 | Secure fault VA (only applicable to certain secure fault types). |
| 3 | Exception Record. |
| 4 | Context Record. |


**Secure fault code bitmask**

```text
     0x1 : KSECURE_FAULT_SLAT_NX
         A no-execute fault occurred due to SLAT page protections.
     0x2 : KSECURE_FALT_SLAT_READ
         A read fault occurred due to SLAT page protections.
     0x4 : KSECURE_FAULT_SLAT_WRITE
         A write fault occurred due to SLAT page protections.
     0x8 : KSECURE_FAULT_DOUBLE_FAULT
         A secure fault occurred before the prior secure fault had been dismissed by the kernel.
```

## ## Cause

A secure fault originated by the secure kernel could not be handled.


## ## See Also-

[Bug Check Code Reference](bug-check-code-reference2.md)
