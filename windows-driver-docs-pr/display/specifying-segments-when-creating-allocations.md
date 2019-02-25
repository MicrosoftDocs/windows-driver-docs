---
title: Specifying Segments When Creating Allocations
description: Specifying Segments When Creating Allocations
ms.assetid: 31bfbfd9-89e5-42fe-90bc-8ff54bac4f8b
keywords:
- memory segments WDK display , allocation creation
- allocations WDK display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Specifying Segments When Creating Allocations


## <span id="ddk_specifying_segments_for_creating_and_rendering_allocations_gg"></span><span id="DDK_SPECIFYING_SEGMENTS_FOR_CREATING_AND_RENDERING_ALLOCATIONS_GG"></span>


The display miniport driver specifies and returns information about its memory segments that it prefers the video memory manager use when the video memory manager calls the driver's [**DxgkDdiCreateAllocation**](https://msdn.microsoft.com/library/windows/hardware/ff559606) function. In the call to *DxgkDdiCreateAllocation*, the driver creates allocations for video resources. The driver returns identifiers of supported segments and segment preferences in the [**DXGK\_ALLOCATIONINFO**](https://msdn.microsoft.com/library/windows/hardware/ff560960) structures that describe the allocations.

From the returned segment information, the video memory manager determines the appropriate memory segment to page-in for the given operation.

 

 





