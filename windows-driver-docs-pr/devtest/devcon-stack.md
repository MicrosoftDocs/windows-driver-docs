---
title: DevCon Stack
description: Displays the expected driver stack for the specified devices, and the GUID and the name of the device setup class for each device.
keywords:
- DevCon Stack Driver Development Tools
topic_type:
- apiref
api_name:
- DevCon Stack
api_type:
- NA
ms.date: 10/28/2022
---

# DevCon Stack

> [!NOTE]
> [PnPUtil](pnputil.md) ships with every release of Windows and makes use of the most reliable and secure APIs available. We recommend using PnPUtil instead of DevCon. See the [Recommended replacement](#recommended-replacement) below and [Replacing DevCon](devcon-migration.md) for more information.

Displays the expected driver stack for the specified devices, and the GUID and the name of the device setup class for each device.

``` console
devcon stack {* | ID [ID ...] | =class [ID [ID...]]}
```

## Parameters

**\***

Represents all devices on the computer.

*ID*

Specifies all or part of a hardware ID, compatible ID, or device instance ID of a device. When specifying multiple IDs, type a space between each ID. IDs that include an ampersand character (**&**) must be enclosed in quotation marks.

The following special characters modify the ID parameter.

| Character | Description |
|---|---|
| **\*** | Matches any character or no character. Use the wildcard character (**\***) to create an ID pattern, for example, ***disk***. |
| **@** | Indicates a device instance ID, for example, **@ROOT\FTDISK\0000**. |
| **'**(single quote) | Matches the string literally (exactly as it appears). Precede a string with a single quote to indicate that an asterisk is part of the ID name and is not a wildcard character, for example, **'\*PNP0600**, where *PNP0600 (including the asterisk) is the hardware ID. |

**=***\<class\>*

Specifies the device setup class of the devices. The equal sign (**=**) identifies the string as a class name. You can also specify hardware IDs, compatible IDs, device instance IDs, or ID patterns following the class name. Type a space between each ID or pattern. DevCon finds devices in the class that match the specified IDs.

## Recommended replacement

``` console
pnputil /enum-devices /stack
```

For more recommended replacements, see [Replacing DevCon](devcon-migration.md).

## Comments

The **DevCon Stack** operation displays the expected driver stack for a device. Although the actual driver stack typically matches the expected stack, variations are possible.

To investigate a device problem, compare the expected driver stack from the stack operation with the actual drivers that the device uses, as displayed by the **[DevCon DriverFiles](devcon-driverfiles.md)** operation.

## Sample usage

``` console
devcon stack pci*
devcon stack * > Stack.txt
devcon stack ISAPNP\ReadDataPort
devcon stack =multifunction
```

## Examples

- [Example 14: Display the driver stack for storage devices](devcon-examples.md#example-14-display-the-driver-stack-for-storage-devices)
- [Example 15: Find the setup class of a device](devcon-examples.md#example-15-find-the-setup-class-of-a-device)
- [Example 16: Display the stack for related devices](devcon-examples.md#example-16-display-the-stack-for-related-devices)
