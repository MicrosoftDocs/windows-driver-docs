---
title: About File System Drivers
description: About File System Drivers
ms.assetid: a64d83c6-d4cd-432d-bc1a-a3ff4656527c
keywords:
- drivers WDK file system
- file system drivers WDK
ms.date: 10/16/2019
ms.localizationpriority: medium
---

# About File System Drivers

In almost all situations, developing a full file system driver is not necessary. If you do decide to develop a new file system driver:

- The  [*fastfat* sample](https://docs.microsoft.com/windows-hardware/drivers/samples/file-system-driver-samples) is available for you to use as a model.

- To learn how to create and install a file system driver, see [Creating an INF File for a File System Driver](creating-an0inf-file-for-a-file-system-driver.md).

The WDK does not provide conceptual documentation for file system development.

Most file system-related development on Windows involves the creation of a [file system minifilter driver](file-system-minifilter-drivers.md) (or a [file system legacy filter driver](file-system-legacy-filter-drivers.md)).
