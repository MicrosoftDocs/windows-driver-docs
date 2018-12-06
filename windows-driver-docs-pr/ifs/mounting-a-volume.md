---
title: Mounting a Volume
description: Mounting a Volume
ms.assetid: 0531b023-f35c-4fe9-9c0d-5acafc42f9b4
keywords:
- filter drivers WDK file system , volume mount process
- file system filter drivers WDK , volume mount process
- volumes WDK file system , mounting
- mounting volumes WDK file systems
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Mounting a Volume


## <span id="ddk_mounting_a_volume_if"></span><span id="DDK_MOUNTING_A_VOLUME_IF"></span>


The volume mount process is typically triggered by a request to open a file on a logical volume (that is, a partition or dynamic volume) as follows:

1.  A user application calls **CreateFile** to open a file. Or a kernel-mode driver calls [**ZwCreateFile**](https://msdn.microsoft.com/library/windows/hardware/ff566424) or [**IoCreateFileSpecifyDeviceObjectHint**](https://msdn.microsoft.com/library/windows/hardware/ff548289).

2.  The I/O Manager determines which logical volume is the target of the request and checks its device object to see whether it is mounted. If the VPB\_MOUNTED flag is set, the volume has been mounted by a file system.

3.  If the volume has not been mounted by a file system since system boot (that is, the VPB\_MOUNTED flag is not set), the I/O Manager sends a volume mount ([**IRP\_MJ\_FILE\_SYSTEM\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff548670), IRP\_MN\_MOUNT\_VOLUME) request to each file system that might claim the volume.

    Not all built-in file systems are necessarily loaded − even well after system boot. (See [What Happens to File Systems During System Boot](what-happens-to-file-systems-during-system-boot.md).) For built-in file systems that are not yet loaded, the I/O Manager sends the volume mount request to the file system recognizer (FsRec), which checks the volume boot sector on behalf of these file systems.

    If FsRec determines that the volume was formatted by a not-yet-loaded file system, the I/O Manager responds by sending a load file system ([**IRP\_MJ\_FILE\_SYSTEM\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff548670), IRP\_MN\_LOAD\_FILE\_SYSTEM) request to FsRec, which loads the file system. The I/O Manager then sends the original volume mount request to the file system.

4.  Each file system that receives the mount volume request examines the volume's boot sector to determine whether the volume's format and other information indicate that the volume was formatted by that particular file system. If the format matches, the file system mounts the volume.

The following sections discuss how the file system mounts the volume after recognizing it:

[How the Volume Is Mounted](how-the-volume-is-mounted.md)

[Volume Mount Example](volume-mount-example.md)

 

 




