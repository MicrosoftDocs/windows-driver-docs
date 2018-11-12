---
title: Editing Boot Options
description: Editing Boot Options
ms.assetid: b50b3ac8-154a-4c26-907f-11e274a5c7c8
keywords:
- boot options WDK , editing
- editing boot options
- Bootcfg tool
- custom boot options WDK
- boot entries WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Editing Boot Options


## <span id="ddk_editing_boot_options_tools"></span><span id="DDK_EDITING_BOOT_OPTIONS_TOOLS"></span>


This section is a practical guide to editing the boot options on a computer running Windows 10, Windows 8, Windows Server 2012, Windows 7, or Windows Server 2008. It suggests a step-by-step procedure for customizing the basic elements of boot options.

This section describes a method of using BCDEdit, a tool included with the operating system. For information about BCDEdit command syntax, type **bcdedit /?** or **bcdedit /? TOPICS** in a Command Prompt window. See [BCD Boot Options Reference](https://msdn.microsoft.com/library/windows/hardware/ff542205) for more information.

**Note**  Before setting BCDEdit options you might need to disable or suspend BitLocker and Secure Boot on the computer.

 

For help on editing boot entry parameters to enable and disable Windows features, see [Using Boot Parameters](using-boot-parameters.md).

To configure operating system features in boot options:

-   [Add a new boot entry](adding-boot-entries.md) for the operating system by copying an existing boot entry from the same operating system.

-   [Change the friendly name](changing-the-friendly-name-of-a-boot-entry.md) of the newly created boot entry so that you can identify it in the boot menu.

-   [Add parameters to the boot entry](changing-boot-parameters.md) that enable and configure Windows features.

Then, to make testing quicker and easier:

-   [Make the new boot entry the default entry](changing-the-default-boot-entry.md).

-   [Change the boot menu time-out](changing-the-boot-menu-time-out.md). You can shorten the boot menu time-out so that Windows boots quickly. Or, lengthen the boot menu time-out so that you have ample time to select the preferred boot entry.

 

 





