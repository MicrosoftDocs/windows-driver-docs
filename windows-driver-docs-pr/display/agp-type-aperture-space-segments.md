---
title: AGP-Type Aperture-Space Segments
description: AGP-Type Aperture-Space Segments
ms.assetid: a531f79e-541a-4454-8337-19a99aa046ae
keywords:
- memory segments WDK display , AGP-type aperture-space segments
- AGP-type aperture-space segments WDK display
- aperture-space segments WDK display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# AGP-Type Aperture-Space Segments


## <span id="ddk_agp_type_aperture_space_segments_gg"></span><span id="DDK_AGP_TYPE_APERTURE_SPACE_SEGMENTS_GG"></span>


An AGP-type aperture-space segment is similar to a linear aperture-space segment; however, the display miniport driver does not expose DXGK\_OPERATION\_MAP\_APERTURE\_SEGMENT and DXGK\_OPERATION\_UNMAP\_APERTURE\_SEGMENT operation types of the [**DxgkDdiBuildPagingBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff559587) callback function through the AGP-type aperture-space segment. Instead, the video memory manager uses the GART driver to map and unmap system pages (that is, the video memory manager does not involve the display miniport driver).

The driver must set the **Agp** bit-field flag in the **Flags** member of the [**DXGK\_SEGMENTDESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff562035) structure to specify an AGP-type aperture-space segment.

 

 





