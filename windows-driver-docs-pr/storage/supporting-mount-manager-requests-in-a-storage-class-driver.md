---
title: Supporting Mount Manager Requests in a Storage Class Driver
description: Describes how to support Mount Manager requests in a Storage Class Driver
keywords:
- storage class drivers WDK , mount manager
- class drivers WDK storage , mount manager
- Mount Manager WDK storage
- MM WDK storage
- volume names WDK storage
- names WDK storage
- unique volume names WDK storage
- persistent name database WDK storage
- MountedDevices
- dead mounted devices WDK storage
- symbolic link names WDK storage
- nonpersistent names WDK storage
ms.date: 06/05/2024
---

# Supporting Mount Manager requests in a Storage Class Driver

The system-supplied mount manager is responsible for managing volume names. For each volume, it stores a name that is unique and permanently identified with the volume, even after the volume is removed from the system. It also manages less permanent names, like drive letters, that persist across reboots but whose assignments can change as volumes are added to or removed from the system.

The mount manager provides a unique interface to each volume in the system by creating a symbolic link to the volume's device object. Since the symbolic links themselves and the device objects they target don't persist when the system restarts, the mount manager preserves the *name* of the symbolic link in a *persistent name database* in the registry.

This symbolic link name is called a *unique volume name*. Like a traditional volume label, it persists when the system restarts. Like a drive letter and unlike a volume label, this name is unique. The format for unique volume names follows, where *GUID* is a globally unique identifier that identifies the volume.

"**\\??\\Volume{**<em>GUID</em>**}\\**

Mount manager's persistent name database is located in the **MountedDevices** registry key of the SYSTEM hive (**HKLM/SYSTEM/MountedDevices**) of the registry. In addition to unique volume names, the mount manager also stores *mount point* names in its persistent name database. Mount point names can be further subdivided into two categories: Win32-style pathnames that serve as the root directory of the mounted volume's file system, and drive letters.

Each persistent symbolic link name in the database appears as the name of a registry value under the **MountedDevices** key accompanied by a *unique ID*. The unique ID is another unique identifier of a volume (different from the unique volume name). It helps identify which of the potentially numerous persistent symbolic link names refer to the same volume.

For instance, a single volume with a unique volume name of **"\\\\?\\Volume{**7603f260-142a-11d4-ac67-806d6172696f **}\\"** might have an accompanying drive letter "\\DosDevices\\D:" and two mount points "\\DosDevices\\C:\\mymount" and "\\DosDevices\\E:\\FilesysD\\mnt". This combination would produce four entries in mount manager's persistent symbolic link name database: one for the unique volume name, one for the drive letter, and two for the two mount point names. All four entries would share the same unique ID. Thus someone viewing the **MountedDevices** registry key would be able to detect that all four persistent names point to the same volume.

The following screenshot illustrates how persistent names appear in the **MountedDevices** registry key.

![screen shot illustrating how persistent names appear in the mounteddevices registry key.](images/mntmgr.png)

The mount manager relies on the Plug and Play device interface notification mechanism to alert it of volume arrival and removal. Therefore every client (that is, every volume driver, usually a class driver) must create an interface in the MOUNTDEV_MOUNTED_DEVICE_GUID interface class by calling [**IoRegisterDeviceInterface**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioregisterdeviceinterface) to notify the mount manager of the arrival in the system of the volume it manages. The MOUNTDEV_MOUNTED_DEVICE_GUID interface class GUID is defined in *mountmgr.h*.

Upon receiving a Plug and Play notification of the arrival of a volume interface, mount manager sends the client three device control IRPs:

* [**IOCTL_MOUNTDEV_QUERY_DEVICE_NAME**](/windows-hardware/drivers/ddi/mountmgr/ni-mountmgr-ioctl_mountdev_query_device_name)
* [**IOCTL_MOUNTDEV_QUERY_UNIQUE_ID**](/windows-hardware/drivers/ddi/mountdev/ni-mountdev-ioctl_mountdev_query_unique_id)
* [**IOCTL_MOUNTDEV_QUERY_SUGGESTED_LINK_NAME**](/windows-hardware/drivers/ddi/mountdev/ni-mountdev-ioctl_mountdev_query_suggested_link_name)

