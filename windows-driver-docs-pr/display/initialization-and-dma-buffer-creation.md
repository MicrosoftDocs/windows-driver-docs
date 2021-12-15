---
title: Initialization and DMA Buffer Creation
description: Initialization and DMA Buffer Creation
keywords:
- DMA buffers WDK display , creating for GDI hardware acceleration
ms.date: 04/20/2017
---

# Initialization and DMA Buffer Creation


## <span id="ddk_introduction_to_command_and_dma_buffers_gg"></span><span id="DDK_INTRODUCTION_TO_COMMAND_AND_DMA_BUFFERS_GG"></span>


To indicate that the GPU supports GDI Hardware Acceleration, a display miniport driver's implementation of the [**DriverEntry**](./driverentry-of-display-miniport-driver.md) function must fill in the **DxgkDdiRenderKm** member of the [**DRIVER\_INITIALIZATION\_DATA**](/windows-hardware/drivers/ddi/dispmprt/ns-dispmprt-_driver_initialization_data) structure with a pointer to the driver-implemented [**DxgkDdiRenderKm**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_renderkm) function.

The DirectX graphics kernel subsystem calls the *DxgkDdiRenderKm* function to generate a DMA buffer from the command buffer that is passed by the kernel-mode Canonical Display Driver (CDD) provided by the operating system.

When the display port driver of the DirectX graphics kernel subsystem (*Dxgkrnl.sys*) calls the [**DxgkDdiCreateContext**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_createcontext) function, it sets the [**pCreateContext**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgkarg_createcontext)-&gt;[**Flags**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_createcontextflags)-&gt;**GdiContext** member to indicate the context that is used for GDI Hardware Acceleration.

Similarly, when the display port driver calls the [**DxgkDdiCreateDevice**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_createdevice) function, it sets the [**pCreateDevice**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgkarg_createdevice)-&gt;[**Flags**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_createdeviceflags)-&gt;**GdiDevice** member to indicate the device that is used for GDI Hardware Acceleration.

 

