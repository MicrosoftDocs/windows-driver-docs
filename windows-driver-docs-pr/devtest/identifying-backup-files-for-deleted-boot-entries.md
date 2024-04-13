---
title: Identifying Backup Files for Deleted Boot Entries
description: Identifying Backup Files for Deleted Boot Entries
keywords:
- NVRAM boot options WDK , backup file searches
- EFI NVRAM boot options WDK , backup file searches
- searches WDK boot options
- locating boot entry backups WDK
- deleted boot entry searches WDK
- boot entry backups WDK
- identifying backup files for boot entries
ms.date: 07/02/2018
---

# Identifying Backup Files for Deleted Boot Entries

Typically, you need to locate a boot entry backup file when a boot entry is inadvertently deleted.

If a boot entry has been deleted from NVRAM, and the operating system is still installed, the boot loader file and the boot entry backup file for the installation still remain on the disk in the installation's directory on the EFI partition.

To find the boot entry backup file for a deleted entry, boot to the EFI shell, and search the EFI partition recursively for boot entry backup files using the command **dir boot\* /s**. Exclude from your results boot entry backup files that are in directories associated with boot entries already in NVRAM. To display the directory for an existing boot entry, use the **nvrboot d** (display) command.

If there are multiple Boot*xxxx* files that are not associated with existing boot entries, use Nvrboot to import the entries from their backup files, and then delete the unwanted boot entries.
