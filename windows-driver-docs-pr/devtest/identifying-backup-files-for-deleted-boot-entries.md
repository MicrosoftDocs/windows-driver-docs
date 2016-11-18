---
title: Identifying Backup Files for Deleted Boot Entries
description: Identifying Backup Files for Deleted Boot Entries
ms.assetid: ba1bcd10-83cb-4d28-9360-7927b169f056
keywords: ["NVRAM boot options WDK , backup file searches", "EFI NVRAM boot options WDK , backup file searches", "searches WDK boot options", "locating boot entry backups WDK", "deleted boot entry searches WDK", "boot entry backups WDK", "identifying backup files for boot entries"]
---

# Identifying Backup Files for Deleted Boot Entries


## <span id="ddk_identifying_backup_files_for_deleted_boot_entries_tools"></span><span id="DDK_IDENTIFYING_BACKUP_FILES_FOR_DELETED_BOOT_ENTRIES_TOOLS"></span>


Typically, you need to locate a boot entry backup file when a boot entry is inadvertently deleted.

If a boot entry has been deleted from NVRAM, and the operating system is still installed, the boot loader file and the boot entry backup file for the installation still remain on the disk in the installation's directory on the EFI partition.

To find the boot entry backup file for a deleted entry, boot to the EFI shell, and search the EFI partition recursively for boot entry backup files using the command **dir boot\* /s**. Exclude from your results boot entry backup files that are in directories associated with boot entries already in NVRAM. To display the directory for an existing boot entry, use the **nvrboot d** (display) command.

If there are multiple Boot*xxxx* files that are not associated with existing boot entries, use Nvrboot to import the entries from their backup files, and then delete the unwanted boot entries.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Identifying%20Backup%20Files%20for%20Deleted%20Boot%20Entries%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




