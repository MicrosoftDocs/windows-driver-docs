---
title: Identifying Backup Files for Existing Boot Entries
description: Identifying Backup Files for Existing Boot Entries
keywords:
- NVRAM boot options WDK , backup file searches
- EFI NVRAM boot options WDK , backup file searches
- searches WDK boot options
- locating boot entry backups WDK
- existing boot entry searches WDK
- boot entry backups WDK
- identifying backup files for boot entries
ms.date: 07/09/2018
ms.localizationpriority: medium
---

# Identifying Backup Files for Existing Boot Entries

To search for the backup copy of a boot entry by its file name, you need the entry's EFI boot entry ID. However, neither Bootcfg nor Nvrboot display this ID.

Instead, you can find a boot entry backup copy by searching for a Boot*xxxx* file in the installation's directory on the EFI partition. To find the installation directory, locate the path to the boot loader file for the operating system installation. The boot entry backup file for the installation is stored in the same directory.

Use the **nvrboot d** (display) command or the **bootcfg** or **bootcfg query** commands to display the path to the directory in which the boot loader for the operating system is stored.

In the following example, the boot loader for a boot entry is stored on the EFI partition in the \\Microsoft\\WINNT50 subdirectory. The backup copy of the boot entry for this installation is a file named Boot*xxxx* in the same subdirectory.

> [!NOTE]
> The **Boot entry ID** field in Bootcfg and the boot entry number in Nvrboot do not display the EFI boot entry ID. The Bootcfg and Nvrboot IDs are line numbers that represent the order of the boot entry in the **Boot Entries** section and change when the entries are reordered.

As shown in the following Bootcfg sample, the path to the boot loader file appears in the **BootFilePath** field.

Bootcfg displays the file location as the [NT device name](../kernel/nt-device-names.md) of the partition, followed by the file system path to the boot loader file.

```
Boot Entries
------------
Boot entry ID:    1
OS Friendly Name: Windows Server 2003, Enterprise
OsLoadOptions:     /debug /debugport=COM1 /baudrate=115200
BootFilePath:     \Device\HarddiskVolume1\EFI\Microsoft\WINNT50\ia64ldr.efi
OsFilePath:       \Device\HarddiskVolume3\WINDOWS
```

In the following sample of an Nvrboot display, the path to the boot loader file for an operating system installation appears in the **EFIOSLoaderFilePath** field.

Nvrboot displays the file location as a partition GUID followed by the path to the boot loader file.

```
1. Load identifier = Windows Server 2003, Enterprise
2. OsLoadOptions = /debug /debugport=COM1 /baudrate=115209
3. EFIOSLoaderFilePath = 006F0073-0066-0074-5C00-570049004E00  ::  \EFI\Microsoft\WINNT50\ia64ldr.efi
4. OSLoaderFilePath = 04000004-5D18-3F27-0000-0000205C273F  :: \Windows
```

In both cases, the boot loader file (and the Boot*xxxx* boot entry backup file) for the operating system are in the WINNT50 directory of the EFI system partition (EFI\\Microsoft\\WINNT50).
