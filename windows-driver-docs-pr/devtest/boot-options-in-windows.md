---
title: Configure and edit boot options in Windows for driver development
description: Learn about boot options in Windows, including the boot loader architecture, boot configuration, and the BCDEdit editing tool.
keywords:
- boot options WDK , Windows
- editing boot options
- multiboot systems WDK boot options
- legacy boot entries WDK
- Boot Configuration Data WDK
- BCD WDK
- BCDEdit tool
- boot options WDK , editing
- ntldr tool
- Windows Boot Manager WDK
- Bootmgr tool
- system-specific boot loaders WDK
- boot loaders WDK
- firmware-independent boot options WDK
ms.date: 11/05/2025
ms.topic: concept-article
---

# Configure and edit boot options in Windows for driver development

This article provides an overview of boot options in Windows. You'll learn about the key components of the boot process, including:

- The Windows Boot Manager, operating system loader, and resume loader.
- The Boot Configuration Data (BCD) store where boot options are kept.
- The BCDEdit tool used to modify boot options.

During development, you can use this information to configure boot options for debugging, testing, and troubleshooting your driver.

> [!CAUTION]
> You need administrative privileges to use BCDEdit to modify BCD. Changing some boot entry options by using BCDEdit could make your computer inoperable. As an alternative, use the System Configuration utility (MSConfig.exe) to change boot settings. For more information, see *[How to open MSConfig in Windows 10](https://support.microsoft.com/help/4026130/windows-how-to-open-msconfig-in-windows-10)*.

## Boot Loading Architecture

Windows uses three primary components to load the operating system quickly and securely:

:::image type="content" source="images/boot-process-diagram.png" alt-text="Diagram showing the boot process from Windows Boot Manager to the OS loader.":::

- **Windows Boot Manager**: Starts the system, displays the boot menu to the user, and loads the selected operating system loader.
- **Windows operating system loader**: Resides in the Windows partition, takes over the boot process, and loads the operating system.
- **Windows resume loader**: Resumes the system from hibernation.

The Windows Boot Manager is generic, while the system-specific boot loaders are optimized for the OS they load. The Boot Manager passes boot parameters to the selected loader, which then completes the boot process.

For additional detail on the Windows startup process, refer to *Windows Internals*, published by Microsoft Press.

## Boot Configuration Data

Windows stores boot options in the Boot Configuration Data (BCD) store on BIOS-based and EFI-based computers. The BCD store uses GUIDs and names like "Default" to identify boot-related applications.

Key BCD capabilities for driver development:

- Access BCD at run time and during system setup
- Manage BCD remotely for troubleshooting
- Restore BCD from USB media or Startup Repair

For a complete list of BCD boot options, see [BCD Boot Options Reference](./bcd-boot-options-reference.md).

## Edit boot options with BCDEdit

To edit boot options in Windows, use BCDEdit (BCDEdit.exe), a command-line tool included in Windows.

### Prerequisites

- Administrator privileges on the computer
- BitLocker and Secure Boot disabled or suspended (if enabled)

### Alternative tools for editing boot options

- [System Configuration utility (MSConfig.exe)](https://support.microsoft.com/help/4026130/windows-how-to-open-msconfig-in-windows-10) - GUI-based boot settings editor
- Advanced Startup settings UI - Built into Windows settings
- [Boot Configuration Data WMI Provider](/previous-versions/windows/desktop/bcd/boot-configuration-data-portal) - For programmatic changes

## Next steps
- [Learn BCDEdit commands and syntax](editing-boot-options.md)
- [View all BCD boot options](bcd-boot-options-reference.md)
- [Set up boot parameters for debugging](using-boot-parameters.md)
