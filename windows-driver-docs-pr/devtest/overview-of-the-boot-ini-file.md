---
title: Overview of the Boot.ini File
description: The Boot.ini file is a text file that contains the boot options for computers with BIOS firmware running NT-based operating system prior to Windows Vista. It is located at the root of the system partition, typically c:\Boot.ini.
keywords:
- Boot.ini files WDK , about Boot.ini files
- boot loader section WDK boot options
- operating systems section WDK boot options
- boot entries WDK
- names WDK boot options
- friendly names WDK boot options
- boot entry parameters WDK
- boot parameters WDK
ms.date: 07/03/2018
ms.localizationpriority: medium
---

# Overview of the Boot.ini File

> [!IMPORTANT] 
> This topic describes the boot options supported in Windows XP and Windows Server 2003. If you are changing boot options for modern versions of Windows, see [Boot Options in Windows Vista and Later](./boot-options-in-windows.md).

The Boot.ini file is a text file that contains the boot options for computers with BIOS firmware running NT-based operating system prior to Windows Vista. It is located at the root of the system partition, typically c:\\Boot.ini. The following sample shows the content of a typical Boot.ini file.

```
[boot loader]
timeout=30
default=multi(0)disk(0)rdisk(0)partition(1)\WINDOWS
[operating systems]
multi(0)disk(0)rdisk(0)partition(1)\WINDOWS="Microsoft Windows XP Professional" /fastdetect
C:\CMDCONS\BOOTSECT.DAT="Microsoft Windows Recovery Console" /cmdcons
```

Boot.ini has two main sections:

-   The **\[boot loader\]** section contains option settings that apply to all boot entries on the system. The options include **timeout**, the boot menu time-out value, and **default**, the location of the default operating system.

    The following sample shows the \[boot loader\] section of Boot.ini.

    ```
    [boot loader]
    timeout=30
    default=multi(0)disk(0)rdisk(0)partition(1)\WINDOWS
    ```

-   The **\[operating systems\]** section is comprised of one or more *boot entries* for each operating system or bootable program installed on the computer.

    A *boot entry* is a set of options that defines a load configuration for an operating system or bootable program. The boot entry specifies an operating system or bootable program and the location of its files. It can also include parameters that configure the operating system or program.

    The following sample shows the \[operating systems\] section of Boot.ini on a computer with two operating systems, Microsoft Windows XP and Microsoft Windows 2000. It has two boot entries, one for each operating system.

    ```
    [operating systems]
    multi(0)disk(0)rdisk(0)partition(1)\WINDOWS="Microsoft Windows XP Professional" /fastdetect
    multi(0)disk(0)rdisk(0)partition(2)\WINNT="Microsoft Windows 2000 Professional" /fastdetect
    ```

Each boot entry includes the following elements:

-   The location of the operating system. Boot.ini uses the Advanced RISC Computing (ARC) naming convention to display the path to the disk partition and directory where the operating system resides. For example:
    ```
    multi(0)disk(0)rdisk(0)partition(1)\WINDOWS
    ```

-   A friendly name for the boot entry. The friendly name represents the boot entry in the boot menu. The friendly name is surrounded by quotation marks and represents the boot entry in the boot menu. For example:
    ```
    "Microsoft Windows XP Professional"
    ```

-   *Boot entry parameters*, also known as *boot parameters* or *load options* enable, disable, and configure operating system features. Boot parameters resemble command-line parameters, each beginning with a forward slash (/), such as [**/debug**](https://support.microsoft.com/help/833721/available-switch-options-for-the-windows-xp-and-the-windows-server-200). You can have zero or more boot parameters on each boot entry.

    For a list of boot parameters that are relevant to driver testing and debugging, see [Boot.ini Boot Parameter Reference](./boot-options-in-a-boot-ini-file.md).

You can have multiple boot entries for the same operating system, each with a different set of boot parameters. Windows creates a standard boot entry when you install the operating system, and you can create additional, customized entries for an operating system by editing Boot.ini.