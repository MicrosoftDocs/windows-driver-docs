---
title: DevCon ClassFilter
description: Adds, deletes, displays, and changes the order of filter drivers for a device setup class. Valid only on the local computer.
ms.assetid: c04200c7-2897-46bd-ac5f-f838efef79d9
keywords:
- DevCon ClassFilter Driver Development Tools
topic_type:
- apiref
api_name:
- DevCon ClassFilter
api_type:
- NA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# DevCon ClassFilter


Adds, deletes, displays, and changes the order of filter drivers for a device setup class. Valid only on the local computer.

```
    devcon classfilter class {upper | lower} [ = | @driver | -driver | +driver | !driver ]...
```

## <span id="ddk_devcon_classfilter_tools"></span><span id="DDK_DEVCON_CLASSFILTER_TOOLS"></span>Parameters


<span id="_______class______"></span><span id="_______CLASS______"></span> *class*   
Specifies the device setup class.

<span id="_______upper______"></span><span id="_______UPPER______"></span> **upper**   
Indicates that the specified drivers are upper-class filter drivers.

<span id="_______lower______"></span><span id="_______LOWER______"></span> **lower**   
Indicates that the specified drivers are lower-class filter drivers.

<span id="______________"></span> **=**   
Moves the cursor to the beginning of the filter driver list (before the first driver).

<span id="________driver______"></span><span id="________DRIVER______"></span> **@**<em>driver</em>   
Positions the cursor on the next instance of the specified driver.

<span id="-driver"></span><span id="-DRIVER"></span>**-***driver*  
Add before. Inserts the specified driver before the driver on which the cursor is positioned.

If the cursor is not positioned on a driver, DevCon inserts the specified driver at the beginning of the list. When the subcommand completes, the cursor is positioned on the newly added driver.

<span id="________driver______"></span><span id="________DRIVER______"></span> **+**<em>driver</em>   
Add after. Inserts the specified driver after the driver on which the cursor is positioned.

If the cursor is not positioned on a driver, DevCon inserts the specified driver at the end of the list. When the subcommand completes, the cursor is positioned on the newly added driver.

<span id="________driver______"></span><span id="________DRIVER______"></span> **!**<em>driver</em>   
Deletes the next occurrence of the specified driver from the list.

When the subcommand completes, the cursor occupies the position of the deleted driver. Subsequent **+** or **-** subcommands insert a new driver at the cursor position.

### <span id="comments"></span><span id="COMMENTS"></span>Comments

A **DevCon ClassFilter** command can include one or more subcommands that consist of an operator (**=**, **@**, **-**, **+**, **!**) and a filter driver name. DevCon executes the subcommands in the order that they appear in the command.

Without subcommands, a **DevCon ClassFilter** command displays the upper or lower filter drivers in the specified class. For example, **devcon classfilter net lower** displays the lower filter drivers in the Net setup class.

The **DevCon ClassFilter** operation uses a virtual cursor to move through the list of filter drivers for a class. The cursor starts at the beginning of the list of filter drivers, before the first driver in the list. Unless returned to the starting position, the cursor always moves forward through the filter driver list as DevCon executes the subcommands.

DevCon does not add a filter driver to a class unless the driver is installed as a service, that is, there must be a registry subkey for the driver in the [HKLM\\SYSTEM\\CurrentControlSet\\Services](https://msdn.microsoft.com/library/windows/hardware/ff546188) registry key. This safeguard prevents you from accidentally adding a filter driver that does not exist and thereby rendering the system unbootable.

Because filter driver changes require that the devices be restarted, use a [**DevCon Restart**](devcon-restart.md) command or include the **/r** (conditional reboot) parameter in the **DevCon ClassFilter** command.

### <span id="sample_usage"></span><span id="SAMPLE_USAGE"></span>Sample Usage

```
devcon classfilter mouse upper
devcon /r classfilter mouse upper !mouclass +newmou
devcon /r classfilter net lower @netfltr -testfltr
devcon /r classfilter volume upper !volsnap =!volsnap2
```

### <span id="examples"></span><span id="EXAMPLES"></span>Examples

[Example 23: Display the filter drivers for a setup class](devcon-examples.md#ddk_example_23_display_the_filter_drivers_for_a_setup_class_tools)

[Example 24: Add a filter driver to a setup class](devcon-examples.md#ddk_example_24_add_a_filter_driver_to_a_setup_class_tools)

[Example 25: Insert a filter driver in the class list](devcon-examples.md#ddk_example_25_insert_a_filter_driver_in_the_class_list_tools)

[Example 26: Replace a filter driver](devcon-examples.md#ddk_example_26_replace_a_filter_driver_tools)

[Example 27: Change the order of filter drivers](devcon-examples.md#ddk_example_27_change_the_order_of_filter_drivers_tools)









