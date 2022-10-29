---
title: DevCon Enable
description: Enables devices on the computer. Valid only on the local computer.To enable a device means that the device driver is loaded into memory and the device is ready for use.
keywords:
- DevCon Enable Driver Development Tools
topic_type:
- apiref
api_name:
- DevCon Enable
api_type:
- NA
ms.date: 10/28/2022
---

# DevCon Enable

> [!NOTE]
> [PnPUtil](pnputil.md) ships with every release of Windows and makes use of the most reliable and secure APIs available. We recommend using PnPUtil instead of DevCon. See the [Recommended replacement](#recommended-replacement) below and [Replacing DevCon](devcon-migration.md) for more information.

Enables devices on the computer. Valid only on the local computer.

To *enable* a device means that the device driver is loaded into memory and the device is ready for use.

``` console
devcon [/r] enable {* | ID [ID ...] | =class [ID [ID ...]]}
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
| **\*** | Matches any character or no character. Use the wildcard character () to create an ID pattern, for example, disk. |
| **@** | Indicates a device instance ID, for example, **@ROOT\FTDISK\0000**. |
| **'** </br>(single quote) | Matches the string literally (exactly as it appears). Precede a string with a single quote to indicate that an asterisk is part of the ID name and is not a wildcard character, for example, **'\*PNP0600**, where *PNP0600 (including the asterisk) is the hardware ID. |

*=class*

Specifies the device setup class of the devices. The equal sign (**=**) identifies the string as a class name.

You can also specify hardware IDs, compatible IDs, device instance IDs, or ID patterns following the class name. Type a space between each ID or pattern. DevCon finds devices in the class that match the specified IDs.

## Recommended replacement

``` console
pnputil /enable-device
```

For more recommended replacements, see [Replacing DevCon](devcon-migration.md).

## Comments

DevCon enables the device even if it is already enabled. Before and after enabling a device, use the **[DevCon Status](devcon-status.md)** operation to verify the device status.

The system might need to be rebooted to make this change effective. To have DevCon reboot the system, add the conditional reboot parameter (/r) to the command.

## Sample usage

``` console
devcon enable * (not recommended)
devcon /r enable *DVD-ROM*
devcon /r enable =printer
```

## Examples

- [Example 28: Enable a particular device](devcon-examples.md#example-28-enable-a-particular-device)
- [Example 29: Enable devices by class](devcon-examples.md#example-29-enable-devices-by-class)
