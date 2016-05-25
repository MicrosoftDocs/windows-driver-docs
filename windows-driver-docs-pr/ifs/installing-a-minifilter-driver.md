---
title: Installing a Minifilter Driver
author: windows-driver-content
description: Installing a Minifilter Driver
ms.assetid: c31aa104-404e-43e3-9215-2671ae6b12c0
keywords: ["file system minifilter drivers WDK , installing", "minifilter drivers WDK , installing"]
---

# Installing a Minifilter Driver


For Microsoft Windows XP and later operating systems, you should install your minifilter driver by using an INF file and an installation application. (On Windows 2000 and earlier operating systems, minifilter drivers were commonly installed by the Service Control Manager.)

In the future, INF-based installation is expected meet Windows Hardware Certification Kit requirements for minifilter drivers. Note that "INF-based installation" means only that you will need to use an INF file to copy files and to store information in the registry. You will not be required to install your entire product by using only an INF file, and you will not be required to provide a ["right-click install"](using-an-inf-file-to-install-a-file-system-filter-driver.md) option for your driver.

This section includes:

[Creating an INF File for a Minifilter Driver](creating-an-inf-file-for-a-minifilter-driver.md)

[Load Order Groups and Altitudes for Minifilter Drivers](load-order-groups-and-altitudes-for-minifilter-drivers.md)

[Allocated Altitudes](allocated-altitudes.md)

[Minifilter Altitude Request](minifilter-altitude-request.md)

[Reparse Point Tag Request](reparse-point-tag-request.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Installing%20a%20Minifilter%20Driver%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


