---
title: GDI as a Rendering Engine
description: GDI as a Rendering Engine
ms.assetid: 3aae0c71-fc98-452c-a7a3-f20a790a466b
keywords:
- GDI WDK Windows 2000 display , rendering engine
- graphics drivers WDK Windows 2000 display , rendering engine
- drawing WDK GDI , rendering engine
- rendering engine WDK GDI
- PDEV WDK GDI
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# GDI as a Rendering Engine


## <span id="ddk_gdi_as_a_rendering_engine_gg"></span><span id="DDK_GDI_AS_A_RENDERING_ENGINE_GG"></span>


For rendering operations, the driver must first enable a [*surface*](https://msdn.microsoft.com/library/windows/hardware/ff556336#wdkgloss-surface) for each [*PDEV*](https://msdn.microsoft.com/library/windows/hardware/ff556325#wdkgloss-pdev) structure that is enabled. A PDEV is a logical representation of a physical device. If the hardware can be set up as a GDI standard-format bitmap, GDI can be used to do some or all of the drawing to the bitmap surface. GDI can also handle advanced [halftoning](gdi-halftoning-capabilities.md).

For information about enabling [*PDEVs*](https://msdn.microsoft.com/library/windows/hardware/ff556325#wdkgloss-pdev) and surfaces, refer to the [**DrvEnablePDEV**](https://msdn.microsoft.com/library/windows/hardware/ff556211) and [**DrvEnableSurface**](https://msdn.microsoft.com/library/windows/hardware/ff556214) functions.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20GDI%20as%20a%20Rendering%20Engine%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




