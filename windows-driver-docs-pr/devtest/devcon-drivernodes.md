---
title: DevCon DriverNodes
description: Lists all driver packages that are compatible with the device, along with their version and ranking. Valid only on the local computer.
keywords:
- DevCon DriverNodes Driver Development Tools
topic_type:
- apiref
api_name:
- DevCon DriverNodes
api_type:
- NA
ms.date: 10/28/2022
---

# DevCon DriverNodes

> [!NOTE]
> [PnPUtil](pnputil.md) ships with every release of Windows and makes use of the most reliable and secure APIs available. We recommend using PnPUtil instead of DevCon. See the [Recommended replacement](#recommended-replacement) below and [Replacing DevCon](devcon-migration.md) for more information.

Lists all [driver packages](../install/components-of-a-driver-package.md) that are compatible with the device, along with their version and ranking. Valid only on the local computer.

``` console
devcon drivernodes {* | ID [ID ...] | =class [ID [ID ...]]}
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
| **'**</br>(single quote) | Matches the string literally (exactly as it appears). Precede a string with a single quote to indicate that an asterisk is part of the ID name and is not a wildcard character, for example, **'\*PNP0600**, where *PNP0600 (including the asterisk) is the hardware ID. |

**=***\<class\>*

Specifies the device setup class of the devices. The equal sign (**=**) identifies the string as a class name.

You can also specify hardware IDs, compatible IDs, device instance IDs, or ID patterns following the class name. Type a space between each ID or pattern. DevCon finds devices in the class that match the specified IDs.

## Recommended replacement

``` console
pnputil /enum-devices /drivers
```

For more recommended replacements, see [Replacing DevCon](devcon-migration.md).

## Comments

The **DevCon DriverNodes** operation runs only on the local computer.

The **DevCon DriverNodes** operation is particularly useful for troubleshooting setup problems. For example, you can use it to determine whether a Windows INF file or a customized third-party INF file was used for a device.

## Sample usage

``` console
devcon drivernodes *
devcon drivernodes *miniport*
devcon drivernodes =usb pci* usb*
```

## Examples

- [Example 10: List driver packages by hardware ID pattern](devcon-examples.md#example-10-list-driver-packages-by-hardware-id-pattern)
- [Example 11: List driver packages by device instance ID pattern](devcon-examples.md#example-11-list-driver-packages-by-device-instance-id-pattern)
