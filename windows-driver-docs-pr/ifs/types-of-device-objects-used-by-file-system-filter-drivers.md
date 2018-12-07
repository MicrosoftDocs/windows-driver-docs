---
title: Types of Device Objects Used by File System Filter Drivers
description: Types of Device Objects Used by File System Filter Drivers
ms.assetid: e5662c95-71a0-49f8-a9d5-a03e2de1f426
keywords:
- target device objects WDK file system
- filter device objects WDK file system
- device objects WDK file system
- control device objects WDK file system
- CDOs WDK file system
- FDOs WDK file system
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Types of Device Objects Used by File System Filter Drivers


## <span id="ddk_types_of_file_system_filter_driver_device_objects_if"></span><span id="DDK_TYPES_OF_FILE_SYSTEM_FILTER_DRIVER_DEVICE_OBJECTS_IF"></span>


To write effective dispatch routines for IRPs and fast I/O requests, it is important to understand the various types of target device objects through which your filter driver can receive these requests.

Unlike drivers for Plug and Play (PnP) devices, such as disk drives, file system filter drivers do not create functional or physical device objects. Instead, they create control device objects and filter device objects. The *control device object* (CDO) represents the filter driver to the system and to user-mode applications. The *filter device object* (filter DO) performs the actual work of filtering a specific file system or volume. A file system filter driver normally creates one CDO and one or more filter DOs.

For each type of I/O request received by your filter driver, the target device object can be one or more of the following:

-   The filter driver's CDO, which is not attached to a driver stack

-   A filter device object that is chained above a file system CDO in the global file system queue

-   A filter device object that is chained above a mounted file system volume device object (VDO)

A filter driver can register only one set of dispatch routines for IRPs and one for fast I/O requests. Thus, each type of request must be handled by a single routine. This routine must ascertain which of the target device objects listed above received the request, so that it can handle the request appropriately.

This section includes:

[The Filter Driver's Control Device Object](the-filter-driver-s-control-device-object.md)

[Filter Device Object Attached to a File System](filter-device-object-attached-to-a-file-system.md)

[Filter Device Object Attached to a Volume](filter-device-object-attached-to-a-volume.md)

 

 




