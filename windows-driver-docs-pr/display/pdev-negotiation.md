---
title: PDEV Negotiation
description: PDEV Negotiation
ms.assetid: d3172dd2-ecf1-4ad8-ba52-776bf712ab7c
keywords:
- GDI WDK Windows 2000 display , PDEV negotiation
- graphics drivers WDK Windows 2000 display , PDEV negotiation
- drawing WDK GDI , PDEV negotiation
- negotiation WDK GDI
- PDEV WDK GDI
- DrvEnablePDEV
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# PDEV Negotiation


## <span id="ddk_pdev_negotiation_gg"></span><span id="DDK_PDEV_NEGOTIATION_GG"></span>


One of the primary responsibilities of any graphics driver is to enable a [*PDEV*](https://msdn.microsoft.com/library/windows/hardware/ff556325#wdkgloss-pdev) during driver initialization. A PDEV is a logical representation of the physical device. This representation is defined by the driver and is typically a private data structure. Refer to [**DrvEnablePDEV**](https://msdn.microsoft.com/library/windows/hardware/ff556211) for more information about enabling PDEVs.

Through the *DrvEnablePDEV* function, the driver must provide information to GDI that describes the requested device and its capabilities. One piece of important information that the driver gives GDI is the set of graphics capability flags (GCAPS\_Xxx and GCAPS2\_Xxx flags) in the **flGraphicsCaps** and **flGraphicsCaps2** members of the [**DEVINFO**](https://msdn.microsoft.com/library/windows/hardware/ff552835) structure.

The capability flags allow GDI to determine which operations the PDEV supports. For example, GDI tests the capability flags that indicate whether the PDEV can handle Bezier curves and geometric wide lines before GDI attempts to call the [**DrvStrokePath**](https://msdn.microsoft.com/library/windows/hardware/ff556316) function to draw paths with these primitive types. If the capability flags indicate that the PDEV cannot handle these primitive types, GDI will break down the lines or curves so it can make simpler calls to the driver.

From the driver's side, whenever the driver gets an advanced path-related call from GDI, it can return **FALSE** if the path or clipping is too complex for the device to process.

The driver cannot return **FALSE** from *DrvStrokePath* when handling a [cosmetic line](cosmetic-lines.md) because the driver must handle any complex clipping or styling for cosmetic lines. However, *DrvStrokePath* can return **FALSE** if the path has Bezier curves or geometric lines. When this occurs, GDI breaks the call down to simpler calls, just as it does if the capability bits are not set. For example, if *DrvStrokePath* returns **FALSE** when it is sent a geometric line, GDI simplifies the line and calls the [**DrvFillPath**](https://msdn.microsoft.com/library/windows/hardware/ff556220) function.

If *DrvStrokePath* is to report an error, it must return DDI\_ERROR.

This kind of negotiation between GDI and the driver, for functions that depend on the PDEV, permits GDI and the driver to produce high quality output without excess communication.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20PDEV%20Negotiation%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




