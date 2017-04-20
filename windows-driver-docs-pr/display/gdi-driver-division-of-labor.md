---
title: GDI/Driver Division of Labor
description: GDI/Driver Division of Labor
ms.assetid: 280addc6-3fc2-4763-ba87-5e9c5e83d22e
keywords:
- GDI WDK Windows 2000 display , driver division of labor
- graphics drivers WDK Windows 2000 display , driver division of labor
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# GDI/Driver Division of Labor


## <span id="ddk_gdi_2f_driver_division_of_labor_gg"></span><span id="DDK_GDI_2F_DRIVER_DIVISION_OF_LABOR_GG"></span>


To understand graphics driver design, it is important to understand the roles of GDI and the driver, and how they negotiate. GDI, with its enhanced capabilities, can handle many operations that previously required a graphics driver. GDI also has the responsibility of managing data structures critical to graphics operations, such as surfaces, although each graphics driver must have access to them.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20GDI/Driver%20Division%20of%20Labor%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




