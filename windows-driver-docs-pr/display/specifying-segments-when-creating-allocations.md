---
title: Specifying Segments When Creating Allocations
description: Specifying Segments When Creating Allocations
keywords:
- memory segments WDK display , allocation creation
- allocations WDK display
ms.date: 04/20/2017
---

# Specifying Segments When Creating Allocations


## <span id="ddk_specifying_segments_for_creating_and_rendering_allocations_gg"></span><span id="DDK_SPECIFYING_SEGMENTS_FOR_CREATING_AND_RENDERING_ALLOCATIONS_GG"></span>


The display miniport driver specifies and returns information about its memory segments that it prefers the video memory manager use when the video memory manager calls the driver's [**DxgkDdiCreateAllocation**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_createallocation) function. In the call to *DxgkDdiCreateAllocation*, the driver creates allocations for video resources. The driver returns identifiers of supported segments and segment preferences in the [**DXGK\_ALLOCATIONINFO**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_allocationinfo) structures that describe the allocations.

From the returned segment information, the video memory manager determines the appropriate memory segment to page-in for the given operation.

 

