---
title: Edit Boot Options in Windows Using BCDEdit
description: Learn how to edit boot options in Windows using BCDEdit. Follow step-by-step instructions to customize boot entries, configure OS features, and modify boot parameters safely.
keywords:
- boot options WDK , editing
- editing boot options
- Bootcfg tool
- custom boot options WDK
- boot entries WDK
ms.date: 11/05/2025
ms.topic: how-to
---

# Edit boot options

Learn how to edit boot options in Windows to customize how your system starts. This guide shows you how to use BCDEdit, a built-in command-line tool, to modify boot entries, configure operating system features, and safely customize boot parameters.

For more information, see [BCDEdit options reference](./bcd-boot-options-reference.md). For information about BCDEdit command syntax, type **bcdedit /?** or **bcdedit /? TOPICS** in a Command Prompt window.

> [!CAUTION]
> You need administrative privileges to use BCDEdit to modify BCD. Changing some boot entry options by using the **BCDEdit /set** command could make your computer inoperable. As an alternative, use the System Configuration utility (MSConfig.exe) to change boot settings. For more information, see *[How to open MSConfig in Windows 10](https://support.microsoft.com/help/4026130/windows-how-to-open-msconfig-in-windows-10)*.

> [!NOTE]
> Before setting BCDEdit options, you might need to disable or suspend BitLocker and Secure Boot on the computer.

For help on editing boot entry parameters to enable and disable Windows features, see [Using boot parameters](using-boot-parameters.md).

## Configure operating system features in boot options

To configure operating system features in boot options:

1. [Add a new boot entry](adding-boot-entries.md) for the operating system by copying an existing boot entry from the same operating system.

1. [Change the friendly name](changing-the-friendly-name-of-a-boot-entry.md) of the newly created boot entry so that you can identify it in the boot menu.

1. [Add parameters to the boot entry](changing-boot-parameters.md) that enable and configure Windows features.

To make testing easier, configure these settings:

1. [Make the new boot entry the default entry](changing-the-default-boot-entry.md) so it boots automatically.

1. [Change the boot menu time-out](changing-the-boot-menu-time-out.md):
   - **Shorten** the time-out for quick testing cycles
   - **Lengthen** the time-out when you need time to select entries

## Related content

[BCDEdit command-line options](/windows-hardware/manufacture/desktop/bcdedit-command-line-options)
