---
title: Linear Aperture-Space Segments
description: Linear Aperture-Space Segments
ms.assetid: bf818841-eb73-442e-8745-a59d9c3a527c
keywords: ["memory segments WDK display , linear aperture-space segments", "linear aperture-space segments WDK display", "aperture-space segments WDK display"]
---

# Linear Aperture-Space Segments


## <span id="ddk_linear_aperture_space_segments_gg"></span><span id="DDK_LINEAR_APERTURE_SPACE_SEGMENTS_GG"></span>


A linear aperture-space segment is similar to a linear memory-space segment; however, the aperture-space segment is only an address space and cannot hold bits. To hold the bits, system memory pages must be allocated, and the address-space range must be redirected to refer to those pages. The display miniport driver must implement the [**DxgkDdiBuildPagingBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff559587) function for DXGK\_OPERATION\_MAP\_APERTURE\_SEGMENT and DXGK\_OPERATION\_UNMAP\_APERTURE\_SEGMENT operation types to handle the redirection and must expose this function as described in [**DriverEntry of Display Miniport Driver**](https://msdn.microsoft.com/library/windows/hardware/ff556157). The *DxgkDdiBuildPagingBuffer* function receives the range to be redirected and the MDL that references the physical system memory pages that were allocated.

The display miniport driver typically accomplishes the redirection of the address-space range by programming a page table, which is unknown to the video memory manager.

The driver must set the **Aperture** bit-field flag in the **Flags** member of the [**DXGK\_SEGMENTDESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff562035) structure to specify a linear aperture-space segment. The driver can also set the following bit-field flags to indicate additional segment support:

-   **CpuVisible** to indicate that the segment is CPU-accessible.

-   **CacheCoherent** to indicate that the segment maintains cache coherency with the CPU for the pages to which the segment redirects.

The following figure shows a visual representation of a linear aperture-space segment.

![diagram illustrating a linear aperture-space segment](images/aptrspac.png)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Linear%20Aperture-Space%20Segments%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




