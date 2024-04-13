---
title: Filtering Raster Data
description: Filtering Raster Data
keywords:
- Unidrv, raster data filtering
- GPD files WDK Unidrv , raster data filtering
- filtering raster data WDK print
- raster data filtering WDK Unidrv
- postprocessing scan line data stream WDK Unidrv
- Unidrv WDK print
ms.date: 01/27/2023
---

# Filtering Raster Data

[!include[Print Support Apps](../includes/print-support-apps.md)]

If you want to provide customized postprocessing of the scan line data stream before it is spooled, you can do so by implementing the [**IPrintOemUni::FilterGraphics**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-filtergraphics) method in a [rendering plug-in](rendering-plug-ins.md). There are no GPD file entries associated with this Unidrv feature.

For more information, see [Customized Data Stream Filtering](customized-data-stream-filtering.md).
