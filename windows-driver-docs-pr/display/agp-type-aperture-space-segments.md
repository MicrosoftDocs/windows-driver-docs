---
title: AGP-Type Aperture-Space Segments
description: AGP-Type Aperture-Space Segments
keywords:
- memory segments WDK display , AGP-type aperture-space segments
- AGP-type aperture-space segments WDK display
- aperture-space segments WDK display
ms.date: 07/01/2024
ms.topic: concept-article
---

# AGP-Type Aperture-Space Segments

An AGP-type aperture-space segment is similar to a linear aperture-space segment. However, the kernel-mode display miniport driver (KMD) doesn't expose DXGK_OPERATION_MAP_APERTURE_SEGMENT and DXGK_OPERATION_UNMAP_APERTURE_SEGMENT operation types of the [**DxgkDdiBuildPagingBuffer**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_buildpagingbuffer) callback function through the AGP-type aperture-space segment. Instead, the video memory manager (*VidMm*) uses the GART driver to map and unmap system pages. That is, *VidMm* doesn't involve the KMD

The KMD must set the **Agp** bit-field flag in the **Flags** member of the [**DXGK_SEGMENTDESCRIPTOR**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_segmentdescriptor) structure to specify an AGP-type aperture-space segment.
