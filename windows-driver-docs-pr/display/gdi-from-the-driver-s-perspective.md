---
title: GDI from the Driver's Perspective
description: GDI from the Driver's Perspective
ms.assetid: 2a6769ea-c6ae-4397-a5e4-f38964d2d8d1
keywords: ["GDI WDK Windows 2000 display , driver communication", "graphics drivers WDK Windows 2000 display , driver communication", "drawing WDK GDI , driver communication"]
---

# GDI from the Driver's Perspective


## <span id="ddk_gdi_from_the_driver_92_s_perspective_gg"></span><span id="DDK_GDI_FROM_THE_DRIVER_92_S_PERSPECTIVE_GG"></span>


GDI is the intermediary support between a Microsoft Windows NT-based graphics driver and an application. Applications call Microsoft Win32 GDI functions to make graphics output requests. These requests are routed to kernel-mode GDI. Kernel-mode GDI then sends these requests to the appropriate graphics driver, such as a display driver or printer driver. Kernel-mode GDI is a system-supplied module that cannot be replaced.

GDI communicates with the graphics driver through a set of graphics device driver interface (graphics DDI) functions. These functions are identified by their *Drv* prefix. Information is passed between GDI and the driver through the input/output parameters of these entry points. The driver *must* support certain *DrvXxx* functions for GDI to call. The driver supports GDI's requests by performing the appropriate operations on its associated hardware before returning to GDI.

GDI includes many graphics output capabilities in itself, eliminating the need for the driver to support these capabilities and thereby making it possible to reduce the size of the driver. GDI also exports service functions that the driver can call, further reducing the amount of support the driver must provide. GDI service functions are identified by their **Eng** prefix, and functions that provide access to GDI-maintained structures have names in the form *Xxx***OBJ*\_****Xxx*.

The following figure shows this flow of communication.

![diagram illustrating the graphics driver and graphics device interface (gdi) interaction](images/gditoddi.png)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20GDI%20from%20the%20Driver's%20Perspective%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




