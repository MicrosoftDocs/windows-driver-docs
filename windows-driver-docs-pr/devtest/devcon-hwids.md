---
title: DevCon HwIDs
description: Displays the hardware IDs, compatible IDs, and device instance IDs of the specified devices.
keywords:
- DevCon HwIDs Driver Development Tools
topic_type:
- apiref
api_name:
- DevCon HwIDs
api_type:
- NA
ms.date: 10/28/2022
---

# DevCon HwIDs

> [!NOTE]
> [PnPUtil](pnputil.md) ships with every release of Windows and makes use of the most reliable and secure APIs available. We recommend using PnPUtil instead of DevCon. See the [Recommended replacement](#recommended-replacement) below and [Replacing DevCon](devcon-migration.md) for more information.

Displays the hardware IDs, compatible IDs, and device instance IDs of the specified devices.

``` console
devcon hwids {* | ID [ID ...] | =class [ID [ID ...]]}
```

## Parameters

**\***

Represents all devices on the computer.

*ID*

Specifies one or more devices by using an identifier.

Type all or part of a hardware ID, compatible ID, or device instance ID of a device. When specifying multiple IDs, type a space between each ID. IDs that include an ampersand character (**&**) must be enclosed in quotation marks.

The following special characters modify the ID parameter.

| Character | Description |
|---|---|
| **\*** | Matches any character or no character. Use the wildcard character (**\***) to create an ID pattern, for example, ***disk***. |
| **@** | Indicates a device instance ID, for example, **@ROOT\FTDISK\0000**. |
| **'**</br>(single quote) | Matches the string literally (exactly as it appears). Precede a string with a single quote to indicate that an asterisk is part of the ID name and is not a wildcard character, for example, **'\*PNP0600**, where *PNP0600 (including the asterisk) is the hardware ID. |

**=***\<class\>*

Specifies one or more devices by using a setup class.

Type all or part of the name of the setup class of the devices. The equal sign (**=**) identifies the string as a class name.

You can also specify hardware IDs, compatible IDs, device instance IDs, or ID patterns following the class name. Type a space between each ID or pattern. DevCon finds devices in the class that match the specified IDs.

## Recommended replacement

``` console
pnputil /enum-devices /deviceids
```

For more recommended replacements, see [Replacing DevCon](devcon-migration.md).

## Comments

To create a hardware ID for a root-enumerated device, use the **[DevCon SetHwID](devcon-sethwid.md)** command.

## Sample usage

``` console
devcon hwids *
devcon hwids acpi* *port*
devcon hwids =usb
```

## Examples

- [Example 1: Find all hardware IDs](devcon-examples.md#example-1-find-all-hardware-ids)
- [Example 2: Find hardware IDs by using a pattern](devcon-examples.md#example-2-find-hardware-ids-by-using-a-pattern)
- [Example 3: Find hardware IDs by using a class](devcon-examples.md#example-3-find-hardware-ids-by-using-a-class)
