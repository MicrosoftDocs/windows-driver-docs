---
title: DevCon ListClass
description: Lists all devices in the specified device setup classes.
keywords:
- DevCon ListClass Driver Development Tools
topic_type:
- apiref
ms.topic: reference
api_name:
- DevCon ListClass
api_type:
- NA
ms.date: 10/28/2022
---

# DevCon ListClass

> [!NOTE]
> [PnPUtil](pnputil.md) ships with every release of Windows and makes use of the most reliable and secure APIs available. We recommend using PnPUtil instead of DevCon. See the [Recommended replacement](#recommended-replacement) below and [Replacing DevCon](devcon-migration.md) for more information.

Lists all devices in the specified device setup classes.

``` console
devcon listclass class [class...]
```

## Parameters

*class*

Specifies a device setup class. No equal sign (=) is required.

## Recommended replacement

``` console
pnputil /enum-devices /class <name or GUID>
```

For more recommended replacements, see [Replacing DevCon](devcon-migration.md).

## Comments

Each entry in a setup class display represents one device. The entry consists of the unique instance name and a description of the device in *instance* **:** *description* format.

To find the setup class of a particular device, use the **[DevCon Stack](devcon-stack.md)** operation.

## Sample usage

``` console
devcon listclass printers ports
devcon listclass SmartCardReader
```

## Examples

- [Example 6: List the devices in a device setup class](devcon-examples.md#example-6-list-the-devices-in-a-device-setup-class)
- [Example 7: List the devices in multiple classes](devcon-examples.md#example-7-list-the-devices-in-multiple-classes)
