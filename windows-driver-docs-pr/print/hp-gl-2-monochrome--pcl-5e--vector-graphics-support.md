---
title: HP-GL/2 Monochrome (PCL-5e) Vector Graphics Support
description: HP-GL/2 Monochrome (PCL-5e) Vector Graphics Support
ms.assetid: 00a8704c-c7aa-4ecd-9c99-03ef6c75574d
keywords: ["vector graphics WDK Unidrv , HP-GL/2 monochrome", "HP-GL/2 monochrome WDK Unidrv", "PCL-5e WDK Unidrv", "HP-GL/2 monochrome WDK Unidrv , about HP-GL/2 monochrome", "monochrome vector graphics WDK Unidrv", "PCL-5e WDK Unidrv , about PCL-5e"]
---

# HP-GL/2 Monochrome (PCL-5e) Vector Graphics Support


## <a href="" id="ddk-hp-gl-2-monochrome-pcl-5e-vector-graphics-support-gg"></a>


HP-GL/2 monochrome (PCL-5e) vector graphics support in Unidrv running on Windows XP and later allows the printer driver to create job data in a format that is optimal for the device: vector graphics versus raster graphics. This normally results in less system overhead, less output data to transmit, and faster print throughput.

HP-GL/2 uses most of the currently-defined GPD features for job setup, page setup, media selection, and paper size. The actual drawing commands are hard-coded in the driver.

The following topics are covered:

[Enabling HP-GL/2 Vector Graphics Support (PCL-5e) in the GPD](enabling-hp-gl-2-vector-graphics-support--pcl-5e--in-the-gpd.md)

[Halftone Algorithms](halftone-algorithms.md)

[HP-GL/2 Supported Fonts](hp-gl-2-supported-fonts.md)

[HP-GL/2 Caveats](hp-gl-2-caveats.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20HP-GL/2%20Monochrome%20%28PCL-5e%29%20Vector%20Graphics%20Support%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




