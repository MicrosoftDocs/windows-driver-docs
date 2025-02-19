---
title: Bug Check 0x1F2 KASAN_ILLEGAL_ACCESS
description: The KASAN_ILLEGAL_ACCESS bug check has a value of 0x000001F2. It indicates that that KASAN detected an illegal memory access being made.  
keywords: ["Bug Check 0x1F2 KASAN_ILLEGAL_ACCESS", "KASAN_ILLEGAL_ACCESS"]
ms.date: 02/18/2025
topic_type:
- apiref
ms.topic: reference
api_name:
- KASAN_ILLEGAL_ACCESS
api_type:
- NA
---

# Bug Check 0x1F2: KASAN\_ILLEGAL\_ACCESS

The KASAN\_ILLEGAL\_ACCESS bug check has a value of 0x000001F2. It indicates that Kernel Address Sanitizer (KASAN) detected an illegal memory access being made.

KASAN is a variation of the user-mode ASAN that has been architected to work specifically for the Windows kernel and its drivers. AddressSanitizer (ASAN) is a compiler and runtime technology that detects several classes of memory bugs in C/C++ programs, including critical security bugs like buffer overflows. 

KASAN checking is enabled using a registry key, and recompiling the kernel driver. For more information, see [Kernel Address Sanitizer (KASAN)](../devtest/kasan.md) and the Microsoft C++ [AddressSanitizer (ASAN)](/cpp/sanitizers/asan) documentation. 

> [!IMPORTANT]
> This article is for programmers. If you're a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


## KASAN\_ILLEGAL\_ACCESS Parameters

| Parameter | Description                           |
|---------- |-------------------------------------- |
| 1         | The address being accessed illegally. |
| 2         | Size of the access.                   |
| 3         | The address of the caller.            |
| 4         | Extra information on the access - memory violation location KASAN shadow code. </p> Bits `[0:7]`: The KASAN shadow code. See the table below. </p> Bit `8`: **1** if the access was a write, **0** if it was a read.|

### KASAN shadow codes

In KASAN, the kernel memory is divided in contiguous chunks of eight-byte-aligned, eight-byte cells. Each eight-byte cell in kernel memory has a shadow code associated with it, which is an one-byte integer that indicates the validity of the cell. The encoding of the shadow codes is shown here:

| Value        | Meaning                        |
|--------------|--------------------------------|
| 0x00	       | The cell is entirely valid: accesses to all eight bytes of the cell are legal. |
| 0x01 -> 0x07 | The cell is partially valid: the first value bytes in the cell are valid, but the rest are invalid. |
| >= 0x80	   | The cell is entirely invalid: accesses to all eight bytes of the cell are illegal. |

 The values of the memory access sub-codes are used for the entirely invalid cells to further indicate what type of memory the cell is associated to, and why it is invalid. For more information on the sub-codes, see [Kernel Address Sanitizer (KASAN)](../devtest/kasan.md).

## See also

- [Kernel Address Sanitizer (KASAN)](../devtest/kasan.md)
- [Bug Check Code Reference](bug-check-code-reference2.md)
