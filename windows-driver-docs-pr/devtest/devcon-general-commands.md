---
title: Device Console (DevCon.exe) Commands
description: DevCon (DevCon.exe) is a command line tool that can display detailed information about devices on computers running Windows. You can also use DevCon to enable, disable, install, configure, and remove devices. DevCon uses the following syntax.
keywords:
- Device Console (DevCon.exe) Commands Driver Development Tools
topic_type:
- apiref
api_name:
- Device Console (DevCon.exe) Commands
api_type:
- NA
ms.custom: contperf-fy22q3 
ms.date: 07/26/2022
---

# Device Console (DevCon.exe) Commands

DevCon (DevCon.exe) is a command line tool that can display detailed information about devices on computers running Windows. You can also use DevCon to enable, disable, install, configure, and remove devices. DevCon uses the following syntax.

```console
devcon [/r] command [arguments] 
```

> [!IMPORTANT]
> [PnPUtil](pnputil.md) ships with every release of Windows and makes use of the most reliable and secure APIs available and its use is recommended. For more information on using PnPutil instead of devcon, see [Replacing DevCon](devcon-migration.md).

## Parameters

> [!NOTE]
> To change the status or configuration of a device, you must be a member of the Administrators group on the computer.

The parameters in a DevCon command must appear in the order shown in the syntax. If parameters are not in order, DevCon ignores them, but does not display a syntax error. Instead, it processes the command with the remaining parameters.

For help on command syntax, you can use the following commands in a Command Prompt window: **DevCon help** or **DevCon help** *command*.

**/r**  
Conditional reboot. Reboots the system after completing an operation only if a reboot is required to make a change effective.

This parameter differs from the [**DevCon Reboot**](devcon-reboot.md) operation, which forces the system to reboot. Instead, the **/r** parameter determines whether a reboot is required based on the return code from the accompanying operation.For more information, see [Rebooting and restarting](#rebooting-and-restarting).

*command*  
Specifies a DevCon command. For information about the available DevCon commands and the command arguments, use the following list.

You can also get syntax help in a Command Prompt window using **DevCon help** *command*.

To *list and display* information about devices on the computer, use the following commands:

[**DevCon HwIDs**](devcon-hwids.md)

[**DevCon Classes**](devcon-classes.md)

[**DevCon ListClass**](devcon-listclass.md)

[**DevCon DriverFiles**](devcon-driverfiles.md)

[**DevCon DriverNodes**](devcon-drivernodes.md)

[**DevCon Resources**](devcon-resources.md)

[**DevCon Stack**](devcon-stack.md)

[**DevCon Status**](devcon-status.md)

[**DevCon Dp\_enum**](devcon-dp-enum.md)

To *search* for information about devices on the computer, use the following commands:

[**DevCon Find**](devcon-find.md)

[**DevCon FindAll**](devcon-findall.md)

To manipulate the device or *change* its configuration, use the following commands:

[**DevCon Enable**](devcon-enable.md)

[**DevCon Disable**](devcon-disable.md)

[**DevCon Update**](devcon-update.md)

[**DevCon UpdateNI**](devcon-updateni.md)

[**DevCon Install**](devcon-install.md)

[**DevCon Remove**](devcon-remove.md)

[**DevCon Rescan**](devcon-rescan.md)

[**DevCon Restart**](devcon-restart.md)

[**DevCon Reboot**](devcon-reboot.md)

[**DevCon SetHwID**](devcon-sethwid.md)

[**DevCon ClassFilter**](devcon-classfilter.md)

[**DevCon Dp\_add**](devcon-dp-add.md)

[**DevCon Dp\_delete**](devcon-dp-delete.md)

*arguments*  
Specifies the arguments for a DevCon command.

**/?** or **help**  
Displays help. If you specify an operation, DevCon displays detailed help for the operation.

The parameters must appear in the specified order. For example, to display help for the [**DevCon Status**](devcon-status.md) operation, type **devcon /? status** (or **devcon help status**), not **devcon status /?**.

### Comments

Many DevCon operations require the hardware ID of the device. To create a list of the hardware IDs of all devices on the computer for use in subsequent DevCon operations, begin with a [**DevCon HwIDs**](devcon-hwids.md) command. For more information, see [Hardware IDs](../install/hardware-ids.md) and [Device Identification Strings](../install/device-identification-strings.md).

### How DevCon searches for devices

DevCon identifies devices by their computer name, hardware ID, compatible ID, device instance ID, and/or device setup class.

If a command includes more than one ID or ID pattern (an ID that contains wildcard characters (\*)), DevCon returns devices whose IDs match any of the IDs or ID patterns. That is, it assumes an "or" between the ID arguments.

For example, **devcon hwids \*pnp\* \*mou\*** returns devices that include either "pnp" or "mou" in their hardware ID or compatible ID.

If a command includes a device setup class, DevCon first limits the search to the setup class and then returns devices in the class that match any of the ID patterns, that is, it assumes an "and" between the class and the IDs and an "or" between each of the ID arguments.

For example, **devcon hwids =media \*pnp\* \*microsoft\*** returns devices in the media device setup class that include either "pnp" or "microsoft" in their hardware ID or compatible ID.

### Rebooting and restarting

DevCon provides two methods to reboot the operating system and one method to restart devices.

- The **/r** parameter is a conditional reboot that reboots the operating system only if a reboot is required to make the accompanying operation effective. This parameter is valid only in commands that include a DevCon operation. It can reboot the system on a local computer.

- The **DevCon Reboot** operation forces the operating system to reboot. It is valid only on a local computer, and it cannot be combined with other operations. Instead of using the reboot operation, users typically add the **/r** parameter to commands.

- The **DevCon Restart** operation restarts the specified devices. It is valid only on a local computer, and it cannot be combined with other operations.

### DevCon return codes

DevCon returns an integer that can be used in programs and scripts to determine the success of a DevCon command (for example, **return = devcon hwids \***).

The following table lists and describes the return codes.

| Return code | Description |
|--|--|
| 0 | Success |
| 1 | Requires reboot |
| 2 | Failure |
| 3 | Syntax error |
