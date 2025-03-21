---
title: Bug Check 0x1F1 KASAN_ENLIGHTENMENT_VIOLATION
description: The KASAN_ENLIGHTENMENT_VIOLATION bug check has a value of 0x000001F1. It indicates that that KASAN enlightenment encoutered a violation when attempting to interact with memory shadow.  
keywords: ["Bug Check 0x1F1 KASAN_ENLIGHTENMENT_VIOLATION", "KASAN_ENLIGHTENMENT_VIOLATION"]
ms.date: 02/18/2025
topic_type:
- apiref
ms.topic: reference
api_name:
- KASAN_ENLIGHTENMENT_VIOLATION
api_type:
- NA
---

# Bug Check 0x1F1: KASAN\_ENLIGHTENMENT\_VIOLATION 

The KASAN\_ENLIGHTENMENT\_VIOLATION bug check has a value of 0x000001F1. It indicates that KASAN enlightenment encoutered a violation when attempting to interact with memory shadow. This bug check is used to check internal operation of KASAN in Windows. For more information, see [Kernel Address Sanitizer (KASAN)](../devtest/kasan.md) and the Microsoft C++ [AddressSanitizer (ASAN)](/cpp/sanitizers/asan) documentation.  

> [!IMPORTANT]
> This article is for programmers. If you're a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


## KASAN\_ENLIGHTENMENT\_VIOLATION Parameters

| Parameter |Description                          |
|---------- |------------------------------------ |
| 1         | Type of KASAN shadow interaction.   |
| 2         | Type of violation.                  | 
| 3         | Extra information on the violation. |
| 4         | Extra information on the violation. |

## See also

- [Kernel Address Sanitizer (KASAN)](../devtest/kasan.md)
- [Bug Check Code Reference](bug-check-code-reference2.md)

