---
title: Processing Subrectangles
description: Processing Subrectangles
keywords:
- deinterlacing WDK DirectX VA , subrectangular processing
- subrectangular processing WDK DirectX VA
ms.date: 04/20/2017
---

# Processing Subrectangles


## <span id="ddk_processing_subrectangles_gg"></span><span id="DDK_PROCESSING_SUBRECTANGLES_GG"></span>


**This section applies only to Windows Server 2003 with SP1 and later, and Windows XP with SP2 and later.**

The VMR on Windows Server 2003 SP1 and later and Windows XP SP2 and later can process subrectangular regions of the source video image and video substreams and can write to subrectangular regions on the destination surface. The VMR performs a subrectangular-process operation by making the coordinates of the rectangles in the **rcSrc** and **rcDest** members of the [**DXVA\_VideoSample2**](/windows-hardware/drivers/ddi/dxva/ns-dxva-_dxva_videosample2) structure for each sample different from the coordinates of the source and destination surfaces.

If the deinterlace hardware supports subrectangular-process operations, the display driver reports this support by setting the DXVA\_VideoProcess\_SubRects flag in the **VideoProcessingCaps** member of the [**DXVA\_DeinterlaceCaps**](/windows-hardware/drivers/ddi/dxva/ns-dxva-_dxva_deinterlacecaps) structure. The driver returns a pointer to DXVA\_DeinterlaceCaps when its [**DeinterlaceQueryModeCaps**](./dxva-deinterlacecontainerdeviceclass-deinterlacequerymodecaps.md) function is called.

In subrectangular-process operations, the VMR can stretch subrectangles and can intersect subrectangles with each other on the destination surface.

The following topics show how to perform various subrectangular-process operations:

[Processing Subrectangles without Stretching](processing-subrectangles-without-stretching.md)

[Stretching Subrectangles](stretching-subrectangles.md)

 

