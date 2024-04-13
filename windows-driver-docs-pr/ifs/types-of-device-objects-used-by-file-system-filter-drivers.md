---
title: Types of Device Objects Used by File System Filter Drivers
description: Types of Device Objects Used by File System Filter Drivers
keywords:
- target device objects WDK file system
- filter device objects WDK file system
- device objects WDK file system
- control device objects WDK file system
- CDOs WDK file system
- FDOs WDK file system
ms.date: 02/23/2023
---

# Types of Device Objects Used by File System Filter Drivers

> [!NOTE]
> For optimal reliability and performance, use [file system minifilter drivers](./filter-manager-concepts.md) with Filter Manager support instead of legacy file system filter drivers. To port your legacy driver to a minifilter driver, see [Guidelines for Porting Legacy Filter Drivers](guidelines-for-porting-legacy-filter-drivers.md).

To write effective dispatch routines for IRPs and fast I/O requests, it's important to understand the various types of target device objects through which your legacy filter driver can receive these requests.

Unlike drivers for Plug and Play (PnP) devices, such as disk drives, file system filter drivers don't create functional or physical device objects. Instead, they create control device objects and filter device objects. The *control device object* (CDO) represents the filter driver to the system and to user-mode applications. The *filter device object* (filter DO) performs the actual work of filtering a specific file system or volume. A file system filter driver normally creates one CDO and one or more filter DOs.

For each type of I/O request received by your filter driver, the target device object can be one or more of the following objects:

- The filter driver's CDO, which isn't attached to a driver stack

- A filter device object that is chained above a file system CDO in the global file system queue

- A filter device object that is chained above a mounted file system volume device object (VDO)

A filter driver can register only one set of dispatch routines for IRPs and one for fast I/O requests. Thus, a single routine must handle each type of request. This routine must ascertain which of the target device objects listed above received the request, so that it can handle the request appropriately.

This section includes:

[The Filter Driver's Control Device Object](the-filter-driver-s-control-device-object.md)

[Filter Device Object Attached to a File System](filter-device-object-attached-to-a-file-system.md)

[Filter Device Object Attached to a Volume](filter-device-object-attached-to-a-volume.md)
