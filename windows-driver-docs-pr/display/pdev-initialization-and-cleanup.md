---
title: PDEV Initialization and Cleanup
description: PDEV Initialization and Cleanup
ms.assetid: 26651869-861a-4be8-bc6c-df3704ca714e
keywords:
- drawing WDK GDI , initialization, PDEV initialization
- initializing graphics drivers WDK Windows 2000 display , PDEV
- GDI WDK Windows 2000 display , initialization, PDEV
- graphics drivers WDK Windows 2000 display , initialization, PDEV
- PDEV WDK GDI
- DrvEnablePDEV
- drawing WDK GDI , PDEV cleanup
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# PDEV Initialization and Cleanup


## <span id="ddk_pdev_initialization_and_cleanup_gg"></span><span id="DDK_PDEV_INITIALIZATION_AND_CLEANUP_GG"></span>


Each kernel-mode graphics driver represents a single logical device managed by GDI. In turn, a driver can manage one or more [*PDEV*](https://msdn.microsoft.com/library/windows/hardware/ff556325#wdkgloss-pdev) structures. A PDEV is a logical representation of the physical device. It is characterized by the type of hardware, logical address, and surfaces that can be supported:

-   **Type of Hardware** âˆ’ As an example of a driver supporting a PDEV characterized by the type of hardware, one driver could support the LaserWhiz, LaserWhiz II, and LaserWhiz Super printers. The device name passed by GDI specifies which logical device is requested from the total set of driver-supported devices.

-   **Logical Address** âˆ’ A single driver can support printers attached to LPT1, COM2, and a server named \\\\SERVER1\\PSLASER, for example. In addition, a display driver that can support more than one VGA display simultaneously might differentiate between them by port numbers, such as 0x3CE, 0x2CE, and so on. The logical address for printers and other hard copy output devices is determined by GDI; the [**EngWritePrinter**](https://msdn.microsoft.com/library/windows/hardware/ff565467) function directs the output to the proper destination. Displays can either determine their own logical address implicitly or retrieve the address from the private section of [**DEVMODEW**](https://msdn.microsoft.com/library/windows/hardware/ff552837).

    The DEVMODEW structure provides the driver with required environment settings, such as the name of the device and other information specific to either printer or display drivers.

-   **Surfaces** âˆ’ Each PDEV requires a unique surface. For example, if a printer driver is to work on two print jobs simultaneously, each requiring a different page format such as the landscape and portrait formats, each print job requires a different PDEV. Similarly, a display driver might support two desktops on the same display, each desktop requiring a different PDEV and surface. For each surface required, there is a call to the [**DrvEnablePDEV**](https://msdn.microsoft.com/library/windows/hardware/ff556211) function to create a different PDEV for that surface.

In response to a call to *DrvEnablePDEV*, the driver returns information about the capabilities of the hardware device to GDI through several structures.

The [**GDIINFO**](https://msdn.microsoft.com/library/windows/hardware/ff566484) structure is zero-filled before GDI calls *DrvEnablePDEV*. The driver fills in GDIINFO to communicate the following information to GDI:

-   Driver version number

-   Basic device technology (raster versus vector)

-   Size and resolution of printable page

-   Color palette and gray scale information

-   Font and text capabilities

-   Halftoning support

-   Style step numbers

The driver should fill only the fields it supports and ignore the rest.

The driver fills in the [**DEVINFO**](https://msdn.microsoft.com/library/windows/hardware/ff552835) structure with flags that describe the graphics capabilities of this PDEV. In nearly all cases, the information from DEVINFO tells GDI the level of graphics support the driver can provide. For example, if a drawing of a treble clef is needed, information within DEVINFO tells GDI whether the driver can handle Bezier curves or whether GDI must send multiple line segments instead. The driver should fill in as many fields as it supports and leave the others untouched.

Another important piece of information the driver must provide is a pointer (*phsurfPatterns*) to a buffer filled with handles for surfaces representing the standard fill patterns. Besides the standard fill patterns, *phsurfPatterns* can contain a null, which causes GDI to create the pattern surface automatically according to the device resolution and the pixel size. When GDI is called on to [realize a brush](realizing-brushes.md) with a standard pattern, it calls the [**DrvRealizeBrush**](https://msdn.microsoft.com/library/windows/hardware/ff556273) function to realize the brush defined for the requested pattern.

GDI passes [**DrvEnablePDEV**](https://msdn.microsoft.com/library/windows/hardware/ff556211) a handle, *hDriver*, for the kernel driver that supports the device. For a printer driver, *hDriver* provides the handle to the printer and is used in calls, such as **EngWritePrinter**, to the spooler.

Whenever GDI calls *DrvEnablePDEV*, the driver must allocate the memory required to support the PDEV that is created, even if *DrvEnablePDEV* is called to create other PDEV structures for different modes. (A driver can have several active PDEVs, although only one can be enabled at a time.) However, an actual surface is not supported until GDI calls [**DrvEnableSurface**](https://msdn.microsoft.com/library/windows/hardware/ff556214).

If a device surface requires the allocation of a bitmap, the allocation is not necessary until the surface is enabled (usually within the [**DrvEnableSurface**](https://msdn.microsoft.com/library/windows/hardware/ff556214) function). Although applications often request device information before actually writing to the device, waiting to allocate a large bitmap can save valuable resources and improve driver performance during system initialization.

When the installation of the PDEV is complete, GDI calls the [**DrvCompletePDEV**](https://msdn.microsoft.com/library/windows/hardware/ff556181) function to inform the driver that installation of the physical device is complete. This function also provides the driver with GDI's logical handle to the PDEV, which the driver uses in calls to GDI functions.

A call to the driver's [**DrvDisablePDEV**](https://msdn.microsoft.com/library/windows/hardware/ff556198) function indicates that the given physical device is no longer needed. In this function, the driver should free any memory and resources used by the physical device.

Refer also to [Enabling and Disabling the Surface](enabling-and-disabling-the-surface.md).

 

 





