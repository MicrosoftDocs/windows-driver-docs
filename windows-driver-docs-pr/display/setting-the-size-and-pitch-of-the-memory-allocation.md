---
title: Setting the Size and Pitch of the Memory Allocation
description: Setting the Size and Pitch of the Memory Allocation
keywords:
- memory allocation WDK display
- allocating memory WDK display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Setting the Size and Pitch of the Memory Allocation


## <span id="ddk_introduction_to_command_and_dma_buffers_gg"></span><span id="DDK_INTRODUCTION_TO_COMMAND_AND_DMA_BUFFERS_GG"></span>


A display miniport driver that supports GDI Hardware Acceleration should set the size and pitch of the allocations of system or video memory when it processes the following allocation calls.

<span id="DxgkDdiCreateAllocation"></span><span id="dxgkddicreateallocation"></span><span id="DXGKDDICREATEALLOCATION"></span>[**DxgkDdiCreateAllocation**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_createallocation)  
When the driver processes a call to *DxgkDdiCreateAllocation*, it should set the size, in bytes, of the system or video memory allocation. The size of the allocation is set through the [**pCreateAllocation**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgkarg_createallocation)*-&gt;* [**pAllocationInfo**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_allocationinfo)<em>-&gt;</em>**Size** member. If the allocation is visible to the CPU, the size should include the pitch value, which is the width of the surface, including padding, in bytes.

Allocations are visible to the CPU if the [**pGetStandardAllocationDriverData**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgkarg_getstandardallocationdriverdata)*-*&gt;[**pCreateGdiSurfaceData**](/windows-hardware/drivers/ddi/d3dkmdt/ns-d3dkmdt-_d3dkmdt_gdisurfacedata)<em>-&gt;</em>**Type** member is set to D3DKMDT\_GDISURFACE\_STAGING\_CPUVISIBLE or D3DKMDT\_GDISURFACE\_EXISTINGSYSMEM. For the properties of these surface types, see the descriptions in [**D3DKMDT\_GDISURFACETYPE**](/windows-hardware/drivers/ddi/d3dkmdt/ne-d3dkmdt-_d3dkmdt_gdisurfacetype).

<span id="DxgkDdiGetStandardAllocationDriverData"></span><span id="dxgkddigetstandardallocationdriverdata"></span><span id="DXGKDDIGETSTANDARDALLOCATIONDRIVERDATA"></span>[**DxgkDdiGetStandardAllocationDriverData**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_getstandardallocationdriverdata)  
When the driver processes a call to *DxgkDdiGetStandardAllocationDriverData* for an allocation that is visible to the CPU, it should:

1.  Set the [**pGetStandardAllocationDriverData**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgkarg_getstandardallocationdriverdata)*-*&gt;[**StandardAllocationType**](/windows-hardware/drivers/ddi/d3dkmdt/ne-d3dkmdt-_d3dkmdt_standardallocation_type) member to D3DKMDT\_STANDARDALLOCATION\_GDISURFACE.

2.  Set the description of a surface that can be used for redirection by GDI Hardware Acceleration and the Desktop Windows Manager (DWM) through the [**D3DKMDT\_GDISURFACEDATA**](/windows-hardware/drivers/ddi/d3dkmdt/ns-d3dkmdt-_d3dkmdt_gdisurfacedata) structure that is pointed to by the [**pGetStandardAllocationDriverData**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgkarg_getstandardallocationdriverdata)*-*&gt;**pCreateGdiSurfaceData** member. For example, set the pitch of the allocation through the **Pitch** member of D3DKMDT\_GDISURFACEDATA.

 

