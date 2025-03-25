---
title: About File System Filter Drivers
description: About file system filter drivers
keywords:
- filter drivers WDK file system , about file system filter drivers
- file system filter drivers WDK , about file system filter drivers
- what is a file system filter driver
- file system filter drivers are not device drivers
ms.date: 06/24/2024
ms.topic: concept-article
---

# About file system filter drivers

## File system filter drivers on Windows

File system filter drivers are optional drivers that attach to the file system software stack. They monitor, filter, and/or modify the behavior of file I/O operations. As kernel-mode components, they run as part of the Windows executive.

A file system filter driver can filter I/O operations for one or more file systems or file system volumes. Depending on the nature of the driver, *filter* can mean *log*, *observe*, *modify*, or even *prevent*. Typical applications for file system filter drivers include:

* Anti-virus/anti-malware utilities that scan files for viruses or malware on file creation, access, or modification.

* Data encryption programs that automatically encrypt and decrypt data being written to or read from disk.

* Backup filters used to create backups of data for disaster recovery and business continuity.

* Compression filters that compress and decompress data on the fly, which saves disk space and improves performance for large volumes of data.

* Hierarchical storage management filters that manage the migration of data between high- and low-cost storage media.

Each filter operates at a different level in the file system stack. Interoperability between minifilters is important to ensure that the filters work together correctly.

There are two file system filter models in Windows:

* The [minifilter model](./filter-manager-concepts.md), in which a *minifilter* uses system-supplied Filter Manager (*FltMgr*) support, thus simplifying filter development

* The [legacy file system filter model](./about-file-system-legacy-filter-drivers.md)

Filter developers should develop [file system minifilter drivers](./filter-manager-concepts.md) with Filter Manager support instead of legacy file system filter drivers. See [Guidelines for Porting Legacy Filter Drivers](guidelines-for-porting-legacy-filter-drivers.md) to port any remaining legacy filters to be minifilter drivers.

## File system filter drivers aren't device drivers

A *device driver* is a software component that controls a particular hardware I/O device. For example, a graphics driver can control video cards, GPUs/NPUs, monitors, and so forth.

In contrast, a *file system filter driver* works with one or more file systems to manage file I/O operations. These operations include:

* Creating, opening, closing, and enumerating files and directories

* Getting and setting file, directory, and volume information

* Reading and writing file data

In addition, file system filter drivers must support file system-specific features such as:

* Caching

* Locking

* Sparse files

* Disk quotas

* Compression

* Security

* Recoverability

* Reparse points

* Volume mount points

For more information, see the following articles:

* [How File System Filter Drivers Are Similar to Device Drivers](how-file-system-filter-drivers-are-similar-to-device-drivers.md)

* [How File System Filter Drivers Are Different from Device Drivers](how-file-system-filter-drivers-are-different-from-device-drivers.md)
