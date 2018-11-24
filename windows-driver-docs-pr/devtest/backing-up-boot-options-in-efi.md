---
title: Backing up Boot Options in EFI
description: Backing up Boot Options in EFI
ms.assetid: a9c7052c-c554-460c-a8ba-12b79126e67f
keywords:
- back ups WDK boot options , EFI
- NVRAM boot options WDK , backing up
- EFI NVRAM boot options WDK , backing up
- copying boot options
- saving boot options
- boot options WDK , backing up
- Nvrboot tool
ms.date: 07/02/2018
ms.localizationpriority: medium
---

# Backing up Boot Options in EFI


When you install a 64-bit version of Windows, Setup automatically creates a boot entry for the installation and saves a backup copy of the boot entry to a binary file named Boot*xxxx*, where Boot*xxxx* is the NVRAM ID for the boot entry. Setup stores the boot entry backup copy in a new directory on the EFI partition, along with the EFI boot loader for the new installation.By default, the installation directory is in the \\EFI\\Microsoft\\ subdirectory.

However, the system does not save backup copies of the boot entries that you create and it does not update backup copies of boot entries after you edit them.

To save backup copies of boot entries that you create and edit, and to save extra backup copies of the entries that Setup creates, use Nvrboot (nvrboot.efi). Nvrboot saves the entries in the binary format that Setup and the EFI components use. Then, if the boot entry for an installation is lost or corrupted, you can use the import command (**nvrboot i**) in Nvrboot to import the backup copy of the boot entry into NVRAM.

This section includes:

- [Exporting and Importing Boot Entries in EFI](exporting-and-importing-boot-entries-in-efi.md)
- [Identifying Backup Files for Existing Boot Entries](identifying-backup-files-for-existing-boot-entries.md)
- [Identifying Backup Files for Deleted Boot Entries](identifying-backup-files-for-deleted-boot-entries.md)
- [Recognizing Unusable Boot Entry Backup Files](recognizing-unusable-boot-entry-backup-files.md)
 





