---
title: PCL XL (PCL-6) Vector Graphics Support
description: PCL XL (PCL-6) Vector Graphics Support
ms.assetid: c8a96506-ed95-44f2-863e-24cbfc919d65
keywords:
- vector graphics WDK Unidrv , PCL XL
- PCL XL vector graphics WDK Unidrv
- PCL XL vector graphics WDK Unidrv , about PCL XL vector graphics
- PCL-6 WDK Unidrv
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# PCL XL (PCL-6) Vector Graphics Support





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

 

 




