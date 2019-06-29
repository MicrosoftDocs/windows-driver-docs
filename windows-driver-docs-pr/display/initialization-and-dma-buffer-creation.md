---
title: Initialization and DMA Buffer Creation
description: Initialization and DMA Buffer Creation
ms.assetid: d84aed8a-9e22-4172-89c2-807b4e06108f
keywords:
- DMA buffers WDK display , creating for GDI hardware acceleration
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Initialization and DMA Buffer Creation


## <span id="ddk_introduction_to_command_and_dma_buffers_gg"></span><span id="DDK_INTRODUCTION_TO_COMMAND_AND_DMA_BUFFERS_GG"></span>


To indicate that the GPU supports GDI Hardware Acceleration, a display miniport driver's implementation of the [**DriverEntry**](https://docs.microsoft.com/windows-hardware/drivers/display/driverentry-of-display-miniport-driver) function must fill in the **DxgkDdiRenderKm** member of the [**DRIVER\_INITIALIZATION\_DATA**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dispmprt/ns-dispmprt-_driver_initialization_data) structure with a pointer to the driver-implemented [**DxgkDdiRenderKm**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dkmddi/nc-d3dkmddi-dxgkddi_renderkm) function.

The DirectX graphics kernel subsystem calls the *DxgkDdiRenderKm* function to generate a DMA buffer from the command buffer that is passed by the kernel-mode Canonical Display Driver (CDD) provided by the operating system.

When the display port driver of the DirectX graphics kernel subsystem (*Dxgkrnl.sys*) calls the [**DxgkDdiCreateContext**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dkmddi/nc-d3dkmddi-dxgkddi_createcontext) function, it sets the [**pCreateContext**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dkmddi/ns-d3dkmddi-_dxgkarg_createcontext)-&gt;[**Flags**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dkmddi/ns-d3dkmddi-_dxgk_createcontextflags)-&gt;**GdiContext** member to indicate the context that is used for GDI Hardware Acceleration.

Similarly, when the display port driver calls the [**DxgkDdiCreateDevice**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dkmddi/nc-d3dkmddi-dxgkddi_createdevice) function, it sets the [**pCreateDevice**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dkmddi/ns-d3dkmddi-_dxgkarg_createdevice)-&gt;[**Flags**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dkmddi/ns-d3dkmddi-_dxgk_createdeviceflags)-&gt;**GdiDevice** member to indicate the device that is used for GDI Hardware Acceleration.

 

 





