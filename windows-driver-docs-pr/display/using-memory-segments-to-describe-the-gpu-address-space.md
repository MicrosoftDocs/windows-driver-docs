---
title: Using Memory Segments to Describe the GPU Address Space
description: Using Memory Segments to Describe the GPU Address Space
keywords:
- memory segments WDK display , about memory segments
- hidden video memory WDK display
- video memory manager WDK display
ms.date: 08/29/2024
---

# Using Memory Segments to Describe the GPU Address Space

The video memory manager (*VidMm*) is responsible for managing the address space of the GPU. Before it can do so, the kernel-mode display miniport driver (KMD) must describe the GPU's address space to *VidMm* by using memory segments.

KMD creates memory segments to generalize and virtualize video memory resources. It can configure memory segments according to the memory types that the hardware supports (for example, frame buffer memory or system memory aperture).

During driver initialization, the KMD must return the list of segment types that describe how *VidMm* can manage memory resources. The KMD specifies the number of segment types that it supports and describes each segment type by responding to calls to its [**DxgkDdiQueryAdapterInfo**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_queryadapterinfo) function. The driver describes each segment using a [**DXGK_SEGMENTDESCRIPTOR**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_segmentdescriptor) structure. For more information, see [Initializing Use of Memory Segments](initializing-use-of-memory-segments.md).

Thereafter, the number and types of segments remain unchanged. *VidMm*:

* Ensures that each process receives a fair share of the resources in any particular segment,

* Manages all segments independently.

Segments don't overlap. So, *VidMm* can allocate a fair amount of video memory resources from one segment regardless of the amount of resources that an application holds from another segment.

The KMD assigns a segment identifier to each of its memory segments. Later, when *VidMm* requests to create allocations for video resources and render those resources, the KMD:

* Identifies the segments that support the request.

* Specifies, in order, the segments that the driver prefers *VidMm* to use.

For more information, see [Specifying Segments When Creating Allocations](specifying-segments-when-creating-allocations.md).

The KMD isn't required to specify all video memory resources available to the GPU in its memory segments. However, the KMD must specify all memory resources that *VidMm* manages among all processes running on the system. For example:

* A vertex shader microcode that implements a fixed function pipeline can reside in the GPU address space, but outside the memory that *VidMm* manages (that is, not part of a segment). This configuration is possible because the microcode is always available to all processes and is never the source of contention between processes.

* For resources such as vertex buffers, textures, render targets, and application-specific shader code, *VidMm* must allocate video memory resources from one of the driver's memory segments. This requirement is because the resource types must be fairly available to all processes.

The following figure shows an example of how a KMD can configure memory segments from the GPU address space.

:::image type="content" source="images/memseg.png" alt-text="Diagram illustrating the division of GPU address space into memory segments.":::

The numbers in the figure correspond to the following memory segments:

1. The CPU-accessible linear segment: This segment is accessible by the CPU and is organized as a linear address space.

2. Non-CPU-accessible linear segment: This segment is organized as a linear address space, but isn't accessible by the CPU. It's used for resources that don't require CPU access.

3. Read-only AGP aperture segment: This segment is used for read-only access to AGP (Accelerated Graphics Port) memory.

4. Aperture segment: This segment is used for resources that are accessed through the AGP aperture.

The Hidden boxes represent memory segments that the KMD doesn't expose to *VidMm*. Video memory that is hidden from *VidMm* can't be mapped into user space or be made exclusively available to any particular process. Doing so breaks the fundamental rules of virtual memory that require all processes running on the system to have access to all memory.
