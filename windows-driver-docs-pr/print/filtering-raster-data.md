---
title: Filtering Raster Data
author: windows-driver-content
description: Filtering Raster Data
ms.assetid: 179a2dc0-8794-4934-99b9-eb3f7900536c
keywords: ["Unidrv, raster data filtering", "GPD files WDK Unidrv , raster data filtering", "filtering raster data WDK print", "raster data filtering WDK Unidrv", "postprocessing scan line data stream WDK Unidrv", "Unidrv WDK print"]
---

# Filtering Raster Data


## <a href="" id="ddk-filtering-raster-data-gg"></a>


If you want to provide customized postprocessing of the scan line data stream before it is spooled, you can do so by implementing the [**IPrintOemUni::FilterGraphics**](https://msdn.microsoft.com/library/windows/hardware/ff554252) method in a [rendering plug-in](rendering-plug-ins.md). There are no GPD file entries associated with this Unidrv feature.

For more information, see [Customized Data Stream Filtering](customized-data-stream-filtering.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Filtering%20Raster%20Data%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


