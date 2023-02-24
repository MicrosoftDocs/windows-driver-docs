---
title: Bug check 0x13A KERNEL_MODE_HEAP_CORRUPTION
description: Learn how the KERNEL_MODE_HEAP_CORRUPTION bug check indicates that the kernel mode heap manager has detected corruption in a heap.
keywords: ["Bug Check 0x13A KERNEL_MODE_HEAP_CORRUPTION", "KERNEL_MODE_HEAP_CORRUPTION"]
ms.date: 02/23/2023
topic_type:
- apiref
api_name:
- KERNEL_MODE_HEAP_CORRUPTION
api_type:
- NA
---

# Bug check 0x13A: KERNEL_MODE_HEAP_CORRUPTION

The KERNEL_MODE_HEAP_CORRUPTION bug check has a value of 0x0000013A. This bug check indicates that the kernel mode heap manager has detected corruption in a heap.

> [!IMPORTANT]
> This article is for programmers. If you're a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).

## KERNEL_MODE_HEAP_CORRUPTION parameters

| Parameter | Description                                      |
|-----------|--------------------------------------------------|
| 1         | Type of corruption detected - see the following list |
| 2         | Address of the heap that reported the corruption |
| 3         | Address at which the corruption was detected     |
| 4         | Reserved                                         |

### Parameter 1 - Type of heap corruption

0x3 : A corrupt entry header was detected.

0x4 : Multiple corrupt entry headers were detected.

0x5 : A corrupt entry header in a large allocation was detected.

0x6 : A corruption was detected with features consistent with a buffer overrun.

0x7 : A corruption was detected with features consistent with a buffer underrun.

0x8 : A free block was passed to an operation that's only valid for busy blocks.

0x9 : An invalid argument was specified for the current operation.

0xA : An invalid allocation type was detected.

0xB : A corruption was detected with features consistent with a use-after-free error.

0xC : The wrong heap was specified for the current operation.

0xD : A corrupt free list was detected.

0xE : The heap detected list corruption in a list other than the free list.

0xF : A free block was passed to an operation that's only valid for busy blocks.

0x10 : The heap detected invalid internal state during the current operation. This is usually the result of a buffer overflow.

0x11 : The heap detected invalid internal state during the current operation. This is usually the result of a buffer overflow.

0x12 : The heap detected invalid internal state during the current operation. This is usually the result of a buffer overflow.

0x13 : The heap API was passed a NULL heap handle. Look at the call stack to determine why a bad handle was supplied to the heap.

0x14 : The requested heap allocation is larger then the current allocation limit.

0x15 : In the process of performing a commit request, it was determined that the request would exceed the current commit limit.

0x16 : In the process of checking the size of the given VA Manager allocation, it was determined that the query was invalid.

## Resolution

The [!analyze](-analyze.md) debug extension displays information about the bug check and can be helpful in determining the root cause.

The [!heap](-heap.md) extension displays heap usage information, controls breakpoints in the heap manager, detects leaked heap blocks, searches for heap blocks, or displays page heap information.

For general information on troubleshooting blue screen bug checks, see [Blue screen data](blue-screen-data.md).

## See also

[Bug check code reference](bug-check-code-reference2.md)

[General tips for blue screens](general-troubleshooting-tips.md)