In response to these three IOCTLs the client should return the volume's non-persistent device object name (or target name) located in the **Device** directory of the system object tree (for example: "\\Device\\HarddiskVolume1"), the unique volume ID, and a suggested persistent symbolic link name for the volume, respectively. Although clients can elect to ignore [**IOCTL_MOUNTDEV_QUERY_SUGGESTED_LINK_NAME**](/windows-hardware/drivers/ddi/mountdev/ni-mountdev-ioctl_mountdev_query_suggested_link_name), they're required to provide a unique volume ID upon receiving [**IOCTL_MOUNTDEV_QUERY_DEVICE_NAME**](/windows-hardware/drivers/ddi/mountmgr/ni-mountmgr-ioctl_mountdev_query_device_name) or [**IOCTL_MOUNTDEV_QUERY_UNIQUE_ID**](/windows-hardware/drivers/ddi/mountdev/ni-mountdev-ioctl_mountdev_query_unique_id). The mount manager relies entirely upon the client to provide the unique volume ID. If the client doesn't provide it, then the mount manager isn't able to assign mount points, such as drive letters, to the volume.

If a client alerts the mount manager of the arrival of its volume but fails to provide a unique ID for the volume when queried, the volume is placed on a *dead mounted device* list. When this situation occurs, clients can send an [**IOCTL_MOUNTMGR_CHECK_UNPROCESSED_VOLUMES**](/windows-hardware/drivers/ddi/mountmgr/ni-mountmgr-ioctl_mountmgr_check_unprocessed_volumes) IOCTL to the mount manager to request that the mount manager rescan its dead mounted device list and make another attempt to query the clients on the list for the unique IDs of their respective volumes.

After the mount manager receives a unique volume ID for a newly introduced volume:

* It searches its database for all of the persistent names assigned to that unique ID.
* It creates symbolic links to the volume for each persistent symbolic link name.

When the mount manager detects that a volume has gone off line, it deletes the symbolic links pointing to the device object without deleting the corresponding symbolic link names in the mount manager's database.

For information about how mount manager clients create persistent symbolic names, see [**IOCTL_MOUNTMGR_CREATE_POINT**](/windows-hardware/drivers/ddi/mountmgr/ni-mountmgr-ioctl_mountmgr_create_point).

## I/O Control Codes sent by Mount Manager clients

The mount manager publishes an interface that allows the mount manager's clients to set, query, and delete persistent names for volumes. To access this interface, clients can obtain a pointer to the mount manager's device object using the object name MOUNTMGR_DEVICE_NAME, defined in *Mountmgr.h*. For instance:

``` C
    // Obtain a pointer to the mount manager device object &
    // use it to send any of the I/O Control codes in this 
    // section to the mount manager.
    RtlInitUnicodeString(&name, MOUNTMGR_DEVICE_NAME);
    status = IoGetDeviceObjectPointer(&name,
                FILE_READ_ATTRIBUTES, 
                &fileObject, &deviceObject);
    irp = IoBuildDeviceIoControlRequest(
            IOCTL_MOUNTMGR_CREATE_POINT,
            deviceObject, createPoint, createPointSize, 
            NULL, 0, FALSE, &event, &ioStatus);
    status = IoCallDriver(deviceObject, irp);
```

The call sequence in this pseudocode sample is simplified for the sake of brevity. For a more complete pseudocode example, see [**IOCTL_MOUNTMGR_CREATE_POINT**](/windows-hardware/drivers/ddi/mountmgr/ni-mountmgr-ioctl_mountmgr_create_point).

Mount manager clients can send any of the documented **IOCTL_MOUNTMGR_*XXX*** control codes to the mount manager, such as[**IOCTL_MOUNTMGR_CREATE_POINT**](/windows-hardware/drivers/ddi/mountmgr/ni-mountmgr-ioctl_mountmgr_create_point).

## I/O Control Codes sent by Mount Manager

The mount manager can send any of the documented **IOCTL_MOUNTDEV_*XXX*** control codes to its clients, such as [**IOCTL_MOUNTDEV_QUERY_DEVICE_NAME**](/windows-hardware/drivers/ddi/mountmgr/ni-mountmgr-ioctl_mountdev_query_device_name).
