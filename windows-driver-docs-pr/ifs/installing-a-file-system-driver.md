---
title: Installing a File System Driver
description: Installing a File System Driver
ms.assetid: 1297b565-ac85-4248-927a-ab91b6cb3ab0
keywords:
- drivers WDK file system , installing
- file system drivers WDK , installing
- INF files WDK file system
- INF files WDK file system , about file system driver installation
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Installing a File System Driver


## <span id="ddk_installing_a_file_system_filter_driver_if"></span><span id="DDK_INSTALLING_A_FILE_SYSTEM_FILTER_DRIVER_IF"></span>


For Microsoft Windows XP and later operating systems, you should install your file system drivers by using an INF file and an installation application. (On Microsoft Windows 2000 and earlier operating systems, file system drivers were commonly installed by the Service Control Manager.)

In the future, INF-based installation is expected to meet Windows Hardware Certification Kit requirements for file system drivers. Note that "INF-based installation" means only that you will need to use an INF file to copy files and to store information in the registry. You will not be required to install your entire product by using only an INF file, and you will not be required to provide a ["right-click install"](using-an-inf-file-to-install-a-file-system-filter-driver.md) option for your driver.

This section includes:

[Creating an INF File for a File System Driver](creating-an-inf-file-for-a-file-system-driver.md)

The following sections in the [File System Filter Drivers](file-system-filter-drivers.md) section regarding installing and uninstalling file system filter drivers is also applicable to file system drivers.

[Using an INF File to Install a File System Filter Driver](using-an-inf-file-to-install-a-file-system-filter-driver.md)

[Using an INF File to Uninstall a File System Filter Driver](using-an-inf-file-to-uninstall-a-file-system-filter-driver.md)

 

 




