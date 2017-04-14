---
title: AGP-Type Aperture-Space Segments
description: AGP-Type Aperture-Space Segments
ms.assetid: a531f79e-541a-4454-8337-19a99aa046ae
keywords: ["memory segments WDK display , AGP-type aperture-space segments", "AGP-type aperture-space segments WDK display", "aperture-space segments WDK display"]
---

# AGP-Type Aperture-Space Segments


## <span id="ddk_agp_type_aperture_space_segments_gg"></span><span id="DDK_AGP_TYPE_APERTURE_SPACE_SEGMENTS_GG"></span>


An AGP-type aperture-space segment is similar to a linear aperture-space segment; however, the display miniport driver does not expose DXGK\_OPERATION\_MAP\_APERTURE\_SEGMENT and DXGK\_OPERATION\_UNMAP\_APERTURE\_SEGMENT operation types of the [**DxgkDdiBuildPagingBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff559587) callback function through the AGP-type aperture-space segment. Instead, the video memory manager uses the GART driver to map and unmap system pages (that is, the video memory manager does not involve the display miniport driver).

The driver must set the **Agp** bit-field flag in the **Flags** member of the [**DXGK\_SEGMENTDESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff562035) structure to specify an AGP-type aperture-space segment.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20AGP-Type%20Aperture-Space%20Segments%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




