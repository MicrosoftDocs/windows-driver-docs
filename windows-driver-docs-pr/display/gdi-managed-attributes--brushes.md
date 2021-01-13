---
title: GDI-Managed Attributes Brushes
description: GDI-Managed Attributes Brushes
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
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# GDI-Managed Attributes: Brushes


## <span id="ddk_gdi_managed_attributes_brushes_gg"></span><span id="DDK_GDI_MANAGED_ATTRIBUTES_BRUSHES_GG"></span>


GDI also manages all attributes. GDI passes attributes to the driver as brushes; the driver *realizes* these brushes by converting them to a useful internal form. GDI maintains this converted information for the driver. GDI also maintains all states of the brushes, including bounds, correlation, current position, and line style. The driver can cache information but is not assumed to maintain any state. Except for initialization and brush realization, GDI calls the driver only to draw on the device. GDI takes care of transformations, region locking, and *pointer exclusion* before it calls the driver.

Whenever a driver needs to use a brush not yet realized, it calls back to GDI. GDI allocates memory for the brush and calls the driver to realize it and, if necessary, dither it.

 

 





