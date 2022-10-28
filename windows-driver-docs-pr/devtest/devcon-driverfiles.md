---
title: DevCon DriverFiles
description: Displays the full path and file name of installed INF files and device driver files for the specified devices. Valid only on the local computer.
keywords:
- DevCon DriverFiles Driver Development Tools
topic_type:
- apiref
api_name:
- DevCon DriverFiles
api_type:
- NA
ms.date: 10/28/2022
---

# DevCon DriverFiles

> [!NOTE]
> [PnPUtil](pnputil.md) ships with every release of Windows and makes use of the most reliable and secure APIs available. We recommend using PnPUtil instead of DevCon. See the [Recommended replacement](#recommended-replacement) below and [Replacing DevCon](devcon-migration.md) for more information.

Displays the full path and file name of installed INF files and device driver files for the specified devices. Valid only on the local computer.

``` console
devcon driverfiles {* | ID [ID ...] | =class [ID [ID ...]]}
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
| **@** | Indicates a device instance ID, for example, **@ROOT\\FTDISK\\0000**. |
| **'**</br>(single quote) | Matches the string literally (exactly as it appears). Precede a string with a single quote to indicate that an asterisk is part of the ID name and is not a wildcard character, for example, **'\*PNP0600**, where \*PNP0600 (including the asterisk) is the hardware ID. |

**=***\<class\>*

Specifies the device setup class of the devices. The equal sign (**=**) identifies the string as a class name.

You can also specify hardware IDs, compatible IDs, device instance IDs, or ID patterns following the class name. Type a space between each ID or pattern. DevCon finds devices in the class that match the specified IDs.

## Recommended replacement

``` console
pnputil /enum-drivers /files
```

For more recommended replacements, see [Replacing DevCon](devcon-migration.md).

## Comments

The **DevCon DriverFiles** operation runs only on the local computer.

## Sample usage

``` console
devcon driverfiles *
devcon driverfiles FDC\GENERIC_FLOPPY_DRIVE pci*
devcon driverfiles =media
devcon driverfiles =media isapnp*
```

## Examples

- [Example 8: List all driver files](devcon-examples.md#example-8-list-all-driver-files)
- [Example 9: List the driver files of a particular device](devcon-examples.md#example-9-list-the-driver-files-of-a-particular-device)
