---
title: Bug check 0x119 VIDEO_SCHEDULER_INTERNAL_ERROR
description: Learn how the VIDEO_SCHEDULER_INTERNAL_ERROR bug check indicates that the video scheduler has detected a fatal violation.
keywords: ["Bug Check 0x119 VIDEO_SCHEDULER_INTERNAL_ERROR", "VIDEO_SCHEDULER_INTERNAL_ERROR"]
ms.date: 02/22/2023
topic_type:
- apiref
ms.topic: reference
api_name:
- VIDEO_SCHEDULER_INTERNAL_ERROR
api_type:
- NA
---

# Bug check 0x119: VIDEO_SCHEDULER_INTERNAL_ERROR

The VIDEO_SCHEDULER_INTERNAL_ERROR bug check has a value of 0x00000119. This bug check indicates that the video scheduler has detected a fatal violation.

> [!IMPORTANT]
> This article is for programmers. If you're a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).

## Parameters

Parameter 1 is the only parameter of interest. It identifies the exact violation.

| Parameter 1 | Cause of error                                       |
|-----------|--------------------------------------------------------|
|0x1| The driver has reported an invalid fence ID. |
|0x2| The driver failed upon the submission of a command. |
|0x3| The driver failed upon patching the command buffer. |
|0x4| The driver reported an invalid flip capability. |
|0x5| The driver failed a system or paging command. |
|0x400| An internal OS state error, typically caused by a memory corruption or bad hardware. |
|0xE00| The OS ran out of memory for pre-allocated packets to handle passive flip requests. |
|0x1000| An internal OS state error, typically caused by a memory corruption or bad hardware. |
|0x10000| An internal OS state error, typically caused by a memory corruption or bad hardware. |

## Resolution

The [!analyze](-analyze.md) debug extension displays information about the bug check and can be helpful in determining the root cause.

If the faulting module listed in the **!analyze** output is a video driver, see if updates are available for that video driver from the vendor.

## See also

- [Handling command and DMA buffers](../display/handling-command-and-dma-buffers.md)

- [Submitting a command buffer](../display/submitting-a-command-buffer.md)

- [Supplying fence identifiers](../display/supplying-fence-identifiers.md)

- [Video memory management and GPU scheduling](../display/video-memory-management-and-gpu-scheduling.md)

- [Direct flip of video memory](../display/direct-flip-of-video-memory.md)
