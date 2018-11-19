---
title: How File System Filter Drivers Are Similar to Device Drivers
description: How File System Filter Drivers Are Similar to Device Drivers
ms.assetid: 7797239e-e0cc-4422-bcc6-31cfe6efd8e4
keywords:
- filter drivers WDK file system , vs. device drivers
- file system filter drivers WDK , vs. device drivers
- device drivers WDK file system
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# How File System Filter Drivers Are Similar to Device Drivers


## <span id="ddk_how_file_system_filter_drivers_are_similar_to_device_drivers_if"></span><span id="DDK_HOW_FILE_SYSTEM_FILTER_DRIVERS_ARE_SIMILAR_TO_DEVICE_DRIVERS_IF"></span>


The following subsections describe some of the similarities between file system filter drivers and device drivers in the Microsoft Windows operating system.

### <span id="Similar_Structure"></span><span id="similar_structure"></span><span id="SIMILAR_STRUCTURE"></span>Similar Structure

Like device drivers, file system filter drivers have [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113), [dispatch](https://msdn.microsoft.com/library/windows/hardware/ff566407), and [I/O completion](https://msdn.microsoft.com/library/windows/hardware/ff565398) routines. They call many of the same kernel-mode routines that device drivers call, and they filter I/O requests for devices (that is, file system volumes) with which they are associated.

### <span id="Similar_Functionality"></span><span id="similar_functionality"></span><span id="SIMILAR_FUNCTIONALITY"></span>Similar Functionality

Because file system filter drivers and device drivers are part of the I/O system, they both receive [I/O request packets](https://msdn.microsoft.com/library/windows/hardware/ff558771) (IRPs) and act on them.

Like device drivers, file system filter drivers can also create their own IRPs and send them to lower-level drivers.

Both kinds of drivers can register for notification (by using callback functions) of various system events.

### <span id="Other_Similarities"></span><span id="other_similarities"></span><span id="OTHER_SIMILARITIES"></span>Other Similarities

Like device drivers, file system filter drivers can receive [Introduction to I/O Control Codes](https://msdn.microsoft.com/library/windows/hardware/ff548059) (IOCTLs). However, file system filter drivers can also receive--and define--[file system control codes](https://msdn.microsoft.com/library/windows/hardware/ff540367) (FSCTLs).

Like device drivers, file system filter drivers can be configured to be loaded at system startup time or to be loaded later, after the system startup process is complete.

 

 




