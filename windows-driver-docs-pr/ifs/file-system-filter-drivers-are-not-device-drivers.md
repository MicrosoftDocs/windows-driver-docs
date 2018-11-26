---
title: File System Filter Drivers Are Not Device Drivers
description: File System Filter Drivers Are Not Device Drivers
ms.assetid: 4a1b2470-0062-4241-952d-ea9351b1a2f9
keywords:
- filter drivers WDK file system , vs. device drivers
- file system filter drivers WDK , vs. device drivers
- device drivers WDK file system
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# File System Filter Drivers Are Not Device Drivers


## <span id="ddk_a_file_system_filter_driver_is_not_a_device_driver_if"></span><span id="DDK_A_FILE_SYSTEM_FILTER_DRIVER_IS_NOT_A_DEVICE_DRIVER_IF"></span>


A *device driver* is a software component that controls a particular hardware I/O device. For example, a DVD storage driver controls a DVD drive.

In contrast, a file system filter driver works in conjunction with one or more file systems to manage file I/O operations. These operations include creating, opening, closing, and enumerating files and directories; getting and setting file, directory, and volume information; and reading and writing file data. In addition, file system filter drivers must support file system-specific features such as caching, locking, sparse files, disk quotas, compression, security, recoverability, reparse points, and volume mount points.

For more details on the similarities and differences between file system filter drivers and device drivers, see the following:

[How File System Filter Drivers Are Similar to Device Drivers](how-file-system-filter-drivers-are-similar-to-device-drivers.md)

[How File System Filter Drivers Are Different from Device Drivers](how-file-system-filter-drivers-are-different-from-device-drivers.md)

 

 




