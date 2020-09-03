---
title: Enabling and Disabling the Surface
description: Enabling and Disabling the Surface
ms.assetid: 34a1d1a5-b139-4d59-8754-b77d71bc75ad
keywords:
- drawing WDK GDI , initialization, enabling and disabling a surface
- initializing graphics drivers WDK Windows 2000 display , enabling and disabling a surface
- GDI WDK Windows 2000 display , initialization, enabling and disabling a surface
- graphics drivers WDK Windows 2000 display , initialization, enabling and disabling a surface
- surface initialization WDK GDI
- surface disabling WDK GDI
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Enabling and Disabling the Surface


## <span id="ddk_enabling_and_disabling_the_surface_gg"></span><span id="DDK_ENABLING_AND_DISABLING_THE_SURFACE_GG"></span>


As the final initialization stage, GDI calls **DrvEnableSurface**. *DrvEnableSurface* must specify the type of surface by calling the appropriate GDI service to create it. As described in [GDI Support for Surfaces](gdi-support-for-surfaces.md), and depending on the device and circumstances, the driver can call the appropriate GDI services from within *DrvEnableSurface* to create the surfaces:

-   For a *device-managed surface*, the driver should call the [**EngCreateDeviceSurface**](/windows/desktop/api/winddi/nf-winddi-engcreatedevicesurface) function to get a handle for the surface.

-   To create a standard-format (*DIB*) bitmap that GDI can manage completely, including the performance of all drawing operations, the driver should call the **EngCreateBitmap** drivers.

*DrvEnableSurface* returns a valid surface handle as a return value.

Following the creation of the surface, the driver must associate that surface with a PDEV by calling the GDI service [**EngAssociateSurface**](/windows/desktop/api/winddi/nf-winddi-engassociatesurface). This call also tells GDI which drawing functions a driver has hooked for that surface.

GDI calls the [**DrvDisableSurface**](/windows/desktop/api/winddi/nf-winddi-drvdisablesurface) function to inform the driver that the current surface created for the PDEV by *DrvEnableSurface* is no longer required. The driver must deallocate any memory and resources allocated during the execution of *DrvEnableSurface*. *DrvDisableSurface* is always called before [**DrvDisablePDEV**](/windows/desktop/api/winddi/nf-winddi-drvdisablepdev), if the PDEV has an enabled surface.

Once created, a surface must be deleted when it is no longer in use. Failure to properly match surface creation with deletion can cause stray objects to accumulate and degrade system performance.

 

