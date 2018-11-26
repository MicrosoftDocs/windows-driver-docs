---
title: Installing a Minifilter Driver
description: Installing a Minifilter Driver
ms.assetid: c31aa104-404e-43e3-9215-2671ae6b12c0
keywords:
- file system minifilter drivers WDK , installing
- minifilter drivers WDK , installing
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Installing a Minifilter Driver


For Microsoft Windows XP and later operating systems, you should install your minifilter driver by using an INF file and an installation application. (On Windows 2000 and earlier operating systems, minifilter drivers were commonly installed by the Service Control Manager.)

In the future, INF-based installation is expected to be necessary in order to meet Windows Hardware Certification Kit requirements for minifilter drivers. Note that "INF-based installation" means only that you will need to use an INF file to copy files and to store information in the registry. You will not be required to install your entire product by using only an INF file, and you will not be required to provide a ["right-click install"](using-an-inf-file-to-install-a-file-system-filter-driver.md) option for your driver.

This section includes:

[Creating an INF File for a Minifilter Driver](creating-an-inf-file-for-a-minifilter-driver.md)

[Load Order Groups and Altitudes for Minifilter Drivers](load-order-groups-and-altitudes-for-minifilter-drivers.md)

[Allocated Altitudes](allocated-altitudes.md)

[Minifilter Altitude Request](minifilter-altitude-request.md)

[Reparse Point Tag Request](reparse-point-tag-request.md)

 

 




