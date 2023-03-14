---
title: DevCon Update
description: Forcibly replaces the current device drivers for a specified device with drivers listed in the specified INF file. Valid only on the local computer.
keywords:
- DevCon Update Driver Development Tools
topic_type:
- apiref
ms.topic: reference
api_name:
- DevCon Update
api_type:
- NA
ms.date: 10/28/2022
---

# DevCon Update

> [!NOTE]
> [PnPUtil](pnputil.md) ships with every release of Windows and makes use of the most reliable and secure APIs available. We recommend using PnPUtil instead of DevCon. See the [Recommended replacement](#recommended-replacement) below and [Replacing DevCon](devcon-migration.md) for more information.

Forcibly replaces the current device drivers for a specified device with drivers listed in the specified INF file. Valid only on the local computer.

``` console
devcon [/r] update INFfile HardwareID
```

## Parameters

**/r**

Conditional reboot. Reboots the system after completing an operation only if a reboot is required to make a change effective.

*INFfile*

Specifies the full path and file name of the INF (information) file used in the update. If you omit the path, DevCon assumes that the file is in the current directory.

*HardwareID*

Updates the drivers for devices with the specified hardware ID. The hardware ID specified in this command must exactly match the hardware ID of the device. Patterns are not valid. Do not type a single quote character (**'**) to indicate a literal value.

## Recommended replacement

``` console
pnputil /add-driver INFfile /install
```

For more recommended replacements, see [Replacing DevCon](devcon-migration.md).

## Comments

The **DevCon Update** operation forces an update to the most appropriate drivers in the specified INF file, even if those drivers are older or less appropriate than the current drivers or the drivers in a different INF file. For more information, see [How Setup Selects Drivers](../install/how-windows-selects-a-driver-for-a-device.md).

You cannot use a **DevCon Update** command to update drivers for nonpresent devices.

Before updating the driver for any device, determine which devices will be affected by the update command. To do so, use the hardware ID in a display command, such as **[DevCon HwIDs](devcon-hwids.md)** or **[DevCon DriverFiles](devcon-driverfiles.md)**. This is especially important in a **DevCon Update** operation because DevCon does not list the device drivers that it updates.

DevCon prompts the user if the INF file specifies an unsigned driver or if it cannot find a required file, such as a driver file on removable media. To suppress prompts that require a response, use the noninteractive update operation, **[DevCon UpdateNI](devcon-updateni.md)**.

The system might need to be rebooted to make this change effective. To have DevCon reboot the system, add the conditional reboot parameter (/r) to the command.

## Sample usage

``` console
devcon update c:\windows\inf\newdvc.inf ISAPNP\CSC4324\0
devcon /r update c:\windows\inf\newdvc.inf *PNP030b
```

## Example

- [Example 32: Update the driver for communication ports](devcon-examples.md#example-32-update-the-driver-for-communication-ports)
- [Example 44: Forcibly update the HAL](devcon-examples.md#example-44-forcibly-update-the-hal)
