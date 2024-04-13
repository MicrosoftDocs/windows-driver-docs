---
title: Installing a File System Filter Driver
description: Installing a File System Filter Driver
keywords:
- filter drivers WDK file system , installing
- file system filter drivers WDK , installing
- INF files WDK file system
- INF files WDK file system , about file system filter driver installs
ms.date: 02/23/2023
---

# Installing a File System Filter Driver

> [!NOTE]
> For optimal reliability and performance, use [file system minifilter drivers](./filter-manager-concepts.md) with Filter Manager support instead of legacy file system filter drivers. To port your legacy driver to a minifilter driver, see [Guidelines for Porting Legacy Filter Drivers](guidelines-for-porting-legacy-filter-drivers.md).

For Microsoft Windows XP and later operating systems, install your legacy file system filter drivers by using an INF file and an installation application. (On Windows 2000 and earlier operating systems, the Service Control Manager commonly installed filter drivers.)

INF-based installation must meet Windows Hardware Certification Kit requirements for file system filter drivers. "INF-based installation" means only that you need to use an INF file to copy files and to store information in the registry. You aren't required to install your entire product by using only an INF file, nor are you required to provide a ["right-click install"](using-an-inf-file-to-install-a-file-system-filter-driver.md) option for your driver.

This section includes:

[Creating an INF File for a File System Filter Driver](creating-an-inf-file-for-a-file-system-filter-driver.md)

[Load Order Groups for File System Filter Drivers](load-order-groups-for-file-system-filter-drivers.md)

[File System Filter Driver Classes and Class GUIDs](file-system-filter-driver-classes-and-class-guids.md)

[Using an INF File to Install a File System Filter Driver](using-an-inf-file-to-install-a-file-system-filter-driver.md)

[Using an INF File to Uninstall a File System Filter Driver](using-an-inf-file-to-uninstall-a-file-system-filter-driver.md)
