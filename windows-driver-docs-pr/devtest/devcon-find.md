---
title: DevCon Find
description: Finds all devices that are currently attached to the computer. Displays the device instance ID and device description.
keywords:
- DevCon Find Driver Development Tools
topic_type:
- apiref
ms.topic: reference
api_name:
- DevCon Find
api_type:
- NA
ms.date: 10/28/2022
---

# DevCon Find

> [!NOTE]
> [PnPUtil](pnputil.md) ships with every release of Windows and makes use of the most reliable and secure APIs available. We recommend using PnPUtil instead of DevCon. See the [Recommended replacement](#recommended-replacement) below and [Replacing DevCon](devcon-migration.md) for more information.

Finds all devices that are currently attached to the computer. Displays the device instance ID and device description.

``` console
devcon find {* | ID [ID ...] | =class [ID [ID ...]]}
```

## Parameters

**\***

Represents all devices on the computer.

*ID*

Specifies all or part of a hardware ID, compatible ID, or device instance ID of a device. When specifying multiple IDs, type a space between each ID. IDs that include an ampersand character (**&**) must be enclosed in quotation marks.

The following special characters modify the ID parameter.

| Character | Description |
|---|---|
| **\*** | Matches any character or no character. Use the wildcard character () to create an ID pattern, for example, ***disk***. |
| **@** | Indicates a device instance ID, for example, **@ROOT\FTDISK\0000**. |
| **'** (single quote) | Matches the string literally (exactly as it appears). Precede a string with a single quote to indicate that an asterisk is part of the ID name and is not a wildcard character, for example, **'\*PNP0600**, where *PNP0600 (including the asterisk) is the hardware ID. |

**=***\<class\>*

Specifies the device setup class of the devices. The equal sign (**=**) identifies the string as a class name.

You can also specify hardware IDs, compatible IDs, device instance IDs, or ID patterns following the class name. Type a space between each ID or pattern. DevCon finds devices in the class that match the specified IDs.

## Recommended replacement

``` console
pnputil /enum-devices
```

For more recommended replacements, see [Replacing DevCon](devcon-migration.md).

## Comments

You can use the **DevCon Find** operation to find devices that are not currently attached to the computer by specifying the full device instance ID of the device instead of a hardware ID or ID pattern. Specifying the full device instance ID overrides the restriction on the **DevCon Find** operation that limits it to attached devices.

The **DevCon Find** operation with a single class argument is the same as the **[DevCon ListClass](devcon-listclass.md)** operation.

To find all devices, including those that are not currently attached to the computer, use the **[DevCon FindAll](devcon-findall.md)** operation.

## Sample usage

``` console
devcon find *
devcon find =media *pnp*
devcon find @*hub*
```

## Examples

- [Example 20: Find devices by hardware ID pattern](devcon-examples.md#example-20-find-devices-by-hardware-id-pattern)
- [Example 21: Find devices by device instance ID or class](devcon-examples.md#example-21-find-devices-by-device-instance-id-or-class)
