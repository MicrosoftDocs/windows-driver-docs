---
title: Supported Scanner Paper Sizes
author: windows-driver-content
description: Supported Scanner Paper Sizes
ms.assetid: c4437c38-b43a-433c-913a-d3de9bf74284
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Supported Scanner Paper Sizes


## <a href="" id="ddk-supported-scanner-paper-sizes-si"></a>


Although two WIA user interface components are able to display a list of page sizes to the user, there is no easy way for a WIA driver to know which page sizes a scanner supports.

### Page Size in WIA Applications

There are no WIA properties that allow WIA drivers to report supported page sizes or that allow applications to specify page size directly. To communicate page size settings to a driver, an application must calculate the required size in dots per inch (dpi) and adjust the origin of the scan to conform with the registration requirements of the device.

### <a href="" id="page-size-in-the-common-scanner-dialog-and-in-the-scanner-and-camera-w"></a>Page Size in the Common Scanner Dialog and in the Scanner and Camera Wizard

Both the Common Scanner Dialog and the Scanner and Camera Wizard have a static table of supported page sizes in which each page size is described by its horizontal width and vertical height, both in increments of 0.001 inch. These page sizes are currently displayed only when the scanner is in document feeder mode.

The largest page size (by area) that a driver supports in page feed mode, as determined by the maximum bed size, is considered the default page size. Paper sizes that do not fit on the feeder or on the bed of the device are not offered to the user.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Supported%20Scanner%20Paper%20Sizes%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


