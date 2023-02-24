---
title: Attaching a Filter to a File System or Volume
description: Attaching a Filter to a File System or Volume
keywords:
- filter drivers WDK file system , attaching filters
- file system filter drivers WDK , attaching filters
- attaching filters to file system or volume
- volumes WDK file system , attaching filters
ms.date: 02/23/2023
---

# Attaching a Filter to a File System or Volume

> [!NOTE]
> For optimal reliability and performance, use [file system minifilter drivers](./filter-manager-concepts.md) with Filter Manager support instead of legacy file system filter drivers. To port your legacy driver to a minifilter driver, see [Guidelines for Porting Legacy Filter Drivers](guidelines-for-porting-legacy-filter-drivers.md).

A legacy file system filter driver attaches itself to one or more mounted volumes and filters all I/O operations on them. But how does it determine which volumes to attach itself to? The sample filter drivers in the Windows Driver Kit (WDK) illustrate the two most common ways in which attachment is done:

- The end user can specify the volumes to filter by, for example, typing in the drive letters for the volumes. The end user's commands are relayed to the filter driver as a private [**IRP_MJ_DEVICE_CONTROL**](./irp-mj-device-control.md) request.

- The file system filter driver can attach to one or more file system drivers, listen for [**IRP_MJ_FILE_SYSTEM_CONTROL**](./irp-mj-file-system-control.md), IRP_MN_MOUNT_VOLUME requests, and attach to volumes as they're mounted.

You should generally assume that the mapping of volumes to drive letters is one-to-many, not one-to-one. This mapping is because of advanced storage features, such as dynamic volumes and volume mount points.

You shouldn't assume that the file system always handles IRP_MN_MOUNT_VOLUME requests synchronously. For example, a floppy drive may be mounted asynchronously if there's no floppy disk in the drive. Thus your filter driver should be prepared to propagate the **PendingReturned** flag in its mount completion routine. For more information, see [Checking the PendingReturned Flag](checking-the-pendingreturned-flag.md).

File system filter drivers can attach to, and filter I/O for, any file system volume. They can't attach directly to storage devices, such as disk drives or partitions. Also, they can't attach to individual directories or files.

For more information, see the following articles:

[Creating the Filter Device Object](creating-the-filter-device-object.md)

[Attaching the Filter Device Object to the Target Device Object](attaching-the-filter-device-object-to-the-target-device-object.md)

[Propagating the DO_BUFFERED_IO and DO_DIRECT_IO Flags](propagating-the-do-buffered-io-and-do-direct-io-flags.md)

[Propagating the FILE_DEVICE_SECURE_OPEN Flag](propagating-the-file-device-secure-open-flag.md)

[Clearing the DO_DEVICE_INITIALIZING Flag](clearing-the-do-device-initializing-flag.md)
