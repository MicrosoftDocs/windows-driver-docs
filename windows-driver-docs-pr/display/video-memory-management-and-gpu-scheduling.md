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
ms.date: 07/01/2024
---

# Video Memory Management and GPU Scheduling

The video memory manager (*VidMm*) is a system-supplied component within the DirectX Graphics Kernel (*Dxgkrnl*) that is responsible for managing a GPU's memory. *VidMm* handles tasks related to the allocation, deallocation, and overall management of graphics memory resources used by both kernel-mode display drivers (KMDs) and user-mode drivers (UMDs). It works alongside the system-supplied GPU scheduler (*VidSch*) to manage memory resources efficiently.

*VidMm* is implemented in the following OS files:

* dxgkrnl.sys
* dxgmms1.sys
* dxgmms2.sys

These files are only available as part of an OS install, and aren't available as a separate download. These files are only designed to work together with the other OS files that accompany them. Graphics driver developers must not mix versions of these files.

The following sections describe the video memory management and graphics processing unit (GPU) scheduling model:

[Handling Memory Segments](handling-memory-segments.md)

[Handling Command and DMA Buffers](handling-command-and-dma-buffers.md)

[GDI Hardware Acceleration](gdi-hardware-acceleration.md)

[Video memory offer and reclaim](video-memory-offer-and-reclaim.md)

[GPU preemption](gpu-preemption.md)
