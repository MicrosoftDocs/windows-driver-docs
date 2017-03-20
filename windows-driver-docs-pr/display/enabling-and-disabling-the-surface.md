---
title: Enabling and Disabling the Surface
description: Enabling and Disabling the Surface
ms.assetid: 34a1d1a5-b139-4d59-8754-b77d71bc75ad
keywords: ["drawing WDK GDI , initialization, enabling and disabling a surface", "initializing graphics drivers WDK Windows 2000 display , enabling and disabling a surface", "GDI WDK Windows 2000 display , initialization, enabling and disabling a surface", "graphics drivers WDK Windows 2000 display , initialization, enabling and disabling a surface", "surface initialization WDK GDI", "surface disabling WDK GDI"]
---

# Enabling and Disabling the Surface


## <span id="ddk_enabling_and_disabling_the_surface_gg"></span><span id="DDK_ENABLING_AND_DISABLING_THE_SURFACE_GG"></span>


As the final initialization stage, GDI calls [**DrvEnableSurface**](https://msdn.microsoft.com/library/windows/hardware/ff556214) to have the driver enable a surface for an existing [*PDEV*](https://msdn.microsoft.com/library/windows/hardware/ff556325#wdkgloss-pdev). *DrvEnableSurface* must specify the type of surface by calling the appropriate GDI service to create it. As described in [GDI Support for Surfaces](gdi-support-for-surfaces.md), and depending on the device and circumstances, the driver can call the appropriate GDI services from within *DrvEnableSurface* to create the surfaces:

-   For a [*device-managed surface*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-managed-surface), the driver should call the [**EngCreateDeviceSurface**](https://msdn.microsoft.com/library/windows/hardware/ff564206) function to get a handle for the surface.

-   To create a standard-format ([*DIB*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-independent-bitmap--dib-)) bitmap that GDI can manage completely, including the performance of all drawing operations, the driver should call the [**EngCreateBitmap**](https://msdn.microsoft.com/library/windows/hardware/ff564199) function. The driver can hook out any drawing operations it can optimize. The driver can either have GDI allocate the space for the pixels or can provide the space itself, although the latter option is usually used only by printer and [*frame buffer*](https://msdn.microsoft.com/library/windows/hardware/ff556280#wdkgloss-frame-buffer) drivers.

*DrvEnableSurface* returns a valid surface handle as a return value.

Following the creation of the surface, the driver must associate that surface with a PDEV by calling the GDI service [**EngAssociateSurface**](https://msdn.microsoft.com/library/windows/hardware/ff564183). This call also tells GDI which drawing functions a driver has hooked for that surface.

GDI calls the [**DrvDisableSurface**](https://msdn.microsoft.com/library/windows/hardware/ff556200) function to inform the driver that the current surface created for the PDEV by *DrvEnableSurface* is no longer required. The driver must deallocate any memory and resources allocated during the execution of *DrvEnableSurface*. *DrvDisableSurface* is always called before [**DrvDisablePDEV**](https://msdn.microsoft.com/library/windows/hardware/ff556198), if the PDEV has an enabled surface.

Once created, a surface must be deleted when it is no longer in use. Failure to properly match surface creation with deletion can cause stray objects to accumulate and degrade system performance.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Enabling%20and%20Disabling%20the%20Surface%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




