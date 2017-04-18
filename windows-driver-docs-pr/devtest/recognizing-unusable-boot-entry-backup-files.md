---
title: Recognizing Unusable Boot Entry Backup Files
description: Recognizing Unusable Boot Entry Backup Files
ms.assetid: ff61c8e9-ad6b-4f3f-9c4b-72c24c27eda6
keywords: ["NVRAM boot options WDK ,", "EFI NVRAM boot options WDK ,"]
---

# Recognizing Unusable Boot Entry Backup Files


## <span id="ddk_recognizing_unusable_boot_entry_backup_files_tools"></span><span id="DDK_RECOGNIZING_UNUSABLE_BOOT_ENTRY_BACKUP_FILES_TOOLS"></span>


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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Recognizing%20Unusable%20Boot%20Entry%20Backup%20Files%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




