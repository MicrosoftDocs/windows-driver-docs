---
title: Storage Device Stacks, Storage Volumes, and File System Stacks
description: Storage Device Stacks, Storage Volumes, and File System Stacks
keywords:
- storage devices WDK file system
- stacks WDK file system
- device objects WDK file system
- volumes WDK file system
ms.date: 10/16/2019
ms.localizationpriority: medium
---

# Storage Device Stacks, Storage Volumes, and File System Stacks

> [!NOTE]
> For optimal reliability and performance, use [file system minifilter drivers](./filter-manager-concepts.md) with Filter Manager support instead of legacy file system filter drivers. To port your legacy driver to a minifilter driver, see [Guidelines for Porting Legacy Filter Drivers](guidelines-for-porting-legacy-filter-drivers.md).

Before exploring how file system legacy filter drivers attach to file systems and volumes, it is necessary to understand the relationship between storage device stacks, storage volumes, and file system stacks.

## Storage Device Stacks

Most storage drivers are PnP device drivers, which are loaded and managed by the PnP Manager. Storage devices are represented in the PnP *device tree*, which contains a device node, or *devnode*, for every physical or logical device on the machine. It is important to note that file systems and file system filter drivers are not PnP device drivers; thus the PnP [device tree](../kernel/device-tree.md) contains no devnodes for them.

The devnode for a particular storage device contains the *storage device stack* for the device; this is the chain of attached device objects that represent the device's storage device drivers. Because a storage device, such as a disk, might contain one or more logical volumes (partitions or dynamic volumes), the storage device stack itself often looks more like a tree than a stack. The root of this tree is a functional device object (FDO) for a storage adapter or for another device stack that is integrated with the storage stack. The leaves of this tree are the physical device objects (PDOs) for the logical volumes, also called *storage volumes*, on which file system volumes can be mounted.

For diagrams and descriptions of some typical storage device stacks, see the following sections of the Storage Devices Design Guide:

- [Device Object Example for a SCSI HBA](../storage/device-object-example-for-a-scsi-hba.md)

- [Device Object Example for an IEEE 1394 Controller](../storage/device-object-example-for-an-ieee-1394-controller.md)

## Storage Volumes

A *volume* is a storage device, such as a fixed disk, floppy disk, or CD-ROM, that is formatted to store directories and files. A large volume can be divided into more than one *logical volume*, also called a *partition*. Each logical volume is formatted for use by a particular media-based file system, such as NTFS, FAT, or CDFS.

A *storage volume*, or *storage device object*, is a device object − usually a physical device object (PDO) − that represents a logical volume to the system. The storage device object resides in the storage device stack, but it is not necessarily the topmost device object in the stack.

When a file system is mounted on a storage volume, it creates a file system volume device object (VDO) to represent the volume to the file system. The file system VDO is mounted on the storage device object by means of a shared object called a *volume parameter block* (VPB).

### Mount Manager

The *Mount Manager* is the part of the I/O system that is responsible for managing storage volume information such as volume names, drive letters, and volume mount points. When a new storage volume is added to the system, Mount Manager is notified of its arrival in either of the following ways:

- The class driver that created the storage volume calls [**IoRegisterDeviceInterface**](/windows-hardware/drivers/ddi/content/wdm/nf-wdm-ioregisterdeviceinterface) to register a new interface in the MOUNTDEV_MOUNTED_DEVICE_GUID interface class. When this happens, the Plug and Play device interface notification mechanism alerts the Mount Manager of the volume's arrival in the system.

- The driver for the storage volume sends the Mount Manager an IRP_MJ_DEVICE_CONTROL request, specifying [**IOCTL_MOUNTMGR_VOLUME_ARRIVAL_NOTIFICATION**](/windows-hardware/drivers/ddi/content/mountmgr/ni-mountmgr-ioctl_mountmgr_volume_arrival_notification) for the I/O control code. This request can be created by calling [**IoBuildDeviceIoControlRequest**](/windows-hardware/drivers/ddi/content/wdm/nf-wdm-iobuilddeviceiocontrolrequest).

### Unique Volume Name

Mount Manager responds to the arrival of a new storage volume by querying the volume driver for the following information:

- The volume's nonpersistent device object name (or target name), located in the **Device** directory of the system object tree (for example: "\Device\HarddiskVolume1")

- The volume's globally unique identifier (GUID), also called the *unique volume name*

- A suggested persistent symbolic link name for the volume, such as a drive letter (for example, "\DosDevices\D:")

For more information about the interaction between storage drivers and Mount Manager, see [Supporting Mount Manager Requests in a Storage Class Driver](../storage/supporting-mount-manager-requests-in-a-storage-class-driver.md).

## File System Stacks

File system drivers create two different types of device objects: control device objects (CDO) and volume device objects (VDO). A *file system stack* consists of one of these device objects, together with any filter device objects for file system filter drivers that are attached to it. The file system's device object always forms the bottom of the stack.

### File System CDOs

File system CDOs represent entire file systems, rather than individual volumes, and are stored in the global file system queue. A file system creates one or more named CDOs in its **DriverEntry** routine. For example, FastFat creates two CDOs: one for fixed media and one for removable media. CDFS creates only one CDO, because it has only removable media.

File system CDOs are required to be named. This is because file system filter drivers, as well as many kernel-mode support routines, rely on this difference between VDOs and CDOs as a way of telling them apart.

### File System VDOs

File system VDOs represent volumes mounted by file systems. A file system creates a VDO when it mounts a volume, usually in response to a volume mount request. Unlike a CDO, a VDO is always associated with a specific logical or physical storage device.

> [!NOTE]
> Unlike CDOs, VDOs must never be named, because naming a volume device object would create a security hole.
