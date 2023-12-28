---
title: Adding Boot Entries
description: Adding Boot Entries in Windows Vista and later, Windows Server 2008 and later, and Windows Recovery Environment
keywords:
- boot options WDK , adding boot entries
- boot entries WDK
- adding boot entries
- Boot.ini files WDK , adding boot entries
ms.date: 11/14/2022
---

# Adding Boot Entries

One method to customize boot options in Windows is to add a new *boot entry* for an operating system. A *boot entry* is a set of options that define a load configuration for an operating system or bootable program.

You can have multiple boot entries for an operating system, each with a different set of boot parameters. The Windows Installer creates a standard boot entry when you install an operating system, and you can create additional, customized boot entries for an operating system by editing the boot options.

You can add, delete, and change the options in the boot entry that Windows Installer created. However, it is prudent to keep the standard entry and, instead, add a separate entry that you customize.

To add a boot entry, copy an existing boot entry, and then modify the copy.

This topic applies to Windows Vista and later, Windows Server 2008 and later, and the Windows Recovery Environment.

> [!CAUTION]
> Administrative privileges are required to use BCDEdit to modify BCD. Changing some boot entry options using the **BCDEdit** command could render your computer inoperable.

## Adding a new boot entry

In Windows, you use BCDEdit to modify your boot options. To add a new boot entry, open a Command Prompt window with elevated privileges (select and hold (or right-click) **Command Prompt** and select **Run as administrator** from the shortcut menu).

**Note**  Before setting BCDEdit options you might need to disable or suspend BitLocker and Secure Boot on the computer.

The easiest way to create a new boot entry is to copy an existing entry and then modify it as you need. To do this, use BCDEdit with the **/copy** option. For example, in the following command, BCDEdit copies the Microsoft Windows boot entry that was last used to boot Windows, identified as **{current}**, and creates a new boot entry. The **/d** description option specifies DebugEntry as the name of the new boot entry.

```
bcdedit /copy {current} /d "DebugEntry"
```

If the command succeeds, BCDEdit displays a message similar to the following:

```
The entry was successfully copied to {49916baf-0e08-11db-9af4-000bdbd316a0}.
```

When you copy a boot loader entry that appears on the boot menu, the copy is automatically added as the last item on the boot menu.

The GUID in the preceding message (which appears between braces ({})) is the identifier of the new boot entry. The **/copy** option creates a new GUID for the boot entry. You use the identifier to represent the entry in all subsequent BCDEdit commands.

If the command fails, be sure that you are running in a Command Prompt window with administrator privileges and that all of the command parameters are spelled correctly, including the braces around **{current}**.

> [!NOTE]
> If you are using [Windows PowerShell](/powershell/module/Microsoft.PowerShell.Core/), you must use quotes around the boot entry identifier, for example: **"{49916baf-0e08-11db-9af4-000bdbd316a0}"** or **"{current}"**.

You can also add a boot entry using the **/create** option. This method is more difficult because you need to provide additional information about the boot entry type. You also need to specify the **/application**, **/inherit**, or **/device** options. For example, the following creates a new operating system boot entry called "My Windows Vista":

```
bcdedit /create /d "My Windows Vista" /application osloader
```

When you use the **/create** option, the new boot loader entries are not added to the boot menu automatically. The **/create** option creates a new GUID for the boot entry. You must add the new boot entry to the boot menu by using the **/displayorder** option. You can place the boot loader entries in any order.

For information about the **/create** command parameters, type **bcdedit /? /create** in a Command Prompt window.

## Editing the boot menu

In Windows, new boot loader entries are not added to the boot menu automatically. You can use the **/displayorder** option to set the order in which the boot manager displays the boot entries on a multi-boot menu. The command has the following syntax:

```
bcdedit /displayorder {ID} {ID} ...
```

You can place the boot loader entries in any order.

The ID is the GUID of the boot entry or a reserved identifier, such as **{current}**. Separate each identifier with a space. Be sure to include the braces ({}).

For example, to add the DebugEntry boot entry to the boot menu after the **{current}** entry, use the following command (remember to use `"{guid}"` in Windows PowerShell):

```
bcdedit /displayorder {current} {49916baf-0e08-11db-9af4-000bdbd316a0}
```

You can also use the options **/addlast, /addfirst**, and **/remove** to order and remove items from the menu. For example, the following command adds the DebugEntry boot entry as the last item on the menu:

```
bcdedit /displayorder {49916baf-0e08-11db-9af4-000bdbd316a0} /addlast
```

## Removing and deleting a boot entry

The following command removes the {49916baf-0e08-11db-9af4-000bdbd316a0} boot entry item from the boot menu.

```
bcdedit /displayorder {49916baf-0e08-11db-9af4-000bdbd316a0} /remove
```

When you remove the specified boot entry using the **/displayorder** and **/remove** options, the boot entry is removed from the boot menu, but it is still in the BCD store. To completely remove a boot loader entry from the boot menu and from the store, use the **/delete** option.

```
bcdedit /delete {49916baf-0e08-11db-9af4-000bdbd316a0}
```

To verify that the display order is correct, use the following command:

```
bcdedit
```

When you type **bcdedit** without additional parameters, BCDEdit displays the boot manager entry and the boot loader entries in the order that they will appear in the menu.

The Windows Boot Manager entry also includes the boot menu display order, as the following example shows.

```
## Windows Boot Manager
identifier              {bootmgr}
device                  partition=C:
description             Windows Boot Manager
locale                  en-US
inherit                 {globalsettings}
isolatedcontext         Yes
default                 {current}
resumeobject            {18b123cd-2bf6-11db-bfae-00e018e2b8db}
displayorder            {current}
toolsdisplayorder       {memdiag}
timeout                 30

## Windows Boot Loader
-------------------
identifier              {current}
device                  partition=C:
path                    \Windows\system32\winload.exe
description             Microsoft Windows 
locale                  en-US
inherit                 {bootloadersettings}
osdevice                partition=C:
systemroot              \Windows
resumeobject            {d7094401-2641-11db-baba-00e018e2b8db}
nx                      OptIn

## Windows Boot Loader
-------------------
identifier              {18b123cd-2bf6-11db-bfae-00e018e2b8db}
device                  partition=C:
path                    \Windows\system32\winload.exe
description             Debugger Boot
locale                  en-US
inherit                 {bootloadersettings}
osdevice                partition=C:
systemroot              \Windows
resumeobject            {d7094401-2641-11db-baba-00e018e2b8db}
nx                      OptIn
debug                   Yes
```

## See Also

[Editing Boot Options](./editing-boot-options.md)