---
title: Storage Volumes
description: Storage Volumes
ms.assetid: 37b65bb6-7c62-47be-a16d-3813dc4c1259
keywords:
- filter drivers WDK file system , storage volumes
- file system filter drivers WDK , storage volumes
- storage volumes WDK file system
- Mount Manager WDK file system
- storage device objects WDK file system
- volumes WDK file system , parameter blocks
- VPBs WDK file system
- volumes WDK file system , about storage volumes
- logical volumes WDK file system
- partitions WDK file system
- unique volume names WDK file system
- GUIDs WDK file system
- names WDK file systems
- Unique Volume Name
- Volume GUID
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Storage Volumes


## <span id="ddk_storage_volumes_if"></span><span id="DDK_STORAGE_VOLUMES_IF"></span>


A *volume* is a storage device, such as a fixed disk, floppy disk, or CD-ROM, that is formatted to store directories and files. A large volume can be divided into more than one *logical volume*, also called a *partition*. Each logical volume is formatted for use by a particular media-based file system, such as NTFS, FAT, or CDFS.

A *storage volume*, or *storage device object*, is a device object − usually a physical device object (PDO) − that represents a logical volume to the system. The storage device object resides in the storage device stack, but it is not necessarily the topmost device object in the stack.

When a file system is mounted on a storage volume, it creates a file system volume device object (VDO) to represent the volume to the file system. The file system VDO is mounted on the storage device object by means of a shared object called a *volume parameter block* (VPB).

### <span id="ddk_mount_manager_if"></span><span id="DDK_MOUNT_MANAGER_IF"></span>Mount Manager

The *Mount Manager* is the part of the I/O system that is responsible for managing storage volume information such as volume names, drive letters, and volume mount points. When a new storage volume is added to the system, the Mount Manager is notified of its arrival in either of the following ways:

-   The class driver that created the storage volume calls [**IoRegisterDeviceInterface**](https://msdn.microsoft.com/library/windows/hardware/ff549506) to register a new interface in the MOUNTDEV\_MOUNTED\_DEVICE\_GUID interface class. When this happens, the Plug and Play device interface notification mechanism alerts the Mount Manager of the volume's arrival in the system.

-   The driver for the storage volume sends the Mount Manager an IRP\_MJ\_DEVICE\_CONTROL request, specifying [**IOCTL\_MOUNTMGR\_VOLUME\_ARRIVAL\_NOTIFICATION**](https://msdn.microsoft.com/library/windows/hardware/ff560477) for the I/O control code. This request can be created by calling [**IoBuildDeviceIoControlRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548318).

### <span id="ddk_unique_volume_name_if"></span><span id="DDK_UNIQUE_VOLUME_NAME_IF"></span>Unique Volume Name

The Mount Manager responds to the arrival of a new storage volume by querying the volume driver for the following information:

-   The volume's nonpersistent device object name (or target name), located in the **Device** directory of the system object tree (for example: "\\Device\\HarddiskVolume1")

-   The volume's globally unique identifier (GUID), also called the *unique volume name*

-   A suggested persistent symbolic link name for the volume, such as a drive letter (for example, "\\DosDevices\\D:")

For more information about the interaction between storage drivers and the Mount Manager, see [Supporting Mount Manager Requests in a Storage Class Driver](https://msdn.microsoft.com/library/windows/hardware/ff567603).

 

 




