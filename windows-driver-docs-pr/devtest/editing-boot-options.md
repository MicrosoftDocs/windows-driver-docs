---
title: Edit boot options
description: This section is a practical guide on how to edit boot options on a computer and suggests a step-by-step procedure for customizing the basic elements of boot options.
keywords:
- boot options WDK , editing
- editing boot options
- Bootcfg tool
- custom boot options WDK
- boot entries WDK
ms.date: 12/27/2023
---

# Edit boot options

This section covers editing boot options on a computer and provides a procedure for customizing the basic elements of boot options. It describes a method of using BCDEdit, a tool included with the operating system.

For more information, see [BCDEdit options reference](./bcd-boot-options-reference.md). For information about BCDEdit command syntax, type **bcdedit /?** or **bcdedit /? TOPICS** in a Command Prompt window.

> [!CAUTION]
> Administrative privileges are required to use BCDEdit to modify BCD. Changing some boot entry options using the **BCDEdit /set** command could render your computer inoperable. As an alternative, use the System Configuration utility (MSConfig.exe) to change boot settings. For more information, see *[How to open MSConfig in Windows 10](https://support.microsoft.com/help/4026130/windows-how-to-open-msconfig-in-windows-10)*.

> [!NOTE]
> Before setting BCDEdit options you might need to disable or suspend BitLocker and Secure Boot on the computer.

For help on editing boot entry parameters to enable and disable Windows features, see [Using boot parameters](using-boot-parameters.md).

## Configure operating system features

To configure operating system features in boot options:

- [Add a new boot entry](adding-boot-entries.md) for the operating system by copying an existing boot entry from the same operating system.

- [Change the friendly name](changing-the-friendly-name-of-a-boot-entry.md) of the newly created boot entry so that you can identify it in the boot menu.

- [Add parameters to the boot entry](changing-boot-parameters.md) that enable and configure Windows features.

Then, to make testing easier:

- [Make the new boot entry the default entry](changing-the-default-boot-entry.md).

- [Change the boot menu time-out](changing-the-boot-menu-time-out.md). You can shorten the boot menu time-out so that Windows boots quickly. Or, lengthen the boot menu time-out so that you have ample time to select the preferred boot entry.

## Related articles

[BCDEdit command-line options](/windows-hardware/manufacture/desktop/bcdedit-command-line-options)
