---
title: GDI/Driver Division of Labor
description: GDI/Driver Division of Labor
ms.assetid: 280addc6-3fc2-4763-ba87-5e9c5e83d22e
keywords:
- GDI WDK Windows 2000 display , driver division of labor
- graphics drivers WDK Windows 2000 display , driver division of labor
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# GDI/Driver Division of Labor


## <span id="ddk_gdi_2f_driver_division_of_labor_gg"></span><span id="DDK_GDI_2F_DRIVER_DIVISION_OF_LABOR_GG"></span>


To understand graphics driver design, it is important to understand the roles of GDI and the driver, and how they negotiate. GDI, with its enhanced capabilities, can handle many operations that previously required a graphics driver. GDI also has the responsibility of managing data structures critical to graphics operations, such as surfaces, although each graphics driver must have access to them.

 

 





