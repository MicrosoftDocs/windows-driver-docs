---
title: GDI Service Routines
description: GDI Service Routines
ms.assetid: ca4fbb84-33a8-498f-8549-c8aaf87429fd
keywords:
- GDI WDK Windows 2000 display , service routines
- graphics drivers WDK Windows 2000 display , service routines
- drawing WDK GDI , service routines
- service routines WDK GDI
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# GDI Service Routines


## <span id="ddk_gdi_service_routines_gg"></span><span id="DDK_GDI_SERVICE_ROUTINES_GG"></span>


GDI exports many service routines, whose names have the form **Eng***Xxx*. The driver dynamically links to *win32k.sys* to directly access these routines. GDI service routines include surface management, rendering simulations, and path, palette, font, and text services. These services are discussed in detail in [GDI Support Services](gdi-support-services.md).

 

 





