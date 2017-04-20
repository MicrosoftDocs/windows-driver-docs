---
title: GDI as a Graphics Language for Applications
description: GDI as a Graphics Language for Applications
ms.assetid: fc824284-0400-47b0-ac4e-ff21e1e0ded9
keywords:
- GDI WDK Windows 2000 display , graphics language for applications
- graphics drivers WDK Windows 2000 display , graphics language for applications
- drawing WDK GDI , graphics language for applications
- graphics language for applications WDK GDI
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# GDI as a Graphics Language for Applications


## <span id="ddk_gdi_as_a_graphics_language_for_applications_gg"></span><span id="DDK_GDI_AS_A_GRAPHICS_LANGUAGE_FOR_APPLICATIONS_GG"></span>


Both the Win32 GDI and the graphics engine are completely device-independent. Consequently, applications do not need to access the hardware directly. Based on an application graphics request, GDI works in conjunction with device-dependent graphics drivers to provide high quality graphics output for an array of graphics devices. The same GDI code paths are used for both printing and display devices.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20GDI%20as%20a%20Graphics%20Language%20for%20Applications%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




