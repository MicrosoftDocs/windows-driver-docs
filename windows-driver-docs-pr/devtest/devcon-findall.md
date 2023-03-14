---
title: DevCon FindAll
description: Finds all devices on the computer, including devices that were once attached to the computer but have been detached or moved.
keywords:
- DevCon FindAll Driver Development Tools
topic_type:
- apiref
ms.topic: reference
api_name:
- DevCon FindAll
api_type:
- NA
ms.date: 10/28/2022
---

# DevCon FindAll

> [!NOTE]
> [PnPUtil](pnputil.md) ships with every release of Windows and makes use of the most reliable and secure APIs available. We recommend using PnPUtil instead of DevCon. See the [Recommended replacement](#recommended-replacement) below and [Replacing DevCon](devcon-migration.md) for more information.

Finds all devices on the computer, including devices that were once attached to the computer but have been detached or moved. (These are known as nonpresent devices or *phantom* devices.) The **DevCon FindAll** operation also finds devices that are enumerated differently as a result of a BIOS change.

``` console
devcon findall {* | ID [ID ...] | =class [ID [ID ...]]}
```

## Parameters

**\***

Represents all devices on the computer.

*ID*

Specifies all or part of a hardware ID, compatible ID, or device instance ID of a device. When specifying multiple IDs, type a space between each ID. IDs that include an ampersand character (**&**) must be enclosed in quotation marks.

The following special characters modify the ID parameter.

|Character|Description|
|--- |--- |
|**\***|Matches any character or no character. Use the wildcard character (**\***) to create an ID pattern, for example, ***disk***.|
|**@**|Indicates a device instance ID, for example, **@ROOT\FTDISK\0000**.|
|**'**</br>(single quote)|Matches the string literally (exactly as it appears). Precede a string with a single quote to indicate that an asterisk is part of the ID name and is not a wildcard character, for example, **'\*PNP0600**, where *PNP0600 (including the asterisk) is the hardware ID.|

**=***\<class\>*
Specifies the device setup class of the devices. The equal sign (**=**) identifies the string as a class name.

You can also specify hardware IDs, compatible IDs, device instance IDs, or ID patterns following the class name. Type a space between each ID or pattern. DevCon finds devices in the class that match the specified IDs.

## Recommended replacement

``` console
pnputil /enum-devices
```

For more recommended replacements, see [Replacing DevCon](devcon-migration.md).

## Comments

To find only devices that are currently attached to the computer, use the **[DevCon Find](devcon-find.md)** operation.

## Sample usage

``` console
devcon resources STORAGE\Volume
devcon resources =ports lpt*
devcon resources @pci*
```

## Example

- [Example 22: Find (and find all) devices in a setup class](devcon-examples.md#example-22-find-and-find-all-devices-in-a-setup-class)
