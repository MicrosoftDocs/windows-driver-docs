---
title: Video Memory Management and GPU Scheduling
description: Video Memory Management and GPU Scheduling
keywords:
- display driver model WDK Windows Vista , video memory management
- Windows Vista display driver model WDK , video memory management
- video memory management WDK display
- GPU scheduling WDK display
- display driver model WDK Windows Vista , GPU scheduling
- Windows Vista display driver model WDK , GPU scheduling
- user-mode display drivers WDK Windows Vista , video memory management
- miniport drivers WDK display , video memory management
- user-mode display drivers WDK Windows Vista , GPU scheduling
- miniport drivers WDK display , GPU scheduling
ms.date: 01/23/2019
ms.localizationpriority: medium
---

# Video Memory Management and GPU Scheduling


## <span id="ddk_video_memory_management_and_gpu_scheduling_gg"></span><span id="DDK_VIDEO_MEMORY_MANAGEMENT_AND_GPU_SCHEDULING_GG"></span>

The video memory manager is currently implemented in the following OS files: 

* dxgkrnl.sys
* dxgmms1.sys
* dxgmms2.sys

These files are only available as part of an OS install, and are not available as a separate download. These files are only designed to work together with the other OS files that accompany them. Mismatching versions between these files are not supported by Microsoft, and routinely do not work.

The following sections describe the video memory management and graphics processing unit (GPU) scheduling model:

[Handling Memory Segments](handling-memory-segments.md)

[Handling Command and DMA Buffers](handling-command-and-dma-buffers.md)

[GDI Hardware Acceleration](gdi-hardware-acceleration.md)

[Video memory offer and reclaim](video-memory-offer-and-reclaim.md)

[GPU preemption](gpu-preemption.md)

 

 





