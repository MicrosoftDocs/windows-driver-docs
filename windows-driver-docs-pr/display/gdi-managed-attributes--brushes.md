---
title: GDI-Managed Attributes Brushes
description: GDI-Managed Attributes Brushes
ms.assetid: 8ca38ba1-824d-45be-9039-13222d3400c3
keywords:
- GDI WDK Windows 2000 display , rendering engine
- graphics drivers WDK Windows 2000 display , rendering engine
- drawing WDK GDI , rendering engine
- rendering engine WDK GDI
- GDI WDK Windows 2000 display , patterns
- graphics drivers WDK Windows 2000 display , patterns
- patterns WDK GDI
- brushes WDK GDI
- realizing brushes WDK GDI
- drawing WDK GDI , brushes
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# GDI-Managed Attributes: Brushes


## <span id="ddk_gdi_managed_attributes_brushes_gg"></span><span id="DDK_GDI_MANAGED_ATTRIBUTES_BRUSHES_GG"></span>


GDI also manages all attributes. GDI passes attributes to the driver as brushes; the driver *realizes* these brushes by converting them to a useful internal form. GDI maintains this converted information for the driver. GDI also maintains all states of the brushes, including bounds, correlation, current position, and line style. The driver can cache information but is not assumed to maintain any state. Except for initialization and brush realization, GDI calls the driver only to draw on the device. GDI takes care of transformations, region locking, and [*pointer exclusion*](https://msdn.microsoft.com/library/windows/hardware/ff556325#wdkgloss-pointer-exclusion) before it calls the driver.

Whenever a driver needs to use a brush not yet realized, it calls back to GDI. GDI allocates memory for the brush and calls the driver to realize it and, if necessary, dither it.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20GDI-Managed%20Attributes:%20Brushes%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




