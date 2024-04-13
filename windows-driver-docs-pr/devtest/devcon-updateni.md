---
title: DevCon UpdateNI
description: Forcibly replaces the current device drivers with drivers listed in the specified INF file without prompting the user for information or confirmation. Valid only on the local computer.
keywords:
- DevCon UpdateNI Driver Development Tools
topic_type:
- apiref
ms.topic: reference
api_name:
- DevCon UpdateNI
api_type:
- NA
ms.date: 10/28/2022
---

# DevCon UpdateNI

> [!NOTE]
> [PnPUtil](pnputil.md) ships with every release of Windows and makes use of the most reliable and secure APIs available. We recommend using PnPUtil instead of DevCon. See the [Recommended replacement](#recommended-replacement) below and [Replacing DevCon](devcon-migration.md) for more information.

Forcibly replaces the current device drivers with drivers listed in the specified INF file without prompting the user for information or confirmation. Valid only on the local computer.

``` console
devcon [/r] updateni INFfile HardwareID
```

## Parameters

**/r**

Conditional reboot. Reboots the system after completing an operation only if a reboot is required to make a change effective.

*INFfile*

Specifies the full path and file name of the INF (information) file for the device. If you omit the path, DevCon assumes that the file is in the current directory.

*HardwareID*

Specifies a hardware ID for the device.

The specified hardware ID must exactly match the hardware ID of the device. Patterns are not valid. Do not type a single quote character (**'**) to indicate a literal value.

## Recommended replacement

``` console
pnputil /add-driver INFfile /install
```

For more recommended replacements, see [Replacing DevCon](devcon-migration.md).

## Comments

The **DevCon UpdateNI** operation suppresses all user prompts that require a response and assumes the default response. As a result, you cannot use this operation to install unsigned drivers. To display user prompts during an update, use **[DevCon Update](devcon-update.md)**.

The **DevCon UpdateNI** operation forces an update, even if the drivers in the specified INF file are older or less appropriate than the current drivers.

Before updating the driver for any device, determine which devices will be affected by the update command. To do so, use the hardware ID in a display command, such as **[DevCon HwIDs](devcon-hwids.md)** or **[DevCon DriverFiles](devcon-driverfiles.md)**. This is especially important in a **DevCon UpdateNI** operation because DevCon does not list the device drivers that it updates.

The system might need to be rebooted to make this change effective. To have DevCon reboot the system, add the conditional reboot parameter (/r) to the command.

## Sample usage

``` console
devcon updateni c:\windows\inf\newdvc.inf ISAPNP\CSC4324\0
devcon /r updateni c:\windows\inf\newdvc.inf *PNP030b
```

## Example

- [Example 32: Update the driver for communication ports](devcon-examples.md#example-32-update-the-driver-for-communication-ports)
