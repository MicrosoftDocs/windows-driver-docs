---
title: About file system filter drivers
description: About file system filter drivers
keywords:
- filter drivers WDK file system , about file system filter drivers
- file system filter drivers WDK , about file system filter drivers
- what is a file system filter driver
- file system filter drivers are not device drivers
ms.date: 02/10/2020
ms.localizationpriority: medium
---

# About file system filter drivers

## File system filter drivers on Windows

A *file system filter driver* is an optional driver that adds value to or modifies the behavior of a file system. It is a kernel-mode component that runs as part of the Windows executive.

A file system filter driver can filter I/O operations for one or more file systems or file system volumes. Depending on the nature of the driver, *filter* can mean *log*, *observe*, *modify*, or even *prevent*. Typical applications for file system filter drivers include antivirus utilities, encryption programs, and hierarchical storage management systems.

There are two file system filter models in Windows:

- The [minifilter model](./filter-manager-concepts.md), in which a filter (also called a minifilter) uses system-supplied Filter Manager support, thus simplifying filter development

- The [legacy file system filter model](./about-file-system-legacy-filter-drivers.md)

> [!NOTE]
> For optimal reliability and performance, use [file system minifilter drivers](./filter-manager-concepts.md) with Filter Manager support instead of legacy file system filter drivers. To port your legacy driver to a minifilter driver, see [Guidelines for Porting Legacy Filter Drivers](guidelines-for-porting-legacy-filter-drivers.md).

## File system filter drivers are not device drivers

A *device driver* is a software component that controls a particular hardware I/O device. For example, a DVD storage driver controls a DVD drive.

In contrast, a *file system filter driver* works in conjunction with one or more file systems to manage file I/O operations. These operations include:

- Creating, opening, closing, and enumerating files and directories

- Getting and setting file, directory, and volume information

- Reading and writing file data

In addition, file system filter drivers must support file system-specific features such as caching, locking, sparse files, disk quotas, compression, security, recoverability, reparse points, and volume mount points.

For more details on the similarities and differences between file system filter drivers and device drivers, see the following:

- [How File System Filter Drivers Are Similar to Device Drivers](how-file-system-filter-drivers-are-similar-to-device-drivers.md)

- [How File System Filter Drivers Are Different from Device Drivers](how-file-system-filter-drivers-are-different-from-device-drivers.md)
