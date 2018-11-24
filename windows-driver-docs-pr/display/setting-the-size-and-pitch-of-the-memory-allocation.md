---
title: Setting the Size and Pitch of the Memory Allocation
description: Setting the Size and Pitch of the Memory Allocation
ms.assetid: babd331f-7aec-4aee-aef9-7c10b98f9181
keywords:
- memory allocation WDK display
- allocating memory WDK display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Setting the Size and Pitch of the Memory Allocation


## <span id="ddk_introduction_to_command_and_dma_buffers_gg"></span><span id="DDK_INTRODUCTION_TO_COMMAND_AND_DMA_BUFFERS_GG"></span>


A display miniport driver that supports GDI Hardware Acceleration should set the size and pitch of the allocations of system or video memory when it processes the following allocation calls.

<span id="DxgkDdiCreateAllocation"></span><span id="dxgkddicreateallocation"></span><span id="DXGKDDICREATEALLOCATION"></span>[**DxgkDdiCreateAllocation**](https://msdn.microsoft.com/library/windows/hardware/ff559606)  
When the driver processes a call to *DxgkDdiCreateAllocation*, it should set the size, in bytes, of the system or video memory allocation. The size of the allocation is set through the [**pCreateAllocation**](https://msdn.microsoft.com/library/windows/hardware/ff557559)*-&gt;* [**pAllocationInfo**](https://msdn.microsoft.com/library/windows/hardware/ff560960)<em>-&gt;</em>**Size** member. If the allocation is visible to the CPU, the size should include the pitch value, which is the width of the surface, including padding, in bytes.

Allocations are visible to the CPU if the [**pGetStandardAllocationDriverData**](https://msdn.microsoft.com/library/windows/hardware/ff557598)*-*&gt;[**pCreateGdiSurfaceData**](https://msdn.microsoft.com/library/windows/hardware/ff546021)<em>-&gt;</em>**Type** member is set to D3DKMDT\_GDISURFACE\_STAGING\_CPUVISIBLE or D3DKMDT\_GDISURFACE\_EXISTINGSYSMEM. For the properties of these surface types, see the descriptions in [**D3DKMDT\_GDISURFACETYPE**](https://msdn.microsoft.com/library/windows/hardware/ff546039).

<span id="DxgkDdiGetStandardAllocationDriverData"></span><span id="dxgkddigetstandardallocationdriverdata"></span><span id="DXGKDDIGETSTANDARDALLOCATIONDRIVERDATA"></span>[**DxgkDdiGetStandardAllocationDriverData**](https://msdn.microsoft.com/library/windows/hardware/ff559673)  
When the driver processes a call to *DxgkDdiGetStandardAllocationDriverData* for an allocation that is visible to the CPU, it should:

1.  Set the [**pGetStandardAllocationDriverData**](https://msdn.microsoft.com/library/windows/hardware/ff557598)*-*&gt;[**StandardAllocationType**](https://msdn.microsoft.com/library/windows/hardware/ff546589) member to D3DKMDT\_STANDARDALLOCATION\_GDISURFACE.

2.  Set the description of a surface that can be used for redirection by GDI Hardware Acceleration and the Desktop Windows Manager (DWM) through the [**D3DKMDT\_GDISURFACEDATA**](https://msdn.microsoft.com/library/windows/hardware/ff546021) structure that is pointed to by the [**pGetStandardAllocationDriverData**](https://msdn.microsoft.com/library/windows/hardware/ff557598)*-*&gt;**pCreateGdiSurfaceData** member. For example, set the pitch of the allocation through the **Pitch** member of D3DKMDT\_GDISURFACEDATA.

 

 





