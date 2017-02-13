---
title: Processing Subrectangles
description: Processing Subrectangles
ms.assetid: d00803c0-98e2-4101-bcfc-ef11fea07962
keywords: ["deinterlacing WDK DirectX VA , subrectangular processing", "subrectangular processing WDK DirectX VA"]
---

# Processing Subrectangles


## <span id="ddk_processing_subrectangles_gg"></span><span id="DDK_PROCESSING_SUBRECTANGLES_GG"></span>


**This section applies only to Windows Server 2003 with SP1 and later, and Windows XP with SP2 and later.**

The VMR on Windows Server 2003 SP1 and later and Windows XP SP2 and later can process subrectangular regions of the source video image and video substreams and can write to subrectangular regions on the destination surface. The VMR performs a subrectangular-process operation by making the coordinates of the rectangles in the **rcSrc** and **rcDest** members of the [**DXVA\_VideoSample2**](https://msdn.microsoft.com/library/windows/hardware/ff564092) structure for each sample different from the coordinates of the source and destination surfaces.

If the deinterlace hardware supports subrectangular-process operations, the display driver reports this support by setting the DXVA\_VideoProcess\_SubRects flag in the **VideoProcessingCaps** member of the [**DXVA\_DeinterlaceCaps**](https://msdn.microsoft.com/library/windows/hardware/ff563939) structure. The driver returns a pointer to DXVA\_DeinterlaceCaps when its [**DeinterlaceQueryModeCaps**](https://msdn.microsoft.com/library/windows/hardware/ff563946) function is called.

In subrectangular-process operations, the VMR can stretch subrectangles and can intersect subrectangles with each other on the destination surface.

The following topics show how to perform various subrectangular-process operations:

[Processing Subrectangles without Stretching](processing-subrectangles-without-stretching.md)

[Stretching Subrectangles](stretching-subrectangles.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Processing%20Subrectangles%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




