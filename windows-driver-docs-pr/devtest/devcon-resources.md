---
title: DevCon Resources
description: Lists the resources allocated to the specified devices. Resources are assignable and addressable bus paths, such as DMA channels, I/O ports, IRQ, and memory addresses.
keywords:
- DevCon Resources Driver Development Tools
topic_type:
- apiref
api_name:
- DevCon Resources
api_type:
- NA
ms.date: 10/28/2022
---

# DevCon Resources

> [!NOTE]
> [PnPUtil](pnputil.md) ships with every release of Windows and makes use of the most reliable and secure APIs available. We recommend using PnPUtil instead of DevCon. See the [Recommended replacement](#recommended-replacement) below and [Replacing DevCon](devcon-migration.md) for more information.

Lists the resources allocated to the specified devices. Resources are assignable and addressable bus paths, such as DMA channels, I/O ports, IRQ, and memory addresses.

``` console
devcon resources {* | ID [ID ...] | =class [ID [ID...]]}
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
| **'**</br>(single quote) | Matches the string literally (exactly as it appears). Precede a string with a single quote to indicate that an asterisk is part of the ID name and is not a wildcard character, for example, **'\*PNP0600'**, where *PNP0600 (including the asterisk) is the hardware ID. |

**=***\<class\>*

Specifies the device setup class of the devices. The equal sign (**=**) identifies the string as a class name.

You can also specify hardware IDs, compatible IDs, device instance IDs, or ID patterns following the class name. Type a space between each ID or pattern. DevCon finds devices in the class that match the specified IDs.

## Recommended replacement

``` console
pnputil /enum-devices /resources
```

For more recommended replacements, see [Replacing DevCon](devcon-migration.md).

## Sample usage

``` console
devcon resources *
devcon resources =media
devcon resources acpi* *port*
devcon resources =class port* (by class and hardware ID)
devcon resources =class @port*(by class and device instance ID)
```

## Examples
- [Example 12: List resources of a class of devices](devcon-examples.md#example-12-list-resources-of-a-class-of-devices)
- [Example 13: List resources of device by ID](devcon-examples.md#example-13-list-resources-of-device-by-id)
