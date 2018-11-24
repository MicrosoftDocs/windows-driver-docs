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
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 





