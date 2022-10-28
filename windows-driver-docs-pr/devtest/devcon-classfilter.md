---
title: DevCon ClassFilter
description: Adds, deletes, displays, and changes the order of filter drivers for a device setup class. Valid only on the local computer.
keywords:
- DevCon ClassFilter Driver Development Tools
topic_type:
- apiref
api_name:
- DevCon ClassFilter
api_type:
- NA
ms.date: 10/28/2022
---

# DevCon ClassFilter

Adds, deletes, displays, and changes the order of filter drivers for a device setup class. Valid only on the local computer.

``` console
devcon classfilter class {upper | lower} [ = | @driver | -driver | +driver | !driver ]...
```

## Parameters

*class*

Specifies the device setup class.

**upper**

Indicates that the specified drivers are upper-class filter drivers.

**lower**

Indicates that the specified drivers are lower-class filter drivers.

**=**

Moves the cursor to the beginning of the filter driver list (before the first driver).

**@***\<driver\>*

Positions the cursor on the next instance of the specified driver.

**-***\<driver\>*

Add before. Inserts the specified driver before the driver on which the cursor is positioned.

If the cursor is not positioned on a driver, DevCon inserts the specified driver at the beginning of the list. When the subcommand completes, the cursor is positioned on the newly added driver.

**+***\<driver\>*

Add after. Inserts the specified driver after the driver on which the cursor is positioned.

If the cursor is not positioned on a driver, DevCon inserts the specified driver at the end of the list. When the subcommand completes, the cursor is positioned on the newly added driver.

**!***\<driver\>*

Deletes the next occurrence of the specified driver from the list.

When the subcommand completes, the cursor occupies the position of the deleted driver. Subsequent **+** or **-** subcommands insert a new driver at the cursor position.

## Comments

A **DevCon ClassFilter** command can include one or more subcommands that consist of an operator (**=**, **@**, **-**, **+**, **!**) and a filter driver name. DevCon executes the subcommands in the order that they appear in the command.

Without subcommands, a **DevCon ClassFilter** command displays the upper or lower filter drivers in the specified class. For example, **devcon classfilter net lower** displays the lower filter drivers in the Net setup class.

The **DevCon ClassFilter** operation uses a virtual cursor to move through the list of filter drivers for a class. The cursor starts at the beginning of the list of filter drivers, before the first driver in the list. Unless returned to the starting position, the cursor always moves forward through the filter driver list as DevCon executes the subcommands.

DevCon does not add a filter driver to a class unless the driver is installed as a service, that is, there must be a registry subkey for the driver in the [HKLM\\SYSTEM\\CurrentControlSet\\Services](../install/hklm-system-currentcontrolset-services-registry-tree.md) registry key. This safeguard prevents you from accidentally adding a filter driver that does not exist and thereby rendering the system unbootable.

Because filter driver changes require that the devices be restarted, use a **[DevCon Restart](devcon-restart.md)** command or include the **/r** (conditional reboot) parameter in the **DevCon ClassFilter** command.

## Sample usage

``` console
devcon classfilter mouse upper
devcon /r classfilter mouse upper !mouclass +newmou
devcon /r classfilter net lower @netfltr -testfltr
devcon /r classfilter volume upper !volsnap =!volsnap2
```

## Examples

- [Example 23: Display the filter drivers for a setup class](devcon-examples.md#example-23-display-the-filter-drivers-for-a-setup-class)
- [Example 24: Add a filter driver to a setup class](devcon-examples.md#example-24-add-a-filter-driver-to-a-setup-class)
- [Example 25: Insert a filter driver in the class list](devcon-examples.md#example-25-insert-a-filter-driver-in-the-class-list)
- [Example 26: Replace a filter driver](devcon-examples.md#example-26-replace-a-filter-driver)
- [Example 27: Change the order of filter drivers](devcon-examples.md#example-27-change-the-order-of-filter-drivers)
