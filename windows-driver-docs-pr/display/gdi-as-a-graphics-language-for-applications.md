---
title: GDI as a Graphics Language for Applications
description: GDI as a Graphics Language for Applications
ms.assetid: fc824284-0400-47b0-ac4e-ff21e1e0ded9
keywords:
- GDI WDK Windows 2000 display , graphics language for applications
- graphics drivers WDK Windows 2000 display , graphics language for applications
- drawing WDK GDI , graphics language for applications
- graphics language for applications WDK GDI
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# GDI as a Graphics Language for Applications


## <span id="ddk_gdi_as_a_graphics_language_for_applications_gg"></span><span id="DDK_GDI_AS_A_GRAPHICS_LANGUAGE_FOR_APPLICATIONS_GG"></span>


Both the Win32 GDI and the graphics engine are completely device-independent. Consequently, applications do not need to access the hardware directly. Based on an application graphics request, GDI works in conjunction with device-dependent graphics drivers to provide high quality graphics output for an array of graphics devices. The same GDI code paths are used for both printing and display devices.

 

 





