---
title: Filtering Raster Data
description: Filtering Raster Data
ms.assetid: 179a2dc0-8794-4934-99b9-eb3f7900536c
keywords:
- Unidrv, raster data filtering
- GPD files WDK Unidrv , raster data filtering
- filtering raster data WDK print
- raster data filtering WDK Unidrv
- postprocessing scan line data stream WDK Unidrv
- Unidrv WDK print
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Filtering Raster Data





If you want to provide customized postprocessing of the scan line data stream before it is spooled, you can do so by implementing the [**IPrintOemUni::FilterGraphics**](https://msdn.microsoft.com/library/windows/hardware/ff554252) method in a [rendering plug-in](rendering-plug-ins.md). There are no GPD file entries associated with this Unidrv feature.

For more information, see [Customized Data Stream Filtering](customized-data-stream-filtering.md).

 

 




