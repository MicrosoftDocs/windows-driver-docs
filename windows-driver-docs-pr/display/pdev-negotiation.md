---
title: PDEV Negotiation
description: PDEV Negotiation
keywords:
- GDI WDK Windows 2000 display , PDEV negotiation
- graphics drivers WDK Windows 2000 display , PDEV negotiation
- drawing WDK GDI , PDEV negotiation
- negotiation WDK GDI
- PDEV WDK GDI
- DrvEnablePDEV
ms.date: 04/20/2017
---

# PDEV Negotiation

One of the primary responsibilities of any graphics driver is to enable a *PDEV* during driver initialization. A PDEV is a logical representation of the physical device. This representation is defined by the driver and is typically a private data structure. Refer to [**DrvEnablePDEV**](/windows/win32/api/winddi/nf-winddi-drvenablepdev) for more information about enabling PDEVs.

Through the *DrvEnablePDEV* function, the driver must provide information to GDI that describes the requested device and its capabilities. One piece of important information that the driver gives GDI is the set of graphics capability flags (GCAPS_Xxx and GCAPS2_Xxx flags) in the **flGraphicsCaps** and **flGraphicsCaps2** members of the [**DEVINFO**](/windows/win32/api/winddi/ns-winddi-devinfo) structure.

The capability flags allow GDI to determine which operations the PDEV supports. For example, GDI tests the capability flags that indicate whether the PDEV can handle Bezier curves and geometric wide lines before GDI attempts to call the [**DrvStrokePath**](/windows/win32/api/winddi/nf-winddi-drvstrokepath) function to draw paths with these primitive types. If the capability flags indicate that the PDEV cannot handle these primitive types, GDI will break down the lines or curves so it can make simpler calls to the driver.

From the driver's side, whenever the driver gets an advanced path-related call from GDI, it can return **FALSE** if the path or clipping is too complex for the device to process.

The driver cannot return **FALSE** from *DrvStrokePath* when handling a [cosmetic line](cosmetic-lines.md) because the driver must handle any complex clipping or styling for cosmetic lines. However, *DrvStrokePath* can return **FALSE** if the path has Bezier curves or geometric lines. When this occurs, GDI breaks the call down to simpler calls, just as it does if the capability bits are not set. For example, if *DrvStrokePath* returns **FALSE** when it is sent a geometric line, GDI simplifies the line and calls the [**DrvFillPath**](/windows/win32/api/winddi/nf-winddi-drvfillpath) function.

If *DrvStrokePath* is to report an error, it must return DDI_ERROR.

This kind of negotiation between GDI and the driver, for functions that depend on the PDEV, permits GDI and the driver to produce high quality output without excess communication.
