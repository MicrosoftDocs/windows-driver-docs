---
title: Recognizing Unusable Boot Entry Backup Files
description: Recognizing Unusable Boot Entry Backup Files
keywords:
- NVRAM boot options WDK ,
- EFI NVRAM boot options WDK ,
ms.date: 07/02/2018
ms.localizationpriority: medium
---

# Recognizing Unusable Boot Entry Backup Files

Unfortunately, boot entry backup copies are not always usable.

In an EFI environment, applications and drivers identify disk partitions by a partition GUID. If the disk partition GUID changes for any reason, then the partition GUID in the boot entry backup copy is no longer valid and the EFI boot loader cannot use the backup copy to boot the system.

The following Bootcfg sample shows a boot entry that was imported with invalid partition GUIDs.

```
Boot entry ID:    4
OS Friendly Name: Windows Server 2003 - mydebug
OsLoadOptions:    /debug /debugport=com1 /baudrate=115200
BootFilePath:     (null)
OsFilePath:       (null)
```

In this case, you must recreate the boot entry by copying another boot entry from the operating system installation, and then changing the parameters.
