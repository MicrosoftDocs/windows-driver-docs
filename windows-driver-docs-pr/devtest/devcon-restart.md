---
title: DevCon Restart
description: Stops and restarts the specified devices. Valid only on the local computer.
keywords:
- DevCon Restart Driver Development Tools
topic_type:
- apiref
api_name:
- DevCon Restart
api_type:
- NA
ms.date: 10/28/2022
---

# DevCon Restart

> [!NOTE]
> [PnPUtil](pnputil.md) ships with every release of Windows and makes use of the most reliable and secure APIs available. We recommend using PnPUtil instead of DevCon. See the [Recommended replacement](#recommended-replacement) below and [Replacing DevCon](devcon-migration.md) for more information.

Stops and restarts the specified devices.

``` console
devcon [/r] restart {* | ID [ID ...] | =class [ID [ID ...]]}
```

## Parameters

**/r**

Conditional reboot. Reboots the system after completing an operation only if a reboot is required to make a change effective.

**\***

Represents all devices on the computer.

*ID*
Specifies all or part of a hardware ID, compatible ID, or device instance ID of a device. When specifying multiple IDs, type a space between each ID. IDs that include an ampersand character (**&**) must be enclosed in quotation marks.

The following special characters modify the ID parameter.

|Character|Description|
|--- |--- |
|**\***|Matches any character or no character. Use the wildcard character (**\***) to create an ID pattern, for example, ***disk***.|
|**@**|Indicates a device instance ID, for example, **@ROOT\FTDISK\0000**.|
|**'**</br>(single quote)|Matches the string literally (exactly as it appears). Precede a string with a single quote to indicate that an asterisk is part of the ID name and is not a wildcard character, for example, **'\*PNP0600'**, where *PNP0600 (including the asterisk) is the hardware ID.|

**=***\<class\>*

Specifies the device setup class of the devices. The equal sign (**=**) identifies the string as a class name.

You can also specify hardware IDs, compatible IDs, device instance IDs, or ID patterns following the class name. Type a space between each ID or pattern. DevCon finds devices in the class that match the specified IDs.

## Recommended replacement

``` console
pnputil /restart-device
```

For more recommended replacements, see [Replacing DevCon](devcon-migration.md).

## Comments

The system might need to be rebooted to make this change effective. To have DevCon reboot the system, add the conditional reboot parameter (/r) to the command.

## Sample usage

``` console
devcon restart *
devcon restart pci*
devcon restart "PCI\VEN_115D&DEV_0003&SUBSYS_0181115D"
devcon restart =printer
devcon restart =printer *desk*
```

## Example

- [Example 38: Restart a device](devcon-examples.md#example-38-restart-a-device)
