---
title: DevCon Install
description: Creates a new, root-enumerated devnode for a non-Plug and Play device and installs its supporting software. Valid only on the local computer.
keywords:
- DevCon Install Driver Development Tools
topic_type:
- apiref
api_name:
- DevCon Install
api_type:
- NA
ms.date: 12/01/2022
---

# DevCon Install

> [!NOTE]
> [PnPUtil](pnputil.md) ships with every release of Windows and makes use of the most reliable and secure APIs available. We recommend using PnPUtil instead of DevCon. See [Replacing DevCon](devcon-migration.md) for more information.

Creates a new, root-enumerated devnode for a non-Plug and Play device and installs its supporting software. Valid only on the local computer.

```console
devcon [/r] install INFfile HardwareID
```

> [!IMPORTANT]
> [PnPUtil](pnputil.md) ships with every release of Windows and makes use of the most reliable and secure APIs available and its use is recommended. For more information on using PnPutil instead of devcon, see [Replacing DevCon](devcon-migration.md).

## Parameters

**/r**

Conditional reboot. Reboots the system after completing an operation when a reboot is required to make the change effective. By default, DevCon does not reboot the system.

*INFfile*

Specifies the full path and file name of the INF file for the device. If you omit the path, DevCon assumes that the file is in the current directory.

*HardwareID*

Specifies a hardware ID for the device.

The specified hardware ID must exactly match the hardware ID of the device. Patterns are not valid. Do not type a single quote character (**'**) to indicate a literal value. For more information, see [Hardware IDs](../install/hardware-ids.md) and [Device Identification Strings](../install/device-identification-strings.md).

## Recommended replacement

``` console
devgen /add /bus ROOT /hardwareid HardwareID
pnputil /add-driver INFfile /install
```

For more recommended replacements, see [Replacing DevCon](devcon-migration.md).

## Comments

The system might need to be rebooted to make this change effective. To have DevCon reboot the system, add the conditional reboot parameter (**/r**) to the command.

You cannot use the **DevCon Install** operation for Plug and Play devices.

The **DevCon Install** operation creates a new non-Plug and Play device node. Then, it uses the **[DevCon Update](devcon-update.md)** operation to install drivers for the newly added device. As a result, the success message for the **DevCon Install** operation reports that DevCon has created the device node and that it has updated the drivers for the device.

If any step of the **DevCon Install** operation fails, DevCon displays a failure message and does not proceed with the driver installation.

The **DevCon Install** command creates a new non-Plug and Play device node each time you run it. To update or reinstall drivers, use the **[DevCon Update](devcon-update.md)** command.

## Sample usage

```console
devcon install c:\windows\inf\newdvc.inf ISAPNP\CSC4324\0
devcon /r install c:\windows\inf\newdvc.inf ISAPNP\CSC4324\0
```

## Examples

- [Example 33: Install a device](devcon-examples.md#example-33-install-a-device)
- [Example 34: Install a device using unattended setup](devcon-examples.md#example-34-install-a-device-using-unattended-setup)

## See also

- [Hardware IDs](../install/hardware-ids.md)
- [Device Identification Strings](../install/device-identification-strings.md)
