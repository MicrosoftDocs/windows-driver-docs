---
title: PCL XL (PCL-6) Vector Graphics Support
author: windows-driver-content
description: PCL XL (PCL-6) Vector Graphics Support
MS-HAID:
- 'nt5gpd\_0434c1a3-a6fd-4ade-aa84-e1c5c6050db9.xml'
- 'print.pcl\_xl\_\_pcl\_6\_\_vector\_graphics\_support'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: c8a96506-ed95-44f2-863e-24cbfc919d65
keywords: ["vector graphics WDK Unidrv , PCL XL", "PCL XL vector graphics WDK Unidrv", "PCL XL vector graphics WDK Unidrv , about PCL XL vector graphics", "PCL-6 WDK Unidrv"]
---

# PCL XL (PCL-6) Vector Graphics Support


## <a href="" id="ddk-pcl-xl-pcl-6-vector-graphics-support-gg"></a>


Unidrv in Windows XP and later supports PCL XL monochrome graphics. Unidrv in Windows Server 2003 and later supports PCL XL color graphics.

Unidrv's support for PCL XL (PCL-6) vector graphics allows it to create job data in PCL XL format as an alternative to pure raster format. PCL XL format is usually optimal for the device, and typically results in less system overhead, less output data, and faster print throughput.

PCL XL uses most of the currently-defined GPD features for job setup, page setup, media selection, and paper size. However, the actual drawing commands are hard-coded within Unidrv. Consequently, most drawing commands within GPD files are ignored. There is no need to remove these commands from the GPD file.

This section contains the following topics:

[Writing a PCL XL GPD File](writing-a-pcl-xl-gpd-file.md)

[Enabling Support for Color in PCL XL Minidrivers](enabling-support-for-color-in-pcl-xl-minidrivers.md)

[Specifying New Device Fonts in PCL XL Minidrivers](specifying-new-device-fonts-in-pcl-xl-minidrivers.md)

[Using Default PCL XL Fonts](using-default-pcl-xl-fonts.md)

[Installing a PCL XL Minidriver](installing-a-pcl-xl-minidriver.md)

[PCL XL Issues](pcl-xl-issues.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20PCL%20XL%20%28PCL-6%29%20Vector%20Graphics%20Support%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


