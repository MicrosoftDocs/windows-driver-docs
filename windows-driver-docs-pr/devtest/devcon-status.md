---
title: DevCon Status
description: Displays the status (running, stopped, or disabled) of the driver for devices on the computer.
keywords:
- DevCon Status Driver Development Tools
topic_type:
- apiref
ms.topic: reference
api_name:
- DevCon Status
api_type:
- NA
ms.date: 10/28/2022
---

# DevCon Status

> [!NOTE]
> [PnPUtil](pnputil.md) ships with every release of Windows and makes use of the most reliable and secure APIs available. We recommend using PnPUtil instead of DevCon. See the [Recommended replacement](#recommended-replacement) below and [Replacing DevCon](devcon-migration.md) for more information.

Displays the status (running, stopped, or disabled) of the driver for devices on the computer.

``` console
devcon status {* | ID [ID ...] | =class [ID [ID ...]]}
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

Specifies the device setup class of the devices. The equal sign (**=**) identifies the string as a class name.

You can also specify hardware IDs, compatible IDs, device instance IDs, or ID patterns following the class name. Type a space between each ID or pattern. DevCon finds devices in the class that match the specified IDs.

## Recommended replacement

``` console
pnputil /enum-devices
```

For more recommended replacements, see [Replacing DevCon](devcon-migration.md).

## Comments

If DevCon cannot determine the status of the device, such as when the device is no longer attached to the computer, DevCon omits the line describing the status from the status display.

The following example shows a successful status command. The text describing the device status appears in bold type.

``` console
STORAGE\VOLUME\1&30A96598&0&SIGNATURE80OFFSET7E0000LENGTH270987600
    Name: Generic volume
    Driver is running.
1 matching device(s) found.
```

In contrast, the following example shows how DevCon displays the status of a device that it cannot find. The status description is missing from the display.

``` console
STORAGE\VOLUME\1&30A96598&0&SIGNATURE80OFFSET7E0000LENGTH270987600
    Name: Generic volume
1 matching device(s) found.
```

## Sample usage

``` console
devcon status *
devcon status pci*
devcon status "PCI\VEN_115D&DEV_0003&SUBSYS_0181115D"
devcon status =printer
```

## Examples

- [Example 17: Display the status of all devices on the local computer](devcon-examples.md#example-17-display-the-status-of-all-devices)
- [Example 18: Display the status of a device by device instance ID](devcon-examples.md#example-18-display-the-status-of-a-device-by-device-instance-id)
- [Example 19: Display the status of related devices](devcon-examples.md#example-19-display-the-status-of-related-devices)
