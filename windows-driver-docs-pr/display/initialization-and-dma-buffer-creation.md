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


To indicate that the GPU supports GDI Hardware Acceleration, a display miniport driver's implementation of the [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff556157) function must fill in the **DxgkDdiRenderKm** member of the [**DRIVER\_INITIALIZATION\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff556169) structure with a pointer to the driver-implemented [**DxgkDdiRenderKm**](https://msdn.microsoft.com/library/windows/hardware/ff559800) function.

The DirectX graphics kernel subsystem calls the *DxgkDdiRenderKm* function to generate a DMA buffer from the command buffer that is passed by the kernel-mode Canonical Display Driver (CDD) provided by the operating system.

When the display port driver of the DirectX graphics kernel subsystem (*Dxgkrnl.sys*) calls the [**DxgkDdiCreateContext**](https://msdn.microsoft.com/library/windows/hardware/ff559612) function, it sets the [**pCreateContext**](https://msdn.microsoft.com/library/windows/hardware/ff557567)-&gt;[**Flags**](https://msdn.microsoft.com/library/windows/hardware/ff561037)-&gt;**GdiContext** member to indicate the context that is used for GDI Hardware Acceleration.

Similarly, when the display port driver calls the [**DxgkDdiCreateDevice**](https://msdn.microsoft.com/library/windows/hardware/ff559615) function, it sets the [**pCreateDevice**](https://msdn.microsoft.com/library/windows/hardware/ff557570)-&gt;[**Flags**](https://msdn.microsoft.com/library/windows/hardware/ff561039)-&gt;**GdiDevice** member to indicate the device that is used for GDI Hardware Acceleration.

 

 





