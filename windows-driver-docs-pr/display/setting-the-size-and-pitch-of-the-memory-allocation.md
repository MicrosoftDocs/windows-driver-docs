---
title: Setting the Size and Pitch of the Memory Allocation
description: Setting the Size and Pitch of the Memory Allocation
ms.assetid: babd331f-7aec-4aee-aef9-7c10b98f9181
keywords:
- memory allocation WDK display
- allocating memory WDK display
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Setting the Size and Pitch of the Memory Allocation


## <span id="ddk_introduction_to_command_and_dma_buffers_gg"></span><span id="DDK_INTRODUCTION_TO_COMMAND_AND_DMA_BUFFERS_GG"></span>


A display miniport driver that supports GDI Hardware Acceleration should set the size and pitch of the allocations of system or video memory when it processes the following allocation calls.

<span id="DxgkDdiCreateAllocation"></span><span id="dxgkddicreateallocation"></span><span id="DXGKDDICREATEALLOCATION"></span>[**DxgkDdiCreateAllocation**](https://msdn.microsoft.com/library/windows/hardware/ff559606)  
When the driver processes a call to *DxgkDdiCreateAllocation*, it should set the size, in bytes, of the system or video memory allocation. The size of the allocation is set through the [**pCreateAllocation**](https://msdn.microsoft.com/library/windows/hardware/ff557559)*-&gt;* [**pAllocationInfo**](https://msdn.microsoft.com/library/windows/hardware/ff560960)*-&gt;***Size** member. If the allocation is visible to the CPU, the size should include the pitch value, which is the width of the surface, including padding, in bytes.

Allocations are visible to the CPU if the [**pGetStandardAllocationDriverData**](https://msdn.microsoft.com/library/windows/hardware/ff557598)*-*&gt;[**pCreateGdiSurfaceData**](https://msdn.microsoft.com/library/windows/hardware/ff546021)*-&gt;***Type** member is set to D3DKMDT\_GDISURFACE\_STAGING\_CPUVISIBLE or D3DKMDT\_GDISURFACE\_EXISTINGSYSMEM. For the properties of these surface types, see the descriptions in [**D3DKMDT\_GDISURFACETYPE**](https://msdn.microsoft.com/library/windows/hardware/ff546039).

<span id="DxgkDdiGetStandardAllocationDriverData"></span><span id="dxgkddigetstandardallocationdriverdata"></span><span id="DXGKDDIGETSTANDARDALLOCATIONDRIVERDATA"></span>[**DxgkDdiGetStandardAllocationDriverData**](https://msdn.microsoft.com/library/windows/hardware/ff559673)  
When the driver processes a call to *DxgkDdiGetStandardAllocationDriverData* for an allocation that is visible to the CPU, it should:

1.  Set the [**pGetStandardAllocationDriverData**](https://msdn.microsoft.com/library/windows/hardware/ff557598)*-*&gt;[**StandardAllocationType**](https://msdn.microsoft.com/library/windows/hardware/ff546589) member to D3DKMDT\_STANDARDALLOCATION\_GDISURFACE.

2.  Set the description of a surface that can be used for redirection by GDI Hardware Acceleration and the Desktop Windows Manager (DWM) through the [**D3DKMDT\_GDISURFACEDATA**](https://msdn.microsoft.com/library/windows/hardware/ff546021) structure that is pointed to by the [**pGetStandardAllocationDriverData**](https://msdn.microsoft.com/library/windows/hardware/ff557598)*-*&gt;**pCreateGdiSurfaceData** member. For example, set the pitch of the allocation through the **Pitch** member of D3DKMDT\_GDISURFACEDATA.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Setting%20the%20Size%20and%20Pitch%20of%20the%20Memory%20Allocation%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




