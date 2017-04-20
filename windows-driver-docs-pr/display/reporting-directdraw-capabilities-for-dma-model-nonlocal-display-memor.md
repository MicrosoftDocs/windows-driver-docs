---
title: Reporting DirectDraw Capabilities for DMA Model Nonlocal Display Memory
description: Reporting DirectDraw Capabilities for DMA Model Nonlocal Display Memory
ms.assetid: e503fc8b-db27-486a-8616-a1b88ea77218
keywords:
- DMA-style AGP WDK DirectDraw
- display memory WDK DirectDraw , DMA-style AGP
- nonlocal display memory WDK DirectDraw , DMA-style AGP
- AGP WDK DirectDraw , DMA-style AGP
- drawing AGP support WDK DirectDraw , DMA-style AGP
- DirectDraw AGP support WDK Windows 2000 display , DMA-style AGP
- memory WDK DirectDraw AGP , DMA-style AGP
- reporting DirectDraw capabilities
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Reporting DirectDraw Capabilities for DMA Model Nonlocal Display Memory


## <span id="ddk_reporting_directdraw_capabilities_for_dma_model_nonlocal_display_m"></span><span id="DDK_REPORTING_DIRECTDRAW_CAPABILITIES_FOR_DMA_MODEL_NONLOCAL_DISPLAY_M"></span>


A DMA model driver has different capabilities for nonlocal display memory than for local display memory. For example, a display card may be able to stretch blit local display memory surfaces but not nonlocal display memory surfaces. If the driver specifies the DDCAPS2\_NONLOCALVIDMEMCAPS flag, the driver is probed for the DirectDraw capabilities of nonlocal display memory surface by the [**DdGetDriverInfo**](https://msdn.microsoft.com/library/windows/hardware/ff549404) driver entry point. The GUID that identifies this probe is GUID\_NonLocalVidMemCaps.

It is important to note that for this release of DirectDraw, a driver can only specify the capabilities for blts from nonlocal display memory to local display memory. Transfers from local display memory to nonlocal display memory, and from nonlocal display memory to nonlocal display memory, are always emulated by the DirectDraw HEL. This restriction may be relaxed in a future release.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Reporting%20DirectDraw%20Capabilities%20for%20DMA%20Model%20Nonlocal%20Display%20Memory%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




