---
title: Linear Aperture-Space Segments
description: Linear Aperture-Space Segments
keywords:
- memory segments WDK display , linear aperture-space segments
- linear aperture-space segments WDK display
- aperture-space segments WDK display
ms.date: 07/01/2024
---

# Linear Aperture-Space Segments

A linear aperture-space segment is similar to a linear memory-space segment. However, the aperture-space segment is only an address space and can't hold bits.

To hold the bits, system memory pages must be allocated, and the address-space range must be redirected to refer to those pages. The kernel-mode display miniport driver (KMD) must implement the [**DxgkDdiBuildPagingBuffer**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_buildpagingbuffer) function for DXGK_OPERATION_MAP_APERTURE_SEGMENT and DXGK_OPERATION_UNMAP_APERTURE_SEGMENT operation types to handle the redirection and must expose this function as described in [**DriverEntry of Display Miniport Driver**](driverentry-of-display-miniport-driver.md). *Dxgkrnl* calls **DxgkDdiBuildPagingBuffer** with the address-space range to be redirected and the MDL that references the physical system memory pages that were allocated.

The KMD typically accomplishes the redirection of the address-space range by programming a page table, which is unknown to the video memory manager (*VidMm*).

The driver must set the **Aperture** bit-field flag in the **Flags** member of the [**DXGK_SEGMENTDESCRIPTOR**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_segmentdescriptor) structure to specify a linear aperture-space segment. The driver can also set the following bit-field flags to indicate other segment support:

* **CpuVisible** to indicate that the segment is CPU-accessible.

* **CacheCoherent** to indicate that the segment maintains cache coherency with the CPU for the pages to which the segment redirects.

The following figure shows a visual representation of a linear aperture-space segment.

:::image type="content" source="images/aptrspac.png" alt-text="Diagram illustrating a linear aperture-space segment.":::
