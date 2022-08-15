---
title: Editing Boot Options
description: Editing Boot Options
keywords:
- boot options WDK , editing
- editing boot options
- Bootcfg tool
- custom boot options WDK
- boot entries WDK
ms.date: 04/23/2019
---

# Editing Boot Options

This section is a practical guide to editing the boot options on a computer running Windows Server 2008, Windows Server 2012, or Windows 7 or later. It suggests a step-by-step procedure for customizing the basic elements of boot options.

This section describes a method of using BCDEdit, a tool included with the operating system. For information about BCDEdit command syntax, type **bcdedit /?** or **bcdedit /? TOPICS** in a Command Prompt window. See [BCDEdit Options Reference](./bcd-boot-options-reference.md) for more information.

> [!NOTE]
> Before setting BCDEdit options you might need to disable or suspend BitLocker and Secure Boot on the computer.

For help on editing boot entry parameters to enable and disable Windows features, see [Using Boot Parameters](using-boot-parameters.md).

To configure operating system features in boot options:

- [Add a new boot entry](adding-boot-entries.md) for the operating system by copying an existing boot entry from the same operating system.

- [Change the friendly name](changing-the-friendly-name-of-a-boot-entry.md) of the newly created boot entry so that you can identify it in the boot menu.

- [Add parameters to the boot entry](changing-boot-parameters.md) that enable and configure Windows features.

Then, to make testing quicker and easier:

- [Make the new boot entry the default entry](changing-the-default-boot-entry.md).

-  [Change the boot menu time-out](changing-the-boot-menu-time-out.md). You can shorten the boot menu time-out so that Windows boots quickly. Or, lengthen the boot menu time-out so that you have ample time to select the preferred boot entry.

## Related Topics 
 [BCDEdit Command-Line Options](/windows-hardware/manufacture/desktop/bcdedit-command-line-options)

> [!CAUTION]
> Administrative privileges are required to use BCDEdit to modify BCD. Changing some boot entry options using the **BCDEdit /set** command could render your computer inoperable. As an alternative, use the System Configuration utility (MSConfig.exe) to change boot settings.
