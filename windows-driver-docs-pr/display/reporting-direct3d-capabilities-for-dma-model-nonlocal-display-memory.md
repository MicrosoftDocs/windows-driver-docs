---
title: Reporting Direct3D Capabilities for DMA Model Nonlocal Display Memory
description: Reporting Direct3D Capabilities for DMA Model Nonlocal Display Memory
ms.assetid: aa1b08c0-b212-48b6-a450-78d36951db80
keywords:
- DMA-style AGP WDK DirectDraw
- display memory WDK DirectDraw , DMA-style AGP
- nonlocal display memory WDK DirectDraw , DMA-style AGP
- AGP WDK DirectDraw , DMA-style AGP
- drawing AGP support WDK DirectDraw , DMA-style AGP
- DirectDraw AGP support WDK Windows 2000 display , DMA-style AGP
- memory WDK DirectDraw AGP , DMA-style AGP
- reporting Direct3D capabilities
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Reporting Direct3D Capabilities for DMA Model Nonlocal Display Memory


## <span id="ddk_reporting_direct3d_capabilities_for_dma_model_nonlocal_display_mem"></span><span id="DDK_REPORTING_DIRECT3D_CAPABILITIES_FOR_DMA_MODEL_NONLOCAL_DISPLAY_MEM"></span>


A DMA model driver must also export the Direct3D capabilities for nonlocal display memory surfaces. This is significantly simpler than reporting DirectDraw capabilities. The only capability affected is D3DDEVCAPS\_TEXTURENONLOCALVIDEOMEMORY. If a display card exporting the DMA model can texture directly from nonlocal display memory, it should set this capability in its Direct3D device description. If it cannot, and the application must explicitly load or blt the nonlocal display memory surface to a local display memory surface before performing texturing, it should not set this capability. For completeness, an execute model driver should always set this capability bit.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Reporting%20Direct3D%20Capabilities%20for%20DMA%20Model%20Nonlocal%20Display%20Memory%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




