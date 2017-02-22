---
title: Specifying Segments When Creating Allocations
description: Specifying Segments When Creating Allocations
ms.assetid: 31bfbfd9-89e5-42fe-90bc-8ff54bac4f8b
keywords: ["memory segments WDK display , allocation creation", "allocations WDK display"]
---

# Specifying Segments When Creating Allocations


## <span id="ddk_specifying_segments_for_creating_and_rendering_allocations_gg"></span><span id="DDK_SPECIFYING_SEGMENTS_FOR_CREATING_AND_RENDERING_ALLOCATIONS_GG"></span>


The display miniport driver specifies and returns information about its memory segments that it prefers the video memory manager use when the video memory manager calls the driver's [**DxgkDdiCreateAllocation**](https://msdn.microsoft.com/library/windows/hardware/ff559606) function. In the call to *DxgkDdiCreateAllocation*, the driver creates allocations for video resources. The driver returns identifiers of supported segments and segment preferences in the [**DXGK\_ALLOCATIONINFO**](https://msdn.microsoft.com/library/windows/hardware/ff560960) structures that describe the allocations.

From the returned segment information, the video memory manager determines the appropriate memory segment to page-in for the given operation.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Specifying%20Segments%20When%20Creating%20Allocations%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




