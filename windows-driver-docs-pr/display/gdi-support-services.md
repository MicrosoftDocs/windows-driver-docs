---
title: GDI Support Services
description: GDI Support Services
ms.assetid: a5521f9f-ddf6-4892-bf6d-aebb7936df11
keywords:
- GDI WDK Windows 2000 display , service routines
- graphics drivers WDK Windows 2000 display , service routines
- drawing WDK GDI , service routines
- service routines WDK GDI
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# GDI Support Services


## <span id="ddk_gdi_support_services_gg"></span><span id="DDK_GDI_SUPPORT_SERVICES_GG"></span>


[*GDI*](https://msdn.microsoft.com/library/windows/hardware/ff556283#wdkgloss-graphics-device-interface--gdi-) exports many service routines that can simplify driver design. The driver can call these routines directly. The names of routines that are general graphics engine services whose names begin with **Eng**. Service routines related to a particular object always start with the name of the object; for example, [**CLIPOBJ\_cEnumStart**](https://msdn.microsoft.com/library/windows/hardware/ff539421) is a [**CLIPOBJ**](https://msdn.microsoft.com/library/windows/hardware/ff539417) service.

**Note**   The service routines in which the first argument is a pointer to a user object are methods on that user object, and are called using the usual C++ conventions. Therefore, drivers written in C++ can access the service routines as methods.

 

These service routines fall into the following categories:

[Surface management](gdi-support-for-surfaces.md)

[Palette services](gdi-support-for-palettes.md)

[Path services](gdi-services-for-paths.md)

[Window services](gdi-support-for-window-objects.md)

[Rendering services](gdi-drawing-and-related-services.md)

[Font and text services](gdi-font-and-text-services.md)

[Memory services](gdi-memory-services.md)

[Event services](gdi-event-services.md)

[File, Module, and Process services](gdi-file--module--and-process-services.md)

[Semaphore services](gdi-semaphore-services.md)

[Printer services](gdi-printer-services.md)

[Driver-related services](gdi-driver-related-services.md)

[Information services](gdi-information-services.md)

[Utility services](gdi-utility-services.md)

[Floating-point services](gdi-floating-point-services.md)

[Halftone services](gdi-halftone-services.md)

[Using the Graphics DDI](using-the-graphics-ddi.md) describes the graphics DDI entry points and also explains where many of these service routines can be used to help the driver implement the entry points. For detailed descriptions of each of the service functions, see [GDI Functions Called by Printer and Display Drivers](https://msdn.microsoft.com/library/windows/hardware/ff566544).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20GDI%20Support%20Services%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




