---
title: Device Console (DevCon.exe) Commands
description: DevCon (DevCon.exe) is a command line tool that can display detailed information about devices on computers running Windows. You can also use DevCon to enable, disable, install, configure, and remove devices. DevCon uses the following syntax.
ms.assetid: b397c407-db1f-4e2a-8beb-4fe989bd06e0
keywords:
- Device Console (DevCon.exe) Commands Driver Development Tools
topic_type:
- apiref
api_name:
- Device Console (DevCon.exe) Commands
api_type:
- NA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Device Console (DevCon.exe) Commands


DevCon (DevCon.exe) is a command line tool that can display detailed information about devices on computers running Windows. You can also use DevCon to enable, disable, install, configure, and remove devices. DevCon uses the following syntax.

```
devcon [/m:\\computer] [/r] command [arguments] 
```

## <span id="ddk_devcon_general_commands_tools"></span><span id="DDK_DEVCON_GENERAL_COMMANDS_TOOLS"></span>Parameters


**Note**  To change the status or configuration of a device, you must be a member of the Administrators group on the computer.

 

The parameters in a DevCon command must appear in the order shown in the syntax. If parameters are not in order, DevCon ignores them, but does not display a syntax error. Instead, it processes the command with the remaining parameters.

For help on command syntax, you can use the following commands in a Command Prompt window: **DevCon help** or **DevCon help** *command*.

<span id="________m___computer______"></span><span id="________M___COMPUTER______"></span> **/m:\\\\**<em>computer</em>
Runs the command on the specified remote computer. The backslashes are required.
**Note**   To run DevCon commands on a remote computer, the Group Policy setting must allow the Plug and Play service to run on the remote computer. On computers that run Windows Vista and later versions of Windows, the Group Policy disables remote access to the service by default. On computers that run WDK 8.1 and WDK 8, the remote access feature is unavailable.

 

<span id="________r______"></span><span id="________R______"></span> **/r**
Conditional reboot. Reboots the system after completing an operation only if a reboot is required to make a change effective.

This parameter differs from the [**DevCon Reboot**](devcon-reboot.md) operation, which forces the system to reboot. Instead, the **/r** parameter determines whether a reboot is required based on the return code from the accompanying operation.For more information, see [Rebooting and restarting](#ddk-rebooting-and-restarting-tools).

<span id="_______command______"></span><span id="_______COMMAND______"></span> *command*
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

<span id="_______arguments______"></span><span id="_______ARGUMENTS______"></span> *arguments*
Specifies the arguments for a DevCon command.

<span id="__________or_help"></span><span id="__________OR_HELP"></span> **/?** or **help**
Displays help. If you specify an operation, DevCon displays detailed help for the operation.

The parameters must appear in the specified order. For example, to display help for the [**DevCon Status**](devcon-status.md) operation, type **devcon /? status** (or **devcon help status**), not **devcon status /?**.

### <span id="comments"></span><span id="COMMENTS"></span>Comments

Many DevCon operations require the hardware ID of the device. To create a list of the hardware IDs of all devices on the computer for use in subsequent DevCon operations, begin with a [**DevCon HwIDs**](devcon-hwids.md) command. For more information, see [Hardware IDs](https://msdn.microsoft.com/library/windows/hardware/ff546152) and [Device Identification Strings](https://msdn.microsoft.com/library/windows/hardware/ff541224).

### <span id="ddk_devcon_search_logic_tools"></span><span id="DDK_DEVCON_SEARCH_LOGIC_TOOLS"></span>How DevCon searches for devices

DevCon identifies devices by their computer name, hardware ID, compatible ID, device instance ID, and/or device setup class.

If a command includes more than one ID or ID pattern (an ID that contains wildcard characters (\*)), DevCon returns devices whose IDs match any of the IDs or ID patterns. That is, it assumes an "or" between the ID arguments.

For example, **devcon hwids \*pnp\* \*mou\\*** returns devices that include either "pnp" or "mou" in their hardware ID or compatible ID.

If a command includes a device setup class, DevCon first limits the search to the setup class and then returns devices in the class that match any of the ID patterns, that is, it assumes an "and" between the class and the IDs and an "or" between each of the ID arguments.

For example, **devcon hwids =media \*pnp\* \*microsoft\\*** returns devices in the media device setup class that include either "pnp" or "microsoft" in their hardware ID or compatible ID.

**Note**   To run DevCon commands on a remote computer, the Group Policy setting must allow the Plug and Play service to run on the remote computer. On computers that run Windows Vista and later versions of Windows, the Group Policy disables remote access to the service by default. On computers that run WDK 8.1 and WDK 8, the remote access feature is unavailable.

 

### <span id="ddk_rebooting_and_restarting_tools"></span><span id="DDK_REBOOTING_AND_RESTARTING_TOOLS"></span><a name="ddk-rebooting-and-restarting-tools"></a>Rebooting and restarting

DevCon provides two methods to reboot the operating system and one method to restart devices.

-   The **/r** parameter is a conditional reboot that reboots the operating system only if a reboot is required to make the accompanying operation effective. This parameter is valid only in commands that include a DevCon operation. It can reboot the system on a local computer or a remote computer (Windows XP and earlier).

-   The **DevCon Reboot** operation forces the operating system to reboot. It is valid only on a local computer, and it cannot be combined with other operations. Instead of using the reboot operation, users typically add the **/r** parameter to commands.

-   The **DevCon Restart** operation restarts the specified devices. It is valid only on a local computer, and it cannot be combined with other operations.

### <span id="ddk_devcon_return_codes_tools"></span><span id="DDK_DEVCON_RETURN_CODES_TOOLS"></span>DevCon return codes

DevCon returns an integer that can be used in programs and scripts to determine the success of a DevCon command (for example, **return = devcon hwids \\***).

The following table lists and describes the return codes.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Return code</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0</p></td>
<td align="left"><p>Success</p></td>
</tr>
<tr class="even">
<td align="left"><p>1</p></td>
<td align="left"><p>Requires reboot</p></td>
</tr>
<tr class="odd">
<td align="left"><p>2</p></td>
<td align="left"><p>Failure</p></td>
</tr>
<tr class="even">
<td align="left"><p>3</p></td>
<td align="left"><p>Syntax error</p></td>
</tr>
</tbody>
</table>

 

 

 





