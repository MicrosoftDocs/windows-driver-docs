---
title: Bug Check 0x119 VIDEO_SCHEDULER_INTERNAL_ERROR
description: The VIDEO_SCHEDULER_INTERNAL_ERROR bug check has a value of 0x00000119. This indicates that the video scheduler has detected a fatal violation.
keywords: ["Bug Check 0x119 VIDEO_SCHEDULER_INTERNAL_ERROR", "VIDEO_SCHEDULER_INTERNAL_ERROR"]
ms.date: 05/24/2023
topic_type:
- apiref
api_name:
- VIDEO_SCHEDULER_INTERNAL_ERROR
api_type:
- NA
---

# Bug Check 0x119: VIDEO_SCHEDULER_INTERNAL_ERROR

The VIDEO_SCHEDULER_INTERNAL_ERROR bug check has a value of 0x00000119. This bug check indicates that the video scheduler has detected a fatal violation.

> [!IMPORTANT]
> This article is for programmers. If you're a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).

## VIDEO_SCHEDULER_INTERNAL_ERROR Parameters

Parameter 1 is the only parameter of interest. It identifies the exact violation.

| Parameter 1 | Cause of error    |
|-----------|--------------------------------------------------------|
|0x1| Driver has reported an invalid fence ID. (DRIVER_REPORTED_INVALID_FENCE_ID) |
|0x2| Driver failed upon the submission of a command. (DRIVER_FAILED_SUBMIT_COMMAND)|
|0x3| Driver failed upon patching the command buffer. (DRIVER_FAILED_PATCH_COMMAND) |
|0x4| Driver reported an invalid flip capability. (DRIVER_INVALID_FLIPQUEUE_LENGTH)|
|0x5| Driver failed a system or a paging command. (DRIVER_FAULTED_SYSTEM_COMMAND)|
|0x6| Driver reports NULL PhysicalAdapterMask for interrupt raised on multi-adapter GPU. (DRIVER_INVALID_ADAPTER_MASK)|
|0x7| Driver reports display VSync on render only adapter. (REPORT_VSYNC_ON_RENDER_ONLY_ADAPTER) |
|0x8| Driver reported incorrect PageFaultFlags in DMA Page Faulted interrupt. (INVALID_NODE_MASK) |
|0x9| Driver failed on a cancel command. (FAILED_CANCEL_COMMAND) |
|0xA| Driver reported and invalid out of range aborted fence. (REPORTED_INVALID_ABORTED_FENCE) |
|0xB| Driver failed the SetVidPnSourceAddressWithMultiPlaneOverlay command. (FAILED_SETVIDPNSOURCEMPO_COMMAND)|
|0xC| Driver PageFaultFlags indicate a fatal hardware fault. (FATAL_PAGE_FAULT)  |
|0xD| Driver reported incorrect PageFaultFlags in DMA Page Faulted interrupt. (INVALID_DMA_FAULT_PARAMETERS)  |
|0xE| Driver reported VSync for a plane index larger than max overlay planes on GPU. (REPORT_VSYNC_PLANE_OUT_OF_RANGE) |
|0xF| Not used. (FAILED_POSTMPOPRESENT_COMMAND) |
|0x10| Driver reported an unexpected interrupt after engine reset and before OS resumed engine. (UNEXPECTED_INTERRUPT_AFTER_RESET) |
|0x11| Driver reports a suspend context completed fence value which OS has not generated yet. (INCORRECT_SUSPEND_FENCE) |
|0x400| This is an internal OS state error, typically caused by a memory corruption or bad hardware.|
|0xE00 | The OS ran out of memory for pre-allocated packets to handle passive flip requests.|
|0x1000| This is an internal OS state error, typically caused by a memory corruption or bad hardware.|
|0xA000| This is an internal OS state error, typically caused by a memory corruption or bad hardware.|
|0x10000| This is an internal OS state error, typically caused by a memory corruption or bad hardware.|

## Resolution

The [!analyze](-analyze.md) debug extension displays information about the bug check and can be helpful in determining the root cause.

If the faulting module listed in the **!analyze** output is a video driver, see if updates are available for that video driver from the vendor.

## See also

- [Handling command and DMA buffers](../display/handling-command-and-dma-buffers.md)

- [Submitting a command buffer](../display/submitting-a-command-buffer.md)

- [Supplying fence identifiers](../display/supplying-fence-identifiers.md)

- [Video memory management and GPU scheduling](../display/video-memory-management-and-gpu-scheduling.md)

- [Direct flip of video memory](../display/direct-flip-of-video-memory.md)
