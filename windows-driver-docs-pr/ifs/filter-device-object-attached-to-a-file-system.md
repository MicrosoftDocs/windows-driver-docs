---
title: Filter Device Object Attached to a File System
description: Filter Device Object Attached to a File System
keywords:
- filter device objects WDK file system
- device object I/O requests WDK file system
- filter drivers WDK file system , device object I/O requests
- file system filter drivers WDK , device object I/O requests
ms.date: 02/23/2023
---

# Filter Device Object Attached to a File System

> [!NOTE]
> For optimal reliability and performance, use [file system minifilter drivers](./filter-manager-concepts.md) with Filter Manager support instead of legacy file system filter drivers. To port your legacy driver to a minifilter driver, see [Guidelines for Porting Legacy Filter Drivers](guidelines-for-porting-legacy-filter-drivers.md).

To filter an entire file system, a legacy file system filter driver creates a filter device object and attaches it above a file system driver's CDO in the global file system queue.

## Types of I/O Requests That Are Sent to a File System

A filter device object that is attached above a file system can generally expect to receive the following types of I/O requests:

[**IRP_MJ_DEVICE_CONTROL**](./irp-mj-device-control.md)

[**IRP_MJ_FILE_SYSTEM_CONTROL**](./irp-mj-file-system-control.md)

[**IRP_MJ_SHUTDOWN**](./irp-mj-shutdown.md)

If the file system supports opening handles to its control device object, filters can expect to see the following types of I/O requests as well:

[**IRP_MJ_CLEANUP**](./irp-mj-cleanup.md)

[**IRP_MJ_CLOSE**](./irp-mj-close.md)

[**IRP_MJ_CREATE**](./irp-mj-create.md)

File system filter device objects attached to file systems must pass all unrecognized or unwanted IRPs to the next-lower driver on the driver stack by default.
