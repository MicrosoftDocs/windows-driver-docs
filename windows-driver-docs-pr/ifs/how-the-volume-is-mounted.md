---
title: How the Volume Is Mounted
description: How the Volume Is Mounted
keywords:
- filter drivers WDK file system , volume mount process
- file system filter drivers WDK , volume mount process
- mounting volumes WDK file systems
- volumes WDK file system , mounting
ms.date: 10/16/2019
---

# How the Volume Is Mounted

> [!NOTE]
> For optimal reliability and performance, use [file system minifilter drivers](./filter-manager-concepts.md) with Filter Manager support instead of legacy file system filter drivers. To port your legacy driver to a minifilter driver, see [Guidelines for Porting Legacy Filter Drivers](guidelines-for-porting-legacy-filter-drivers.md).

After [the volume has been recognized](how-the-volume-is-recognized.md), how the volume is mounted depends on the file system and whether it has previously mounted the volume.

When a file system receives the volume mount request for a new volume, it creates a volume device object (VDO) for the volume. The VDO consists of a DEVICE_OBJECT plus an optional file-system-defined device extension. The newly created VDO forms the base of the file system volume stack for the new (or remounted) volume.

The file system mounts the volume by associating the VDO with the volume parameter block (VPB) for the corresponding storage device object and sets the VPB_MOUNTED flag on the VPB.

After the volume is mounted by the file system, file system filter drivers can attach to the top of the new file system volume stack. Any I/O requests sent to the file system are automatically sent first to the file system filter device object at the top of the volume stack. However, file system filters should only detach from the volume stack when the I/O Manager sends a fast I/O detach request to notify drivers on the volume stack that the volume is about to be removed.

See [Volume Mount Example](volume-mount-example.md) for an example.

> [!NOTE]
> The storage device object for the volume resides in the storage device stack, but it is not necessarily the topmost device object in the stack. Moreover, even after the volume is mounted, storage filter drivers can still attach to the top of the storage stack. It is important for driver writers to keep in mind that, when the file system sends an IRP from the VDO to the storage device stack, it sends it to the storage device object for the volume, not the topmost device object in the stack. (However, when the I/O Manager sends an IRP directly to the storage stack, bypassing the file system, that IRP is sent to the topmost device object in the stack.)
