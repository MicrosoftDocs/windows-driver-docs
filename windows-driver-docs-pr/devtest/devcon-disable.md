---
title: DevCon Disable
description: Disables devices on the computer.
keywords:
- DevCon Disable Driver Development Tools
topic_type:
- apiref
api_name:
- DevCon Disable
api_type:
- NA
ms.date: 10/28/2022
---

# DevCon Disable

> [!NOTE]
> [PnPUtil](pnputil.md) ships with every release of Windows and makes use of the most reliable and secure APIs available. We recommend using PnPUtil instead of DevCon. See the [Recommended replacement](#recommended-replacement) below and [Replacing DevCon](devcon-migration.md) for more information.

Disables devices on the computer. Valid only on the local computer.

To *disable* a device means that the device remains physically connected to the computer, but its driver is unloaded from memory and its resources are freed so that the device cannot be used.

``` console
devcon [/r] disable {* | ID [ID ...] | =class [ID [ID ...]]}
```

## Parameters

**/r**

Conditional reboot. Reboots the system after completing an operation only if a reboot is required to make a change effective.

**\***

Represents all devices on the computer.

*ID*

Specifies all or part of a hardware ID, compatible ID, or device instance ID of a device. When specifying multiple IDs, type a space between each ID. IDs that include an ampersand character (**&**) must be enclosed in quotation marks.

The following special characters modify the ID parameter.

| Character | Description |
|---|---|
| **\*** | Matches any character or no character. Use the wildcard character (\*) to create an ID pattern, for example, ***disk***. |
| **@** | Indicates a device instance ID, for example, **@ROOT\\FTDISK\\0000**. |
| **'**</br>(single quote) | Matches the string literally (exactly as it appears). Precede a string with a single quote to indicate that an asterisk is part of the ID name and is not a wildcard character, for example, **'\*PNP0600**, where *PNP0600 (including the asterisk) is the hardware ID. |

**=***\<class\>*

Specifies the device setup class of the devices. The equal sign (**=**) identifies the string as a class name.

You can also specify hardware IDs, compatible IDs, device instance IDs, or ID patterns following the class name. Type a space between each ID or pattern. DevCon finds devices in the class that match the specified IDs.

## Recommended replacement

``` console
pnputil /disable-device
```

For more recommended replacements, see [Replacing DevCon](devcon-migration.md).

## Comments

DevCon disables the device even if the device is already disabled. Before and after disabling a device, use the **[DevCon Status](devcon-status.md)** operation to verify the device status.

Before using an ID pattern to disable a device, determine which devices will be affected. To do so, use the pattern in a display command, such as `devcon status USB\*` or `devcon hwids USB\*`.

The system might need to be rebooted to make this change effective. To have DevCon reboot the system, add the conditional reboot parameter (/r) to the command.

## Sample usage

``` console
devcon disable * (not recommended)
devcon /r disable *DVD-ROM*
devcon /r disable =printer
```

## Examples

- [Example 30: Disable devices by an ID pattern](devcon-examples.md#example-30-disable-devices-by-an-id-pattern)
- [Example 31: Disable devices by device instance ID](devcon-examples.md#example-31-disable-devices-by-device-instance-id)
