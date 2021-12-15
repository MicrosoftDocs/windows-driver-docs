---
title: How the Volume is Recognized
description: How the Volume is Recognized
keywords:
- filter drivers WDK file system , volume mount process , recognizing the volume
- file system filter drivers WDK , volume mount process , recognizing the volume
- volumes WDK file system , mounting
- mounting volumes WDK file systems
ms.date: 10/16/2019
---

# How the Volume is Recognized

> [!NOTE]
> For optimal reliability and performance, use [file system minifilter drivers](./filter-manager-concepts.md) with Filter Manager support instead of legacy file system filter drivers. To port your legacy driver to a minifilter driver, see [Guidelines for Porting Legacy Filter Drivers](guidelines-for-porting-legacy-filter-drivers.md).

The volume mount process is typically triggered by a request to open a file on a logical volume (that is, a partition or dynamic volume) as follows:

1. A user application calls **CreateFile** to open a file. Or a kernel-mode driver calls [**ZwCreateFile**](/windows-hardware/drivers/ddi/content/ntifs/nf-ntifs-ntcreatefile) or [**IoCreateFileSpecifyDeviceObjectHint**](/windows-hardware/drivers/ddi/content/ntddk/nf-ntddk-iocreatefilespecifydeviceobjecthint).

2. The I/O Manager determines which logical volume is the target of the request and checks its device object to see whether it is mounted. If the VPB_MOUNTED flag is set, the volume has been mounted by a file system.

3. If the volume has not been mounted by a file system since system boot (that is, the VPB_MOUNTED flag is not set), the I/O Manager sends a volume mount ([**IRP_MJ_FILE_SYSTEM_CONTROL**](./irp-mj-file-system-control.md), IRP_MN_MOUNT_VOLUME) request to each file system that might claim the volume.

   Not all built-in file systems are necessarily loaded − even well after system boot. (See [What Happens to File Systems During System Boot](what-happens-to-file-systems-during-system-boot.md).) For built-in file systems that are not yet loaded, the I/O Manager sends the volume mount request to the file system recognizer (FsRec), which checks the volume boot sector on behalf of these file systems.

   If FsRec determines that the volume was formatted by a not-yet-loaded file system, the I/O Manager responds by sending a load file system ([**IRP_MJ_FILE_SYSTEM_CONTROL**](./irp-mj-file-system-control.md), IRP_MN_LOAD_FILE_SYSTEM) request to FsRec, which loads the file system. The I/O Manager then sends the original volume mount request to the file system.

4. Each file system that receives the mount volume request examines the volume's boot sector to determine whether the volume's format and other information indicate that the volume was formatted by that particular file system. If the format matches, the file system mounts the volume.

The following sections discuss how the file system mounts the volume after recognizing it:

[How the Volume Is Mounted](how-the-volume-is-mounted.md)

[Volume Mount Example](volume-mount-example.md)
