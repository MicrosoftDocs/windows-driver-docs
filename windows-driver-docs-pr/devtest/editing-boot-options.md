---
title: Editing Boot Options
description: Editing Boot Options
ms.assetid: b50b3ac8-154a-4c26-907f-11e274a5c7c8
keywords: ["boot options WDK , editing", "editing boot options", "Bootcfg tool", "custom boot options WDK", "boot entries WDK"]
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Editing%20Boot%20Options%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




