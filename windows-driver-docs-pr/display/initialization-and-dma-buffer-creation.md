---
title: Initialization and DMA Buffer Creation
description: Initialization and DMA Buffer Creation
ms.assetid: d84aed8a-9e22-4172-89c2-807b4e06108f
keywords: ["DMA buffers WDK display , creating for GDI hardware acceleration"]
---

# Initialization and DMA Buffer Creation


## <span id="ddk_introduction_to_command_and_dma_buffers_gg"></span><span id="DDK_INTRODUCTION_TO_COMMAND_AND_DMA_BUFFERS_GG"></span>


To indicate that the GPU supports GDI Hardware Acceleration, a display miniport driver's implementation of the [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff556157) function must fill in the **DxgkDdiRenderKm** member of the [**DRIVER\_INITIALIZATION\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff556169) structure with a pointer to the driver-implemented [**DxgkDdiRenderKm**](https://msdn.microsoft.com/library/windows/hardware/ff559800) function.

The DirectX graphics kernel subsystem calls the *DxgkDdiRenderKm* function to generate a DMA buffer from the command buffer that is passed by the kernel-mode Canonical Display Driver (CDD) provided by the operating system.

When the display port driver of the DirectX graphics kernel subsystem (*Dxgkrnl.sys*) calls the [**DxgkDdiCreateContext**](https://msdn.microsoft.com/library/windows/hardware/ff559612) function, it sets the [**pCreateContext**](https://msdn.microsoft.com/library/windows/hardware/ff557567)-&gt;[**Flags**](https://msdn.microsoft.com/library/windows/hardware/ff561037)-&gt;**GdiContext** member to indicate the context that is used for GDI Hardware Acceleration.

Similarly, when the display port driver calls the [**DxgkDdiCreateDevice**](https://msdn.microsoft.com/library/windows/hardware/ff559615) function, it sets the [**pCreateDevice**](https://msdn.microsoft.com/library/windows/hardware/ff557570)-&gt;[**Flags**](https://msdn.microsoft.com/library/windows/hardware/ff561039)-&gt;**GdiDevice** member to indicate the device that is used for GDI Hardware Acceleration.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Initialization%20and%20DMA%20Buffer%20Creation%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




