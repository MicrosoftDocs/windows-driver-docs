---
title: Backing up Boot Options in EFI
description: Backing up Boot Options in EFI
ms.assetid: a9c7052c-c554-460c-a8ba-12b79126e67f
keywords: ["back ups WDK boot options , EFI", "NVRAM boot options WDK , backing up", "EFI NVRAM boot options WDK , backing up", "copying boot options", "saving boot options", "boot options WDK , backing up", "Nvrboot tool"]
---

# Backing up Boot Options in EFI


## <span id="ddk_backing_up_boot_options_in_efi_tools"></span><span id="DDK_BACKING_UP_BOOT_OPTIONS_IN_EFI_TOOLS"></span>


When you install a 64-bit version of Windows, Setup automatically creates a boot entry for the installation and saves a backup copy of the boot entry to a binary file named Boot*xxxx*, where Boot*xxxx* is the NVRAM ID for the boot entry. Setup stores the boot entry backup copy in a new directory on the EFI partition, along with the EFI boot loader for the new installation.By default, the installation directory is in the \\EFI\\Microsoft\\ subdirectory.

However, the system does not save backup copies of the boot entries that you create and it does not update backup copies of boot entries after you edit them.

To save backup copies of boot entries that you create and edit, and to save extra backup copies of the entries that Setup creates, use Nvrboot (nvrboot.efi). Nvrboot saves the entries in the binary format that Setup and the EFI components use. Then, if the boot entry for an installation is lost or corrupted, you can use the import command (**nvrboot i**) in Nvrboot to import the backup copy of the boot entry into NVRAM.

This section includes:

[Exporting and Importing Boot Entries in EFI](exporting-and-importing-boot-entries-in-efi.md)

[Identifying Backup Files for Existing Boot Entries](identifying-backup-files-for-existing-boot-entries.md)

[Identifying Backup Files for Deleted Boot Entries](identifying-backup-files-for-deleted-boot-entries.md)

[Recognizing Unusable Boot Entry Backup Files](recognizing-unusable-boot-entry-backup-files.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Backing%20up%20Boot%20Options%20in%20EFI%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




