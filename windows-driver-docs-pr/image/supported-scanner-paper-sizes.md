---
title: Supported Scanner Paper Sizes
description: Supported Scanner Paper Sizes
ms.assetid: c4437c38-b43a-433c-913a-d3de9bf74284
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Supported Scanner Paper Sizes





Although two WIA user interface components are able to display a list of page sizes to the user, there is no easy way for a WIA driver to know which page sizes a scanner supports.

### Page Size in WIA Applications

There are no WIA properties that allow WIA drivers to report supported page sizes or that allow applications to specify page size directly. To communicate page size settings to a driver, an application must calculate the required size in dots per inch (dpi) and adjust the origin of the scan to conform with the registration requirements of the device.

### <a href="" id="page-size-in-the-common-scanner-dialog-and-in-the-scanner-and-camera-w"></a>Page Size in the Common Scanner Dialog and in the Scanner and Camera Wizard

Both the Common Scanner Dialog and the Scanner and Camera Wizard have a static table of supported page sizes in which each page size is described by its horizontal width and vertical height, both in increments of 0.001 inch. These page sizes are currently displayed only when the scanner is in document feeder mode.

The largest page size (by area) that a driver supports in page feed mode, as determined by the maximum bed size, is considered the default page size. Paper sizes that do not fit on the feeder or on the bed of the device are not offered to the user.

 

 




