---
title: File System Filter Drivers Are Not Device Drivers
author: windows-driver-content
description: File System Filter Drivers Are Not Device Drivers
ms.assetid: 4a1b2470-0062-4241-952d-ea9351b1a2f9
keywords: ["filter drivers WDK file system , vs. device drivers", "file system filter drivers WDK , vs. device drivers", "device drivers WDK file system"]
---

# File System Filter Drivers Are Not Device Drivers


## <span id="ddk_a_file_system_filter_driver_is_not_a_device_driver_if"></span><span id="DDK_A_FILE_SYSTEM_FILTER_DRIVER_IS_NOT_A_DEVICE_DRIVER_IF"></span>


A *device driver* is a software component that controls a particular hardware I/O device. For example, a DVD storage driver controls a DVD drive.

In contrast, a file system filter driver works in conjunction with one or more file systems to manage file I/O operations. These operations include creating, opening, closing, and enumerating files and directories; getting and setting file, directory, and volume information; and reading and writing file data. In addition, file system filter drivers must support file system-specific features such as caching, locking, sparse files, disk quotas, compression, security, recoverability, reparse points, and volume mount points.

For more details on the similarities and differences between file system filter drivers and device drivers, see the following:

[How File System Filter Drivers Are Similar to Device Drivers](how-file-system-filter-drivers-are-similar-to-device-drivers.md)

[How File System Filter Drivers Are Different from Device Drivers](how-file-system-filter-drivers-are-different-from-device-drivers.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20File%20System%20Filter%20Drivers%20Are%20Not%20Device%20Drivers%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


