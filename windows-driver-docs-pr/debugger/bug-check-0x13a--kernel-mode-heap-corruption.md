---
title: Bug Check 0x13A KERNEL_MODE_HEAP_CORRUPTION
description: Learn how the KERNEL_MODE_HEAP_CORRUPTION bug check indicates that the kernel mode heap manager has detected corruption in a heap.
keywords: ["Bug Check 0x13A KERNEL_MODE_HEAP_CORRUPTION", "KERNEL_MODE_HEAP_CORRUPTION"]
ms.date: 05/27/2025
topic_type:
- apiref
ms.topic: reference
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

| Parameter | Description                                           |
|-----------|-------------------------------------------------------|
| 1         | Type of corruption detected - see the following list. |
| 2         | Address of the heap that reported the corruption.     |
| 3         | Address at which the corruption was detected.         |
| 4         | Reserved                                              |

### Parameter 1 - Type of heap corruption

0x3: A corrupt entry header was detected.

0x4: Multiple corrupt entry headers were detected.

0x5: A corrupt entry header in a large allocation was detected.

0x6: A corruption was detected with features consistent with a buffer overrun.

0x7: A corruption was detected with features consistent with a buffer underrun.

0x8: A free block was passed to an operation that is only valid for busy blocks.

0x9: An invalid argument was specified for the current operation.

0xA: An internal heap error occurred related to the allocation type.

0xB: The heap detected an error whose features are consistent with using a block after freeing it.

0xC: The wrong heap was specified for the current operation.

0xD: The heap detected a corrupt free list. This can be the result of a use-after-free error or a buffer overflow of an adjacent block.

0xE: The heap detected list corruption in a list other than the free list.

0xF: The caller performed an operation (such as a free or a size check) that is illegal on a free block.

0x10: The heap detected invalid internal state during the current operation. This can be the result of a buffer overflow.

0x11: The heap detected invalid internal state during the current operation. This can be the result of a double-free or heap corruption.

0x12: The heap detected invalid internal state during the current operation. This can be the result of a use-after-free error or a buffer overflow of an adjacent block.

0x13: The heap API was passed a NULL heap handle. Look at the call stack and to determine why a bad handle was supplied to the heap.

0x14: The requested heap allocation is larger than the current allocation limit.

0x15: In the process of performing a commit request, it was determined that the request would exceed the current commit limit.

0x16: Indicates an internal heap error. This can be the result of a bad address or memory corruption.

0x17: The heap detected that a block was corrupted in a delay free list. This is likely a use-after-free error or a buffer overflow of an adjacent block.

## Resolution

The [!analyze](../debuggercmds/-analyze.md) debug extension displays information about the bug check and can be helpful in determining the root cause.

The [!heap](../debuggercmds/-heap.md) extension displays heap usage information, controls breakpoints in the heap manager, detects leaked heap blocks, searches for heap blocks, or displays page heap information.

For general information on troubleshooting blue screen bug checks, see [Analyze Bug Check Blue Screen Data](blue-screen-data.md).

## See also

[Bug check code reference](bug-check-code-reference2.md)

[Bug Checks (Blue Screens)](bug-checks--blue-screens-.md)
